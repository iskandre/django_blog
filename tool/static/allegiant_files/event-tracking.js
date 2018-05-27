( function( $ ) {

	'use strict';

	function redirect( url ) {
		window.location.href = url;
	}

	var links = $( 'a.macho-event-targeting' );
	if ( links.length > 0 && 'function' === typeof ga ) {
		links.click( function( event ){
			
			var $element = $(this),
				data = $element.data(),
				link = $element.attr( 'href' );

			event.preventDefault();

			if ( undefined !== data['eventcategory'] && undefined !== data['eventaction'] && undefined !== data['eventlabel'] ) {

				ga( 'send', {
					hitType: 'event',
					eventCategory: data['eventcategory'],
					eventAction: data['eventaction'],
					eventLabel: data['eventlabel'],
					hitCallback: function(){
						redirect( link );
					}
				});

			}

		});
	}

})( jQuery );
