$(document).ready(function() {

    $(".ButtForOpenBar").click(function() {
        if($('.leftBarDinamic').css('width') == "0px") {
            $("#mainContainer").attr("style", "padding-left:14vw");
            $(".publicathion").attr("style", "margin-left:15%");

            $(".leftBarDinamic").attr("id", "leftBarOpen");
            $(".ButtForOpenBar").attr("id", "ButtForOpenLeftBar");
        }else{
            $(".leftBarDinamic").attr("id", "leftBarClose");
            $(".ButtForOpenBar").attr("id", "ButtForCloseLeftBar");

            $("#mainContainer").attr("style", "padding-left:0px");
            $(".publicathion").attr("style", "margin-left:10%");

        }
    });
});




$(document).ready(function() {

    $("#up_r_bar_id").click(function() {
        if($('.rightBarDinamic').css('width') == "0px") {
            $(".rightBarDinamic").attr("id", "rightBarOpen");
        }else{
            $(".rightBarDinamic").attr("id", "rightBarClose");
        }
    });
});
$(document).ready(function() {

    $("#closeLeftBar ").click(function() {
        if($('.rightBarDinamic').css('width') == "0px") {
            $(".rightBarDinamic").attr("id", "rightBarOpen");
        }else{
            $(".rightBarDinamic").attr("id", "rightBarClose");
        }
    });
});



$(document).ready(function() {

    $("#check4").click(function() {
        if($('#comentCont').css('display') == "none") {
            $("#comentCont").attr("style", "display: block");
        }else{
            $("#comentCont").attr("style", "display: none");
        }
    });
});




