$(document).ready(function () {

    $('.preloader').hide();

    var main_pic = $('.pic-link:first').attr('href');

    $('.gallery-container').html('<img src="' + main_pic + '" class="picture">');

    $('.pic-link').click(function () {
        var selected_pic = $(this).attr('href');

        if (selected_pic != main_pic) {
            main_pic = selected_pic;

            $('.pic-link').each(function () {
                if ($(this).attr('href') == selected_pic) {
                    $(this).animate({'opacity': '.5'});
                }
                else {
                    $(this).animate({'opacity': '1'});
                }
            });

            $('.gallery-container').html('<img src="' + selected_pic + '" class="picture">').animate({'opacity': '0'}, 0);
            $('.preloader').fadeIn();
            $('.gallery-container .picture').load(function () {
                $('.preloader').fadeOut(500, function () {
                    $('.gallery-container').animate({'opacity': '1'}, 200);
                });
            });
            return false;
        }
        else {
            return false;
        }
    });
});
