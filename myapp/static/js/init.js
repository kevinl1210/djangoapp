(function($){
  $(function(){

  	// materialize js initialization
    $('.button-collapse').sideNav();

    // side nav bar active highlight
    var path = window.location.pathname
     $(".side-nav li a").each(function(){
          if($(this).attr("href") == path)
          	$(this).addClass("active");
     })

     // spinning pepe!
     var deg = 0
	$(".pepe").mouseover(
		function(){
			if ( typeof rollback !== "undefined" ){
				clearInterval(rollback)
			}
  			spin = setInterval(function() { 
    			deg += 5;
    			$(".pepe").css('transform', "rotate("+deg+"deg)"); 
      		}, 20);
  		}
	).mouseout(
		function(){
			clearInterval(spin);
			rollback = setInterval(function(){
			if ((deg > 360 && deg % 360 != 0) || deg < 360){
				deg += 5;
				$(".pepe").css('transform', "rotate("+deg+"deg)");
			}
			}, 30);
		}
	);

  }); // end of document ready
})(jQuery); // end of jQuery name space