#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WebApp.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys
import cherrypy

from barleymapcore.db.ConfigBase import ConfigBase
from barleymapcore.db.PathsConfig import PathsConfig
from barleymapcore.db.MapsConfig import MapsConfig
from barleymapcore.db.DatabasesConfig import DatabasesConfig

from html.HtmlLayout import HtmlLayout
from FormsFactory import FormsFactory

VERBOSE = False

PATHS_CONFIG = "paths_config"
CONFIG_FILE = "bmap.conf"
APP_NAME = "barleymap"
MOUNT_POINT = "/"+APP_NAME

DEFAULT_THRESHOLD_ID = 98.0
DEFAULT_THRESHOLD_COV = 95.0
DEFAULT_GENES_WINDOW_CM = 0.5
DEFAULT_GENES_WINDOW_BP = 1000000
DEFAULT_SORT_PARAM = "map default"

N_THREADS = 2
MAX_QUERIES = 100

########## MAIL SERVER
# check file in /home/barleymap/email/

class Root():
    
    def _get_html_layout(self):
        
        return HtmlLayout(MOUNT_POINT)
    
    @cherrypy.expose
    def index(self):
        
        sys.stderr.write("server.py: request to /index\n")
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
        
        html_layout = self._get_html_layout()
        
        citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")
        
        contents = [html_layout.main_text(citation)]
        
        output = "".join([html_layout.html_head(),
                         html_layout.header(),
                         html_layout.html_container(contents),
                         html_layout.footer(),
                         html_layout.html_end()])
        
        return output
    
    @cherrypy.expose
    def find(self):
        sys.stderr.write("server.py: request to /find/\n")
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
        
        html_layout = self._get_html_layout()
        
        app_path = paths_config.get_app_path()#paths_config[PathsConfig._APP_PATH]
        maps_conf_file = app_path+ConfigBase.MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, VERBOSE)
        
        if cherrypy.session.get('session_token'):
            find_form = FormsFactory.get_find_form_session(session)
        else:
            find_form = FormsFactory.get_find_form_empty(DEFAULT_GENES_WINDOW_CM,
                                                           DEFAULT_GENES_WINDOW_BP)
        
        find_form.get_query()
        
        find_component = html_layout.find_components(find_form, maps_config)
        
        citation = paths_config.get_citation().replace("_", " ")#paths_config[PathsConfig._CITATION].replace("_", " ")
        
        contents = [html_layout.menu(citation),
                    find_component]
        
        output = "".join([html_layout.html_head(),
                          html_layout.header(),
                          html_layout.html_container(contents),
                          html_layout.footer(),
                          html_layout.html_end()])
        
        return output
    
    @cherrypy.expose
    def align(self):
        sys.stderr.write("server.py: request to /align/\n")
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
        
        html_layout = self._get_html_layout()
        
        app_path = paths_config.get_app_path()#[PathsConfig._APP_PATH]
        maps_conf_file = app_path+ConfigBase.MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, VERBOSE)
        
        databases_conf_file = app_path+ConfigBase.DATABASES_CONF
        databases_config = DatabasesConfig(databases_conf_file, VERBOSE)
        
        if cherrypy.session.get('session_token'):
            align_form = FormsFactory.get_align_form_session(session)
        else:
            align_form = FormsFactory.get_align_form_empty(DEFAULT_GENES_WINDOW_CM,
                                                           DEFAULT_GENES_WINDOW_BP,
                                                           DEFAULT_THRESHOLD_ID,
                                                           DEFAULT_THRESHOLD_COV)
        
        align_component = html_layout.align_components(align_form, maps_config, databases_config)
        
        citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")
        
        contents = [html_layout.menu(citation),
                    align_component]
        
        output = "".join([html_layout.html_head(),
                          html_layout.header(),
                          html_layout.html_container(contents),
                          html_layout.footer(),
                          html_layout.html_end()])
        
        return output
    
    @cherrypy.expose
    def help(self):
        sys.stderr.write("server.py: request to /help/\n")
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[PATHS_CONFIG])
        
        html_layout = self._get_html_layout()
        
        citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")
        
        contents = [html_layout.menu(citation),
                    html_layout.help()]
        
        output = "".join([html_layout.html_head(),
                          html_layout.header(),
                          html_layout.html_container(contents),
                          html_layout.footer(),
                          html_layout.html_end()])
        
        return output

## END