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

SERVER_CONFIG_FILE = "server.conf"

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
    root = WebApp.Root()
    root.mapmarkers = RunQuery.Root()
    
    # Mount app on server, with webapp config file
    bmap_conf_file = os.path.join(os.path.dirname(__file__), WebApp.CONFIG_FILE)
    
    app = cherrypy.tree.mount(root, script_name=WebApp.MOUNT_POINT, config=bmap_conf_file)
    
    sys.stderr.write("\t"+WebApp.APP_NAME+" mounted\n")
    
    # Add barleymap configuration
    #bmap_conf_dict = _load_globals()
    abs_path = os.path.dirname(os.path.abspath(__file__))
    paths_config = PathsConfig(abs_path, WebApp.VERBOSE)
    #global_conf_dict[WebApp.PATHS_CONFIG] = paths_config.as_dict()
    bmap_conf_dict = {WebApp.PATHS_CONFIG:paths_config.as_dict()}
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