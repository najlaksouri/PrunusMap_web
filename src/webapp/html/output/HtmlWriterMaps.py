#!/usr/bin/env python
# -*- coding: utf-8 -*-

# html_writer_maps.py is part of Barleymap web app.
# Copyright (C)  2013-2014  Carlos P Cantalapiedra.
# Copyright (C)  2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys

from barleymapcore.m2p_exception import m2pException
#from barleymapcore.maps.MapsBase import MapTypes
from barleymapcore.output.OutputFacade import MapHeaders
from barleymapcore.maps.enrichment.FeatureMapping import FeatureMapping
from barleymapcore.db.DatasetsConfig import DatasetsConfig

class HtmlMapsWriter():
    output_buffer = None
    __base_url = ""
    
    def __init__(self, base_url):
        self.__base_url = base_url
    
    def set_output_buffer(self, _buffer):
        self.output_buffer = _buffer
        return
    
    def init_output_buffer(self):
        self.output_buffer = []
        return
    
    def get_output_buffer(self):
        return self.output_buffer
    
    def __interpro_html_link(self, ipr_code):
        if ipr_code != "-":
            retValue = '<a href="http://www.ebi.ac.uk/interpro/entry/'+ipr_code+'" rel="external" target="_blank">'+ipr_code+'</a>'
        else: retValue = ipr_code
        return retValue
    
    def __interpro_html_links(self, ipr_code_list):
        return " ".join([self.__interpro_html_link(x) for x in ipr_code_list.split(",")])
    
    def __go_html_link(self, go_term):
        if go_term != "-":
            retValue = '<a href="http://amigo.geneontology.org/cgi-bin/amigo/term_details?term='+go_term+'" \
                       rel="external" target="_blank">'+go_term+'</a>'
        else: retValue = go_term
        return retValue
    
    def __go_html_set_links(self, go_term_set):
        return "|".join([self.__go_html_link(x) for x in go_term_set.split("|")])
    
    def __go_html_links(self, go_term_list):
        return "<br/>".join([self.__go_html_set_links(x) for x in go_term_list.split(",")])
    
    def __location_html_link(self, chrom, bp):
        return '<a href="http://plants.ensembl.org/Hordeum_vulgare/Location/View?r='+str(chrom)+':'+str(bp)+'" \
                        rel="external" target="_blank">'+str(bp)+'</a>'
        
    def __gene_html_link(self, gene_id):
        return '<a href="http://plants.ensembl.org/Hordeum_vulgare/Gene/Summary?g='+str(gene_id)+'" \
                        rel="external" target="_blank">'+str(gene_id)+'</a>'
        
    #def __output_html_gene(self, map_has_cm_pos, map_has_bp_pos, gene, load_annot):
    #    
    #    gene_cm = gene[GenesFields.GENES_CM_POS]
    #    if gene_cm != "-":
    #        cm_pos = str("%0.2f" % float(gene_cm))
    #    else:
    #        cm_pos = gene_cm
    #    
    #    chrom = gene[GenesFields.GENES_CHR_POS]
    #    bp = gene[GenesFields.GENES_BP_POS]
    #    
    #    gene_data = []
    #    gene_data.append("<td></td>")
    #    
    #    gene_id = gene[GenesFields.GENES_ID_POS]
    #    if gene_id != "-": gene_data.append("<td>"+self.__gene_html_link(gene_id)+"</td>")
    #    else: gene_data.append("<td>"+gene_id+"</td>")
    #    
    #    gene_data.append("<td>"+gene[GenesFields.GENES_TYPE_POS]+"</td>")
    #    gene_data.append("<td>"+str(chrom)+"</td>")
    #    
    #    if map_has_cm_pos:
    #        gene_data.append("<td>"+str(cm_pos)+"</td>")
    #    
    #    if map_has_bp_pos:
    #        if bp != "-": gene_data.append("<td>"+self.__location_html_link(chrom, bp)+"</td>")
    #        else: gene_data.append("<td>"+str(bp)+"</td>")
    #    
    #    self.output_buffer.append("".join(gene_data))
    #    
    #    if load_annot != 0:
    #        annot = gene[len(MapHeaders.GENES_HEADERS):]
    #        self.output_buffer.append("<td>"+annot[AnnotFields.GENES_ANNOT_DESC]+"</td>") # Readable description
    #        
    #        # InterPro
    #        if annot[AnnotFields.GENES_ANNOT_INTERPRO] != "-":
    #            self.output_buffer.append("<td>"+self.__interpro_html_links(annot[AnnotFields.GENES_ANNOT_INTERPRO])+"</td>")
    #        else:
    #            self.output_buffer.append("<td>-</td>")
    #        
    #        # PFAM and others
    #        pfam_annot = annot[AnnotFields.GENES_ANNOT_PFAM].replace(",", "<br/>")
    #        self.output_buffer.append("<td>"+pfam_annot+"</td>") # PFAM ID
    #        #self.output_buffer.append("<td>"+x[7]+"</td>") # PFAM source
    #        self.output_buffer.append("<td>"+self.__go_html_links(annot[AnnotFields.GENES_ANNOT_GO])+"</td>") # GO terms
    #    
    #    return
    
    #def __same_position(self, pos, last_pos, map_has_cm_pos, map_has_bp_pos):
    #    
    #    retValue = False
    #    
    #    ## last position data: to compare with previous position and dont show redundant fields
    #    last_marker_id = last_pos[MapFields.MARKER_NAME_POS]
    #    last_chrom = last_pos[MapFields.MARKER_CHR_POS]
    #    
    #    if map_has_cm_pos:
    #        last_cm = last_pos[MapFields.MARKER_CM_POS]
    #    
    #    if map_has_bp_pos:
    #        last_bp = last_pos[MapFields.MARKER_BP_POS]
    #    
    #    ## Current position data
    #    marker_id = pos[MapFields.MARKER_NAME_POS]
    #    chrom = pos[MapFields.MARKER_CHR_POS]
    #    
    #    if map_has_cm_pos:
    #        cm = pos[MapFields.MARKER_CM_POS]
    #        
    #    if map_has_bp_pos:
    #        bp = pos[MapFields.MARKER_BP_POS]
    #    
    #    # Comparison
    #    if map_has_cm_pos and map_has_bp_pos:
    #        if last_marker_id == marker_id and \
    #            last_chrom == chrom and \
    #            last_cm == cm and last_bp == bp:
    #                retValue = True
    #    elif map_has_cm_pos:
    #        if last_marker_id == marker_id and \
    #            last_chrom == chrom and \
    #            last_cm == cm:
    #                retValue = True
    #    elif map_has_bp_pos:
    #        if last_marker_id == marker_id and \
    #            last_chrom == chrom and \
    #            last_bp == bp:
    #                retValue = True
    #    else:
    #        raise m2pException("html_writer_maps. Bad map configuration.")
    #    
    #    return retValue
    
    def __output_html_positions_base_header(self, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, table_id = "positions_table"):
        
        self.output_buffer.append('<table id="'+table_id+'">') #
        self.output_buffer.append("<thead><tr>")
        
        if map_as_physical:
            self.output_buffer.append("<th>"+MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_ID]+"</th>")
            self.output_buffer.append("<th>"+MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_CHR]+"</th>")
            self.output_buffer.append("<th>"+MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_START_POS]+"</th>")
            self.output_buffer.append("<th>"+MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_END_POS]+"</th>")
            self.output_buffer.append("<th>"+MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_STRAND]+"</th>")
            
            if multiple_param:
                html_header = MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_MULTIPLE_POS].replace("_", "<br/>")
                self.output_buffer.append("<th>"+html_header+"</th>")
            
            self.output_buffer.append("<th>"+MapHeaders.PHYSICAL_HEADERS[MapHeaders.PHYSICAL_OTHER_ALIGNMENTS].replace("_", "<br/>")+"</th>")
            
        else:
            
            self.output_buffer.append("<th>"+MapHeaders.OUTPUT_HEADERS[MapHeaders.MARKER_NAME_POS]+"</th>")
            self.output_buffer.append("<th>"+MapHeaders.OUTPUT_HEADERS[MapHeaders.MARKER_CHR_POS]+"</th>")
            
            if map_has_cm_pos:
                self.output_buffer.append("<th>"+MapHeaders.OUTPUT_HEADERS[MapHeaders.MARKER_CM_POS]+"</th>")
            
            if map_has_bp_pos:
                self.output_buffer.append("<th>"+MapHeaders.OUTPUT_HEADERS[MapHeaders.MARKER_BP_POS]+"</th>")
                
            if multiple_param:
                html_header = MapHeaders.OUTPUT_HEADERS[MapHeaders.MULTIPLE_POS].replace("_", "<br/>")
                self.output_buffer.append("<th>"+html_header+"</th>")
            
            html_header = MapHeaders.OUTPUT_HEADERS[MapHeaders.OTHER_ALIGNMENTS].replace("_", "<br/>")
            self.output_buffer.append("<th>"+html_header+"</th>")
        
        return
    
    def __output_html_pos_base(self, pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos, td_class = "std_td"):
        
        #if not same_pos:
        
        td = '<td class="'+td_class+'">'
        
        ## Marker ID
        marker_id = str(pos.get_marker_id())#pos[MapFields.MARKER_NAME_POS]
        self.output_buffer.append(td+str(marker_id)+"</td>")
        
        ## Chromosome
        chrom = pos.get_chrom_name()#pos[MapFields.MARKER_CHR_POS]
        self.output_buffer.append(td+str(chrom)+"</td>")
        
        if map_as_physical:
            bp = pos.get_bp_pos()#pos[MapFields.MARKER_CM_POS]
            #if cm != "-": self.output_buffer.append("<td>"+str("%0.2f" % cm)+"</td>")
            #else: self.output_buffer.append("<td>"+str(cm)+"</td>")
            self.output_buffer.append(td+str(bp)+"</td>")
            
            bp_end = pos.get_bp_end_pos()#pos[MapFields.MARKER_BP_POS]
            #if bp != "-": self.output_buffer.append("<td>"+self.__location_html_link(chrom, bp)+"</td>")
            #else: self.output_buffer.append("<td>"+str(bp)+"</td>")
            self.output_buffer.append(td+str(bp_end)+"</td>")
            
            strand = pos.get_strand()#pos[MapFields.MARKER_BP_POS]
            self.output_buffer.append(td+str(strand)+"</td>")
            
        else:
            ## cM
            if map_has_cm_pos:
                cm = pos.get_cm_pos()#pos[MapFields.MARKER_CM_POS]
                if cm != "-": self.output_buffer.append(td+str("%0.2f" % float(cm))+"</td>")
                else: self.output_buffer.append(td+str(cm)+"</td>")
            
            ## bp
            if map_has_bp_pos:
                bp = pos.get_bp_pos()#pos[MapFields.MARKER_BP_POS]
                if bp != "-": self.output_buffer.append(td+self.__location_html_link(chrom, bp)+"</td>")
                else: self.output_buffer.append(td+str(bp)+"</td>")
        
        if pos.is_empty():
            if multiple_param:
                self.output_buffer.append(td+"-"+"</td>") # multiple positions
            self.output_buffer.append(td+"-"+"</td>") # other alignments
        else:
            ## Multiple
            if multiple_param:
                mult = pos.has_multiple_pos() #[MapFields.MULTIPLE_POS]
                if mult:
                    self.output_buffer.append(td+"Yes"+"</td>")
                else:
                    self.output_buffer.append(td+"No"+"</td>")
                
            ## Other alignments
            if pos.has_other_alignments():
                self.output_buffer.append(td+"Yes"+"</td>")
            else:
                self.output_buffer.append(td+"No"+"</td>")
        
        #else:
        #    self.output_buffer.append('<td style="border:none;border-color:#FFFFFF;background-color:#FFFFFF;"></td>')
        #    self.output_buffer.append('<td style="border:none;border-color:#FFFFFF;background-color:#FFFFFF;"></td>')
        #    
        #    ## cM
        #    if map_has_cm_pos:
        #        self.output_buffer.append('<td style="border:none;border-color:#FFFFFF;background-color:#FFFFFF;"></td>')
        #    
        #    ## bp
        #    if map_has_bp_pos:
        #        self.output_buffer.append('<td style="border:none;border-color:#FFFFFF;background-color:#FFFFFF;"></td>')
        #    
        #    ## Multiple
        #    if multiple_param == "yes":
        #        self.output_buffer.append('<td style="border:none;border-color:#FFFFFF;background-color:#FFFFFF;"></td>')
        #    
        #    ## Other alignments
        #    self.output_buffer.append('<td style="border:none;border-color:#FFFFFF;background-color:#FFFFFF;"></td>')
        
        return
    
    def __marker_html_link(self, marker_id):
        return marker_id
    
    #def __output_html_marker(self, map_has_cm_pos, map_has_bp_pos, marker):
    #    
    #    marker_cm = marker[MarkersFields.MARKER_CM_POS]
    #    if marker_cm != "-":
    #        cm_pos = str("%0.2f" % float(marker_cm))
    #    else:
    #        cm_pos = marker_cm
    #    
    #    chrom = marker[MarkersFields.MARKER_CHR_POS]
    #    bp = marker[MarkersFields.MARKER_BP_POS]
    #    
    #    marker_data = []
    #    marker_data.append("<td></td>")
    #    
    #    marker_id = marker[MarkersFields.MARKER_ID_POS]
    #    if marker_id != "-": marker_data.append("<td>"+self.__marker_html_link(marker_id)+"</td>")
    #    else: marker_data.append("<td>"+marker_id+"</td>")
    #    
    #    marker_data.append("<td>"+marker[MarkersFields.MARKER_DATASET_POS].replace("_", " ")+"</td>")
    #    marker_data.append("<td>"+str(chrom)+"</td>")
    #    
    #    if map_has_cm_pos:
    #        marker_data.append("<td>"+str(cm_pos)+"</td>")
    #    
    #    if map_has_bp_pos:
    #        if bp != "-": marker_data.append("<td>"+self.__location_html_link(chrom, bp)+"</td>")
    #        else: marker_data.append("<td>"+str(bp)+"</td>")
    #    
    #    if marker[MarkersFields.MARKER_GENES_CONFIGURED_POS]:
    #        if len(marker[MarkersFields.MARKER_GENES_POS]) > 0:
    #            links_array = [self.__gene_html_link(gene_id) for gene_id in marker[MarkersFields.MARKER_GENES_POS]]
    #            marker_data.append("<td>"+"<br/>".join(links_array)+"</td>")
    #        else:
    #            marker_data.append("<td>no hits</td>")
    #    else:
    #        marker_data.append("<td>nd</td>")
    #    
    #    self.output_buffer.append("".join(marker_data))
    #    
    #    return
    
    def __output_basic_pos(self, pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos):
        
        self.output_buffer.append("<tr>")
        
        self.__output_html_pos_base(pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
        
        self.output_buffer.append("</tr>")
        
        return
    
    def __output_feature_pos(self, pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos):
        
        self.output_buffer.append("<tr>")
        
        if pos.get_row_type() == FeatureMapping.ROW_TYPE_MAPPING_RESULT:
            td_class = "std_td"
        elif pos.get_row_type() == FeatureMapping.ROW_TYPE_ENRICHMENT:
            td_class = "feature_td"
        
        self.__output_html_pos_base(pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos, td_class)
        
        return
    
    def output_genetic_map(self, positions, map_config, multiple_param):
        
        #positions = mapping_results.get_mapped()
        #map_config = mapping_results.get_map_config()
        map_has_cm_pos = map_config.has_cm_pos()
        map_has_bp_pos = map_config.has_bp_pos()
        map_name = map_config.get_name()
        map_as_physical = map_config.as_physical()
        
        self.__output_html_positions_base_header(map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param)
        self.output_buffer.append("</tr></thead>")
        
        #last_pos = None
        for pos in positions:
            #same_pos = (last_pos != None and self.__same_position(pos, last_pos, map_has_cm_pos, map_has_bp_pos))
            
            #if not same_pos:
            #    self.__output_basic_pos(pos, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            same_pos = False
            self.__output_basic_pos(pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            
            #last_pos = pos
        
        self.output_buffer.append("</table><br/>")
        
        return
    
    def output_map_with_markers(self, positions, map_config, multiple_param):
        
        map_has_cm_pos = map_config.has_cm_pos()
        map_has_bp_pos = map_config.has_bp_pos()
        map_name = map_config.get_name()
        map_as_physical = map_config.as_physical()
        
        #if collapsed_view:
        self.__output_html_positions_base_header(map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param)
        #else: add fields of feature
        
        self.output_buffer.append("</tr></thead>")
        
        #last_pos = None
        for pos in positions:
            
            self.output_buffer.append("<tr>")
            
            #same_pos = (last_pos != None and self.__same_position(pos, last_pos, map_has_cm_pos, map_has_bp_pos))
            #self.__output_html_pos_base(pos, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            same_pos = False
            self.__output_feature_pos(pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            
            #marker = pos[len(MapHeaders.OUTPUT_HEADERS):]
            #self.__output_html_marker(map_has_cm_pos, map_has_bp_pos, marker)
            
            #last_pos = pos
            self.output_buffer.append("</tr>")
        
        self.output_buffer.append("</table><br/>")
        
        return
    
    def output_map_with_genes(self, positions, map_config, multiple_param, annotator):
        
        map_has_cm_pos = map_config.has_cm_pos()
        map_has_bp_pos = map_config.has_bp_pos()
        map_name = map_config.get_name()
        map_as_physical = map_config.as_physical()
        
        anntypes_config = annotator.get_anntypes_config()
        anntypes_list = anntypes_config.get_anntypes_list()
        loaded_anntypes = annotator.get_loaded_anntypes()
        
        #if collapsed_view:
        self.__output_html_positions_base_header(map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param)
        
        for anntype_id in anntypes_list:
            if anntype_id in loaded_anntypes:
                anntype = anntypes_config.get_anntype(anntype_id)
                self.output_buffer.append("<th>"+anntype.get_name()+"</th>")
                
        #else: add fields of feature
        
        self.output_buffer.append("</tr></thead>")
        
        for pos in positions:
            self.output_buffer.append("<tr>")
            
            #same_pos = (last_pos != None and self.__same_position(pos, last_pos, map_has_cm_pos, map_has_bp_pos))
            #self.__output_html_pos_base(pos, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            same_pos = False
            self.__output_feature_pos(pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            
            #marker = pos[len(MapHeaders.OUTPUT_HEADERS):]
            #self.__output_html_marker(map_has_cm_pos, map_has_bp_pos, marker)
            
            #last_pos = pos
            
            feature_type = pos.get_feature_type()
            if feature_type == DatasetsConfig.DATASET_TYPE_GENE:
                gene_annots = pos.get_annots()
                
                # This is read like this to keep the same order of annotation types
                # in all the records so that they can share column (and header title)
                for anntype_id in [anntype_id for anntype_id in anntypes_list if anntype_id in loaded_anntypes]:
                        
                        # load gene_annots only of that anntype
                        gene_annots_anntype = [gene_annot for gene_annot in gene_annots if gene_annot.get_anntype().get_anntype_id()==anntype_id]
                        if len(gene_annots_anntype)>0:
                            for gene_annot_anntype in gene_annots_anntype:
                                data_line = " ".join(gene_annot_anntype.get_annot_data())
                                self.output_buffer.append('<td class="feature_td">'+data_line+"</td>")
                        else:
                            self.output_buffer.append('<td class="empty_td"></td>')
            #else:
            #    self.output_buffer.append('<td class="std_td">O</td>')
            
            self.output_buffer.append("</tr>")
        
        self.output_buffer.append("</table><br/>")
        
        return
    
    def output_map_with_anchored(self, positions, map_config, multiple_param):
        
        map_has_cm_pos = map_config.has_cm_pos()
        map_has_bp_pos = map_config.has_bp_pos()
        map_name = map_config.get_name()
        map_as_physical = map_config.as_physical()
        
        #if collapsed_view:
        self.__output_html_positions_base_header(map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param)
        #else: add fields of feature
        
        self.output_buffer.append("</tr></thead>")
        
        #last_pos = None
        for pos in positions:
            
            self.output_buffer.append("<tr>")
            
            #same_pos = (last_pos != None and self.__same_position(pos, last_pos, map_has_cm_pos, map_has_bp_pos))
            #self.__output_html_pos_base(pos, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            same_pos = False
            self.__output_feature_pos(pos, map_as_physical, map_has_cm_pos, map_has_bp_pos, multiple_param, same_pos)
            
            #marker = pos[len(MapHeaders.OUTPUT_HEADERS):]
            #self.__output_html_marker(map_has_cm_pos, map_has_bp_pos, marker)
            
            self.output_buffer.append("</tr>")
            
            #last_pos = pos
        
        self.output_buffer.append("</table><br/>")
        
        return
    
    def output_unmapped(self, results):
        self.output_buffer.append('<table class="unmapped_table" id="unmapped_table">') #
        self.output_buffer.append("<thead><tr>")
        self.output_buffer.append("<th>Query ID</th>")
        self.output_buffer.append("<th>Target ID</th>")
        self.output_buffer.append("</tr></thead>")
        
        for result in results:
            self.output_buffer.append("<tr><td>"+str(result[0])+"</td><td>"+str(result[1])+"</td></tr>")
        
        self.output_buffer.append("</table><br/>")
        
        return
    
    def output_unaligned(self, identifiers):
        self.output_buffer.append('<table class="unmapped_table" id="unaligned_table">') #
        self.output_buffer.append("<thead><tr>")
        self.output_buffer.append("<th>Query ID</th>")
        self.output_buffer.append("</tr></thead>")
        
        for identifier in identifiers:
            self.output_buffer.append("<tr><td>"+str(identifier)+"</td></tr>")
        
        self.output_buffer.append("</table><br/>")
        
        return

## END