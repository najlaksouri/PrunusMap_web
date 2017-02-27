#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RunQuery.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys
import cherrypy

from FormsFactory import FormsFactory

class Root():
    # Index method for direct requests from outside barleymap by url
    # For example, T3 or GrainGenes links
    # Maybe, this could be implemented as REST API in the future
    @cherrypy.expose
    def index(self, input_query = "", input_multiple = "", input_sort = "", input_genes = "",
              load_annot = "", genes_window = "",
              input_maps = "", send_email = "", email_to = ""):
        
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
        
        # Genes information: on marker
        input_genes = "marker"
        input_extend = "1"
        user_file = None
        
        output = self.find(input_query, input_multiple, input_sort, input_genes,
                          load_annot, input_exted, genes_window, genes_window,
                          input_maps, send_email, email_to, user_file)
        
        return output
    
    @cherrypy.expose
    def find(self, input_query = "", input_multiple = "", input_sort = "", input_genes = "",
             load_annot = "", input_extend = "", genes_window_cm = "", genes_window_bp = "",
              input_maps = "", send_email = "", email_to = "", user_file = None):
        
        sys.stderr.write("server.py: request to /mapmarkers/find\n")
        
        find_form = FormsFactory.get_new_find_form(input_query, input_multiple, input_sort, input_genes,
                                                     load_annot, input_extend, genes_window_cm, genes_window_bp,
                                                     input_maps, send_email, email_to, user_file)
        
        find_form.set_session(cherrypy.session)
        
        output = mapmarkers.find(find_form)
        
        return output
    
    @cherrypy.expose
    def align(self, input_query = "", input_multiple = "", input_sort = "", input_genes = "",
              load_annot = "", input_extend = "", genes_window_cm = "", genes_window_bp = "",
              input_maps = "", input_databases = "", send_email = "", email_to = "",
              queries_type = "", threshold_id = "", threshold_cov = "", user_file = None):
        
        sys.stderr.write("server.py: request to /mapmarkers/align\n")
        
        align_form = FormsFactory.get_new_align_form(input_query, input_multiple, input_sort, input_genes,
                                                     load_annot, input_extend, genes_window_cm, genes_window_bp,
                                                     input_maps, input_databases, send_email, email_to,
                                                     queries_type, threshold_id, threshold_cov, user_file)
        
        align_form.set_session(cherrypy.session)
        
        output = mapmarkers.align(align_form)
        
        return output
    
## END