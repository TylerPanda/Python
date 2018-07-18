$(document).ready(function(){
    var el = document.getElementById('text');

    $('[data-trigger = "dropdown"]').on('mouseenter', function(){
        var submenu = $(this).parent().find('.submenu');
        // submenu.addClass('active');
        submenu.fadeIn(500);

        $('.profile-menu').on('mouseleave', function(){
            // submenu.removeClass('active');
            submenu.fadeOut(500);
        });
    });
});
