#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlLayoutBarleymap.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class HtmlLayoutBarleymap(object):
    
    @staticmethod
    def output_html_img_button(action, url, img_url, width = "3%", height = "3%", img_url_hover = None):
        output = []
        if url and img_url:
            output.append("""<a href="{1}">
                          <img style="width:{2};height:{3}; border:0;"
                          onmouseover="hover_{0}(this);" onmouseout="unhover_{0}(this);"
                          src="{4}"/>
                          </a>""".format(action, url, width, height, img_url))
            
            if img_url_hover:
                # Functions to change maps image (zoom or full maps)
                output.append("""
                <script>
                    // Functions to change image with mouse over and out
                    function hover_{0}(element) {{
                        element.setAttribute('src', '{2}');
                    }}
                    function unhover_{0}(element) {{
                        element.setAttribute('src', '{1}');
                    }}
                </script>
                """.format(action, img_url, img_url_hover))
        else:
            Exception("HtmlLayoutBarleymap: No URL or img_url provided for img button.")
        
        return "".join(output)
    
    @staticmethod
    def main_text(citation, base_url, PREFIX_UI_CTRLS_ALIGN, PREFIX_UI_CTRLS_FIND, PREFIX_UI_CTRLS_LOCATE):
        output = []
        #output.append('<br/>')
        output.append('<div id="main_buttons" style="margin:0px;">')
        output.append('<table id="main_buttons_table" center><tr>')
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_FIND, base_url+"/"+PREFIX_UI_CTRLS_FIND+"/",
                                                                 base_url+"/img/ui_buttons_find.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_find_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_ALIGN, base_url+"/"+PREFIX_UI_CTRLS_ALIGN+"/",
                                                                 base_url+"/img/ui_buttons_align.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_align_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_LOCATE, base_url+"/"+PREFIX_UI_CTRLS_LOCATE+"/",
                                                                 base_url+"/img/ui_buttons_locate.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_locate_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button("help", base_url+"/help/",
                                                                 base_url+"/img/ui_buttons_help.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_help_hover.png"))
        output.append("</td>")
        output.append("</tr>")
        output.append("</table>")
        output.append("</div>")
        #output.append('<br/>')
        
        output.append('<div id="main_text">')
        output.append(HtmlLayoutBarleymap.text_menu(citation, base_url, show_last_changes = True))
        output.append("</div>")
        
        return "".join(output)
    
    @staticmethod
    def head(base_url):
        return """
        <!DOCTYPE html>
        <!--[if lt IE 7 ]> <html class="ie6"> <![endif]-->
        <!--[if IE 7 ]>    <html class="ie7"> <![endif]-->
        <!--[if IE 8 ]>    <html class="ie8"> <![endif]-->
        <!--[if IE 9 ]>    <html class="ie9"> <![endif]-->
        <!--[if (gt IE 9)|!(IE)]><!--> <html class=""> <!--<![endif]-->
        <head>
            <meta charset="utf-8" />
            <title>Barleymap</title>
            <meta content="CPCantalapiedra" name="CPCantalapiedra" />
            <meta content="Map markers to the barley genome" name="Map markers to the barley genome" />
            <meta content="barley, barleymap, physical map, genetic map, markers, mapping, bioinformatics, blast, gmap, genome, genomics" name="keywords" />
            <link rel="stylesheet" href="{0}" type="text/css" media="screen"/>
        </head>""".format(base_url+"/style.css")
    
    @staticmethod
    def js_scripts(base_url):
        return """
            <body>
        <script src="{0}"></script>
        <script src="{1}"></script>
        """.format("http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", \
                   base_url+"/js/index.js")
    
    @staticmethod
    def js_scripts_maps(base_url):
        return """
            <body>
        <script src="{0}"></script>
        <script src="{1}"></script>
        """.format("http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", \
                   base_url+"/js/maps.js")
    
    @staticmethod
    def title_header(base_url):
        return """
        <header id="top">
            <h2><a href="{1}/">Barleymap</a></h2>
            <h3 class="infobar">({0})</h3>
        </header>
        """.format("Map markers to the barley genome - Morex Genome 2017 edition", base_url)
    
    @staticmethod
    def footer():
        return """
        <footer class="infobar">
            <a href="http://www.eead.csic.es/compbio/" target="_blank">Laboratory of Computational Biology</a>
            ::
            <a href="http://eead.csic.es/" target="_blank">Estaci&oacute;n Experimental de Aula Dei</a>
            ::
            <a href="http://www.csic.es/" target="_blank">Consejo Superior de Investigaciones Cient&iacute;ficas</a>
        </footer>
        """
    
    @staticmethod
    def text_menu(citation, base_url, show_last_changes = False):
        text_buffer = []
        text_buffer.append("""
            <b><a href="{2}">Barleymap</a></b> was designed to search the position of barley genetic markers on the <strong>Barley Physical Map</strong> (IBSC<sup>[1]</sup>) 
            and the <strong>POPSEQ map</strong> (Mascher <i>et al.</i><sup>[2]</sup>). 
            The current version was updated to work with the <strong>Morex Genome</strong> (released in 2017)<sup>[3]</sup>.
            <br/><br/>
            
            All the public data used by Barleymap can be found at
            <a href="ftp://ftpmips.helmholtz-muenchen.de/plants/barley/public_data/" target="_blank">MIPS FTP server</a>
            , <a href="ftp://ftp.ipk-gatersleben.de/barley-popseq/" target="_blank">IPK FTP server</a>, 
            and <a href="http://webblast.ipk-gatersleben.de/barley_ibsc/downloads/" target="_blank">FTP server for Morex Genome 2017 data</a>.
            <br/><br/>
            
            The <strong><i><a href="{2}/find/">Find markers</a></i></strong> option allows to find the position of markers by using their identifiers as input.
            <br/>Note that those markers must be part of one of the
            <!--<strong><a href="{0}#barleymap_datasets">-->precalculated datasets<!--</a></strong>--> available (e.g.: Illumina 50K markers).
            <br/><br/>
            
            To use the <strong><i><a href="{2}/align/">Align sequences</a></i></strong> option you must provide nucleotide sequences of the markers (in FASTA format).
            <br/>These will be used to retrieve their positions through
            <strong><a href="{0}#references_and_algorithms_used_for_alignment">sequence alignment</a></strong> to the selected map (IBSC2012, POPSEQ or MorexGenome).
            <br/><br/>
            
            The <strong><i><a href="{2}/locate/">Locate by position</a></i></strong> option allows to examine the map context of specific positions,
            which must be provided as tuples with chromosome (or contig) and position (local position, within the chromosome or contig, in base pairs).
            For example, an user could provide as input "chr1H   10000" to find out which genes are in that specific region of chromosome 1H.
            <br/><br/>
            
            In addition to locate a list of markers or sequences,
            <strong><a href="{0}#genes_markers_enrichment_and_annotation">information of genes, genetic markers, and anchored features,</a></strong>
            that enrich the context around or between the queries will be shown.<br/><br/>
            
            <strong><a href="https://github.com/Cantalapiedra/barleymap_web">Barleymap web</a></strong> 
            works on top of <strong><a href="https://github.com/Cantalapiedra/barleymapcore">barleymap core API</a></strong>, used also in a
            <strong><a href="https://github.com/Cantalapiedra/barleymap">standalone application</a></strong>
            that allows loading custom databases, maps and datasets, among other features.
            <br/>Such application can be used with data from any organism for which sequences anchored to a genetic/physical background are available.
            
            <br/><br/>
            
            <strong>Further information</strong> about how this tool works and help on using it can be found
            <strong><a href="{0}">here</a></strong>.
            <br/>
            Or you may wish to <strong>contact</strong> the <a href="http://www.eead.csic.es/compbio/" target="_blank">Laboratory of Computational Biology</a>
            (<a href="http://www.eead.csic.es">EEAD</a> - <a href="http://www.csic.es">CSIC</a>):<br/>
            <a href="mailto:cpcantalapiedra@eead.csic.es">Carlos P Cantalapiedra</a>
            <br/>
            <a href="mailto:bcontreras@eead.csic.es">Bruno Contreras-Moreira</a>
            <br/><br/>
            
            <strong>Citation:</strong> <a href="http://link.springer.com/article/10.1007%2Fs11032-015-0253-1">{1}</a>
            <br/><br/>
            <hr/>
            <br/>
            
            <cite><sup>[1]</sup>IBSC. 2012.
            <a href="http://dx.doi.org/10.1038/nature11543" target="_blank">A physical, genetic and functional sequence assembly of the barley genome.</a>
            Nature. 491:711-16. doi:10.1038/nature11543
            </cite>
            <br/>
            <cite><sup>[2]</sup>Mascher et al. 2013.
            <a href="http://onlinelibrary.wiley.com/doi/10.1111/tpj.12319/abstract" target="_blank">Anchoring and ordering NGS contig assemblies by population sequencing (POPSEQ).</a>
            The Plant Journal, 76: 718–727. doi: 10.1111/tpj.12319
            </cite>
            <br/>
            <cite><sup>[3]</sup>In press
            <!--<a href="http://onlinelibrary.wiley.com/doi/10.1111/tpj.12319/abstract" target="_blank">Anchoring and ordering NGS contig assemblies by population sequencing (POPSEQ).</a>-->
            <!--The Plant Journal, 76: 718–727. doi: 10.1111/tpj.12319-->
            </cite>
        """.format(base_url+"/help/", citation, base_url))
        
        if show_last_changes:
            text_buffer.append("""
            <br/><br/><hr/><br/><strong>Last changes</strong>
            <br/><br/>
            This is an early deployment of Barleymap Morex Genome 2017 edition. Therefore, the <strong>main updates</strong> from the previous POPSEQ edition to
            this Morex Genome 2017 edition are explained next.
            Note that most of this information will be included, and more detailed, in the Help section in the near future.
            This is also true for the standalone application, which is in general updated but the help files are not.
            
            <br/><br/>2017-03-30:<br/>
            · New <strong><i><a href="{2}/locate/">Locate by position</a></i></strong> action available.
            
            <br/><br/><!--07-03-2017:<br/>-->
            · Support for the <strong>Morex Genome released in 2017</strong>.
            
            <br/><br/>
            · New datasets have been added, to be searched with Barleymap Find, including: BOPA1, BOPA2, iSelect Infinium 9K,
            <strong>Illumina 50K</strong>, Darts, DartSeq, GBS SNPs from OWB, Haruna Nijo flcDNAs, HarvEST 36 tags,
            IBSC2012 genes ("MLOCs"), <strong>IBSC2016 genes ("HORVUs")</strong>,
            and IBSC2012 BacEndSequences (BES), sequenced BACs, and <strong>IBSC2012 WGS contigs</strong> from Barke, Bowman and Morex.
            Note that not all this datasets can be searched in the three maps. For example, HORVUs are limited to MorexGenome (2017),
            whereas Barke WGS contigs can only be found in IBSC2012 and MorexGenome, but no in POPSEQ; Morex WGS contigs can be found in all three maps.
            Finally, some of these datasets can be queried with different synonyms. For example, BOPA1 markers (e.g.: BOPA1_10114-1946, 10114-1946), or
            iSelect Infinium 9K markers (e.g.: i_SCRI_RS_100054, SCRI_RS_100054; or i_11_10006, 11_10006, 1016-376, BOPA1_1016-376).
            
            <br/><br/>
            · IBSC2012 BES, sequenced BACs and WGS contigs are not genes nor markers, but a different kind of feature which we called <strong>anchored features</strong>.
            Besides searching them by identifier, anchored features close to map positions obtained can be included
            in the output map through the enrichment options.
            This allows including, for example, the position of Morex WGS contigs in the output map.
            However, note that the enrichment with anchored features is slow, so we encourage you to use enrichment of anchored features only when really needed.
            
            <br/><br/>
            · A new option <strong>"show only main features"</strong>, has been added in the "enrichment" options section. When checked, the output map will include, as additional features,
            only the main ones (for example, the HORVUs in the MorexGenome, but no the MLOCs or the flcDNAs). When unchecked, the enrichment process will be slower,
            but all the available features will be included in
            the output map (in the previous example, MLOCs, flcDNAs, and other genes will be included along with HORVUs).
            
            <br/><br/>
            · The <strong>results tables</strong> have been remodelled.
            Now, the enriched features are shown in line with the queries, but in a different background color.
            In the downloadable CSV files, both row types are differentiated with the first field of the table.
            
            <br/><br/>
            · Also in the results page, an icon has been included to <strong>zoom</strong> in the markers of interest in the graphical chromosomes.
            
            <br/><br/>
            · There are <strong>other minor changes</strong>, and more of them in the standalone application and the core API.
                               """)
        
        return "".join(text_buffer)
    
## END
