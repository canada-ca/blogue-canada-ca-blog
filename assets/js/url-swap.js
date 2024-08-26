document.addEventListener("DOMContentLoaded", function() {
    // Select the div with the class 'brand'
    var brandDiv = document.querySelector('.brand');

    // Check if the div exists
    if (brandDiv) {
        // Find the <a> element within the div
        var link = brandDiv.querySelector('a');

        // Check if the <a> element exists
        if (link) {
            // Detect the language from the html element's lang attribute
            var lang = document.documentElement.lang || 'en'; 

            // Determine the base URL based on the detected language
            var baseUrl = lang === 'fr' ? 'https://www.canada.ca/fr' : 'https://www.canada.ca/en';

            // Change the href attribute to the appropriate URL
            link.setAttribute('href', baseUrl);
        }
    }
});