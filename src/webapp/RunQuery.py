#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RunQuery.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys
import cherrypy

from barleymapcore.db.PathsConfig import PathsConfig

from FormsFactory import FormsFactory
from Bmap import Bmap

from WebApp import VERBOSE, DEFAULT_SORT_PARAM, PATHS_CONFIG, MAX_QUERIES
from Bmap import FIND_ACTION, ALIGN_ACTION

class Root():
    # Index method for direct requests from outside barleymap by url
    # For example, T3 or GrainGenes links
    # Maybe, this could be implemented as REST API in the future
    @cherrypy.expose
    def index(self, action = "", input_query = "", input_multiple = "", input_sort = "", input_genes = "",
              load_annot = "", genes_window = "",
              input_maps = "", send_email = "", email_to = ""):
        
        sys.stderr.write("server.py: request to T3 links\n")
        
        verbose_param = VERBOSE
        
        #config_path_dict = read_paths("paths.conf") # data_utils.read_paths
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
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
        
        find_form = FormsFactory.get_find_form_new(query, multiple, sort,
                                                   show_markers, show_genes, show_anchored,
                                                   extend, extend_cm, extend_bp,
                                                   maps, send_email, email_to, user_file)
        
        find_form.set_session(cherrypy.session)
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
        
        bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, MAX_QUERIES, FIND_ACTION, VERBOSE)
        output = bmap.find(find_form)
        
        return output
    
    @cherrypy.expose
    def align(self, action = "", query = "", multiple = "", sort = "",
              show_markers = "", show_genes = "", show_anchored = "",
              load_annot = "", extend = "", extend_cm = "", extend_bp = "",
              maps = "", send_email = "", email_to = "", user_file = None,
              queries_type = "", threshold_id = "", threshold_cov = ""):
        
        sys.stderr.write("server.py: request to /mapmarkers/align\n")
        
        align_form = FormsFactory.get_align_form_new(query, multiple, sort,
                                                   show_markers, show_genes, show_anchored,
                                                   extend, extend_cm, extend_bp,
                                                   maps, send_email, email_to, user_file,
                                                     queries_type, threshold_id, threshold_cov)
        
        align_form.set_session(cherrypy.session)
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
        
        bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, MAX_QUERIES, ALIGN_ACTION, VERBOSE)
        output = bmap.align(align_form)
        
        return output
    
## END