#!/usr/bin/env python
# -*- coding: utf-8 -*-

# m2p_mail.py is part of Barleymap web app.
# Copyright (C)  2013-2014  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys, smtplib, traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from barleymapcore.m2p_exception import m2pException
from resources_mng import ResourcesMng

def send_files(form, filenames):
    try:
        sys.stderr.write("M2P: Sending email to "+email_to+"\n")
        
        email_to = form.get_email_to()
        params = form.as_params_list() # This should be a string with one line per parameter "name: value"
        
        # Create the enclosing (outer) message
        outer = __create_outer_msg(email_to, 'Markers mapped to barley map')
        
        # Main Text
        email_text = MIMEText(params, _subtype='plain')
        outer.attach(email_text)
        
        # Attachments
        i = 0
        for file_name in filenames:
            __add_file(file_name, outer, file_name+".csv")
            
            i+=1
        
        # Connection to server and delivery
        __send(email_to, outer)
    
    except m2pException:
        raise
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise m2pException("Error sending email to "+email_to)

def __create_outer_msg(email_to, subject):
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = subject
    outer['To'] = email_to
    outer['From'] = ResourcesMng.get_mail_sender()
    
    return outer

def __add_file(file_name, outer, map_name):
    # Attached CSV
    fp = open(file_name)
    try:
        msg = MIMEText(fp.read(), _subtype="csv")
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise m2pException("Error opening file to send by email.")
    finally:
        fp.close()
    
    msg.add_header('Content-Disposition', 'attachment', filename=map_name)
    outer.attach(msg)
    
    return

def __send(email_to, outer):
    # Connection to server and delivery
    s = smtplib.SMTP()
    try:
        s.connect(ResourcesMng.get_mail_host(), ResourcesMng.get_mail_port())
        s.starttls()
        s.login(ResourcesMng.get_mail_user(), ResourcesMng.get_mail_pass())
        s.sendmail(ResourcesMng.get_mail_sender(), [email_to], outer.as_string())
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise m2pException("Error sending email to "+email_to+".")
    finally:
        s.close()
    
    return

#def _format_params(params):
#    # Parameters (see mapmarkers_cp.py --> parameters_list)
#    # [input_query, multiple, action, input_datasets, input_genes, input_sort, genes_window,
#    # queries_type, threshold_id, threshold_cov]
#    
#    text_params = []
#    
#    for a in [0]:
#        text_params.append(params[a][0]+": "+str(params[a][1]))
#    
#    if params[0][1] == ALIGN_ACTION:
#        for a in [1, 2, 3]:
#            text_params.append(params[a][0]+": "+str(params[a][1]))
#    
#    for a in [6, 5, 7, 8, 9, 4, 10, 11]:
#        text_params.append(params[a][0]+": "+str(params[a][1]))
#    
#    return "\n".join(text_params)

#def send_file(email_to, filename, params):
#    try:
#        sys.stderr.write("M2P: Sending email to "+email_to+"\n")
#        
#        # Create the enclosing (outer) message
#        outer = __create_outer_msg(email_to, 'Markers mapped to barley map')
#        
#        # Main Text
#        email_text = MIMEText(_format_params(params), _subtype='plain')
#        outer.attach(email_text)
#        
#        # Attachment
#        __add_file(filename, outer, "markers2barleymap.csv")
#        
#        # Connection to server and delivery
#        __send(email_to, outer)
#    
#    except m2pException:
#        raise
#    except Exception:
#        traceback.print_exc(file=sys.stderr)
#        raise m2pException("Error sending email to "+email_to)
#    
#    return

## END