
$(function() {
    $('#filter_panel').change(function(){
        var selected_brand = $('input[class="brand"]:checked').map(function(){return this.value;}).get();
        var selected_color = $('input[class="color"]:checked').map(function(){return this.value;}).get();
        var selected_movement = $('input[class="movement"]:checked').map(function(){return this.value;}).get();
        var selected_type = $('input[class="type"]:checked').map(function(){return this.value;}).get();
        var filter_price_max = $( "#slider-range" ).slider( "values", 1 );
        var filter_price_min = $( "#slider-range" ).slider( "values", 0 )
        var filter_list = []
//        var selected_price = [], selected_color =[], selected_brand = []
//        $(".checkbox .brand:checked").each(function(){
//                selected_brand.push($(this).val());
//        });

        $.ajax({
            url: "/search/", // link of your "whatever" php
            type: "POST",
            data: {
                "selected_brand[]": selected_brand,
                "selected_color[]": selected_color,
                "selected_movement[]": selected_movement,
                "selected_type[]": selected_type,
                filter_price_max,
                filter_price_min,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken").val(),
                 // all data will be passed here
            },
            success: function(data){
                 $('#search-results').html(data);
            }
        });
        })
        });




$('#index_filter').submit(function (e) {
    e.preventDefault();
    console.log("Inside click");
    var selected_brand = $('input[class="brand"]:checked').map(function(){return this.value;}).get();
    var selected_movement = $('input[class="movement"]:checked').map(function(){return this.value;}).get();
    var filter_price_max = $( "#slider-range" ).slider( "values", 1 );
    var filter_price_min = $( "#slider-range" ).slider( "values", 0 );
    $.ajax({
        url: "/update_session/",
        type: "POST",
        data: {
            "selected_brand[]": selected_brand,
            "selected_movement[]": selected_movement,
            filter_price_max,
            filter_price_min,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken").val(),
             // all data will be passed here
        },
        success: function(data){
             window.location.assign('/watch');
        }
    });
});

$('#custom-search-input').submit(function () {
    $.ajax({
        url: "/update_session/",
        type: "POST",
        data: {
            "custom-search-input": $('#srchFld').val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken").val(),
             // all data will be passed here
        },
        success: function(data){
             window.location.assign('/watch');
        }
    });
});

$("input[id^='browseby']").click(function () {
    if($("input[id^='browsebybrand']")) {selected_brand = [$(this).attr('value')];}
    if($("input[id^='browsebytype']")) {selected_type = [$(this).attr('value')];}
    if($("input[id^='browsebymovement']")) {selected_movement = [$(this).attr('value')];}

    console.log(selected_brand)
    $.ajax({
        url: "/update_session/",
        type: "POST",
        data: {
            "selected_brand[]": selected_brand,
            "selected_type[]": selected_type,
            "selected_movement[]": selected_movement,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken").val(),
             // all data will be passed here
        },
        success: function(data){
             window.location.assign('/watch');
        }
    });
});

//$(function() {
//    $('#index_filter').change(function(){
//        $.post('/update_session/', function(data) {
//        alert(data);
//        });
//});
//})