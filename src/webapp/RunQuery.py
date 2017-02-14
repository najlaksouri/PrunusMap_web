#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RunQuery.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys
import cherrypy

class Root():
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
    
## END