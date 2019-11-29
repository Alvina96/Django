$(document).ready(function(){
	$(".burger button").on("click", function () {
		$(".burger button").toggleClass("active");
		$(".header__menu ul").slideToggle();
		$(".menu__under").hide();
	})
});
$(document).ready(function(){
	$(".fancybox").fancybox({
		"padding": '0',
		'scrolling':  'no',
		"height" : '1100',
		autoCenter: false,
		helpers: {
			overlay: {
				locked: false
			}
		}
	})
});

function tabInit(){ 
	$('.tabs__content').not('.tabs__content_active').hide(); 
	$('.tabs-list__item button').click(function(){ 
		$('.tabs-list__item').not($(this).parent()).removeClass('tabs-list__item_active'); 
		$(this).parent().addClass('tabs-list__item_active'); 
		$('.tabs__content').not('#'+$(this).attr('data-content')).removeClass('tabs__content_active').hide(); 
		$('#'+$(this).attr('data-content')).addClass('tabs__content_active').fadeIn(); 
	}); 
}; 
tabInit();
function tabInit1(){ 
	$('.tabs__content1').not('.tabs__content_active1').hide(); 
	$('.tabs-list__item1 button').click(function(){ 
		$('.tabs-list__item1').not($(this).parent()).removeClass('tabs-list__item_active1'); 
		$(this).parent().addClass('tabs-list__item_active1'); 
		$('.tabs__content1').not('#'+$(this).attr('data-content')).removeClass('tabs__content_active1').hide(); 
		$('#'+$(this).attr('data-content')).addClass('tabs__content_active1').fadeIn(); 
	}); 
}; 
tabInit1();
$(document).ready(function(){
	$(".info-item__title").on("click", function () {
		$(this).parent().toggleClass("active");
		$(this).siblings(".info-item__body").slideToggle();
		$(this).parent().siblings(".info-item").removeClass("active");
		$(this).parent().siblings(".info-item").children(".info-item__body").slideUp();
	})
});
$(document).ready(function(){
	$(".tree-item h4").on("click", function () {
		$(this).parent().toggleClass("active");
		$(this).parents('.col-sm-3').siblings().children(".tree-item").removeClass("active");
	})
});
$(document).ready(function(){
	$(".tovar__title").on("click", function () {
		$(this).parent().toggleClass("active");
		$(this).siblings(".tovar__body").slideToggle();
	})
});

	$(".news-box").niceScroll({
		cursorcolor: "#cfd7dd",
		cursorwidth: "17px",
		cursorborderradius: "0px"
	});
$(document).ready(function(){
	$(".leson-wrap").niceScroll({
		cursorcolor: "#cfd7dd",
		cursorwidth: "17px",
		cursorborderradius: "0px"
	});
	$(".min-les").niceScroll({
		cursorcolor: "#cfd7dd",
		cursorwidth: "17px",
		cursorborderradius: "0px"
	});
	// $(".news-btn").on("hover", function () {
	// 	$(".fanc-wrap").fadeToggle();
	// })
});

$(document).ready(function(){
	$(".coments-read").niceScroll({
		cursorcolor: "#cfd7dd",
		cursorwidth: "17px",
		cursorborderradius: "0px",
		railalign: "left"
	});
});

$(document).ready(function(){
	$(".min-les").niceScroll({
		cursorcolor: "#cfd7dd",
		cursorwidth: "17px",
		cursorborderradius: "0px"
	});
	// $(".news-btn").on("hover", function () {
	// 	$(".fanc-wrap").fadeToggle();
	// })
});

$(document).ready(function(){
	$(".hide-lesson").on("click", function () {
		$(".tree-item p").hide();
		$(".tree-item__img").hide();
		$(".tree-item__btn").hide();
	})
});

$(document).ready(function(){
	$(".show-lesson").on("click", function () {
		$(".tree-item p").show();
		$(".tree-item__img").show();
		$(".tree-item__btn").show();
	})
});
