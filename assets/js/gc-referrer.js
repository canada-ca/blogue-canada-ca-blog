(function ($, window, wb) {
    "use strict";

    var componentName = "gc-referer",
        selector = "." + componentName,
        initEvent = "wb-init" + selector,
        $document = wb.doc,
        defaults = {
            thankYouPage: "/thank-you"
        },
        settings;

    // Initialization function for the plugin
    function init(event) {
        var elm = wb.init(event, componentName, selector),
            $elm = $(elm);

        if (elm) {
            settings = $.extend(true, {}, defaults, window[componentName], wb.getData($elm, componentName));

            $elm.find("#referrer").val(document.referrer);

            // Trigger the custom events with settings
            $elm.trigger("submit", settings);
            $elm.trigger("wb-ready.wb", settings);

            // Identify that initialization has completed
            wb.ready($elm, componentName);
        }
    }

    // Event listener for form submission
    $document.on("submit", selector + " form", function (event, settings) {
        event.preventDefault(); // Intercepts the form's submit event

        var $form = $(this),
            formName = $form.attr("name"),
            formData = new FormData($form[0]),
            contactForm = {};

        formData.forEach(function (value, key) {
            contactForm[key] = value;
        });

        // Store form data in sessionStorage using form name as key
        sessionStorage.setItem(formName, JSON.stringify(contactForm));

        // Redirect to the thank you page specified in the data attribute or defaults
        location.href = settings["data-contact-us-thank-you"] || settings.thankYouPage;
    });

    // Event listener for setting the backToReferrer link on a different page
    $document.on("wb-ready.wb", function () {
        var $backToReferrer = $( "a" + componentName ),
            contactFormData;

        // Loop through sessionStorage to find the item with a referrer or thank-you-page value
        for (var i = 0; i < sessionStorage.length; i++) {
            var key = sessionStorage.key(i),
                storedData = JSON.parse(sessionStorage.getItem(key));

            if (storedData && (storedData.referrer || storedData["data-contact-us-thank-you"])) {
                contactFormData = storedData;
                break; // Stop after finding the first matching item
            }
        }

        // Check if the backToReferrer element exists and session data is present
        if ($backToReferrer.length && contactFormData && contactFormData.referrer) {
            $backToReferrer.attr("href", contactFormData.referrer);
        }
    });

    // Bind the init event of the plugin
    $document.on("timerpoke.wb " + initEvent, selector, init);

    // Add the timerpoke event to initialize the plugin
    wb.add(selector);

})(jQuery, window, wb);