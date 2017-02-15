/* # index.js is part of Barleymap web app.
 * # Copyright (C)  2013-2014  Carlos P Cantalapiedra.
 * # (terms of use can be found within the distributed LICENSE file).
*/
$(document).ready(function(){
    
    if($('#genes_no').is(':checked')) {
        $("#input_extend_fieldset").hide();
        $("#genes_text").text("");
    } else if ($('#genes_between').is(':checked')) {
        $("#input_extend_fieldset").show();
        $("#genes_text").text("Genes between each two markers will be added to the results.");
    } else if ($('#genes_marker').is(':checked')) {
        $("#input_extend_fieldset").show();
        $("#genes_text").text("Genes on the position of each marker will be shown.");
    }
    
    if($("#input_extend").is(':checked')){
        $("#input_extend_text").show();
        if ($("#sort_cm").is(":checked")) {
                $("#genes_window_cm").show();
                $("#genes_window_bp").hide();
            } else {
                $("#genes_window_cm").hide();
                $("#genes_window_bp").show();
            }
    } else {
        $("#input_extend_text").hide();
        $("#genes_window_cm").hide();
        $("#genes_window_bp").hide();
    }
    
    if ($('#queries_type').children(":selected").val() == "auto") {
        $("#algorithm_text").text("Perform a BLASTN search, followed by GMAP alignment for unmapped sequences. Input data must be in FASTA format.");
    } else if ($('#queries_type').children(":selected").val() == "cdna") {
        $("#algorithm_text").text("Perform a GMAP alignment. Input data must be in FASTA format.");
    } else if ($('#queries_type').children(":selected").val() == "genomic") {
        $("#algorithm_text").text("Perform a BLASTN search. Input data must be in FASTA format.");
    }
    
    // LOAD DEMO SEQUENCES
    $("#align_demo_button").click(function(){
        $("#align_input_query").text(">i_SCRI_RS_129789\n\
AATTTACTGGTACTATGCGCAAMTATTGAAGGYCGATGAGGAAGAGTTTGGAGGCCACGGNGCGCTGCTTCAGGAGGGGATGTTCGCGTCTTTCACCCTTTTCCTGCTTTCATGGATTCTT\n\
>i_12_30948\n\
GTAGCAATCCGCCCGTGCAGGTTCCAATGGCGAGCTCGACTTGTTCCGATGACAAGGTTGNTCCCCTGGTTCAGAAACACGCACCCGCCGGAAWCCCGGAGGCGCTTACGACGACGAAGAA\n\
>i_SCRI_RS_130600\n\
CGATGAAGAAGGAGCGATCGAGAAACTCCTCCGGTGGTCCGCCGCGACATTGGAGGCAACNGCCTTGTGGGTTGCTGCTATATGTGGGGGCAAGGACCGTGATGTCTAAGTGTGCCCTGAA\n\
>i_SCRI_RS_189465\n\
ATAGAGCAATATTACTTGCATTCAGTTTTGTGTCGTCGTGGAAATTCAGATGGCCGTCTCNTGACGCCACAACGTCTTCATTCAGATCTTAATTGGAAAGCAAGAACCAAATTCTTTTTTT\n"
        );
    });
    
    $("#clear_demo_button").click(function(){
        $("#align_input_query").text("");
        $("#find_input_query").text("");
    });
    
    // LOAD DEMO IDS
    $("#find_demo_button_full").click(function(){
        $("#find_input_query").text("i_11_10419\ni_11_20854\ni_11_20855\ni_11_20856\n\
i_SCRI_RS_104699\ni_11_20851\ni_SCRI_RS_66562\ni_12_11139\ni_SCRI_RS_104697\ni_SCRI_RS_135425\ni_BK_19\ni_11_11127\n\
i_12_11504\ni_SCRI_RS_144535\ni_SCRI_RS_175682\ni_BK_10\ni_BK_10\ni_BK_10\ni_BK_10\ni_BK_10\ni_BK_11\n\
i_BK_12\ni_BK_13\ni_BK_14\ni_BK_16\ni_BK_17\ni_SCRI_RS_10111\ni_SCRI_RS_169728\ni_11_20320\ni_11_10933\n\
i_11_20454\ni_11_10935\ni_11_20325\ni_11_20458\ni_11_10939\ni_11_20328\ni_11_20853\ni_SCRI_RS_228070\n\
i_SCRI_RS_177919\ni_SCRI_RS_159526\ni_11_11359\ni_SCRI_RS_235243\ni_SCRI_RS_154541\ni_SCRI_RS_177133\n\
i_SCRI_RS_182637\ni_SCRI_RS_4697\ni_11_11352\ni_11_11350\ni_12_11181\ni_12_11183\ni_11_11354\ni_SCRI_RS_197270\n\
i_11_11222\ni_11_11221\ni_11_20537\ni_11_11227\ni_11_11224\ni_11_10336\ni_SCRI_RS_148722\ni_SCRI_RS_204144\n\
i_SCRI_RS_196677\ni_SCRI_RS_192360\ni_11_10331\ni_SCRI_RS_205658\ni_SCRI_RS_151894\ni_SCRI_RS_222357\ni_SCRI_RS_175469\n\
i_SCRI_RS_171144\ni_SCRI_RS_204353\ni_SCRI_RS_171142\ni_SCRI_RS_173807\ni_SCRI_RS_13262\ni_12_11437\ni_SCRI_RS_176086\n\
i_SCRI_RS_140931\ni_SCRI_RS_176084\ni_12_10151\ni_11_21037\ni_SCRI_RS_157816\ni_SCRI_RS_222936\ni_12_11438\n\
i_SCRI_RS_189167\ni_12_10923\ni_11_20524\ni_SCRI_RS_178618\ni_11_20526\ni_11_10807\ni_11_20521\ni_SCRI_RS_168603\n\
i_SCRI_RS_114741\ni_SCRI_RS_171543\ni_11_11534\ni_11_20514\ni_11_20528\ni_11_20529\ni_11_11530\ni_11_10480\n\
i_SCRI_RS_1426\ni_SCRI_RS_198888\ni_SCRI_RS_128254\ni_SCRI_RS_223224\ni_SCRI_RS_1429\ni_11_10775\ni_11_20660\n");
    });
    
    
    //>100002678|F|0 \n\GBS PAVs \n\>100021533|F|0--60:C>G \n\GBS SNPs"
    
    // LOAD DEMO IDS
    $("#find_demo_button_region").click(function(){
        $("#find_input_query").text("i_SCRI_RS_129789\ni_12_30588\ni_12_30948\n\
i_SCRI_RS_130600\ni_SCRI_RS_150677\ni_SCRI_RS_189465\nowbGBS13547\n");
    });
    
    $("#genes_no").click(function(){
        $("#input_extend_fieldset").hide();
        $("#genes_text").text("");
    });
    
    $("#genes_between").click(function(){
        $("#input_extend_fieldset").show();
        $("#genes_text").text("Genes between each two markers will be added to the results.");
    });
    
    $("#genes_marker").click(function(){
        $("#input_extend_fieldset").show();
        $("#genes_text").text("Genes on the position of each marker will be shown.");
    });
    
    $("#input_extend").change(function(){
        if ($(this).is(":checked")) {
            $("#input_extend_text").show();
            if ($("#sort_cm").is(":checked")) {
                $("#genes_window_cm").show();
                $("#genes_window_bp").hide();
            } else {
                $("#genes_window_cm").hide();
                $("#genes_window_bp").show();
            }
        } else {
            $("#input_extend_text").hide();
            $("#genes_window_cm").hide();
            $("#genes_window_bp").hide();
        }
    });
    
    $("#sort_cm").click(function(){
        if($("#input_extend").is(':checked')){
            $("#genes_window_cm").show();
            $("#genes_window_bp").hide();
        }
    });
        
    $("#sort_bp").click(function(){
        if($("#input_extend").is(':checked')){
            $("#genes_window_cm").hide();
            $("#genes_window_bp").show();
        }
    });
    
    $("#email_text").hide();
    
    $("#input_send_email").change(function(){
        if ($(this).is(":checked") == "1") {
            $("#email_text").show();
        } else {
            $("#email_text").hide();
        }
        
    });
    
    $("#align_my_file").change(function(){
        $("#align_clear_file_button").show();
    });
    
    $("#align_clear_file_button").click(function(){
        $(this).hide();
        $("#align_my_file").replaceWith( control = $("#align_my_file").clone( true ) );
    });
    
    $("#find_my_file").change(function(){
        $("#find_clear_file_button").show();
    });
    
    $("#find_clear_file_button").click(function(){
        $(this).hide();
        $("#find_my_file").replaceWith( control = $("#find_my_file").clone( true ) );
    });
    
    // CHANGE OF ALGORITHM
    $('#queries_type').change(function() {
        if ($('#queries_type').children(":selected").val() == "auto") {
            $("#algorithm_text").text("Perform a BLASTN search, followed by GMAP alignment for unmapped sequences. Input data must be in FASTA format.");
        } else if ($('#queries_type').children(":selected").val() == "cdna") {
            $("#algorithm_text").text("Perform a GMAP alignment. Input data must be in FASTA format.");
        } else if ($('#queries_type').children(":selected").val() == "genomic") {
            $("#algorithm_text").text("Perform a BLASTN search. Input data must be in FASTA format.");
        }
    });
});