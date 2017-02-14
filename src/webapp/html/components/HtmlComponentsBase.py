#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsBase.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class HtmlComponentsBase(object):
    
    @staticmethod
    def _load_input_file(action):
        output = []
        
        output.append("""
                    <br/><span class="explain_text">Or you rather prefer to upload a file</span>
                    <input type="file" name="my_file" id="{0}_my_file" class="demobutton"/>
                    <input type="button" id="{0}_clear_file_button" value="clear" class="demobutton" style="display:none;"/>
        """.format(action))
        
        return "".join(output)
    
    @staticmethod
    def _load_query_area_align(input_query, legend, action):
        output = []
        
        output.append("""
                <!-- QUERY AREA -->
                <fieldset style="border:none">
                    <legend>{2}
                        <input type="button" id="{1}_demo_button" value="demo" class="demobutton"/>
                        <input type="button" id="clear_demo_button" value="clear" class="demobutton"/>
                    </legend>
                    <textarea rows="16" cols="100" id="{1}_input_query" name="input_query"
                    autofocus="autofocus">{0}</textarea>
                    """.format(input_query, action, legend))
        output.append(HtmlComponentsBase._load_input_file(action))
        output.append("""
                </fieldset>
        """)
        
        return "".join(output)
    
    @staticmethod
    def _load_query_area_find(input_query, legend, action):
        output = []
        
        output.append("""
                <!-- QUERY AREA -->
                <fieldset style="border:none">
                    <legend>{2}
                        <input type="button" id="{1}_demo_button_full" value="demo full map" class="demobutton"/>
                        <input type="button" id="{1}_demo_button_region" value="demo region" class="demobutton"/>
                        <input type="button" id="clear_demo_button" value="clear" class="demobutton"/>
                    </legend>
                    <textarea rows="16" cols="100" id="{1}_input_query" name="input_query"
                    autofocus="autofocus">{0}</textarea>
                    """.format(input_query, action, legend))
        output.append(HtmlComponentsBase._load_input_file(action))
        output.append("""
                </fieldset>
        """)
        
        return "".join(output)
    
    @staticmethod
    def _load_output_area(input_multiple, input_sort, send_email, email_to, action):
        output = []
        
        output.append("""
                <fieldset style="border:solid thin;width:350px;height:170px;">
                    <legend>Output options:</legend>
                    <table style="width:100%;text-align:center;">
                    <tr>
                    """)
        
        ########## MULTIPLE
        output.append("""
                        <!-- FILTER MULTIPLE RADIO BUTTON -->
                        <td style="width:50%;">
                            <label for = "input_multiple">Markers with multiple mappings: </label>
                            <input type="radio" name="input_multiple" id="multiple_no" value="1"
            """)
            
        if input_multiple == "" or input_multiple == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="multiple_no">show</label>
                            <input type="radio" name="input_multiple" id="multiple_filter" value="0"
            """)
        
        if input_multiple == "0": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="multiple_filter">filter out</label>
                        </td>
                        <!--br/-->
                      </tr>
                      <tr><td><hr/></td></tr>
                      <tr>
                      """)
        
        ############ SORT
        output.append("""
                        <!-- SORTING FIELD -->
                        <td style="width:50%;">
                            <label for = "input_sort">Sort by: </label>
                            <input type="radio" name="input_sort" id="sort_cm" value="cm" 
                    """)
        
        if input_sort == "" or input_sort == "cm": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="sort_cm">cM</label>
                            <input type="radio" name="input_sort" id="sort_bp" value="bp"
                    """)
        if input_sort == "bp": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                            <label for ="sort_bp">bp</label>
                         </td>
                    </tr>
                    <tr><td><hr/></td></tr>
                    <tr><td>
                    """)
        
        ############## email
        output.append("""
                    <fieldset style="border:none;text-align:center;">
                        <label for="send_email">Send by e-mail</label>
                        <input id="input_send_email" type="checkbox" name="send_email" value="1"
                    """)
        
        if send_email == "1": output.append(" checked/>")
        else: output.append(" />")
        
        if email_to: output.append('<input type="email" name="email_to" autocomplete="on" value="'+str(email_to)+'"/>')
        else: output.append('<input type="email" name="email_to" autocomplete="on" value=""/>')
        
        output.append("""
                        <br/><span id="email_text" class="explain_text">Results will be sent to the speficied address.</span>
                    </fieldset>
                    </td></tr></table>
                </fieldset>
                """)
        
        return "".join(output)
    
    @staticmethod
    def _load_genes_area(input_genes, load_annot, input_extend, genes_window_cm, genes_window_bp, action):
        output = []
        
        output.append("""
                
                <!-- GENES AND MARKERS OPTIONS -->
                <fieldset style="border:solid thin;height:170px;padding-bottom: 1em;padding-top: 0%;width:430px">
                    <legend>Genes/Markers enrichment:</legend>
                    <table id="genes_table" style="">
                    <tr>
                        <td>
                           <!-- SHOW GENES RADIO BUTTON -->
                    """)
        
        output.append("""
                          <label>Show genes:</label>
                    """)
        
        output.append("""
                          
                          <input type = "radio"
                                 name = "input_genes"
                                 id = "genes_marker"
                                 value = "marker" 
                    """)
        
        if input_genes == "" or input_genes == "marker": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                          <label for = "genes_marker">on marker</label>
                          
                          <input type = "radio"
                                 name = "input_genes"
                                 id = "genes_between"
                                 value = "between"
                    """)
        if input_genes == "between": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
        
                          <label for = "genes_between">between</label>
                      """)
        
        output.append("""
                      <div id="genes_text" class="explain_text"></div><!-- Text is created with .js -->
                        </td></tr></table>
                        """)
        
        #### GENES OPTIONS FIELDSET
        output.append("""
                        <table id="input_extend_fieldset">
                        <tr><td id="genes_hr"><hr/></td></tr>
                        """)
        
        output.append("""
                        <!-- LOAD GENES ANNOTATION -->
                        <tr><td id="genes_annot_td">
                                <input type="checkbox" name="load_annot" value="1"
                        """)
        
        if load_annot == "" or load_annot == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                                <label for="load_annot">Load genes annotation</label>
                        </td></tr>
                        <tr><td id="annot_hr"><hr/></td></tr>
                        """)
        
        ################# GENES Extend search
        output.append("""
                    <tr><td>
                        <input type="checkbox" id="input_extend" name="input_extend" value="1"
                    """)
        
        if input_extend == "1": output.append(" checked/>")
        else: output.append(" />")
        
        output.append("""
                        <label for="input_extend">Extend genes/markers search</label>
                      
                """)
        
        output.append("""
                            <span id="genes_window_cm">
                                <input type="number" name="genes_window_cm" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.0" max="9999.9"
                        """)
        if not genes_window_cm or genes_window_cm == "": output.append(' value="'+str(ResourcesMng.get_def_genes_window_cm())+'"')
        else:
            myvar = ' value="'+str(genes_window_cm)+'"' # If I dont do the cast, it crashes
            output.append(myvar)
        
        output.append("""
                                       style="text-align:right;width:4em"/>
                                <label for="window">cM</label>
                            </span>
                            """)
        
        output.append("""
                            <span id="genes_window_bp">
                                <input type="number" name="genes_window_bp" id="window" pattern="[0-9]+" step="1" min="1" max="10000000000"
                        """)
        if not genes_window_bp or genes_window_bp == "": output.append(' value="'+str(ResourcesMng.get_def_genes_window_bp())+'"')
        else:
            myvar = ' value="'+str(genes_window_bp)+'"' # If I dont do the cast, it crashes
            output.append(myvar)
        
        output.append("""
                                       style="text-align:right;width:7em"/>
                                <label for="window">bp</label>
                            </span>
                            """)
        
        output.append("""
                            <br/><span id="input_extend_text" class="explain_text">Search will be extended, according to the specified interval.</span>
                        </td>
                        </tr>
                    </tr></table>
                </fieldset>
                """)
        
        return "".join(output)
    
    @staticmethod
    def _load_alignment_area(queries_type, threshold_id, threshold_cov):
        output = []
        
        output.append("""
                <fieldset id="alignment_fieldset" style="border:solid thin;">
                <legend>Choose an action:</legend>
                    <select name="queries_type" id="queries_type">
                    """)
        
        ############## ALIGNMENT ALGORITHM
        if queries_type == "auto":
            output.append('             <option value="auto" selected>auto</option>')
        else:
            output.append('             <option value="auto">auto</option>')
            
        if queries_type == "cdna":
            output.append('             <option value="cdna" selected>cdna</option>')
        else:
            output.append('             <option value="cdna">cdna</option>')
            
        if queries_type == "genomic":
            output.append('             <option value="genomic" selected>genomic</option>')
        else:
            output.append('             <option value="genomic">genomic</option>')
                        
        output.append("""
                    </select>
                    <span id="algorithm_text" class="explain_text">Perform a BLASTN search. Input data must be in FASTA format.</span>
                    <br/>
                    <br/>
                    <label for="threshold_id">min. id.</label>
                    <input type="number" name="threshold_id" id="threshold_id" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.1" max="100.0"
                        """)
        
        ############# ALIGNMENT THRESHOLDS
        if not threshold_id or threshold_id == "":
            myvar = ' value="'+str(def_threshold_id)+'"'
            output.append(myvar)
        else:
            myvar = ' value="'+str(threshold_id)+'"' # If I dont do the cast, it crashes
            output.append(myvar)
            
        output.append("""
                            style="text-align:right;width:4em"/>
                    
                    <label for="threshold_cov">min. query cov.</label>
                    <input type="number" name="threshold_cov" id="threshold_cov" pattern="[0-9]+[\.][0-9]+" step="0.1" min="0.1" max="100.0"
                        """)
        if not threshold_cov or threshold_cov == "":
            myvar = ' value="'+str(def_threshold_cov)+'"'
            output.append(myvar)
        else:
            myvar = ' value="'+str(threshold_cov)+'"' # If I dont do the cast, it crashes
            output.append(myvar)
            
        output.append("""
                            style="text-align:right;width:4em"/>
                    </fieldset>
                    """)
        
        return "".join(output)
    
    @staticmethod
    def _load_data(input_data, config_data, input_name):
        output = []
        
        output.append('<select name="{0}" id="{0}" multiple>'.format("input_"+str(input_name)))
        
        if input_data == "":
            input_data = []
        elif isinstance(input_data, basestring): # If only one dataset provided, best if embeb it in a list
            input_data = [input_data]
        #else: input_data is already a list
        
        #(data_names, data_ids) = load_data(conf_file, verbose = ResourcesMng.get_verbose())
        
        for configured_data in config_data:
            if configured_data in input_data or len(input_data)==0:
                output.append('           <option value="{0}" selected>{1}</option>'.format(configured_data, configured_data.replace("_", " ")))
            else:
                output.append('           <option value="{0}">{1}</option>'.format(configured_data, configured_data.replace("_", " ")))
            
        
        output.append("</select>")
        
        return "".join(output)

## END