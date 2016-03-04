var HomePage = (function () {
	
	var initSwiper = function () {
		var swiper = new Swiper('.swiper-container', {
			pagination: '.swiper-pagination',
			autoplay: 3500,
			paginationClickable: '.swiper-pagination',
			spaceBetween: 30,
			effect: 'fade',
			loop: true
		});
	};

	return {
		init: function () {
			initSwiper();
		}
	}
})();