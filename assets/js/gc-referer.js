( function ( $, window, document, wb ) {
    "use strict";

    var componentName = "gc-referer",
        selector = "." + componentName,
        initEvent = "wb-init" + selector,
        $document = wb.doc,
        defaults = {
            thankYouPage: "/thank-you.html",
        };

    // Initialization function for the plugin
    function init( event ) {
        var elm = wb.init( event, componentName, selector ),
            $elm = $( elm );

        if ( elm ) {
            var settings = $.extend( {}, defaults, $elm.data() );

            handleFormSubmit( settings, $elm );
            setBackToReferrer( settings, $elm );

            // Identify that initialization has completed
            wb.ready( $elm, componentName );
        }
    }

    function handleFormSubmit( settings, $elm ) {
        $elm.find( "#referrer" ).val( document.referrer );

        $elm.on( "submit", "form", function ( event ) {
            event.preventDefault();
            var form = $( this )[ 0 ];
            var formData = new FormData( form );
            var contactDto = {};

            formData.forEach( function ( value, key ) {
                contactDto[ key ] = value;
            });

            sessionStorage.setItem( "contact-dto", JSON.stringify( contactDto ) );

            location.href = settings[ "data-contact-us-thank-you" ] || settings.thankYouPage;
        });
    }

    function setBackToReferrer( $elm ) {
        var referrerLink = $elm.find( "#backToReferrer" ),
            contactDto = JSON.parse( sessionStorage.getItem( "contact-dto" ));

        if ( contactDto && contactDto.referrer ) {
            referrerLink.attr( "href", contactDto.referrer );
        }
    }

    // Bind the plugin init event
    $document.on( initEvent, selector, init );

    // Add the timerpoke event (in case the plugin is added after the page load)
    wb.add( selector );

} )( jQuery, window, document, wb );