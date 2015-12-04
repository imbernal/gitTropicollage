$(document).ready(function () {

    var home_id = $('#entity_id').attr('value');
    var imageName = [];

    console.log(home_id);

    $.ajax({
        method: 'POST',
        url: '/home_pictures/',
        data: {
            'home_id': home_id
        }
    })
        .done(function (data) {
            imageName = data.pictures_list;
        })
        .fail(function (data, err) {
            console.log('ERROR: ' + err);
        });
    
    var count = 0;

    var click_away =
        function go() {
            $('.picture').fadeOut(300, function () {
                var self = $(this);
                self.attr("src", "/media/imagenes/" + imageName[count]);
                count++;

                if (count > imageName.length - 1) {
                    count = 0;
                }
                self.fadeIn(500).delay(3000);
                go();
            });
        };
    click_away();
});
