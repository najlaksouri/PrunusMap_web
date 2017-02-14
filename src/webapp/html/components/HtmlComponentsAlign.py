#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsAlign.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

from HtmlComponentsBase import HtmlComponentsBase

class HtmlComponentsAlign(object):
    
    ################################## ALIGN HTML COMPONENTS
    ########################################################
    @staticmethod
    def align(base_url, align_form, PREFIX_UI_CTRLS_ALIGN, maps_config, databases_config):
        output = []
        
        ####### INPUT QUERY TEXT AREA
        output.append("""
        <section id="content">
            <form name="input_align" action="{0}" method="post" enctype="multipart/form-data">
            """.format(base_url+"/mapmarkers/run"))
        
        output.append(HtmlComponentsBase._load_query_area_align(align_form.get_input_query(),
                                              "Input FASTA sequences:",
                                              PREFIX_UI_CTRLS_ALIGN))
        output.append("<br/>")
        output.append("<table><tr><td>")
        output.append(HtmlComponentsBase._load_output_area(align_form.get_input_multiple(),
                                         align_form.get_input_sort(),
                                         align_form.get_send_email(),
                                         align_form.get_email_to(),
                                         PREFIX_UI_CTRLS_ALIGN))
        output.append("</td><td>")
        output.append(HtmlComponentsBase._load_genes_area(align_form.get_input_genes(),
                                        align_form.get_load_annot(),
                                        align_form.get_input_extend(),
                                        align_form.get_genes_window_cm(),
                                        align_form.get_genes_window_bp(),
                                        PREFIX_UI_CTRLS_ALIGN))
        
        output.append("</td></tr></table>")
        output.append("<br/>")
        output.append(HtmlComponentsBase._load_alignment_area(align_form.get_queries_type(),
                                            align_form.get_threshold_id(),
                                            align_form.get_threshold_cov()))
        output.append("<br/>")
        
        output.append("""
                <table><tr>
                <td>
                    <fieldset id="align_fieldset" style="border:solid thin;">
                    <legend>Choose genetic/physical maps and databases:</legend>
                    """)
        
        #### MAPS AND DATABASES
        output.append('<table style="margin:auto"><tr><td>')
        output.append(HtmlComponentsBase._load_data(align_form.get_input_maps(), maps_config.get_maps(), "maps"))
        output.append("</td><td>")
        output.append(HtmlComponentsBase._load_data(align_form.get_input_databases(), databases_config.get_databases(), "databases"))
        output.append("</td></tr></table>")
        
        output.append("""
                      
                    </fieldset>
                </td><td id="submit_button_td">
                    <button id="submit_button" name="action_blast" type="submit" value="Blast">
                        <img src="{0}"/>
                    </button>
                </td>
                </tr></table>
            </form>
        </section><hr/> <!-- content -->
        """.format(base_url+"/img/ui_buttons_align.png"))
        
        return "".join(output)
    
## END