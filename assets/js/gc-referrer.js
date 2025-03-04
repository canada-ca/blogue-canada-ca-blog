( function ( $, window, wb ) {
    "use strict";

    var componentName = "gc-referrer",
        selector = "." + componentName,
        initEvent = "wb-init" + selector,
        $document = wb.doc;

    // Initialization function for the plugin
    function init( event ) {
        var elm = wb.init( event, componentName, selector ),
            $elm = $( elm );		
		
  		// Commented to remove referrer on the emails
		// Afonso, Mar. 4, 2025  
		/*
        if ( elm ) {
            // Set referrer value on initialization
            $elm.find( "#referrer" ).val( document.referrer );

            $elm.trigger( "wb-ready.wb" );

            // Identify that initialization has completed
            wb.ready( $elm, componentName );
        } */
		
    }

    // Event listener for form submission
    $document.on( "submit", "form" + selector, function ( event ) {
        event.preventDefault(); // Intercepts the form's submit event

        var elm = event.currentTarget,
            $elm = $( elm ),
            formName = $elm.attr( "name" ),
            formData = new FormData( elm ),
            contactForm = {};

        formData.forEach( function ( value, key ) {
            contactForm[ key ] = value;
        });

        // Store form data in sessionStorage using form name as key
        sessionStorage.setItem( formName, JSON.stringify( contactForm ) );

        // Submit the form programmatically
        elm.submit();
    });

    // Event listener for setting the backToReferrer link on a different page
    $document.on( "wb-ready.wb", "a" + selector, function ( event ) {
        var elm = event.currentTarget,
            $elm = $( elm );

        // Loop through sessionStorage to find the item with a referrer
        for ( var i = 0; i < sessionStorage.length; i++ ) {
            var key = sessionStorage.key( i ),
                storedData = JSON.parse( sessionStorage.getItem( key ) );

            if ( storedData.referrer ) {
                $elm.attr( "href", storedData.referrer );
                break; // Stop after finding the first matching item
            }
        }
    });

    // Bind the init event of the plugin
    $document.on( "timerpoke.wb " + initEvent, selector, init );

    // Add the timerpoke event to initialize the plugin
    wb.add( selector );

})( jQuery, window, wb );
