(function($) {

	var	$window = $(window),
		$body = $('body'),
		$sidebar = $('#sidebar');


	// Hack: Enable IE flexbox workarounds.
		if (browser.name == 'ie')
			$body.addClass('is-ie');

	// Sidebar.
		if ($sidebar.length > 0) {

			var $sidebar_a = $sidebar.find('a');

			$sidebar_a
				.on('click', function() {

					var $this = $(this);

					// Deactivate all links.
						$sidebar_a.removeClass('active');

					// Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
						$this
                            .addClass('active');

				})

		}

})(jQuery);