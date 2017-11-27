(function($){
  $(function(){

    $('.button-collapse').sideNav();

    var path = window.location.pathname
     $(".side-nav li a").each(function(){
          if($(this).attr("href") == path)
          	$(this).addClass("active");
     })
  }); // end of document ready
})(jQuery); // end of jQuery name space