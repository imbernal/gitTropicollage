function parsePicture(patt) {
	var a = patt.split('/');
	return a[a.length - 1].replace(')', '');
}

$(function () {
	var images = ["03.JPG", "04.JPG", "05.JPG", "054.jpg"];
	
	var initial_image = parsePicture($('#tf-home').css('background-image')).replace('"', '');
	var initial_index = images.indexOf(initial_image);
	var curr_index = 1;


	setInterval(function () {
		if (curr_index > images.length - 1) {
			curr_index = 0;
		}

		var image_path = '';
		image_path = image_path + images[curr_index];

		var abs = "url('/static/img/"+image_path+"')";

		$('#tf-home').animate({ opacity: 0.9 }, 'slow', function() {
        		$(this).css({ 'background-image': abs }).animate({ opacity: 1 });
    });

		//without any animations
		// $('#tf-home').css();

		curr_index++;


	}, 3500)

});

function l(patt) {
	console.log(patt);
}
