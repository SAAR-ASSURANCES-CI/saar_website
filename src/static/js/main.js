(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });


    // International Tour carousel
    $(".InternationalTour-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav : false,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });


    // packages carousel
    $(".packages-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: false,
        dots: false,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });


    // testimonial carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });

    
   // Back to top button
//    $(window).scroll(function () {
//     if ($(this).scrollTop() > 300) {
//         $('.back-to-top').fadeIn('slow');
//     } else {
//         $('.back-to-top').fadeOut('slow');
//     }
//     });


$(window).scroll(function () {
    // Vérifier si le chat est ouvert
    if ($('#chatSection').is(':visible')) {
        // Si le chat est ouvert, masquer le bouton back-to-top
        // $('.back-to-top').fadeOut('slow');
        $('.back-to-top').hide();
        // $('.back-to-top').style.display = 'none';
        $('.back-to-top').css('z-index', 'initial');
    } else {
        // Si le chat n'est pas ouvert, appliquer la logique de défilement normale
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    }
});


    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    }); 


    // Amélioration des sous-menus pour mobile
    $(document).ready(function() {
        // Initialiser le menu dans l'état fermé
        $('.navbar-toggler').attr('aria-expanded', 'false');
        $('.navbar-collapse').removeClass('show');
        $('.navbar-toggler .navbar-toggler-icon').css('transform', 'rotate(0deg)');
        
        // Gestion des sous-menus sur mobile
        $('.dropdown-submenu > .dropdown-toggle').on('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            var $submenu = $(this).next('.dropdown-menu');
            var $parent = $(this).parent();
            
            // Fermer tous les autres sous-menus
            $('.dropdown-submenu').not($parent).removeClass('show');
            $('.dropdown-submenu .dropdown-menu').not($submenu).removeClass('show');
            
            // Toggle le sous-menu actuel
            $parent.toggleClass('show');
            $submenu.toggleClass('show');
        });
        
        // Fermer les sous-menus quand on clique ailleurs
        $(document).on('click', function(e) {
            if (!$(e.target).closest('.dropdown-submenu').length) {
                $('.dropdown-submenu').removeClass('show');
                $('.dropdown-submenu .dropdown-menu').removeClass('show');
            }
        });
        
        // Gestion du toggle parfait du menu hamburger
        $('.navbar-toggler').on('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            var $toggler = $(this);
            var $collapse = $($toggler.data('bs-target'));
            var $icon = $toggler.find('.navbar-toggler-icon');
            var isExpanded = $toggler.attr('aria-expanded') === 'true';
            
            console.log('Toggle clicked - isExpanded:', isExpanded);
            console.log('Menu has show class:', $collapse.hasClass('show'));
            
            // Fermer tous les sous-menus quand on ouvre/ferme le menu principal
            $('.dropdown-submenu').removeClass('show');
            $('.dropdown-submenu .dropdown-menu').removeClass('show');
            
            // Toggle du menu
            if (isExpanded) {
                // Fermer le menu
                console.log('Closing menu');
                $collapse.removeClass('show');
                $toggler.attr('aria-expanded', 'false');
                $icon.css('transform', 'rotate(0deg)');
            } else {
                // Ouvrir le menu
                console.log('Opening menu');
                $collapse.addClass('show');
                $toggler.attr('aria-expanded', 'true');
                $icon.css('transform', 'rotate(180deg)');
            }
            
            // Vérifier l'état après
            setTimeout(function() {
                console.log('After toggle - isExpanded:', $toggler.attr('aria-expanded'));
                console.log('After toggle - has show class:', $collapse.hasClass('show'));
            }, 100);
        });
        
        // Le menu reste ouvert quand on clique sur un lien
        // (fonction supprimée pour permettre au menu de rester ouvert)
    });

})(jQuery);

