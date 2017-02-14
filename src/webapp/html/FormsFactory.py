#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FormsFactory.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class FormsFactory(object):
    
    @staticmethod
    def get_empty_align_form(DEFAULT_GENES_WINDOW_CM,
                             DEFAULT_GENES_WINDOW_BP,
                             DEFAULT_THRESHOLD_ID,
                             DEFAULT_THRESHOLD_COV):
        align_form = None
        
        align_form = AlignForm()
        align_form.set_genes_window_cm(DEFAULT_GENES_WINDOW_CM)
        align_form.set_genes_window_bp(DEFAULT_GENES_WINDOW_BP)
        align_form.set_threshold_id(DEFAULT_THRESHOLD_ID)
        align_form.set_threshold_cov(DEFAULT_THRESHOLD_COV)
        
        return align_form
    
    @staticmethod
    def get_align_form(session):
        align_form = None
        
        align_form = AlignForm.init_from_session(session)
        
        return align_form
    
    @staticmethod
    def get_empty_find_form(DEFAULT_GENES_WINDOW_CM,
                            DEFAULT_GENES_WINDOW_BP):
        find_form = None
        
        find_form = FindForm()
        find_form.set_genes_window_cm(DEFAULT_GENES_WINDOW_CM)
        find_form.set_genes_window_bp(DEFAULT_GENES_WINDOW_BP)
        
        return find_form
    
    @staticmethod
    def get_find_form(session):
        find_form = None
        
        find_form = FindForm.init_from_session(session)
        
        return find_form
    
class AlignForm(object):
    
    ACTION = "action_blast"
    INPUT_QUERY = "input_query"
    INPUT_MULTIPLE = "input_multiple"
    INPUT_SORT = "input_sort"
    INPUT_GENES = "input_genes"
    LOAD_ANNOT = "load_annot"
    INPUT_EXTEND = "input_extend"
    GENES_WINDOW_CM = "genes_window_cm"
    GENES_WINDOW_BP = "genes_window_bp"
    INPUT_MAPS = "input_maps"
    INPUT_DATABASES = "input_databases"
    SEND_EMAIL = "send_email"
    EMAIL_TO = "email_to"
    QUERIES_TYPE = "queries_type"
    THRESHOLD_ID = "threshold_id"
    THRESHOLD_COV = "threshold_cov"
    
    _input_query = ""
    _input_multiple = ""
    _input_sort = ""
    _input_genes = ""
    _load_annot = ""
    _input_extend = ""
    _genes_window_cm = ""
    _genes_window_bp = ""
    _input_maps = ""
    _input_databases = ""
    _send_email = ""
    _email_to = ""
    _queries_type = ""
    _threshold_id = ""
    _threshold_cov = ""
    _is_empty = True
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session):
        
        align_form = AlignForm()
        
        if session[AlignForm.ACTION] and session[AlignForm.ACTION] != "":
            align_form._input_query = session.get(AlignForm.INPUT_QUERY)
        else: # Comes from find action
            align_form._input_query = ""
        
        align_form._input_multiple = session.get(AlignForm.INPUT_MULTIPLE)
        align_form._input_sort = session.get(AlignForm.INPUT_SORT)
        align_form._input_genes = session.get(AlignForm.INPUT_GENES)
        align_form._load_annot = session.get(AlignForm.LOAD_ANNOT)
        
        align_form._input_extend = session.get(AlignForm.INPUT_EXTEND)
        align_form._genes_window_cm = session.get(AlignForm.GENES_WINDOW_CM)
        align_form._genes_window_bp = session.get(AlignForm.GENES_WINDOW_BP)
        align_form._input_maps = session.get(AlignForm.INPUT_MAPS)
        align_form._input_databases = session.get(AlignForm.INPUT_DATABASES)
        
        align_form._send_email = session.get(AlignForm.SEND_EMAIL)
        align_form._email_to = session.get(AlignForm.EMAIL_TO)
        align_form._queries_type = session.get(AlignForm.QUERIES_TYPE)
        align_form._threshold_id = session.get(AlignForm.THRESHOLD_ID)
        align_form._threshold_cov = session.get(AlignForm.THRESHOLD_COV)
        
        align_form._is_empty = False
        
        return align_form
    
    def get_input_query(self):
        return self._input_query
    
    def get_input_multiple(self):
        return self._input_multiple
    
    def get_input_sort(self):
        return self._input_sort
    
    def get_input_genes(self, ):
        return self._input_genes
    
    def get_load_annot(self, ):
        return self._load_annot
    
    def get_input_extend(self, ):
        return self._input_extend
    
    def get_genes_window_cm(self, ):
        return self._genes_window_cm
    
    def set_genes_window_cm(self, genes_window_cm):
        self._genes_window_cm = genes_window_cm
    
    def get_genes_window_bp(self, ):
        return self._genes_window_bp
    
    def set_genes_window_bp(self, genes_window_bp):
        self._genes_window_bp = genes_window_bp
    
    def get_input_maps(self, ):
        return self._input_maps
    
    def get_input_databases(self, ):
        return self._input_databases
    
    def get_send_email(self, ):
        return self._send_email
    
    def get_email_to(self, ):
        return self._email_to
    
    def get_queries_type(self, ):
        return self._queries_type
    
    def get_threshold_id(self, ):
        return self._threshold_id
    
    def set_threshold_id(self, threshold_id):
        self._threshold_id = threshold_id
    
    def get_threshold_cov(self, ):
        return self._threshold_cov
    
    def set_threshold_cov(self, threshold_cov):
        self._threshold_cov = threshold_cov
    
    def is_empty(self, ):
        return self._is_empty

class FindForm(object):
    
    ACTION = "action_dataset"
    INPUT_QUERY = "input_query"
    INPUT_MULTIPLE = "input_multiple"
    INPUT_SORT = "input_sort"
    INPUT_GENES = "input_genes"
    LOAD_ANNOT = "load_annot"
    INPUT_EXTEND = "input_extend"
    GENES_WINDOW_CM = "genes_window_cm"
    GENES_WINDOW_BP = "genes_window_bp"
    INPUT_MAPS = "input_maps"
    INPUT_DATABASES = "input_databases"
    SEND_EMAIL = "send_email"
    EMAIL_TO = "email_to"
    QUERIES_TYPE = "queries_type"
    THRESHOLD_ID = "threshold_id"
    THRESHOLD_COV = "threshold_cov"
    
    _input_query = ""
    _input_multiple = ""
    _input_sort = ""
    _input_genes = ""
    _load_annot = ""
    _input_extend = ""
    _genes_window_cm = ""
    _genes_window_bp = ""
    _input_maps = ""
    _input_databases = ""
    _send_email = ""
    _email_to = ""
    _queries_type = ""
    _threshold_id = ""
    _threshold_cov = ""
    _is_empty = True
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session):
        
        find_form = FindForm()
        
        if session[FindForm.ACTION] and session[FindForm.ACTION] != "":
            find_form._input_query = session.get(FindForm.INPUT_QUERY)
        else: # Comes from align action
            find_form._input_query = ""
        
        find_form._input_multiple = session.get(FindForm.INPUT_MULTIPLE)
        find_form._input_sort = session.get(FindForm.INPUT_SORT)
        find_form._input_genes = session.get(FindForm.INPUT_GENES)
        find_form._load_annot = session.get(FindForm.LOAD_ANNOT)
        
        find_form._input_extend = session.get(FindForm.INPUT_EXTEND)
        find_form._genes_window_cm = session.get(FindForm.GENES_WINDOW_CM)
        find_form._genes_window_bp = session.get(FindForm.GENES_WINDOW_BP)
        find_form._input_maps = session.get(FindForm.INPUT_MAPS)
        
        find_form._send_email = session.get(FindForm.SEND_EMAIL)
        find_form._email_to = session.get(FindForm.EMAIL_TO)
        
        find_form._is_empty = False
        
        return find_form
    
    def get_input_query(self):
        return self._input_query
    
    def get_input_multiple(self):
        return self._input_multiple
    
    def get_input_sort(self):
        return self._input_sort
    
    def get_input_genes(self, ):
        return self._input_genes
    
    def get_load_annot(self, ):
        return self._load_annot
    
    def get_input_extend(self, ):
        return self._input_extend
    
    def get_genes_window_cm(self, ):
        return self._genes_window_cm
    
    def set_genes_window_cm(self, genes_window_cm):
        self._genes_window_cm = genes_window_cm
    
    def get_genes_window_bp(self, ):
        return self._genes_window_bp
    
    def set_genes_window_bp(self, genes_window_bp):
        self._genes_window_bp = genes_window_bp
    
    def get_input_maps(self, ):
        return self._input_maps
    
    def get_send_email(self, ):
        return self._send_email
    
    def get_email_to(self, ):
        return self._email_to
    
    def is_empty(self, ):
        return self._is_empty

## END