#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsFind.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

from HtmlComponentsBase import HtmlComponentsBase

class HtmlComponentsFind(object):
    
    ######################### FIND FORM HTML COMPONENTS
    ###################################################
    @staticmethod
    def find(base_url, find_form, PREFIX_UI_CTRLS_FIND, maps_config):
        output = []
        
        ####### INPUT QUERY TEXT AREA
        output.append("""
        <section id="content">
            <form name="input_find" action="{0}" method="post" enctype="multipart/form-data">
            """.format(base_url+"/mapmarkers/run"))
        
        output.append(HtmlComponentsBase._load_query_area_find(find_form.get_input_query(),
                                             "Input a list of marker IDs:",
                                             PREFIX_UI_CTRLS_FIND))
        output.append("<br/>")
        output.append("<table><tr><td>")
        output.append(HtmlComponentsBase._load_output_area(find_form.get_input_multiple(),
                                         find_form.get_input_sort(),
                                         find_form.get_send_email(),
                                         find_form.get_email_to(),
                                         PREFIX_UI_CTRLS_FIND))
        output.append("</td><td>")
        output.append(HtmlComponentsBase._load_genes_area(find_form.get_input_genes(),
                                        find_form.get_load_annot(),
                                        find_form.get_input_extend(),
                                        find_form.get_genes_window_cm(),
                                        find_form.get_genes_window_bp(),
                                        PREFIX_UI_CTRLS_FIND))
        output.append("</td></tr></table>")
        output.append("<br/>")
        
        output.append("""
                <table><tr>
                <td>
                    <fieldset id="find_fieldset" style="border:solid thin;">
                    <legend>Choose genetic/physical maps:</legend>
                    """)
        
        #### MAPS
        output.append(HtmlComponentsBase._load_data(find_form.get_input_maps(), maps_config.get_maps(), "maps"))
        
        output.append("""
                      
                    </fieldset>
                </td><td id="submit_button_td">
                    <button id="submit_button" name="action_dataset" type="submit" value="Find">
                        <img src="{0}"/>
                    </button>
                </td>
                </tr></table>
            </form>
        </section><hr/> <!-- content -->
        """.format(base_url+"/img/ui_buttons_find.png"))
        
        return "".join(output)

## END