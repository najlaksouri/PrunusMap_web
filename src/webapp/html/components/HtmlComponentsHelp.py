#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsHelp.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class HtmlComponentsHelp(object):
    
    @staticmethod
    def _help_menu(output_buffer):
        output_buffer.append("""
            <article class="help_article">
                <section class="help_section">
                    <hr/>
                    <ul class="help_menu">
                        <li><a href="#overview">
                        
                            Overview
                            
                        </a></li>
                        <li><a href="#align_sequences">
                        
                            Align sequences
                            
                        </a></li>
                            <ul>
                                <li><a href="#references_and_algorithms_used_for_alignment">
                                
                                    References and algorithms used for alignment
                                    
                                </a></li>
                                <li><a href="#alignment_input_and_parameters">
                                
                                    Alignment input and parameters
                                    
                                </a></li>
                            </ul>
                        <li><a href="#find_markers">
                        
                            Find markers
                            
                        </a></li>
                            <ul>
                                <li><a href="#barleymap_datasets">
                                
                                    Barleymap datasets
                                    
                                </a></li>
                                <li><a href="#input_for_finding_markers">
                                
                                    Input for finding markers
                                    
                                </a></li>
                            </ul>
                        <li><a href="#output_options_and_genes_markers_enrichment">
                        
                            Output options and genes/markers enrichment
                            
                        </a></li>
                            <ul>
                                <li><a href="#output_options">
                                
                                    Output options
                                    
                                </a></li>
                                <li><a href="#genes_markers_enrichment_and_annotation">
                                
                                    Genes/markers enrichment and annotation
                                    
                                </a></li>
                            </ul>
                        <li><a href="#barleymap_output">
                        
                            Barleymap output
                            
                        </a></li>
                            <ul>
                                <li><a href="#mapping_results">
                                
                                    Mapping results
                                    
                                </a></li>
                                <li><a href="#map_enriched_with_genes_information">
                                
                                    Map enriched with genes information
                                    
                                </a></li>
                                <li><a href="#other_markers_located_in_the_mapping_interval">
                                
                                    Other markers located in the mapping interval
                                    
                                </a></li>
                                <li><a href="#unmapped_and_unaligned_markers">
                                
                                    Unmapped and unaligned markers
                                    
                                </a></li>
                                <li><a href="#other_features">
                                
                                    Other features
                                    
                                </a></li>
                            </ul>
                        <li><a href="#confidentiality">
                        
                            Confidentiality
                            
                        </a></li>
                        <li><a href="#disclaimer">
                        
                            Disclaimer
                            
                        </a></li>
                    </ul>
                """)
        
        return
    
    @staticmethod
    def help(base_url):
        output_buffer = []
        output_buffer.append("""
                             <section id="content">
                                <a href="{0}"><img style="width:5%;height:5%;border:none;" src="{1}" alt="back"/></a>
                             """.format(base_url+"/", base_url+"/img/back.gif"))
        
        HtmlComponentsHelp._help_menu(output_buffer)
        
        ## OVERVIEW
        
        output_buffer.append("""
                    <hr/>
                    
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="overview">Overview</h2>
                    
                        <br/>
                        Barleymap was designed to search the genetic and physical positions of barley markers on
                        the Barley Physical Map<sup>[1]</sup> and the POPSEQ map<sup>[2]</sup>. Please, see the original 
                        references for details on these resources and their comparison.
                        <br/><br/>
                        Barleymap provides two separate applications to retrieve data from the maps:
                        <ul class="help_list">
                            <li>"Find markers": to retrieve the position of markers providing their identifiers.</li>
                            <li>"Align sequences": to obtain the position of FASTA sequences by pairwise alignment.</li>
                        </ul>
                        <br/>
                """.format(base_url))
        
        ## ALIGN SEQUENCES
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="align_sequences">Align sequences</h2>
                        
                        <h3 id="references_and_algorithms_used_for_alignment">References and algorithms used for alignment</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                        <br/>
                        The previous version of Barleymap used as reference for the alignment the DNA sequence datasets
                        associated to the IBSC physical map: AC1, AC2 and AC3.
                        However, we consider that the alignment step benefits from the use of more comprehensive sequence references.
                        This also improves flexibility,
                        since the results of alignment can be used to retrieve positions from different maps.
                        Moreover, using the previous version of Barleymap resulted in a high number of false multiple position mappings.
                        Therefore, the current version of Barleymap uses the following databases of sequences as references:
                        <ul class="help_list">
                            <li>Three <i>WGS</i> assemblies from different cultivars: "MorexWGS", "BowmanWGS" and "BarkeWGS"</li>
                            <li>Morex cultivar sequenced BACs, assembled into BAC contigs: "SequencedBACs"</li>
                            <li>Morex cultivar BAC End sequences: "BACEndSequences"</li>
                        </ul>
                        
                        Barleymap performs alignments to the databases sequentially (see pipeline schema below),
                        so that queries that have been successfully aligned
                        to one database are not further searched in the remaining ones (NOTE: this procedure can be modified by the user
                        in the <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone version</a>). The hierarchical order in which databases are queried is the same in which are mentioned 
                        above and the one shown in the "Align sequences" page. This order has been chosen based on the idea that the WGS assemblies
                        are more comprehensive than the other ones, and the Morex cultivar is the main one used as reference in the major
                        barley genomics projects. The order in which BowmanWGS and BarkeWGS datasets are used was chosen based on subtle performance
                        differences.
                        On the other hand, a sequential search has been chosen based on the assumption that, although fragmented, each database
                        would be almost complete (close to the barley genome),
                        regarding sequence diversity, though some sequences could be absent in some of them. In addition, it is expected that these
                        databases will be improved in the future, so that each one will be considered an independent reference genome.
                        This procedure allows Barleymap to avoid the high redundancy that would result
                        from the use of all the databases for every query.
                        In addition, it reduces server load, by decreasing the number of alignments
                        that are performed. As a drawback, if a sequence has actually more than one copy in the genome,
                        but the different targets are in
                        different databases, the query could be marked as aligned to only one loci,
                        when it should have multiple targets with different positions.
                        In spite of that, we consider that Barleymap loses just a few true multiple alignments,
                        while discarding many false ones.
                        <br/><br/>
                        For the alignment step, Barleymap can use Blast<sup>[3]</sup> (megablast), GMAP<sup>[4]</sup>, or both,
                        depending on user choice (see pipeline schema below and "Alignment input and parameters").
                        If both alignment programs are used,
                        the first alignment step is performed with Blast against one database.
                        Then, the unaligned queries are searched in the same database
                        by means of GMAP.
                        This one can align sequences that are splitted between two exons, which can be useful when using cDNA sequences as queries.
                        The ones that remain unaligned
                        will be used afterwards to align against another database, first with Blast, then with GMAP.
                        Note that the user can choose to use only Blast or GMAP, which will be faster, although less sensitive.
                        <br/><br/>
                        There is an additional difference between the Blast and the GMAP alignment. In both cases, results are filtered according to identity
                        and coverage thresholds, and alignments to multiple targets with the same map position are merged.
                        However, when post-processing Blast results, Barleymap chooses only the ones with the best bit score for a given query.
                        This is different from GMAP, in which an alignment score is calculated in function of query aligned segment length and alignment identity.
                        In addition, filter steps for GMAP results remove those ones that have been identified as chimeras.
                        <br/><br/>
                        Internally, once Barleymap has a list of query-target pairs, obtained by means of Blast and GMAP alignments,
                        map data is retrieved
                        to obtain the known position of targets. Therefore, target position can be assigned to the associated query. 
                        Thus, alignments are performed
                        once to obtain the position from multiple maps.
                        <br/>
                        """.format(base_url))
        
        # PIPELINE IMAGE
        output_buffer.append("""
                        <br/>
                        <center><img width="499" height="526" style="float:right;margin-left:80px;margin-right:0px;border:none;" src="{0}"/></center>
                        """.format(base_url+"/img/barleymap_popseq.pipeline_2.png"))
        
        output_buffer.append("""
                        
                        <h3 id="alignment_input_and_parameters">Alignment input and parameters</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                        <br/>
                        The user of Barleymap "Align sequences" must provide the input as FASTA formatted sequences.
                        This can be done by pasting sequences in the "Input FASTA sequences" text area, or by uploading a file to the server.
                        <br/><br/>
                        In the other hand, under the "Choose an action" area, the user can choose the alignment mode, and the minimum identity (min.id.)
                        and minimum query coverage (min. query cov.) thresholds. There are three alignment modes in Barleymap:
                        <ul class="help_list">
                            <li>"auto": both Blast and GMAP are used, as described above.</li>
                            <li>"cdna": uses only GMAP, what would be beneficial specially when aligning cDNA queries.</li>
                            <li>"genomic": uses only a Blast (megablast) search.</li>
                        </ul>
                        
                        Finally, the user can choose the databases and maps for which results will be retrieved.
                        The selection lists are in the "Choose genetic/physical maps and databases" area.
                        If more than one map is chosen, results are separated so that output for each
                        of the maps can be read and downloaded independently.
                        In the case of databases, Barleymap aligns the queries to them sequentially,
                        in the hierarchical order shown in the selection list. The user can activate/desactivate databases but the order can not be changed
                        (note that this behaviour can be changed in the <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone version</a>, though).
                        This means that, if active, "MorexWGS" would be always the first database used (i.e.: all the query sequences will be aligned against it)
                        while "BACEndSequences" would be the last one (i.e.: will be used as subject for aligning the sequences that remain unmapped in the other databases).
                        <br/><br/>
                        The options under "Output options" and "Genes/Markers enrichment" are common for both Barleymap applications, so they are discussed below.
                        <br/><br/>
                """.format(base_url))
        
        ## FIND MARKERS
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="find_markers">Find markers</h2>
                    
                        <h3 id="barleymap_datasets">Barleymap datasets</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        An alignment search for many sequences at once can take a long time. However, some of those sequences can be
                        expected to be searched repeatedly. For example, those corresponding to molecular markers used
                        for genotyping many mapping populations.
                        Therefore, for some sequences, the alignment results have been stored and can be recovered just by looking up their
                        unique identifiers. This is what Barleymap "Find markers" uses as dataset (or pre-calculated dataset).
                        <br/><br/>
                        The only caveat of these datasets could be the fact that have been generated by fixing some of the parameters
                        that otherwise can be
                        tuned when using "Align sequences" or, to a more extent, when using the <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone version</a> 
                        of Barleymap. All the pre-calculated datasets have been obtained by
                        aligning the sequences to the references
                        MorexWGS, BowmanWGS, BarkeWGS, SequencedBACs, BACEndSequences;
                        and by using 98% and 95% as identity and coverage thresholds respectively. All of them will be queried
                        as having been generated hierarchically using the databases in the previous order.
                        <br/><br/>
                        In addition, the generation of a unique table of results from several datasets could be used to combine data from different platforms.
                        For example, when a mapping population has been genotyped with both GBS and microarray based SNPs.
                        On the other hand, in the previous version of Barleymap, the user could choose which datasets were used as reference.
                        However, being "Find markers" a fast process, in this version all datasets are always queried by Barleymap.
                        The user only needs to choose the maps for which he wants to obtain the results, what can be
                        done using the "Choose genetic/physical maps" selection list.
                        <br/><br/>
                        
                        <h3 id="input_for_finding_markers">Input for finding markers</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        The user must supply a list of identifiers in the "Input a list of marker IDs" text area, or by uploading a file with such list.
                        It is important then that the different datasets and their marker identifiers are known, so that the user is aware of which
                        ones to use as queries. Currently, the following datasets are available:
                        <ul class="help_list">
                            <li>
                                <b>BOPA1</b> dataset<sup>[11]</sup>: bears 1,536 sequences.
                                "BOPA consensus" (e.g.: 11_20003 or 11_10017) or "POPA12" identifiers must be provided (e.g.: ABC09016-2-2-348 or 7174-365).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [11] (supplementary Table S9).
                            </li>
                            <li>
                                <b>BOPA2</b> dataset<sup>[11]</sup>: bears 1,536 sequences.
                                "BOPA consensus" identifiers must be provided (e.g.: 12_31342 or 12_31187).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [11] (supplementary Table S10).
                            </li>
                            <li>
                                <b>Illumina iSelect Infinium</b><sup>[5]</sup>: 7,864 sequences.
                                "iSelect" identifiers must be provided (e.g.: i_11_20502 or i_BK_05).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [5'] (supplementary Table 6).
                                <br/>
                                (Illumina Infinium iSelect technology belongs to Illumina®)
                            </li>
                            <li><b>DArTs</b><sup>[6]</sup>: 2,000 sequences (e.g.: bPb-3150_PUR_f+r or bPb-2614_WSU_r).
                                <br/>Sequences for DArTs can be found at [6'].
                            </li>
                            <li><b>DArTseq SNPs</b><sup>[7]</sup>: 8,535 sequences (e.g.: 3254894|F|0 or 3260868|F|0).</li>
                            <li><b>DArTseq PAVs (SilicoDArTs)</b><sup>[7]</sup>: 15,526 sequences (e.g.: 3271396|F|0 or 3272248|F|0).
                                <br/>
                                NOTE that 1,761 sequences from DArTseq are PAVs and contain SNPs, so that the identifier is the same for both markers.
                                <br/>
                                (DArTs<sup>TM</sup> and DArTseq<sup>TM</sup> technologies belong to Diversity Arrays Technology®)
                            </li>
                            <li><b>Oregon Wolfe Barley GBS SNPs</b><sup>[8]</sup>: 34,396 sequences (e.g.: owbGBS1162 or owbGBS34926).
                                <br/>
                                A full list of markers their sequences can be found at the previous reference (supplementary Dataset S1).
                            </li>
                            <li><b>Haruna nijo cultivar flcDNAs</b><sup>[9]</sup>: 28620 sequences (e.g.: AK358336.1 or AK248138.1).</li>
                            <li><b>HarvEST Unigenes (assembly #36)</b><sup>[10]</sup>: 70148 sequences (e.g.: U36_70143 or U36_998).</li>
                        </ul>
                        
                        Comprehensive lists of identifiers of markers and mapping statistics will be published soon.
                        <br/>
                        Also we hope to keep adding new pre-calculated datasets as they become available.
                        <br/>We shall be pleased to add
                        any dataset you suggest to the web application, if the use of its sequences is public.
                        <br/>Alternatively, you could add your own datasets to Barleymap in the <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone version</a>.
                        <br/><br/>
                        The options under "Output options" and "Genes/Markers enrichment" are common for both Barleymap applications, so they are discussed below.
                        <br/><br/>
                """.format(base_url))
        
        ## OPTIONS: OUTPUT AND ENRICHMENT
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="output_options_and_genes_markers_enrichment">Output options and genes/markers enrichment</h2>
                    
                        <br/>
                        Both "Align sequences" and "Find markers" have two common sets of options: "Output options" and "Genes/Markers enrichment".
                        <br/>
                        
                        <h3 id="output_options">Output options</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        In this area, there are three general options related to the output of Barleymap.
                        <ul class="help_list">
                            <li>"Markers with multiple mappings" allows to either show or filter out the queries which have multiple mappings as result
                            (see below the "Barleymap output" section for more information on multiple mappings).</li>
                            <li>"Sort by" can be used to change the sorting field of the Barleymap results, by centimorgan (cM) or basepairs (bp)*.
                            Note that this affects the extended search of genes and markers, as explained below.</li>
                            <li>"Send by e-mail" request Barleymap to send the CSV result files to a given address.
                            This can be useful specially when mapping many markers by alignment, since the process could take several minutes,
                            or when the user is interested in the CSV files, so he/she does not need to download manually each of them.</li>
                        </ul>
                        
                        <h3 id="genes_markers_enrichment_and_annotation">Genes/markers enrichment and annotation</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                        <br/>
                        The "Genes/Markers enrichment" area allows to manage the information of genes or markers that will be shown in their respective enriched
                        maps (see "Barleymap output" below). Note that these maps are only generated when all markers map to a single chromosome
                        (although in the <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone version</a> they can be retrieved
                        for any result set).
                        <br/><br/>
                        For genes, the data used is that from IBSC transcriptome<sup>[1]</sup>. Regarding markers, those from Illumina iSelect Infinium,
                        DArTs, DArTseq and OWB GBS will be shown if they are located in the mapping region. In addition, those genes that are target of alignment of the
                        previous markers will be reported for each marker shown. Such marker-genes hits have been obtained by using the
                        <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone pipeline</a> of Barleymap
                        to align marker's sequences to the HC and LC genes from IBSC. All alignments have been performed in hierarchical mode, with both Blastn and
                        GMAP active and with default identity and coverage thresholds.
                        <br/><br/>
                        There are two basic options in the "Show genes"
                        radiobutton, that affect only to the map enriched with genes:
                        <br/>
                        <ul class="help_list">
                            <li>"On marker" can be selected to show the genes that have associated the same position as each one of the markers of the results table.</li>
                            <li>If the user is interested in showing the genes between each two markers of the results table,
                            he/she should select the "between" option. Note that for the map enriched with markers, this is always the case.</li>
                        </ul>
                        
                        Both with "on marker" or "between" selected, other options can be chosen by the user. When "Load genes annotation" checkbox
                        is marked, functional annotation of genes (InterPro, GeneOntology and others) from IBSC will be added
                        to the results table of the map with genes information .
                        <br/><br/>
                        The "Extend genes/markers search" allows to find genes and markers that are beyond de positions of mapped markers. For the map with genes,
                        it has a different behaviour depending on the "Show genes" option currently selected.
                        In both cases, the unit (or distance) to extend the search of genes can be specified. It will be centimorgans or basepairs,
                        depending on the value selected at the "Sort by" field under "Output options" area*.
                        However, if "on marker" is active,
                        genes information upstream and downstream of each gene will be added to the results, according to the unit (cM or bp) specified.
                        If "between" is selected, when "Extend genes search" is active, genes information upstream and downstream of the first and last marker
                        of each chromosome,
                        respectively, will be appended to the results. This is always the behaviour when extending the search for the map enriched with markers.
                        <br/><br/>
                """.format(base_url))
        
        ## OUTPUT
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="barleymap_output">Barleymap output</h2>
                    
                        <br/>
                        Barleymap shows up to five tables of results: "Map", "Map with genes", "Map with markers", "Markers without map position" and
                        "Unaligned markers".
                        
                        <br/>
                        
                        <h3 id="mapping_results">Mapping results</h3>
                        <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        The mapping results are reported in the <strong>"Map"</strong> table, sorted by chromosome and centimorgans or basepairs,
                        depending on user's choice*.
                        The fields related with mapping and position of queries are shown:
                        <ul class="help_list">
                            <li>"Marker": identifier of the query sequence, either the user supplied value in "Find markers" or the FASTA header
                            of the sequence in "Align sequences."
                            </li>
                            <li>"chr": chromosome.</li>
                            <li>"cM": centimorgans position*.</li>
                            <li>"bp": basepairs position*.</li>
                            <li>"multiple positions": whether the current query sequence has more than one different mapping position in the current map.
                                <br/>
                                However, a sequence with more than one alignment target is not considered
                                as having multiple positions if only one map position has been found.
                                <br/>This field is shown only if "Markers with multiple mappings" radio button has the "show" option selected.
                                <br/>
                            </li>
                            <li>"other alignments": whether the current query sequence has other alignment targets which lack map position.
                                <br/>
                                In this case, the sequence could be considered as appearing more than once in the reference, but the position information
                                is not available for all the alignments in the current map.
                                <br/>At least one unmapped alignment should be found in the "Markers without map position" table for such query
                                (see "Unmapped and unaligned markers" below).
                            </li>
                        </ul>
                        
                        <h3 id="map_enriched_with_genes_information">Map enriched with genes information</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        A second table of results will be reported if all the queries hit the same chromosome. Such table, <b>"Map with genes"</b>,
                        is enriched with genes that are located around or between markers (according to the "Show genes" option selected).
                        Thus, in addition to the fields from the "Map" table, other fields are added related with the genes found:
                        
                        <ul class="help_list">
                            <li>"Gene": gene identifier.</li>
                            <li>"HC/LC": whether the current gene is classified as High Confidence or Low Confidence in the IBSC data.</li>
                            <li>"chr", "cM", "bp"*: position associated to this gene.
                                <br/>
                                Note that the position of the gene corresponds to the position of the query sequence that has been selected in the "Sort by" option
                                of the "Output options" area*. For example, if results are sorted by centimorgans, the gene associated to a position will have the
                                same centimorgan value, but the basepairs value could be different.
                            </li>
                        </ul>
                        
                        Moreover, depending on whether "Load genes annotation" is active, more fields may be added as columns of the results table.
                        
                        <ul class="help_list">
                            <li>"Description": human readable description of current gene.</li>
                            <li>"InterPro": identifiers of the domains detected in the current gene.</li>
                            <li>"Signatures": predictive models obtained from InterPro's signatures.</li>
                            <li>"GO terms": identifiers of the GeneOntology terms annotated for this gene.</li>
                        </ul>
                        
                        <h3 id="other_markers_located_in_the_mapping_interval">Other markers located in the mapping interval</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        Similar to the "Map with genes" table, the <b>"Map with markers"</b> one will be shown if all the queries hit the same chromosome.
                        In this case, the mapping results are enriched with information of markers that are
                        located between the queries, providing the following additional fields:
                        
                        <ul class="help_list">
                            <li>"Marker": marker identifier.</li>
                            <li>"Dataset": the dataset which this marker belongs to (see "Find markers" section above).</li>
                            <li>"chr", "cM", "bp"*: position associated to this marker.
                                <br/>
                                Note that the position of the marker corresponds to the position of the query sequence that has been selected in the "Sort by" option
                                of the "Output options" area*. For example, if results are sorted by centimorgans, the marker associated to a position will have the
                                same centimorgan value, but the basepairs value could be different.
                            </li>
                            <li>"genes": a list of genes associated to this marker.
                                <br/>
                                If markers from a dataset have been aligned to genes, the list of alignment hits is shown.
                                If no hits were found for one marker, its field will be filled with the text "no hit".
                                However, some datasets could lack such information. In such case, "nd" (no data) will be the value of this field.
                            </li>
                        </ul>
                        
                        <h3 id="unmapped_and_unaligned_markers">Unmapped and unaligned markers</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        In addition to the mapping results, two more tables are shown for each map.
                        <br/><br/>
                        The <b>"Markers without map position"</b> table shows those query-target pairs, obtained from alignment step,
                        for which position of the target is not available for the current map.
                        However, this does not mean that the marker is unmapped, since it could have a map position from a
                        different alignment target in the mappings table.
                        <br/><br/>
                        The <b>"Unaligned markers"</b> table shows the identifiers of those sequences for which no valid alignment has been found.
                        <br/><br/>
                        
                        <h3 id="other_features">Other features</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        Finally, the web page showing the results of Barleymap has other features.
                        First, the mappings table as well as the enriched ones can be downloaded independently for each map as a CSV file.
                        Second, navigation through the different maps and tables is facilitated
                        by different hyperlinks provided along with the results.
                        Finally, some of the fields of the mappings table, as "Gene" or "InterPro" field, link to external resources where information about
                        structure or function of the feature could be obtained.
                        <br/><br/>
            """.format(base_url))
        
        ## CONFIDENTIALITY
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="confidentiality">Confidentiality</h2>
                    
                        <br/>
                        The general question an user could have when using BARLEYMAP, regarding privacy of the data, it could be:
                        <br/>
                        What about the security aspects of the plant breeders for using BARLEYMAP
                        <br/><br/>
                        Unfortunately, we can not guarantee the security of the data used with the web tool.
                        Currently, it is NOT using any kind of encryption algorithm for sending and receiving data (such as https).
                        However, the results obtained by users are private as only they have access to them.
                        In addition, input data are removed from the server after completion of the job.
                        <br/><br/>
                        Should this naïve confidentiality be not acceptable to some users, then we recommend they install and use the
                        <a href="http://eead.csic.es/compbio/soft/barleymap.php">standalone software</a>.
                        This opens the available options, since it can be used to serve the application in
                        several ways (e.g.: a Galaxy local server). In addition, we plan to make the web
                        application available as well, so that interested users could make a local install.  
                        <br/><br/>
            """.format(base_url))
        
        ## DISCLAIMER
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="disclaimer">Disclaimer</h2>
                        <br/>
                        This service is available AS IS and at your own risk.
                        EEAD/CSIC do not give any representation or warranty nor assume
                        any liability or responsibility for the service or the results posted
                        (whether as to their accuracy, completeness, quality or otherwise).
                        Access to the service is available free of charge for ordinary use
                        in the course of academic research.
                        <br/><br/>
                    <hr/>
                </section>
                <br/>
            """.format(base_url))
        
        ## APPENDIX
        
        output_buffer.append("""
                <section class="help_section">
                    * Note that the user's choice for "Sort by" will applied only for those maps
                      with both centimorgans and basepairs information available.
                      For example, POPSEQ data will be always sorted and retrieved based on centimorgans. Accordingly, base pairs and centimorgans
                      fields will be only reported if available.
                    <br/><br/>
                    
                    WGS: Whole Genome Shotgun<br/>
                    BAC: Bacterial Artifial Chromosome<br/>
                    cDNA: complementary DNA<br/>
                    GBS: Genotyping By Sequencing<br/>
                    SNPs: Single Nucleotide Polymorphisms<br/>
                    PAVs: Presence-Absence Variations<br/>
                </section>
                <br/>
                <section class="help_section">
                
                    <cite><sup>[1]</sup><a href="http://dx.doi.org/10.1038/nature11543"
                                            target="_blank">IBSC 2012</a></cite>
                    <br/>
                    <cite><sup>[2]</sup><a href="http://onlinelibrary.wiley.com/doi/10.1111/tpj.12319/abstract"
                                            target="_blank">Mascher et al. 2013</a></cite>
                    <br/>
                    <cite><sup>[3]</sup><a href="http://www.ncbi.nlm.nih.gov/pubmed/2231712"
                                            target="_blank">Altschul et al. 1990</a></cite>
                    <br/>
                    <cite><sup>[4]</sup><a href="http://bioinformatics.oxfordjournals.org/content/21/9/1859.long"
                                            target="_blank">Wu and Watanabe 2005</a></cite>
                    <br/>
                    <cite><sup>[5]</sup><a href="http://www.scribd.com/doc/110542041/18/A-9K-Infinium-array-for-the-characterization-of-barley-lines-and-genetic-mapping"
                                           target="_blank">Ganal et al. 2011</a></cite>
                    <br/>
                    <cite><sup>[5']</sup><a href="http://www.nature.com/ng/journal/v44/n12/full/ng.2447.html"
                                           target="_blank">Comadran et al. 2012</a></cite>
                    <br/>
                    <cite><sup>[6]</sup><a href="http://www.pnas.org/content/101/26/9915.full"
                                           target="_blank">Wenzl et al. 2004</a></cite>
                    <br/>
                    <cite><sup>[6']</sup><a href="http://www.diversityarrays.com/dart-map-sequences"
                                           target="_blank">www.diversityarrays.com</a></cite>
                    <br/>
                    <cite><sup>[7]</sup><a href="http://link.springer.com/protocol/10.1007%2F978-1-61779-870-2_5"
                                           target="_blank">Kilian et al. 2012</a></cite>
                    <br/>
                    <cite><sup>[8]</sup><a href="http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0032253"
                                           target="_blank">Poland et al. 2012</a></cite>
                    <br/>
                    <cite><sup>[9]</sup><a href="http://www.plantphysiol.org/content/156/1/20"
                                           target="_blank">Matsumoto et al. 2011</a></cite>
                    <br/>
                    <cite><sup>[10]</sup><a href="http://harvest.ucr.edu"
                                           target="_blank">HarvEST</a></cite>
                    <br/>
                    <cite><sup>[11]</sup><a href="http://www.biomedcentral.com/1471-2164/10/582/"
                                           target="_blank">Close et al. 2009</a></cite>
                    <br/>
                </section>
                <br/>
                <hr/>
            </article>
            """)
        output_buffer.append("""
            <a href="{0}"><img style="width:5%;height:5%;border:none;" src="{1}" alt="back"/></a>
        </section> <!-- content -->
        """.format(base_url+"/", base_url+"/img/back.gif"))
        
        return "".join(output_buffer)

## END