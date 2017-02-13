#!/usr/bin/env python
# -*- coding: utf-8 -*-

# server.py is part of Barleymap web app.
# Copyright (C)  2013-2014  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import os, sys
import cherrypy

#from barleymapcore.utils.data_utils import read_paths, load_data
from barleymapcore.db.PathsConfig import PathsConfig

import plain_html, mapmarkers
from resources_mng import ResourcesMng

DEBUG = True
verbose_param = DEBUG

class Base:
    
    def html_head(self):
        return plain_html.html_head()
    
    def header(self):
        return plain_html.header()
    
    def menu(self, citation):
        return plain_html.menu(citation)
    
    def footer(self):
        return plain_html.footer()
    
    def html_end(self):
        return plain_html.html_end()
    
    def html_container(self, contents = []):
        return '<div id="container" style="margin:10px;">'+"".join(contents)+'</div> <!-- container -->'

class Root(Base):
    @cherrypy.expose
    def index(self):
        
        sys.stderr.write("server.py: request to /index\n")
        
        ## Read conf file
        app_abs_path = os.path.dirname(os.path.abspath(__file__))
        
        paths_config = PathsConfig(app_abs_path, verbose_param)
        __app_path = paths_config.get_app_path()
        
        #config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        #__app_path = config_path_dict["app_path"]
        
        citation = "<a href='http://link.springer.com/article/10.1007%2Fs11032-015-0253-1' target='_blank' style='text-decoration:none;'>"+\
                    paths_config.get_citation().replace("_", " ")+\
                    "</a>"
        
        sys.stderr.write("\t/index of app: "+__app_path+"\n")
        
        # This was removed, but I leave it as example of how to obtain a value from cherrypy config file
        #print cherrypy.request.app.config['barleymap_settings']['deploy_dir']
        
        return self.html_head()+self.header()+self.html_container([self.index_content(citation)])+self.footer()+self.html_end()
    
    def index_content(self, citation):
        return plain_html.main_text(citation)
    
    @cherrypy.expose
    def align(self):
        sys.stderr.write("server.py: request to /align/\n")
        
        ## Read conf file
        config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        __app_path = config_path_dict["app_path"]
        
        citation = "<a href='http://link.springer.com/article/10.1007%2Fs11032-015-0253-1' target='_blank' style='text-decoration:none;'>"+config_path_dict["citation"].replace("_", " ")+"</a>"
        
        return self.html_head()+self.header()+self.html_container([self.menu(citation), self.align_content()])+self.footer()+self.html_end()
    
    def align_content(self, ):
        if cherrypy.session.get('session_token'):
            
            if cherrypy.session['action_blast'] and cherrypy.session['action_blast'] != "":
                input_query = cherrypy.session.get('input_query')
            else: # Comes from find action
                input_query = ""
            input_multiple = cherrypy.session.get('input_multiple')
            input_sort = cherrypy.session.get('input_sort')
            input_genes = cherrypy.session.get('input_genes')
            load_annot = cherrypy.session.get('load_annot')
            
            input_extend = cherrypy.session.get('input_extend')
            genes_window_cm = cherrypy.session.get('genes_window_cm')
            genes_window_bp = cherrypy.session.get('genes_window_bp')
            input_maps = cherrypy.session.get('input_maps')
            input_databases = cherrypy.session.get('input_databases')
            
            send_email = cherrypy.session.get('send_email')
            email_to = cherrypy.session.get('email_to')
            queries_type = cherrypy.session.get('queries_type')
            threshold_id = cherrypy.session.get('threshold_id')
            threshold_cov = cherrypy.session.get('threshold_cov')
            
            retValue = plain_html.align_seqs_form(input_query, input_multiple, input_sort, input_genes, load_annot, \
                                                  input_extend, genes_window_cm, genes_window_bp, input_maps, input_databases, \
                                        send_email, email_to, queries_type, threshold_id, threshold_cov)
        else:
            retValue = plain_html.align_seqs_form()
        
        return retValue
    
    @cherrypy.expose
    def find(self):
        sys.stderr.write("server.py: request to /find/\n")
        
        ## Read conf file
        config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        __app_path = config_path_dict["app_path"]
        
        citation = "<a href='http://link.springer.com/article/10.1007%2Fs11032-015-0253-1' target='_blank' style='text-decoration:none;'>"+config_path_dict["citation"].replace("_", " ")+"</a>"
        
        return self.html_head()+self.header()+self.html_container([self.menu(citation), self.find_content()])+self.footer()+self.html_end()
    
    def find_content(self):
        if cherrypy.session.get('session_token'):
            
            if cherrypy.session['action_dataset'] and cherrypy.session['action_dataset'] != "":
                input_query = cherrypy.session.get('input_query')
            else: # Comes from align action
                input_query = ""
                
            input_multiple = cherrypy.session.get('input_multiple')
            input_sort = cherrypy.session.get('input_sort')
            input_genes = cherrypy.session.get('input_genes')
            load_annot = cherrypy.session.get('load_annot')
            
            input_extend = cherrypy.session.get('input_extend')
            genes_window_cm = cherrypy.session.get('genes_window_cm')
            genes_window_bp = cherrypy.session.get('genes_window_bp')
            input_maps = cherrypy.session.get('input_maps')
            
            #sys.stderr.write("server find_content "+str(input_maps)+"\n")
            
            send_email = cherrypy.session.get('send_email')
            email_to = cherrypy.session.get('email_to')
            
            retValue = plain_html.find_markers_form(input_query, input_multiple, input_sort, input_genes, load_annot, \
                                                    input_extend, genes_window_cm, genes_window_bp, input_maps, \
                                                     send_email, email_to)
        else:
            retValue = plain_html.find_markers_form()
        
        return retValue
    
    @cherrypy.expose
    def help(self):
        sys.stderr.write("server.py: request to /help/\n")
        config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        
        citation = "<a href='http://link.springer.com/article/10.1007%2Fs11032-015-0253-1' target='_blank' style='text-decoration:none;'>"+config_path_dict["citation"].replace("_", " ")+"</a>"
        
        return self.html_head()+self.header()+self.html_container([self.menu(citation), self.help_content()])+self.footer()+self.html_end()
    
    def help_content(self):
        return plain_html.help()

    
class Mapmarkers():
    @cherrypy.expose
    def index(self, input_query = "", \
              input_multiple = "", \
              input_sort = "", \
              input_genes = "", \
              load_annot = "", \
              genes_window = "", \
              action_blast = "", \
              action_dataset = "", \
              input_datasets = "", \
              send_email = "", \
              email_to = "", \
              queries_type = "", \
              threshold_id = "", \
              threshold_cov = "", \
              my_file = None):
        
        sys.stderr.write("server.py: request to T3 links\n")
        
        verbose_param = ResourcesMng.get_verbose()
        
        config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        __app_path = config_path_dict["app_path"]
        
        # Load all configured maps
        maps_conf_file = __app_path+"conf/maps.conf"
        (maps_names, maps_ids) = load_data(maps_conf_file, verbose = verbose_param) # data_utils.load_data
        if len(maps_names) > 1:
            input_maps = maps_names.split(",")
        else:
            input_maps = maps_names
        
        #sys.stderr.write("server index "+str(input_maps)+"\n")
        
        # Load all configured databases
        databases_conf_file = __app_path+"conf/references.conf"
        (databases_names, databases_ids) = load_data(databases_conf_file, verbose = verbose_param) # data_utils.load_data
        if len(databases_names) > 1:
            input_databases = databases_names.split(",")
        else:
            input_databases = databases_names
        
        # FIND ACTION
        from barleymapcore.MapMarkers import FIND_ACTION
        
        action_dataset = FIND_ACTION
        
        # Genes information: on marker
        input_genes = "marker"
        
        output = self.run(input_query = input_query, \
                          input_multiple = input_multiple, \
                          input_sort = input_sort, \
                          input_genes = input_genes, \
                          load_annot = load_annot, \
                          input_extend = "1", \
                          genes_window_cm = genes_window, \
                          genes_window_bp = genes_window, \
                          input_maps = input_maps, \
                          input_databases = input_databases, \
                          action_blast = "", \
                          action_dataset = action_dataset, \
                          send_email = send_email, \
                          email_to = email_to, \
                          queries_type = queries_type, \
                          threshold_id = threshold_id, \
                          threshold_cov = threshold_cov, \
                          my_file = my_file)
        
        return output
        
    @cherrypy.expose
    def run(self, input_query = "", \
              input_multiple = "", \
              input_sort = "", \
              input_genes = "", \
              load_annot = "", \
              input_extend = "", \
              genes_window_cm = "", \
              genes_window_bp = "", \
              input_maps = "", \
              input_databases = "", \
              action_blast = "", \
              action_dataset = "", \
              send_email = "", \
              email_to = "", \
              queries_type = "", \
              threshold_id = "", \
              threshold_cov = "", \
              my_file = None):
        
        sys.stderr.write("server.py: request to /mapmarkers\n")
        
        cherrypy.session['session_token'] = "1"
        cherrypy.session['input_query'] = input_query
        cherrypy.session['input_multiple'] = input_multiple
        cherrypy.session['input_sort'] = input_sort
        cherrypy.session['input_genes'] = input_genes
        
        if load_annot == "1": cherrypy.session['load_annot'] = load_annot
        else: cherrypy.session['load_annot'] = "0"
        
        if input_extend == "1": cherrypy.session['input_extend'] = input_extend
        else: cherrypy.session['input_extend'] = "0"
        
        cherrypy.session['genes_window_cm'] = genes_window_cm
        cherrypy.session['genes_window_bp'] = genes_window_bp
        cherrypy.session['input_maps'] = input_maps
        
        #sys.stderr.write("server run "+str(input_maps)+"\n")
        
        #if input_databases:
        cherrypy.session['input_databases'] = input_databases
        #else:
        #    input_databases = ""
        #    cherrypy.session['input_databases'] = ""
        
        cherrypy.session['action_blast'] = action_blast
        cherrypy.session['action_dataset'] = action_dataset
        
        if send_email == "1": cherrypy.session['send_email'] = send_email
        else: cherrypy.session['send_email'] = "0"
            
        cherrypy.session['email_to'] = email_to
        cherrypy.session['queries_type'] = queries_type
        cherrypy.session['threshold_id'] = threshold_id
        cherrypy.session['threshold_cov'] = threshold_cov
        
        output = mapmarkers.mapmarkers(action_blast, action_dataset, input_query, my_file, \
                                       input_multiple, input_sort, input_genes, load_annot, \
                                       input_extend, genes_window_cm, genes_window_bp, \
                                       input_maps, input_databases, \
                                       queries_type, threshold_id, threshold_cov, \
                                       send_email, email_to)
        
        return output

sys.stderr.write("Starting server...\n")

root = Root()
root.mapmarkers = Mapmarkers()

sys.stderr.write("\tcherrypy paths loaded\n")

global_conf = os.path.join(os.path.dirname(__file__), ResourcesMng.get_config_file())

sys.stderr.write("\tcherrypy conf file loaded\n")

def start_standalone():
    sys.stderr.write("\tQUICKSTART STDALONE\n")
    cherrypy.quickstart(root, script_name="/"+ResourcesMng.get_app_name(), config=global_conf)

#
# If we're not being imported, it means we should be running stand-alone.
#
if __name__ == '__main__':
    start_standalone()

#def start_modpython():
#    cherrypy.engine.SIGHUP = None
#    cherrypy.engine.SIGTERM = None
#    cherrypy.config.update(global_conf)
#    cherrypy.tree.mount(root, script_name='/', config=global_conf)
#    cherrypy.engine.start(blocking=False)

## END