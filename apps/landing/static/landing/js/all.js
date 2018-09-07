$(document).ready(function () {
	
	// fancybox
	jQuery('.fancybox').fancybox();
	
	// mob-nav
	$(document).on('click','.mob-nav-icon',function(e){
		e.preventDefault();
		if($(this).hasClass('active')){
			$(this).removeClass('active');
			$('.header-nav').removeClass('vis');
		}else{
			$(this).addClass('active');
			$('.header-nav').addClass('vis');
		}
	});

	$(".input[name='phone']").mask("+7 (999) 999-99-99");
  $('.js-ticket-form').each(function(){
    $(this).validate({
      rules: {
        name: {
          required: true
        },
        mail: {
          required: true,
          email: true
        },
        phone: {
          required: true,
          minlength: 6
        },
				terms: {
          required: true
        }
      },
			messages: {
        phone: false,
        name: false,
        mail: false,
        terms: 'Вы не можете оставить заявку без согласия на обработку персональных данных'
      }
    });
  });
	$('.js-plan-form').validate({
		rules: {
			mail: {
				required: true,
				email: true
			},
			terms: {
				required: true
			}
		},
		messages: {
			mail: false,
			terms: 'Вы не можете оставить заявку без согласия на обработку персональных данных'
		}
	});


	// typing animation
	var typed = new Typed('.type-animation', {
		strings: ["Прибыльная франшиза в сфере рекламы"],
		typeSpeed: 45
	});
	
	// scroll
	$('.scroll').click(function(e){
		e.preventDefault();
		var selected = $(this).attr('href').replace('/', '');
		$.scrollTo(selected, 1000, {offset: -20});
		return false;
	});
	// header fixed
	$(window).scroll( function(){
		if ($(this).scrollTop() > 100){
			$('.header-top').addClass('fix');	
		}else{
			$('.header-top').removeClass('fix');
		}		
	});
	
	// case show more	
	var number = 7 + Math.floor(Math.random() * 7);
	$('.order-button-text span').text(number);
	
	// case show more		
	$(document).on('click','.case-more',function(e){
		e.preventDefault();
		var expanded = $('.case-collapsed').slice(0,2);
		expanded.show();
		expanded.removeClass('case-collapsed');
		if($('.case-collapsed').length == 0) {
			$(this).parent().hide();
		}
	});
	
	// leave popup
	$('.fancy-black').fancybox({
		tpl: {
			wrap     : '<div class="fancybox-wrap black-fancybox" tabIndex="-1"><div class="fancybox-skin"><div class="fancybox-outer"><div class="fancybox-inner"></div></div></div></div>'
		}
	});
	$(".popup-trigger").mouseenter(function() {
		$(".popup-trigger-link").click();
		setTimeout(function(){
		  $('.top-trigger').addClass('hidden');
		}, 1000);
	}).mouseleave(function() {
		
	});
	$(document).on('click','.fancy-close',function(e){
		e.preventDefault();
		$.fancybox.close();
	});
	
	// review show more		
	if($(window).width() < 1024){
		$('.review-item:nth-child(3)').addClass('review-collapsed');
	}else{
		$('.review-item:nth-child(3)').removeClass('review-collapsed');
	}
	$(window).resize(function(e){
		if($(window).width() < 1024){
			$('.review-item:nth-child(3)').addClass('review-collapsed');
		}else{
			$('.review-item:nth-child(3)').removeClass('review-collapsed');
		}
	});
	$(document).on('click','.review-more',function(e){
		e.preventDefault();
		if($(window).width() < 1024){
			var expanded = $('.review-collapsed').slice(0,2);
		}else{
			var expanded = $('.review-collapsed').slice(0,3);
		}	
		expanded.show();
		expanded.removeClass('review-collapsed');
		if($('.review-collapsed').length == 0) {
			$(this).parent().hide();
		}
	});
	
	// animation trigger
	var document_top = $(document).scrollTop();
	var height = $(window).height();
	$('.animate').each(function(){
		var offset = $(this).offset().top - height + height/6;
		if(document_top > offset){
			$(this).addClass('ani_start');
		}else{
			$(this).removeClass('ani_start');
		}
	});
	$(window).scroll( function(e){
		var document_top = $(document).scrollTop();
		var height = $(window).height();
		$('.animate').each(function(){
			var offset = $(this).offset().top - height + height/6;
			if(document_top > offset){
				$(this).addClass('ani_start');
			}else{
				$(this).removeClass('ani_start');
			}
		});
		
	});
	
});


// animation parallax
function parallaxCall(e){
	parallax(e);
}
function parallax(e){
	
	var offsetX1 = e.pageX - $('.market').offset().left;
	var offsetY1 = e.pageY - $('.market').offset().top;
	$('.market-title').css({'transform' : 'translate(' + offsetX1/45 + 'px, ' + offsetY1/45 + 'px)'});
	
	var offsetX2 = e.pageX - $('.order .order-holder').offset().left;
	var offsetY2 = e.pageY - $('.order .order-holder').offset().top;
	$('.frame1').css({'transform' : 'translate(' + offsetX2/65 + 'px, ' + offsetY2/65 + 'px)'});
	$('.order-img1').css({'transform' : 'translate(' + offsetX2/25 + 'px, ' + offsetY2/25 + 'px)'});
	$('.order-img2').css({'transform' : 'translate(' + offsetX2/35 + 'px, ' + offsetY2/35 + 'px)'});
	$('.order-img3').css({'transform' : 'translate(' + offsetX2/45 + 'px, ' + offsetY2/45 + 'px)'});
	
	var offsetX3 = e.pageX - $('.order2 .order-holder').offset().left;
	var offsetY3 = e.pageY - $('.order2 .order-holder').offset().top;
	$('.frame2').css({'transform' : 'translate(' + offsetX3/65 + 'px, ' + offsetY3/65 + 'px)'});
	$('.order-img11').css({'transform' : 'translate(' + offsetX3/25 + 'px, ' + offsetY3/25 + 'px)'});
	$('.order-img12').css({'transform' : 'translate(' + offsetX3/35 + 'px, ' + offsetY3/35 + 'px)'});
	$('.order-img13').css({'transform' : 'translate(' + offsetX3/45 + 'px, ' + offsetY3/45 + 'px)'});
	//$('.bg5').css({left: -182 - (offsetX2)/15, top: -17 - (offsetY2)/15});
	//$('.bg3').css({left: -147 - (offsetX2)/30, top: 57 - (offsetY2)/30});

}
$(window).load(function(e){			
	if($(window).width() > 1024){
		$(window).bind('mousemove', parallaxCall);
	}

});












