#!/usr/bin/env python
# -*- coding: utf-8 -*-

# server.py is part of Barleymap web app.
# Copyright (C) 2013-2014  Carlos P Cantalapiedra.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import os, sys
import cherrypy

from barleymapcore.db.PathsConfig import PathsConfig

import webapp.WebApp as WebApp
import webapp.RunQuery as RunQuery

APP_NAME = "barleymap"
MOUNT_POINT = "/"+APP_NAME

SERVER_CONFIG_FILE = "server.conf"
CONFIG_FILE = "bmap.conf"
PATHS_CONFIG = "paths_config"

N_THREADS = 2
MAX_QUERIES = 100

DEFAULT_THRESHOLD_ID = 98.0
DEFAULT_THRESHOLD_COV = 95.0
DEFAULT_ALIGNER = "gmap"
DEFAULT_MAPS = "morex_genome"
DEFAULT_GENES_WINDOW_CM = 0.5
DEFAULT_GENES_WINDOW_BP = 1000000

VERBOSE = False

## Loads server and barleymap configuration,
## loads the app into the server,
## and deploys the server
def start_standalone():
    sys.stderr.write("Starting server...\n")
    
    ############## LOAD SERVER CONFIGURATION
    ########################################
    server_conf_file = os.path.join(os.path.dirname(__file__), SERVER_CONFIG_FILE)
    cherrypy.config.update(server_conf_file)
    
    sys.stderr.write("\tcherrypy configuration files loaded\n")
    
    ############### LOAD THE BMAP APP
    #################################
    # Classes with exposed methods
    root = WebApp.Root(MOUNT_POINT, PATHS_CONFIG, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV, DEFAULT_ALIGNER, DEFAULT_MAPS,
                       DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP, VERBOSE)
    
    root.mapmarkers = RunQuery.Root(MOUNT_POINT, PATHS_CONFIG, APP_NAME, N_THREADS, MAX_QUERIES, VERBOSE)
    
    # Mount app on server, with webapp config file
    bmap_conf_file = os.path.join(os.path.dirname(__file__), CONFIG_FILE)
    
    app = cherrypy.tree.mount(root, script_name=MOUNT_POINT, config=bmap_conf_file)
    
    sys.stderr.write("\t"+APP_NAME+" mounted\n")
    
    # Add barleymap configuration
    #bmap_conf_dict = _load_globals()
    abs_path = os.path.dirname(os.path.abspath(__file__))
    paths_config = PathsConfig()
    paths_config.load_config(abs_path)
    bmap_conf_dict = {PATHS_CONFIG:paths_config.as_dict()}
    app.merge(bmap_conf_dict)
    
    ################ STARTING THE SERVER
    ####################################
    if hasattr(cherrypy.engine, "signal_handler"):
        cherrypy.engine.signal_handler.subscribe()
    if hasattr(cherrypy.engine, "console_control_handler"):
        cherrypy.engine.console_control_handler.subscribe()
    
    cherrypy.engine.start()
    
    sys.stderr.write("Server started. Accepting requests...\n")
    
    cherrypy.engine.block() ## Here the server stops to accept requests
    
    ####################################
    
    #cherrypy.quickstart(root, script_name="/"+ResourcesMng.get_app_name(), config=global_conf_dict)
    
    sys.stderr.write("Server stopped.\n")
    
    return

##########################
########################## START
if __name__ == '__main__':
    sys.stderr.write("In the beginning...\n")
    start_standalone()
    sys.stderr.write("...towards an end.\n")

## END