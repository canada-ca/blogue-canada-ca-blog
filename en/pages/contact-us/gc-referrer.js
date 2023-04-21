/**
 * @title WET-BOEW GC Referrer Plugin
 * @overview Plugin to capture the referrer and store it for later use in a form or navigation
 * @license wet-boew.github.io/wet-boew/License-en.html / wet-boew.github.io/wet-boew/Licence-fr.html
 * @author @delisma
 */
( function ( $, window, wb ) {
    "use strict";
  
    // 1. Define plugin variables and functions
    var componentName = "gc-referrer",
        selector = "." + componentName,
        initEvent = "wb-init" + selector,
        //eventName = componentName + ".process",
        $document = wb.doc,
        defaults = {},
        init = function ( event ) {
          // Check if the element is already initialized
          var elm = wb.init( event, componentName, selector ),
              $elm,
              settings;
          if ( elm ) {
            // If not, proceed with initialization
            $elm = $( elm );
  
            // Get the settings (thank you page url or the id of the back to referrer link) from the element's data attributes
            settings = $.extend(
              true,
              {},
              defaults,
              window[ componentName ],
              wb.getData( $elm, componentName )
            );
  
            // Trigger a custom event with the settings
            $elm.trigger( "wb-ready.wb", settings );
  
            // Mark the element as initialized
            wb.ready( $elm, componentName );
          }
        };
  
    // Define custom event handler
    $document.on( "submit", selector, function ( event ) {
      // Event handler function (event, data): on submit or on page load
      // event: the event object
      // data: the data object
      event.preventDefault();
      var elm = event.currentTarget,
          $elm = $( elm ),
          formId = $elm.attr( "id" ),
          formData = $elm.serializeArray(),
          content = {},
          referrer = document.referrer;
  
      $( "input[name='referer']" ).val( referrer );
      $( "input[name='formId']" ).val( formId );
  
      $.each(formData, function ( index, field ) {
        content[ field.name ] = field.value;
      });
  
      sessionStorage.setItem( formId, JSON.stringify( content ) );
      location.href = $elm.attr( "action" );
    });
  
    $document.on( "wb-ready.wb", selector, function ( event, data ) {
      var elm = event.currentTarget,
          $elm = $( elm ),
          formStorage = JSON.parse( sessionStorage.getItem( data.formId ) );
          // referrerLink = $( selector );
      // Set the back to referrer link to the referrer page if it exists
      // Otherwise, set it to go back to the previous page
      // This is done because the referrer page is not always the previous page
      // For example, when the user clicks on a link in the referrer page,
      // the referrer page is not the previous page, but the page the user clicked on
  
      if ( formStorage && formStorage.referrer ) {
        $elm.attr( "href", formStorage.referrer );
      } else {
        $elm.attr( "href", "/" );
      }
    });
  
    // Bind the init event
    $document.on( "timerpoke.wb " + initEvent, selector, init );
  
    // Add timer poke to initialize the plugin
    wb.add( selector );
  })( jQuery, window, wb );