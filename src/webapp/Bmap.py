#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bmap.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys, tempfile, os

from barleymapcore.db.ConfigBase import ConfigBase
from barleymapcore.db.MapsConfig import MapsConfig
from barleymapcore.db.DatasetsConfig import DatasetsConfig
from barleymapcore.datasets.DatasetsFacade import DatasetsFacade
from barleymapcore.annotators.GenesAnnotator import AnnotatorsFactory
from barleymapcore.maps.MapMarkers import MapMarkers

MAPS_CONF = ConfigBase.MAPS_CONF
DATASETS_CONF = ConfigBase.DATASETS_CONF
DATASETS_ANNOTATION_CONF = ConfigBase.DATASETS_ANNOTATION_CONF
ANNOTATION_TYPES_CONF = ConfigBase.ANNOTATION_TYPES_CONF

FIND_ACTION = "find"
ALIGN_ACTION = "align"

class Bmap(object):
    _paths_config = None
    
    _default_sort = None
    _max_queries = None
    _action = None
    
    _verbose = False
    
    def __init__(self, paths_config, default_sort, max_queries, action, verbose = False):
        self._paths_config = paths_config
        self._default_sort = default_sort
        self._max_queries = max_queries
        self._action = action
        self._verbose = verbose
    
    def __tmpfile_from_list(self, input_list, tmp_dir):
        input_file_name = ""
        input_file = None
        try:
            (file_desc, input_file_name) = tempfile.mkstemp(suffix="_mapm", dir=tmp_dir)
            input_file = os.fdopen(file_desc, 'w')
            
            for array_line in input_list:
                input_file.write(array_line+"\n")
            input_file.close()
            
        except Exception:
            raise
        finally:
            if input_file:
                input_file.close()
        
        return input_file_name
    
    def __check_input_query(self, input_lines):
        
        action = self._action
        ## Preprocessing and format control of input data (either uploaded file and text area)
        # FASTA FORMAT
        if input_lines[0].startswith(">"):
            if action == ALIGN_ACTION:
                
                ## LIMIT OF QUERIES ACCEPTED IN THE WEB 20140529
                num_queries = len([x for x in input_lines if x.startswith(">")])
                
                max_queries = self._max_queries#ResourcesMng.get_max_queries()
                
                if num_queries > max_queries:
                    if self._verbose: sys.stderr.write("NUM QUERIES ******************** "+str(num_queries)+" ---- "+str(max_queries)+"\n")
                    raise m2pException("The web application only accepts currently "+str(max_queries)+" in the alignment mode.\
                                       We counted "+str(num_queries)+" in your request.\
                                       We would recommend you to use the standalone version.")
                
                # OK
                
            elif action == FIND_ACTION:
                raise m2pException("Find action requires a list of identifiers. Avoid FASTA format (e.g. lines starting with \">\")") 
            else:
                raise m2pException("Unknown action requested.")
                
        # NO fasta format
        else:
            if action == ALIGN_ACTION:
                raise m2pException("The input for "+ALIGN_ACTION+" action must be in FASTA format.")
            elif action == FIND_ACTION:
                pass # OK
            else:
                raise m2pException("Unknown action requested.")
        
        return

    def __get_input_file(self, input_form):
        
        query = input_form.get_query()
        user_file = input_form.get_user_file()
        
        if ((not query) or (query.strip() == "")) and (not user_file or not user_file.file):
            raise m2pException("No input data provided.")
        
        if user_file and user_file.file: # Uploaded file
            input_lines = []
            for line in user_file.file:
                input_lines.append(line)
        else: # Text Area
            input_lines = query.strip().split("\n")
        
        # Check input data
        self.__check_input_query(input_lines)
        
        # Input tmp file
        tmp_dir = self._paths_config.get_tmp_files_path()
        input_file_name = self.__tmpfile_from_list(input_lines, tmp_dir)
        
        return input_file_name
    
    ##
    def align(self, align_form):
        
        input_file_name = self.__get_input_file(find_form)
        
        ## Configuration files and paths
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()
        
        output = "OK"
        
        return output
    
    ##
    def find(self, find_form):
        
        input_file_name = self.__get_input_file(find_form)
        
        ## Configuration files and paths
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()
        
        # Datasets
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file, self._verbose)
        datasets_ids = datasets_config.get_datasets().keys()
        
        # Maps
        maps_conf_file = __app_path+MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, self._verbose)
        if find_form.get_maps():
            maps_names = find_form.get_maps()
            maps_ids = maps_config.get_maps_ids(maps_names.strip().split(","))
        else:
            maps_ids = maps_config.get_maps().keys()
            maps_names = ",".join(maps_config.get_maps_names(maps_ids))
        
        maps_path = paths_config.get_maps_path() #__app_path+config_path_dict["maps_path"]
        
        # Datasets
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file, self._verbose)
        
        ############ ALIGNMENTS - DATASETS
        # Load configuration paths
        datasets_path = paths_config.get_datasets_path() #__app_path+config_path_dict["datasets_path"]
        datasets_facade = DatasetsFacade(datasets_config, datasets_path, verbose = self._verbose)
        
        ############ Pre-loading of some objects
        ############
        #load_annot = True always
        # GenesAnnotator
        if find_form.get_show_genes():
            ## Load annotation config
            dsannot_conf_file = __app_path+DATASETS_ANNOTATION_CONF
            anntypes_conf_file = __app_path+ANNOTATION_TYPES_CONF
            annot_path = paths_config.get_annot_path()
            
            annotator = AnnotatorsFactory.get_annotator(dsannot_conf_file, anntypes_conf_file, annot_path, self._verbose)
        else:
            annotator = None
            
        # OutputFacade
        #if collapsed_view:
        #    outputPrinter = OutputFacade.get_collapsed_printer(sys.stdout, verbose = self._verbose, beauty_nums = beauty_nums, show_headers = True)
        #else:
        #    outputPrinter = OutputFacade.get_expanded_printer(sys.stdout, verbose = self._verbose, beauty_nums = beauty_nums, show_headers = True)
        
        ########### Create maps
        ###########
        sort_param = find_form.get_sort()
        multiple_param = find_form.get_multiple()
        show_markers = find_form.get_show_markers()
        show_genes = find_form.get_show_genes()
        show_anchored = find_form.get_show_anchored()
        extend_window = find_form.get_extend()
        collapsed_view = False
        constrain_fine_mapping = True
        
        for map_id in maps_ids:
            sys.stderr.write("Bmap.find: Map "+map_id+"\n")
            map_config = maps_config.get_map_config(map_id)
            
            sort_by = map_config.check_sort_param(map_config, sort_param, self._default_sort)
            
            mapMarkers = MapMarkers(maps_path, map_config, datasets_facade, self._verbose)
            
            mapMarkers.retrieve_mappings(input_file_name, datasets_ids,
                                        sort_by, multiple_param)
            
            mapMarkers.enrichment(annotator, show_markers, show_genes, show_anchored,
                                  datasets_facade, extend_window, collapsed_view, constrain_fine_mapping)
            
            mapping_results = mapMarkers.get_mapping_results()
            
            ############################################################ OUTPUT
        
        output = "OK"
        
        return output

## END