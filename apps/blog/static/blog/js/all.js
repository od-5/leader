$(document).ready(function () {

  $('.header-nav a').each(function(){
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
    if ($(this).scrollTop() > 100){
      $('.header-fix-top').addClass('fixed');
      $('.blog').addClass('margin');
    }else{
      $('.header-fix-top').removeClass('fixed');
      $('.blog').removeClass('margin');
    }

    var t = $(this).scrollTop() + 275;
    var sid = '';
    var lid = '';
    $('.header-nav a').each(function(){
      var id = $(this).attr('href').replace('/', '');
      var o = $(id).offset().top;
      if(o < t){
        sid = id;
      }
    });
    var lid = sid.replace('#', '');
    $('.header-nav a').removeClass('active');
    if(lid){
      $('.header-nav a.' + lid).addClass('active');
    }

  });
  // scroll
  $('.header-nav a').click(function(e){
    e.preventDefault();
    var selected = $(this).attr('href').replace('/', '');
    $.scrollTo(selected, 1000, {offset: -0});
    return false;
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
        },
        comment: {
          required: true
        },
        terms: {
          required: true
        }
      },
      messages: {
        phone: false,
        name: false,
        mail: false,
        comment: false,
        terms: 'Вы не можете оставить заявку без согласия на обработку персональных данных'
      }
    });
  });
  $('form').ajaxForm({
    success: function(data){
      var error = data.error;
      if (error) {
        $('form').resetForm();
        $.notify('Сообщение не было отправлено. Проверьте правильность ввода данных!', 'error');
      } else {
        $('form').resetForm();
        if (data.sender) {
          $.notify('Спасибо, что подписались на нашу рассылку!', 'success');
        } else {
          if (data.comment) {
            $.notify('Ваш комментарий появится на сайте в ближайшее время. Если не хотите ждать - обновите страницу', 'success');
          } else {
            $.notify('Ваше сообщение успешно отправлено!', 'success');
          }
        }
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

  // comment form
  $(document).on('click','.comment-button',function(e){
    e.preventDefault();
    var form = $(this).parent().find('.comment-form');
    if($(this).hasClass('comment-vis')){
      $('.comment-button').removeClass('comment-vis');
      $('.comment-form').slideUp();
    }else{
      $('.comment-button').removeClass('comment-vis');
      $('.comment-form').slideUp();
      $(form).slideDown();
      $(this).addClass('comment-vis').hide();
    }
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

  //Скрипт подгрузки статей
  var button_selector = $('#js-button-show-more-post');
  $('.blog-list').on('click', '#js-button-show-more-post', function(){
    console.log('start');
    console.log(button_selector.data('count'));
    $.ajax({
      type: "GET",
      url: button_selector.data('ajax-url'),
      data: {
        count: button_selector.data('count'),
        section: button_selector.data('section'),
      }
    }).done(function( data ) {
      if (data.post_list) {
        var post_list = data.post_list;
        for(var i=0; i < post_list.length; i++){
          console.log(post_list[i]['title']);
          console.log(post_list[i]['created']);
          console.log(post_list[i]['video']);
          console.log(post_list[i]['image']);
          console.log(post_list[i]['url']);
          console.log(post_list[i]['description']);
          console.log(post_list[i]['comment']);
          if (post_list[i]['image']) {
            var image = '<a href="' + post_list[i]['url'] + '" class="blog-img">' +
                          '<img src="' + post_list[i]['image'] + '" alt="' + post_list[i]['title'] + '">' +
                        '</a>';
          } else {
            var image = '';
          }
          button_selector.before(
            '<div class="blog-item">' +
              image +
              post_list[i]['video'] +
              '<h3>' + post_list[i]['title'] + '</h3>' +
              '<div class="blog-line">' +
                '<span class="blog-date">' + post_list[i]['created'] + '</span>' +
                '<a href="' + post_list[i]['url'] + '#comment" class="blog-comment-link">комментариев: ' + post_list[i]['comment'] + '</a>' +
              '</div>' +
              '<div class="blog-text">' + post_list[i]['description'] + '</div>' +
              '<div class="blog-button"><a href="' + post_list[i]['url'] + '" class="submit">Читать далее</a></div>' +
            '</div>'
          );
        }
        console.log('next: '+ data.next);
        if (data.next) {
          button_selector.data('count', data.next);
        }

        console.log('has data');
      } else {
        if (data.error) {
          console.log('error');
        } else {
          if (data.end) {
            console.log('end of list');
            button_selector.text('Новых статей не найдено');
            button_selector.attr('disabled', 'disabled');
          }
        }
      }
    });
  });
});
