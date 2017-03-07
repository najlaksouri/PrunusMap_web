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

########## MAIL SERVER
# check file in /home/barleymap/email/

class Root():
    
    MOUNT_POINT = None
    PATHS_CONFIG = None
    DEFAULT_THRESHOLD_ID = None
    DEFAULT_THRESHOLD_COV = None
    DEFAULT_ALIGNER = None
    DEFAULT_MAPS = None
    DEFAULT_GENES_WINDOW_CM = None
    DEFAULT_GENES_WINDOW_BP = None
    
    VERBOSE = False
    
    def __init__(self, MOUNT_POINT, PATHS_CONFIG, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV, DEFAULT_ALIGNER, DEFAULT_MAPS,
                 DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP, VERBOSE):
        
        self.MOUNT_POINT = MOUNT_POINT
        self.PATHS_CONFIG = PATHS_CONFIG
        self.DEFAULT_THRESHOLD_ID = DEFAULT_THRESHOLD_ID
        self.DEFAULT_THRESHOLD_COV = DEFAULT_THRESHOLD_COV
        self.DEFAULT_ALIGNER = DEFAULT_ALIGNER
        self.DEFAULT_MAPS = DEFAULT_MAPS
        self.DEFAULT_GENES_WINDOW_CM = DEFAULT_GENES_WINDOW_CM
        self.DEFAULT_GENES_WINDOW_BP = DEFAULT_GENES_WINDOW_BP
        self.VERBOSE = VERBOSE
        return
    
    def _get_html_layout(self):
        return HtmlLayout(self.MOUNT_POINT)
    
    @cherrypy.expose
    def index(self):
        
        sys.stderr.write("server.py: request to /index\n")
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
        
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
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
        
        html_layout = self._get_html_layout()
        
        app_path = paths_config.get_app_path()#paths_config[PathsConfig._APP_PATH]
        maps_conf_file = app_path+ConfigBase.MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, self.VERBOSE)
        
        session = cherrypy.session
        if session.get('session_token'):
            find_form = FormsFactory.get_find_form_session(session)
        else:
            find_form = FormsFactory.get_find_form_empty(self.DEFAULT_GENES_WINDOW_CM, self.DEFAULT_GENES_WINDOW_BP,
                                                         self.DEFAULT_MAPS)
        
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
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
        
        html_layout = self._get_html_layout()
        
        app_path = paths_config.get_app_path()#[PathsConfig._APP_PATH]
        maps_conf_file = app_path+ConfigBase.MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, self.VERBOSE)
        
        session = cherrypy.session
        if session.get('session_token'):
            align_form = FormsFactory.get_align_form_session(session, self.DEFAULT_ALIGNER,
                                                             self.DEFAULT_THRESHOLD_ID, self.DEFAULT_THRESHOLD_COV)
        else:
            align_form = FormsFactory.get_align_form_empty(self.DEFAULT_GENES_WINDOW_CM, self.DEFAULT_GENES_WINDOW_BP,
                                                           self.DEFAULT_ALIGNER, self.DEFAULT_MAPS,
                                                           self.DEFAULT_THRESHOLD_ID, self.DEFAULT_THRESHOLD_COV)
        
        align_component = html_layout.align_components(align_form, maps_config)
        
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
        
        paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
        
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