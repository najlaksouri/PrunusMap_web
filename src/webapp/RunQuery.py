#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RunQuery.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys, traceback
import cherrypy

from barleymapcore.db.PathsConfig import PathsConfig

from html.HtmlLayout import HtmlLayout
from FormsFactory import FormsFactory
from Bmap import Bmap

from Bmap import FIND_ACTION, ALIGN_ACTION

DEFAULT_SORT_PARAM = "map default"

class Root():
    
    MOUNT_POINT = None
    PATHS_CONFIG = None
    APP_NAME = None
    N_THREADS = None
    MAX_QUERIES = None
    
    VERBOSE = False
    
    def __init__(self, MOUNT_POINT, PATHS_CONFIG, APP_NAME, N_THREADS, MAX_QUERIES, VERBOSE):
        self.MOUNT_POINT = MOUNT_POINT
        self.PATHS_CONFIG = PATHS_CONFIG
        self.APP_NAME = APP_NAME
        self.N_THREADS = N_THREADS
        self.MAX_QUERIES = MAX_QUERIES
        self.VERBOSE = VERBOSE
    
    def _get_html_layout(self):
        return HtmlLayout(self.MOUNT_POINT)
    
    # Index method for direct requests from outside barleymap by url
    # For example, T3 or GrainGenes links
    # Maybe, this could be implemented as REST API in the future
    @cherrypy.expose
    def index(self, action = "", input_query = "", input_multiple = "", input_sort = "", input_genes = "",
              load_annot = "", genes_window = "",
              input_maps = "", send_email = "", email_to = ""):
        
        sys.stderr.write("server.py: request to T3 links\n")
        
        verbose_param = self.VERBOSE
        
        #config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
        __app_path = paths_config.get_app_path()#config_path_dict["app_path"]
        
        # Load all configured maps
        maps_conf_file = paths_config.get_maps_path()#__app_path+"conf/maps.conf"
        (maps_names, maps_ids) = load_data(maps_conf_file, verbose = verbose_param) # data_utils.load_data
        if len(maps_names) > 1:
            input_maps = maps_names.split(",")
        else:
            input_maps = maps_names
        
        # Genes information: on marker
        input_genes = "marker"
        input_extend = "1"
        user_file = None
        
        output = self.find(input_query, input_multiple, input_sort, input_genes,
                          load_annot, input_exted, genes_window, genes_window,
                          input_maps, send_email, email_to, user_file)
        
        return output
    
    @cherrypy.expose
    def find(self, action = "", query = "", multiple = "", sort = "",
             show_markers = "", show_genes = "", show_anchored = "",
             load_annot = "", extend = "", extend_cm = "", extend_bp = "",
             maps = "", send_email = "", email_to = "", user_file = None):
        
        sys.stderr.write("server.py: request to /mapmarkers/find\n")
        
        try:
            
            form = FormsFactory.get_find_form_new(query, multiple, sort,
                                                       show_markers, show_genes, show_anchored,
                                                       extend, extend_cm, extend_bp,
                                                       maps, send_email, email_to, user_file)
            
            form.set_session(cherrypy.session)
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, self.MAX_QUERIES, FIND_ACTION, self.N_THREADS, self.APP_NAME, self.VERBOSE)
            
            results = bmap.find(form)
            
            csv_files = bmap.csv_files(results, form)
            
            output = bmap.output(results, form, self._get_html_layout(), csv_files)
            
            bmap.email(form, csv_files)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            raise e
        
        return output
    
    @cherrypy.expose
    def align(self, action = "", query = "", multiple = "", sort = "",
              show_markers = "", show_genes = "", show_anchored = "",
              load_annot = "", extend = "", extend_cm = "", extend_bp = "",
              maps = "", send_email = "", email_to = "", user_file = None,
              aligner = "", threshold_id = "", threshold_cov = ""):
        
        sys.stderr.write("server.py: request to /mapmarkers/align\n")
        
        try:
            form = FormsFactory.get_align_form_new(query, multiple, sort,
                                                   show_markers, show_genes, show_anchored,
                                                   extend, extend_cm, extend_bp,
                                                   maps, send_email, email_to, user_file,
                                                     aligner, threshold_id, threshold_cov)
            
            form.set_session(cherrypy.session)
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, self.MAX_QUERIES, ALIGN_ACTION, self.N_THREADS, self.APP_NAME, self.VERBOSE)
            
            results = bmap.align(form)
            
            csv_files = bmap.csv_files(results, form)
            
            output = bmap.output(results, form, self._get_html_layout(), csv_files)
            
            bmap.email(form, csv_files)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            raise e
        
        return output
    
## END