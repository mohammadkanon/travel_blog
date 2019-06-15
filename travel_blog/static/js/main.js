$(document).ready(function(){

	$("#side-menu-singup").click(function(){
		  $(this).css('display','none');
		  $("#main-menu-option-mobile").css('display','block');
		  $("#side-menu-singout").css('display','block');
          console.log("Hello World");
	});

	$("#side-menu-singout").click(function(){
         $("#side-menu-singup").css('display','block');
         $("#side-menu-singout").css('display','none');
         $("#main-menu-option-mobile").css('display','none');
    });

    $("#main-menu-option li a").hover(function(){
    	$(this).css('color','#0dc5fa');
    },function(){
        $(this).css('color','black');
    });

    $("ul#main-menu-option-mobile li a").hover(function(){
    	$(this).css('color','#0dc5fa');
    },function(){
        $(this).css('color','black');
    });

    $("#right-icons").click(function(){
    	$("#top-header-article").toggle();
    });

    $("#top-email").hover(function(){
    	$(this).css({'background':'#00aff9','padding':'3px'});
    },function(){
        $(this).css({'background':'#00aff9','padding':'0px'});
    });

    $("#slider-button1").hover(function(){
    	$(this).css({'background':'#1fb8d1','border':'#1fb8d1','cursor':'pointer','font-size':'15px','font-weight':'800'});
    },function(){
        $(this).css({'background':'','border':'','font-size':'','font-weight':''});
    });

    $("span#slider-button2").hover(function(){
    	$(this).css({'background':'transparent','border':'2px solid white','cursor':'pointer','font-size':'15px','font-weight':'800'});
    },function(){
        $(this).css({'background':'','border':'','font-size':'','font-weight':''});
    });

    $("#featured-top").click(function(){
    	$(this).toggleClass('addthecolor');
    	$("#logo-list").toggle();
    });

     $("p#article-read-me-options").hover(function(){
    	$(this).css({'cursor':'pointer'});
    },function(){
        $(this).css({'cursor':''});
    });

    $("div#line-num-one").click(function(){
    	$(".toggle-class-one").toggle();
    	$("#imag-box-one").toggle();
    	$("#add-image-section").toggle();
    });

    $("#line-num-two").click(function(){
    	$(".toggle-class-two").toggle();
    	$("#imag-box-two").toggle();
    });

    $("#line-num-three").click(function(){
    	$(".toggle-class-three").toggle();
    	$("#video-img-profile").toggle();
    });

    $("#line-num-four").click(function(){
    	$(".toggle-class-four").toggle();
    	$("#imag-box-four").toggle();
    });

    $("#line-num-five").click(function(){
    	$("#main-menu-option").toggle();
    });

   $("#latest-big-pic").hover(function(){
    	$("#hello-world").css({'display':'block'});
       },function(){
        $("#hello-world").css({'display':''});
      });

    $("#latest-small-pic").hover(function(){
   	   $("#hello-world1").css({'display':'block'});
   	   console.log("hello");
   },function(){
       $("#hello-world1").css({'display':''});
       console.log("hello2");
    });

    $("#latest-small-pic-section2").hover(function(){
          $(".hello-wordl2").css({'display':'block'});
    },function(){
          $(".hello-wordl2").css({'display':''});
    });
     
    $("p#hello-world").hover(function(){
    	$(this).css({'background':'#1ca6bebd','border':'4px solid white','font-weight':'800'});
    	 $("#hello-world").css({'display':'block'});
     },function(){
       $(this).css({'background':'','border':'','font-weight':''});
        $("#hello-world").css({'display':'block'});
     });

    $("p#hello-world1").hover(function(){
    	$(this).css({'background':'#1ca6bebd','border':'4px solid white','font-weight':'800'});
    	 $("#hello-world1").css({'display':'block'});
     },function(){
       $(this).css({'background':'','border':'','font-weight':''});
        $("#hello-world1").css({'display':'block'});
     });

    
    
	console.log("Hello World");
});


