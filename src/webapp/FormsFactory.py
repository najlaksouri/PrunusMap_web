#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FormsFactory.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class FormsFactory(object):
    
    @staticmethod
    def get_align_form_new(self, query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           extend = "", extend_cm = "", extend_bp = "",
                           maps = "", send_email = "", email_to = "", user_file = None,
                           queries_type = "", threshold_id = "", threshold_cov = ""):
        
        form = AlignForm()
        
        form.set_query(query)
        form.set_multiple(multiple)
        form.set_sort(sort)
        form.set_show_markers(show_markers)
        form.set_show_genes(show_genes)
        form.set_show_anchored(show_anchored)
        form.set_extend(extend)
        form.set_extend_cm(extend_cm)
        form.set_extend_bp(extend_bp)
        form.set_maps(maps)
        form.set_send_email(send_email)
        form.set_email_to(email_to)
        form.set_user_file(user_file)
        
        form.set_queries_type(queries_type)
        form.set_threshold_id(threshold_id)
        form.set_threshold_cov(threshold_cov)
        
        return form
    
    @staticmethod
    def get_align_form_empty(DEFAULT_GENES_WINDOW_CM,
                             DEFAULT_GENES_WINDOW_BP,
                             DEFAULT_THRESHOLD_ID,
                             DEFAULT_THRESHOLD_COV):
        
        align_form = AlignForm()
        
        align_form.set_extend_cm(DEFAULT_GENES_WINDOW_CM)
        align_form.set_extend_bp(DEFAULT_GENES_WINDOW_BP)
        align_form.set_threshold_id(DEFAULT_THRESHOLD_ID)
        align_form.set_threshold_cov(DEFAULT_THRESHOLD_COV)
        
        return align_form
    
    @staticmethod
    def get_align_form_session(session):
        align_form = None
        
        align_form = AlignForm.init_from_session(session)
        
        return align_form
    
    @staticmethod
    def get_find_form_new(self, query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           load_annot = "", extend = "", extend_cm = "", extend_bp = "",
                           maps = "", send_email = "", email_to = "", user_file = None):
        
        form = FindForm()
        
        form.set_query(query)
        form.set_multiple(multiple)
        form.set_sort(sort)
        form.set_show_markers(show_markers)
        form.set_show_genes(show_genes)
        form.set_show_anchored(show_anchored)
        form.set_extend(extend)
        form.set_extend_cm(extend_cm)
        form.set_extend_bp(extend_bp)
        form.set_maps(maps)
        form.set_send_email(send_email)
        form.set_email_to(email_to)
        form.set_user_file(user_file)
        
        return form
    
    @staticmethod
    def get_find_form_empty(DEFAULT_GENES_WINDOW_CM,
                            DEFAULT_GENES_WINDOW_BP):
        
        find_form = FindForm()
        
        find_form.set_extend_cm(DEFAULT_GENES_WINDOW_CM)
        find_form.set_extend_bp(DEFAULT_GENES_WINDOW_BP)
        
        return find_form
    
    @staticmethod
    def get_find_form_session(session):
        find_form = None
        
        find_form = FindForm.init_from_session(session)
        
        return find_form

class InputForm(object):
    
    SESSION = "session_token"
    QUERY = "query"
    MULTIPLE = "multiple"
    SORT = "sort"
    SHOW_MARKERS = "show_markers"
    SHOW_GENES = "show_genes"
    SHOW_ANCHORED = "show_anchored"
    EXTEND = "extend"
    EXTEND_CM = "extend_cm"
    EXTEND_BP = "extend_bp"
    MAPS = "maps"
    SEND_EMAIL = "send_email"
    EMAIL_TO = "email_to"
    USER_FILE = "user_file"
    
    _query = ""
    _multiple = ""
    _sort = ""
    _show_markers = ""
    _show_genes = ""
    _show_anchored = ""
    _extend = ""
    _extend_cm = ""
    _extend_bp = ""
    _maps = ""
    _send_email = ""
    _email_to = ""
    _user_file = None
    
    _is_empty = True
    
    def get_query(self):
        return self._query
    
    def set_query(self, query):
        self._query = query
    
    def get_multiple(self):
        return self._multiple
    
    def set_multiple(self, multiple):
        self._multiple = multiple
    
    def get_sort(self):
        return self._sort
    
    def set_sort(self, sort):
        self._sort = sort
    
    def get_show_markers(self):
        return self._show_markers
    
    def set_show_markers(self, show_markers):
        self._show_markers = show_markers
    
    def get_show_genes(self):
        return self._show_genes
    
    def set_show_genes(self, show_genes):
        self._show_genes = show_genes
    
    def get_show_anchored(self):
        return self._show_anchored
    
    def set_show_anchored(self, show_anchored):
        self._show_anchored = show_anchored
    
    def get_extend(self):
        return self._extend
    
    def set_extend(self, extend):
        self._extend = extend
    
    def get_extend_cm(self):
        return self._extend_cm
    
    def set_extend_cm(self, extend_cm):
        self._extend_cm = extend_cm
    
    def get_extend_bp(self, ):
        return self._extend_bp
    
    def set_extend_bp(self, extend_bp):
        self._extend_bp = extend_bp
    
    def get_maps(self, ):
        return self._maps
    
    def set_maps(self, maps):
        self._maps = maps
        
    def get_send_email(self, ):
        return self._send_email
    
    def set_send_email(self, send_email):
        self._send_email = send_email
    
    def get_email_to(self, ):
        return self._email_to
    
    def set_email_to(self, email_to):
        self._email_to = email_to
    
    def get_user_file(self):
        return self._user_file
    
    def set_user_file(self, user_file):
        self._user_file = user_file
    
    def is_empty(self, ):
        return self._is_empty
    
    def set_empty(self, is_empty):
        self._is_empty = is_empty
    
    def set_session_input_form(self, session):
        
        session[self.SESSION] = self.SESSION
        session[self.ACTION] = self.ACTION
        
        session[self.QUERY] = self.get_query()
        session[self.MULTIPLE] = self.get_multiple()
        session[self.SORT] = self.get_sort()
        session[self.SHOW_MARKERS] = self.get_show_markers()
        session[self.SHOW_GENES] = self.get_show_genes()
        session[self.SHOW_ANCHORED] = self.get_show_anchored()
        
        if self.get_extend() == "1":
            session[self.EXTEND] = self.get_extend()
        else:
            session[self.EXTEND] = "0"
        
        session[self.EXTEND_CM] = self.get_extend_cm()
        session[self.EXTEND_BP] = self.get_extend_bp()
        session[self.MAPS] = self.get_maps()
        
        if self.get_send_email() == "1":
            session[self.SEND_EMAIL] = self.get_send_email()
        else:
            session[self.SEND_EMAIL] = "0"
            
        session[self.EMAIL_TO] = self.get_email_to()
        
        return
    
    @staticmethod
    def init_from_session(session, form):
        if session[form.ACTION] and session[form.ACTION] != "":
            form._query = session.get(form.QUERY)
        else: # Comes from find action
            form._query = ""
        
        form._multiple = session.get(form.MULTIPLE)
        form._sort = session.get(form.SORT)
        form._show_markers = session.get(form.SHOW_MARKERS)
        form._show_genes = session.get(form.SHOW_GENES)
        form._show_anchored = session.get(form.SHOW_ANCHORED)
        form._extend = session.get(form.EXTEND)
        form._extend_cm = session.get(form.EXTEND_CM)
        form._extend_bp = session.get(form.EXTEND_BP)
        form._maps = session.get(form.MAPS)
        form._send_email = session.get(form.SEND_EMAIL)
        form._email_to = session.get(form.EMAIL_TO)
        form._user_file = session.get(form.USER_FILE)
        
        form._is_empty = False
        
        return form
    
class AlignForm(InputForm):
    
    ACTION = "action_blast"

    QUERIES_TYPE = "queries_type"
    THRESHOLD_ID = "threshold_id"
    THRESHOLD_COV = "threshold_cov"
    
    _queries_type = ""
    _threshold_id = ""
    _threshold_cov = ""
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session):
        
        new_form = AlignForm()
        
        InputForm.init_from_session(session, new_form)
        
        new_form._queries_type = session.get(new_form.QUERIES_TYPE)
        new_form._threshold_id = session.get(new_form.THRESHOLD_ID)
        new_form._threshold_cov = session.get(new_form.THRESHOLD_COV)
        
        new_form._is_empty = False
        
        return new_form
    
    def set_session(self, session):
        
        self.set_session_input_form(session)
        
        session[self.QUERIES_TYPE] = self.get_queries_type()
        session[self.THRESHOLD_ID] = self.get_threshold_id()
        session[self.THRESHOLD_COV] = self.get_threshold_cov()
        
        return
    
    def get_queries_type(self, ):
        return self._queries_type
    
    def set_queries_type(self, queries_type):
        self._queries_type = queries_type
    
    def get_threshold_id(self, ):
        return self._threshold_id
    
    def set_threshold_id(self, threshold_id):
        self._threshold_id = threshold_id
    
    def get_threshold_cov(self, ):
        return self._threshold_cov
    
    def set_threshold_cov(self, threshold_cov):
        self._threshold_cov = threshold_cov
    

class FindForm(InputForm):
    
    ACTION = "action_dataset"
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session):
        
        new_form = FindForm()
        
        InputForm.init_from_session(session, new_form)
        
        return new_form
    
    def set_session(self, session):
        
        self.set_session_input_form(session)
        
        return

## END