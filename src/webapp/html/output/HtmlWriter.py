#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlWriter.py is part of Barleymap web app.
# Copyright (C)  2013-2014  Carlos P Cantalapiedra.
# Copyright (C)  2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys, os

from barleymapcore.m2p_exception import m2pException
from barleymapcore.maps.MapsBase import MapTypes
from barleymapcore.maps.reader.MapFiles import ChromosomesFile

MAPPED_TITLE = "Map"
UNMAPPED_TITLE = "Unmapped"
UNALIGNED_TITLE = "Unaligned"
MAP_WITH_GENES_TITLE = "Map with genes"
MAP_WITH_MARKERS_TITLE = "Map with markers"
MAP_WITH_ANCHORED_TITLE = "Map with anchored features"

#from barleymapcore.genes.GenesBase import GenesFields, AnnotFields
#from barleymapcore.maps.MarkersBase import MarkersFields

from HtmlWriterMaps import HtmlMapsWriter
import bmap_svg_img

BACK_BUTTON_IMG = "/img/back.gif"

class HtmlWriter():
    output_buffer = None
    __base_url = ""
    _tmp_files_path = None
    _genmap_path = None
    _maps_path = None
    _maps_writer = None
    
    def __init__(self, base_url, tmp_files_path, genmap_path, maps_path):
        self.__base_url = base_url
        self._tmp_files_path = tmp_files_path
        self._genmap_path = genmap_path
        self._maps_path = maps_path
        self._maps_writer = HtmlMapsWriter(base_url)
    
    def init_output_buffer(self):
        self.output_buffer = []
        self._maps_writer.set_output_buffer(self.output_buffer)
        return
    
    def set_output_buffer(self, _buffer):
        self.output_buffer = _buffer
        self._maps_writer.set_output_buffer(_buffer)
        return
    
    def get_output_buffer(self):
        return self.output_buffer
    
    def output_html_back_button(self, action):
        url = self.get_back_url(action)
        img_url = self.get_back_button()
        if url and img_url:
            self.output_buffer.append('<a class="boton" href="'+url+'"><img style="width:50px;height:40px;border:none;" src="'+img_url+'"/></a>')
        else: raise m2pException("No URL or img_url provided for back button")
        return
    
    def get_back_url(self, action):
        return self.__base_url+"/"+action+"/"
    
    def get_back_button(self, ):
        return self.__base_url+BACK_BUTTON_IMG
    
    def output_html_top_button(self):
        return self.output_buffer.append(self._maps_writer.output_html_top_img())
    
    def output_text(self, text):
        self.output_buffer.append(text)
        return
    
    def output_html_report(self, report):
        self.output_buffer.append("<strong>"+report+"</strong>")
        self.output_buffer.append('<br/>')
        return
    
    def output_top_menu(self, genetic_map_dict):
        ## MENU
        self.output_text('<hr/>')
        self.output_text('<section id="top_menu">')
        self.output_text('<span class="top_menu_maps">Maps:</span>')
        self.output_text('<span class="tab"></span>')
        
        for genetic_map in genetic_map_dict:
            #genetic_map_data = genetic_map_dict[genetic_map]
            genetic_map_name = genetic_map.get_map_config().get_name()
            #genetic_map_name = genetic_map_data["map_name"]
            
            self.output_text('<a class="map_link" href="#'+str(genetic_map_name)+'">'+str(genetic_map_name)+'</a>')
            self.output_text('<span class="tab"></span>')
        
        self.output_text('</section>')
        self.output_text('<hr/>')
        self.output_text('<br/>')
        return
    
    def output_map_link(self, genetic_map_name, result_name):
        
        result_link = genetic_map_name+"_"+str(result_name)
        
        self.output_text('<li>')
        self.output_text('<a class="map_result_link" href="#'+result_link+'">'+str(result_name)+'</a>')
        self.output_text('</li>')
        
        return result_link
    
    def output_map_menu(self, genetic_map_data, form):
        map_links_dict = {} # Contains the links to the different results sections of a single map
        
        map_config = genetic_map_data.get_map_config()
        genetic_map_name = map_config.get_name()#genetic_map_data["map_name"]
        # MAP MENU
        self.output_text('<h1 class="map_title" id="'+str(genetic_map_name)+'">Map: '+str(genetic_map_name)+'')
        self.output_html_top_button()
        self.output_text('</h1>')
        
        self.output_text('<section class="map_menu">')
        self.output_text('<ul>')
        
        ## Mapped
        result_name = MAPPED_TITLE
        result_link = self.output_map_link(genetic_map_name, result_name)
        map_links_dict[result_name] = result_link
        
        if form.get_show_markers():
            result_name = MAP_WITH_MARKERS_TITLE
            result_link = self.output_map_link(genetic_map_name, result_name)
            map_links_dict[result_name] = result_link
        
        if form.get_show_genes():
            result_name = MAP_WITH_GENES_TITLE
            result_link = self.output_map_link(genetic_map_name, result_name)
            map_links_dict[result_name] = result_link
        
        if form.get_show_anchored():
            result_name = MAP_WITH_ANCHORED_TITLE
            result_link = self.output_map_link(genetic_map_name, result_name)
            map_links_dict[result_name] = result_link
        
        ## Unmapped
        if genetic_map_data.get_unmapped():
            result_name = UNMAPPED_TITLE
            result_link = self.output_map_link(genetic_map_name, result_name)
            map_links_dict[result_name] = result_link
        
        ## Unaligned
        if genetic_map_data.get_unaligned():
            result_name = UNALIGNED_TITLE
            result_link = self.output_map_link(genetic_map_name, result_name)
            map_links_dict[result_name] = result_link
        
        #for result in MapTypes.RESULTS_LIST:
        #    result_name = MapTypes.RESULTS_DICT[result]
        #    
        #    result_link = genetic_map_name+"_"+str(result)
        #    map_links_dict[result] = result_link
        #    self.output_text('<li>')
        #    self.output_text('<a class="map_result_link" href="#'+result_link+'">'+str(result_name)+'</a>')
        #    self.output_text('</li>')
        
        self.output_text('</ul>')
        self.output_text('</section>')
        #self.output_text('<a class="top_link" href="#">top</a>')
        #self.output_text("<br/>")
        self.output_text("<br/>")
        
        return map_links_dict
    
    #def output_html_header(self):
    #    self.output_buffer.append('<!DOCTYPE html>\n\n')
    #    self.output_buffer.append('<!--[if lt IE 7 ]> <html class="ie6"> <![endif]-->')
    #    self.output_buffer.append('<!--[if IE 7 ]>    <html class="ie7"> <![endif]-->')
    #    self.output_buffer.append('<!--[if IE 8 ]>    <html class="ie8"> <![endif]-->')
    #    self.output_buffer.append('<!--[if IE 9 ]>    <html class="ie9"> <![endif]-->')
    #    self.output_buffer.append('<!--[if (gt IE 9)|!(IE)]><!--> <html class=""> <!--<![endif]-->')
    #    self.output_buffer.append('<head>')
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('<meta charset="utf-8" />')
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('<title>Map markers</title>')
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('<meta content="CPCantalapiedra" name="CPCantalapiedra" />')
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('<meta content="Map markers to barley physical map" name="Map to physical map" />')
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('<meta content="etiqueta1, etiqueta2, etiqueta3" name="keywords" />')
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('<link rel="stylesheet" href="{0}" type="text/css" media="screen" />'.format(self.__base_url+"/style.css"))
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('</head>')
    #    self.output_buffer.append('\n')
    #    return
    
    #def output_html_end(self):
    #    self.output_buffer.append('\n')
    #    self.output_buffer.append('</body>\n</html>')
    #    return
    
    def output_html_parameters(self, parameters):
        # Parameters (see mapmarkers_cp.py --> parameters_list)
        # [input_query, multiple, action, input_datasets, input_genes, input_sort, genes_window,
        # queries_type, threshold_id, threshold_cov]
        self.output_buffer.append('<table border="1" style="border-collapse:collapse;padding:5px;text-align:center">')
        self.output_buffer.append('<caption style="text-align:left;">Parameters</caption>')
        self.output_buffer.append('<thead><tr>')
        
        # Headers
        if parameters[2] == "blast":
            self.output_buffer.append("<th>Alignment</th>")
            self.output_buffer.append("<th>Min. Identity</th>")
            self.output_buffer.append("<th>Min. Coverage</th>")
        else:
            self.output_buffer.append("<th>Datasets</th>")
        
        self.output_buffer.append('<th>Multiple mappings</th>')
        
        self.output_buffer.append("<th>Genes info</th>")
        self.output_buffer.append("<th>Genes window</th>")
        self.output_buffer.append("<th>Sort by</th>")
        
        self.output_buffer.append("</tr></thead>")
        self.output_buffer.append("<tr>")
        
        # Action
        if parameters[2] == "blast":
            self.output_buffer.append("<td>"+parameters[7]+"</td>")
            self.output_buffer.append("<td>"+str(parameters[8])+"</td>")
            self.output_buffer.append("<td>"+str(parameters[9])+"</td>")
        else:
            self.output_buffer.append("<td>"+",".join(parameters[3])+"</td>")
            
        # Multiple
        if parameters[1] == 0:
            self.output_buffer.append("<td>Filter</td>")
        else:
            self.output_buffer.append("<td>Allow</td>")
            
        self.output_buffer.append("<td>"+parameters[4]+"</td>")
        self.output_buffer.append("<td>"+str(parameters[6])+" cM</td>")
        self.output_buffer.append("<td>"+parameters[5]+"</td>")
        self.output_buffer.append("</tr>")
        self.output_buffer.append("</table>")
        self.output_buffer.append("<br/>")
        return
    
    def output_download_html_link(self, url, name):
        if url and name:
            self.output_buffer.append('<a href="'+url+'" download="report.csv">'+name+'</a>')
        else: raise m2pException("No URL or name provided to output_html_link in html_writer.py")
        return
    
    def output_download_html_img(self, url, img_url):
        if url and img_url:
            self.output_buffer.append('<br/><a href="'+url+'" download="report.csv"><img style="width:3%;height:3%;" src="'+img_url+'"/></a>')
        else:
            raise m2pException("No URL or img_url provided to output_html_link in html_writer.py")
        
        return
    
    def output_svg_img(self, svg_code, map_id, fine_mapping):
        if svg_code and svg_code != "":
            self.output_buffer.append('<br/>')
            if fine_mapping:
                self.output_buffer.append('<span id="graphical_maps_'+map_id+'_fine" style="display:none;">'+svg_code+'</span>')
            else:
                self.output_buffer.append('<span id="graphical_maps_'+map_id+'" style="display:initial;">'+svg_code+'</span>')
        return
    
    def output_html_top(self):
        self.output_buffer.append('<a class="top_link" href="#">top</a>')
    
    def output_html_map_message(self, map_section_link, message):
        self.output_buffer.append('<span id="'+map_section_link+'">'+message+'</span> <caption><a class="top_link" href="#">top</a></caption>')
    
    def _output_graphical_maps(self, mapping_results, csv_file_name):
        ########## GRAPHICAL MAPS ################################################################
        genmap_path = self._genmap_path
        
        #chr_list = {}
        
        map_config = mapping_results.get_map_config()
        map_as_physical = map_config.as_physical()
        map_has_cm_pos = map_config.has_cm_pos()
        map_has_bp_pos = map_config.has_bp_pos()
        
        map_id = map_config.get_id()
        map_dir = map_config.get_map_dir()
        
        sort_param = mapping_results.get_sort_by()
        
        # File with map-DB positions
        map_chrom_order_path = self._maps_path+map_dir+"/"+map_dir+ChromosomesFile.FILE_EXT
        
        # Position to show in graphical maps (cM or bp)
        graph_map_as_physical = False
        if map_as_physical:
            pos_position = 2
            graph_map_as_physical = True
        else:
            if map_has_cm_pos and map_has_bp_pos:
                if sort_param == "cm":
                    pos_position = 2
                    graph_map_as_physical = False
                else:
                    pos_position = 3
                    graph_map_as_physical = True
            else:
                pos_position = 2
                if map_has_bp_pos: graph_map_as_physical = True
        
        ## button to change svg view (full chromosomes or fine mapping)
        img_url = self.__base_url+"/img/lupa.png"
        img2_url = self.__base_url+"/img/lupa_hover.png"
        self.output_buffer.append("""
                                 <br/><img title="toggle map view"
                                 class="toggle_button"
                                 id="toggle_view_button_{0}" border:none;"
                                 /*onmouseover="hover(this);" onmouseout="unhover(this);"*/
                                 src="{1}"/>
                                 """.format(map_id, img_url))
        
        # Functions to change maps image (zoom or full maps) with the
        # magnifying glass button
        self.output_buffer.append("""
        <script>
            // Functions to change image with mouse over and out
            /*function hover(element) {{
                element.setAttribute('src', '{2}');
            }}
            function unhover(element) {{
                element.setAttribute('src', '{1}');
            }}*/
            $("#toggle_view_button_{0}").click(function(){{
                $("#graphical_maps_{0}").toggle();
                $("#graphical_maps_{0}_fine").toggle();
            }});
        </script>
        """.format(map_id, img_url, img2_url))
        
        ## Graphical maps with full chromosomes
        fine_mapping = False
        svg_code = bmap_svg_img.output_genetic_map(csv_file_name, genmap_path, map_chrom_order_path, graph_map_as_physical, fine_mapping, pos_position)
        self.output_svg_img(svg_code, map_id, fine_mapping)
        
        ## Graphical maps with fine mapping
        fine_mapping = True
        svg_code = bmap_svg_img.output_genetic_map(csv_file_name, genmap_path, map_chrom_order_path, graph_map_as_physical, fine_mapping, pos_position)
        self.output_svg_img(svg_code, map_id, fine_mapping)
        
        return
    
    def _output_map_title(self, map_section_link, section_name, map_name, top = True):
        
        self.output_buffer.append('<span class="results_table_title" id="'+map_section_link+'" style="text-align:left;">'+\
                                  str(section_name)+'')
        if top: self.output_buffer.append(self._maps_writer.output_html_top_img(map_name))
        self.output_buffer.append("</span><br/>")
        
        return
    
    def output_genetic_map(self, map_links_dict, mapping_results, multiple_param, csv_file_name):
        
        positions = mapping_results.get_mapped()
        map_config = mapping_results.get_map_config()
        map_name = map_config.get_name()
        section_name = MAPPED_TITLE
        map_section_link = map_links_dict[section_name]
        
        if len(positions)>0:
            ## Title
            self._output_map_title(map_section_link, section_name, map_name, top = False)
            
            ## Graphical maps
            self._output_graphical_maps(mapping_results, csv_file_name)
            
            ## CSV file download link
            try:
                basename_csv_file = os.path.split(csv_file_name)[1]
                self.output_download_html_img(self.__base_url+"/"+os.path.basename(self._tmp_files_path)+"/"+basename_csv_file, \
                                                     self.__base_url+"/img/csv_download.jpg")
            except m2pException as e:
                self.output_text("No URL or name provided for CSV file.")
                raise e
            
            ## Actual tabular map
            self._maps_writer.output_genetic_map(positions, map_config, multiple_param)
            
        else:
            self.output_buffer.append('<span id="'+map_section_link+'">No results found for map '+map_name+'.</span><br/>')
        
        return
    
    def output_map_with_markers(self, map_links_dict, mapping_results, multiple_param, csv_file_name):
        
        positions = mapping_results.get_map_with_markers()
        map_config = mapping_results.get_map_config()
        map_name = map_config.get_name()
        section_name = MAP_WITH_MARKERS_TITLE
        map_section_link = map_links_dict[section_name]
        
        if len(positions)>0:
            ## Title
            self._output_map_title(map_section_link, section_name, map_name)
            
            ## CSV file download link
            try:
                basename_csv_file = os.path.split(csv_file_name)[1]
                self.output_download_html_img(self.__base_url+"/"+os.path.basename(self._tmp_files_path)+"/"+basename_csv_file, \
                                                     self.__base_url+"/img/csv_download.jpg")
            except m2pException as e:
                self.output_text("No URL or name provided for CSV file.")
                raise e
            
            ## Tabular map
            self._maps_writer.output_map_with_markers(positions, map_config, multiple_param)
        
        return
    
    def output_map_with_genes(self, map_links_dict, mapping_results, multiple_param, csv_file_name, annotator):
        
        positions = mapping_results.get_map_with_genes()
        map_config = mapping_results.get_map_config()
        map_name = map_config.get_name()
        section_name = MAP_WITH_GENES_TITLE
        map_section_link = map_links_dict[section_name]
        
        if len(positions)>0:
            ## Title
            self._output_map_title(map_section_link, section_name, map_name)
            
            ## CSV file download link
            try:
                basename_csv_file = os.path.split(csv_file_name)[1]
                self.output_download_html_img(self.__base_url+"/"+os.path.basename(self._tmp_files_path)+"/"+basename_csv_file, \
                                                     self.__base_url+"/img/csv_download.jpg")
            except m2pException as e:
                self.output_text("No URL or name provided for CSV file.")
                raise e
            
            ## Tabular map
            self._maps_writer.output_map_with_genes(positions, map_config, multiple_param, annotator)
        
        return
    
    def output_map_with_anchored(self, map_links_dict, mapping_results, multiple_param, csv_file_name):
        
        positions = mapping_results.get_map_with_anchored()
        map_config = mapping_results.get_map_config()
        map_name = map_config.get_name()
        section_name = MAP_WITH_ANCHORED_TITLE
        map_section_link = map_links_dict[section_name]
        
        if len(positions)>0:
            ## Title
            self._output_map_title(map_section_link, section_name, map_name)
            
            ## CSV file download link
            try:
                basename_csv_file = os.path.split(csv_file_name)[1]
                self.output_download_html_img(self.__base_url+"/"+os.path.basename(self._tmp_files_path)+"/"+basename_csv_file, \
                                                     self.__base_url+"/img/csv_download.jpg")
            except m2pException as e:
                self.output_text("No URL or name provided for CSV file.")
                raise e
            
            ## Tabular map
            self._maps_writer.output_map_with_anchored(positions, map_config, multiple_param)
        
        return
    
    def output_unmapped(self, map_links_dict, mapping_results, csv_file_name):
        
        unmapped = mapping_results.get_unmapped()
        map_config = mapping_results.get_map_config()
        map_name = map_config.get_name()
        section_name = UNMAPPED_TITLE
        map_section_link = map_links_dict[section_name]
        
        if len(unmapped)>0:
            ## Title
            self._output_map_title(map_section_link, section_name, map_name)
            
            ## CSV file download link
            try:
                basename_csv_file = os.path.split(csv_file_name)[1]
                self.output_download_html_img(self.__base_url+"/"+os.path.basename(self._tmp_files_path)+"/"+basename_csv_file, \
                                                     self.__base_url+"/img/csv_download.jpg")
            except m2pException as e:
                self.output_text("No URL or name provided for CSV file.")
                raise e
            
            ## Tabular output
            self._maps_writer.output_unmapped(unmapped)
            
        else:
            self.output_buffer.append('<span id="'+map_section_link+'">There are no alignments without position for this map.</span>')
            self.output_buffer.append(self._maps_writer.output_html_top_img())
            self.output_buffer.append("</caption>")
        
        return
    
    def output_unaligned(self, map_links_dict, mapping_results, csv_file_name):
        
        unaligned = mapping_results.get_unaligned()
        map_config = mapping_results.get_map_config()
        map_name = map_config.get_name()
        section_name = UNALIGNED_TITLE
        map_section_link = map_links_dict[section_name]
        
        if len(unaligned)>0:
            ## Title
            self._output_map_title(map_section_link, section_name, map_name)
            
            ## CSV file download link
            try:
                basename_csv_file = os.path.split(csv_file_name)[1]
                self.output_download_html_img(self.__base_url+"/"+os.path.basename(self._tmp_files_path)+"/"+basename_csv_file, \
                                                     self.__base_url+"/img/csv_download.jpg")
            except m2pException as e:
                self.output_text("No URL or name provided for CSV file.")
                raise e
            
            ## Tabular output
            self._maps_writer.output_unaligned(unaligned)
            
        else:
            self.output_buffer.append('<span id="'+map_section_link+'">There are no queries without alignments for this map.</span>')
            self.output_buffer.append(self._maps_writer.output_html_top_img())
            self.output_buffer.append("</caption>")
        
        return
    
## END