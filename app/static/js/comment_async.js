function parse_data(full_name, email, body) {
	var html = '<div class="item col-xs-12"> \
                        <div class="col-xs-12 col-sm-12 col-md-2 col-lg-2">\
                            <div class="container"> \
                                <div class="usr-logo"></div>\
                                <small class="author">' + full_name + '</small>\
                            </div>\
                        </div>\
                        <div class="col-xs-12 col-sm-12 col-md-10 col-lg-10">\
                            <p>'+ body +'</p>\
                        </div>\
                        <div class="date col-xs-12 col-xs-offset-10"><span class="ion-android-calendar"></span>\
                            <small>A moment ago</small>\
                        </div>\
                    </div>';
    return html;
}

$('input[value="Comment"]').click(function (e) {
	e.preventDefault();
	$.ajax({
		method: "POST",
		url: $('#post_url').val(),
		data: {
			full_name: $('#full_name').val(),
			email: $('#user_email').val(),
			body: $('#comment-body').val(),
			home_id: $('#home_id').val()
		}
	})
	.done(function () {
		var html = parse_data($('#full_name').val(), $('#user_email').val(), $('#comment-body').val());
		$('.reviews-list').append(html);
	})
	.error(function (){
		console.log("Oops");
	});
});