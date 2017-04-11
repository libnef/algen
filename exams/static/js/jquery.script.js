$(document).ready(function(){
	$(".solution").hide();
	$(".hide_it").hide();
   	// jQuery methods go here...
   	$(".show_it").click(function(){
    	$(".solution").show();
    	$(".show_it").hide();
    	$(".hide_it").show();
	});

	$(".hide_it").click(function(){
    	$(".solution").hide();
    	$(".hide_it").hide();
    	$(".show_it").show();
	});
});