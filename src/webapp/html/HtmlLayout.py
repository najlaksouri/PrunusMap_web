#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlLayout.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

from components.HtmlComponents import HtmlComponents

from HtmlLayoutBarleymap import HtmlLayoutBarleymap
from FormsFactory import FormsFactory

PREFIX_UI_CTRLS_ALIGN = "align"
PREFIX_UI_CTRLS_FIND = "find"

class HtmlLayout(object):
    _base_url = None
    
    def __init__(self, base_url):
        self._base_url = base_url
    
    ## Basic layout methods
    ##
    def html_head(self):
        output = []
        output.append(HtmlLayoutBarleymap.head(self._base_url))
        output.append(HtmlLayoutBarleymap.js_scripts(self._base_url))
        
        return "".join(output)  
    
    def header(self):
        return HtmlLayoutBarleymap.title_header(self._base_url)
    
    def html_container(self, contents = []):
        return '<div id="container" style="margin:10px;">'+"".join(contents)+'</div> <!-- container -->'
    
    def footer(self):
        return HtmlLayoutBarleymap.footer()
    
    def html_end(self):
        return """
        </body>
        </html>
        """
    
    ## Methods which add content to the previous layout
    ##
    def main_text(self, citation):
        
        return HtmlLayoutBarleymap.main_text(citation, self._base_url, PREFIX_UI_CTRLS_ALIGN, PREFIX_UI_CTRLS_FIND)
    
    def menu(self, citation):
        
        output = []
        output.append('<div id="menu">')
        output.append(HtmlLayoutBarleymap.text_menu(citation, self._base_url, show_last_changes = False))
        output.append('</div>')
        
        return "".join(output)
    
    ## Methods for specific contents
    ##
    def help(self):
        return HtmlComponents.help(self._base_url)
    
    def align_components(self, session, maps_config, databases_config,
                         DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP,
                         DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):
        
        if session.get('session_token'):
            align_form = FormsFactory.get_align_form(session)
        else:
            align_form = FormsFactory.get_empty_align_form(DEFAULT_GENES_WINDOW_CM,
                                                           DEFAULT_GENES_WINDOW_BP,
                                                           DEFAULT_THRESHOLD_ID,
                                                           DEFAULT_THRESHOLD_COV)
        
        align_components = HtmlComponents.align(self._base_url, align_form, PREFIX_UI_CTRLS_ALIGN,
                                                maps_config, databases_config)
        
        return align_components
    
    def find_components(self, session, maps_config,
                        DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP):
        
        if session.get('session_token'):
            find_form = FormsFactory.get_find_form(session)
        else:
            find_form = FormsFactory.get_empty_find_form(DEFAULT_GENES_WINDOW_CM,
                                                         DEFAULT_GENES_WINDOW_BP)
        
        find_components = HtmlComponents.find(self._base_url, find_form, PREFIX_UI_CTRLS_FIND,
                                              maps_config)
        
        return find_components

## END