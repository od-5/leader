$(document).ready(function () {
	
	$('.scroll a').each(function(){
		var some_id = $(this).attr('href').replace('#', '');
		$(this).addClass(some_id);
	});
	$(window).scroll( function(){
		if ($(this).scrollTop() > 1004){
			$('.header-fix').addClass('fixed');
			$('.header-main').addClass('margin');
		}else{
			$('.header-fix').removeClass('fixed');
			$('.header-main').removeClass('margin');
		}
		
		var t = $(this).scrollTop() + 275;
		var sid = '';
		var lid = '';
		$('.scroll a').each(function(){
				
			var nav = $('.scroll a');
			if (nav.length) {
				var id = $(this).attr('href').replace('/', '');
				var o = $(id).offset().top;
				if(o < t){
					sid = id;	
				}	
			}	
							
		});
		var lid = sid.replace('#', '');
		$('.scroll a').removeClass('active');
		if(lid){
			$('.scroll a.' + lid).addClass('active');
		}
		
	});
	// scroll
	$('.scroll a').click(function(e){
		e.preventDefault();
		var selected = $(this).attr('href').replace('/', '');
		$.scrollTo(selected, 1000, {offset: -0});
		return false;
	});
	
	$('#slider').nivoSlider({
		effect: 'fold',                 // Specify sets like: 'fold,fade,sliceDown'
		slices: 10,                     // For slice animations
		boxCols: 8,                     // For box animations
		boxRows: 4,                     // For box animations
		animSpeed: 500,                 // Slide transition speed
		pauseTime: 3000,                 // How long each slide will show
		startSlide: 0,                     // Set starting Slide (0 index)
		directionNav: false,             // Next & Prev navigation
		controlNav: true,                 // 1,2,3... navigation
		controlNavThumbs: false,         // Use thumbnails for Control Nav
		pauseOnHover: false,             // Stop animation while hovering
		manualAdvance: false,             // Force manual transitions
		prevText: 'Prev',                 // Prev directionNav text
		nextText: 'Next',                 // Next directionNav text
		randomStart: false             // Start on a random slide
	});
	// fancybox
	$('.fancybox').fancybox();
	$(".input[name='phone']").mask("+7 (999) 999-99-99");
	$('form').each(function(){
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
				}
			}
	    });
	});	
	$('form').ajaxForm({
    success: function(data){
      var error = data.error;
      if (error) {
        $('form').resetForm();
        $.notify('Сообщение не было отправлено. Проверьте правильность ввода данных!', 'error');
        console.log(error);
      } else {
        $('form').resetForm();
        $.notify('Ваше сообщение успешно отправлено!', 'success');
        console.log('not error');
      }
    }
  });
	// city hidden
	$(document).on('click','.header-city-link a',function(e){
		e.preventDefault();
		if($(this).hasClass('active')){
			$(this).removeClass('active');
			$('.city-hidden').slideUp();
		}else{
			$(this).addClass('active');
			$('.city-hidden').slideUp();
			$('.city1').slideDown();
		}	
	});
	$(document).on('click','.header-fix-link a',function(e){
		e.preventDefault();
		$('.header-city-link a').removeClass('active');
		if($(this).hasClass('active')){
			$(this).removeClass('active');
			$('.city-hidden').slideUp();
		}else{
			$(this).addClass('active');
			$('.city-hidden').slideUp();
			$('.city2').slideDown();
		}
	});
	$(document).on('click','.city-close',function(e){
		e.preventDefault();
		$('.city-hidden').slideUp();
		$('.header-city-link a, .header-fix-link a').removeClass('active');
	});
	 	
	
	//Скрипт всплывающих окон  
	$('.modal').click(function(e) {
		e.preventDefault();
		$('#mask, .window').hide();
		var id = $(this).attr('href');
		var maskHeight = $(document).height();
		var maskWidth = $(window).width();
		$('#mask').css({'height':maskHeight});
		$('#mask').fadeTo("slow",0.9);
		var winH = $(window).height();
		var winW = $(window).width();
		$(id).css('top',  winH/2-$(id).height()/2);
		$(id).css('left', winW/2-$(id).width()/2);
		$(id).fadeIn(1000);	
	});
	$('.window .close').click(function (e) {
		e.preventDefault();
		$('#mask, .window').hide();
	});
	$('#mask').click(function () {
		$(this).hide();
		$('.window').hide();
	});
	//Скрипт всплывающих окон
		
		// animation trigger	
		
		$(window).scroll( function(e){		
			var document_top = $(document).scrollTop();	
			var height = $(window).height();	
			
			var about_offset = $('.about-top').offset().top - height + height/4;
			var advantages_offset = $('.advantages').offset().top - height + height/4;
			var monitor_offset = $('.video-monitor').offset().top - height + height/4;
			var tablet_offset = $('.video-tablet').offset().top - height + height/4;
			
			if (document_top > about_offset){
				setTimeout(function() {
					$('.about1').addClass('vis');
					setTimeout(function() {
						$('.about2').addClass('vis');
						setTimeout(function() {
							$('.about3').addClass('vis');
							setTimeout(function() {
								$('.about4').addClass('vis');
								setTimeout(function() { 		
									$('.about5').addClass('vis');
									setTimeout(function() { 		
										$('.about6').addClass('vis');
										setTimeout(function() { 		
											$('.about7').addClass('vis');
											setTimeout(function() { 		
												$('.about8').addClass('vis');
											}, 200)
										}, 200)
									}, 200)
								}, 200)
							}, 200)
						}, 200)
					}, 200)
				}, 200)
			};
			if (document_top > advantages_offset){
				setTimeout(function() {
					$('.ad1').addClass('vis');
					setTimeout(function() {
						$('.ad2').addClass('vis');
						setTimeout(function() {
							$('.ad3').addClass('vis');
							setTimeout(function() {
								$('.ad4').addClass('vis');
								setTimeout(function() { 		
									$('.ad5').addClass('vis');
									setTimeout(function() { 		
										$('.ad6').addClass('vis');	
									}, 200)
								}, 200)
							}, 200)
						}, 200)
					}, 200)
				}, 200)
			};
			if (document_top > monitor_offset){
				$('.video-monitor').addClass('vis');
			};	
			if (document_top > tablet_offset){
				$('.video-tablet').addClass('vis');
			};	
				
		});
	
});
