(function ($) {
    "use strict";

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('.navbar').addClass('nav-sticky');
        } else {
            $('.navbar').removeClass('nav-sticky');
        }
    });

    // Counter
    $(document).ready(function() {
        $('.counter').each(function() {
            $(this).prop('Counter', 0).animate({
                Counter : $(this).text()
            }, {
                duration: 3500,
                easing : 'swing',
                step : function(now) {
                    $(this).text(Math.ceil(now) + '+');
                }
            })
        });
    });

})(jQuery);

// Causes carousel
$(document).ready(function() {
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        responsiveClass:true,
        center:true,
        nav:true,
        NavText:[
            "<i class='bx bx-chevron-left'></i>",
            "<i class='bx bxs-chevron-right'></i>"
        ],
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:3,
            },
            1000:{
                items:3,
            }
        }
    })
});

// Back to Top 
const toTop = document.querySelector(".to-top");
window.addEventListener("scroll", () => {
    if(window.pageYOffset > 100) {
        toTop.classList.add("active");
    } else {
        toTop.classList.remove("active");
    }
})