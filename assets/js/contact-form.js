---
---

(function () {
  // Configuration object for URLs
  const config = {
    thankYouPage: {
      en: "{{ site.data.locales.contact-form.thankYouPage.en }}",
      fr: "{{ site.data.locales.contact-form.thankYouPage.fr }}"
    },
    contactUsPage: {
		en: "{{ site.data.locales.contact-form.contact-us.en }}",
		fr: "{{ site.data.locales.contact-form.contact-us.fr }}"
	},
  };

  function handleFormSubmit() {
    document.getElementById("referrer").value = document.referrer;

    document.addEventListener("DOMContentLoaded", function () {
      var form = document.querySelector("form");

      form.addEventListener("submit", function (event) {
        event.preventDefault();
        var formData = new FormData(form);
        var contactDto = {};

        formData.forEach(function (value, key) {
          contactDto[key] = value;
        });

        sessionStorage.setItem("contact-dto", JSON.stringify(contactDto));

        // Use the appropriate thank you page based on the current language
        var lang = document.documentElement.lang || 'en';
        location.href = config.thankYouPage[lang];
      });
    });
  }

  function setBackToReferrer() {
    document.addEventListener("DOMContentLoaded", function () {
      var referrerLink = document.getElementById("backToReferrer");
      var contactDto = JSON.parse(sessionStorage.getItem("contact-dto"));

      if (contactDto && contactDto.referer) {
        referrerLink.href = contactDto.referer;
      }
    });
  }

  // Run the appropriate function based on the current page
  var currentPage = document.location.pathname;

  if (currentPage.endsWith(config.contactUsPage) || currentPage.endsWith(config.contactUsPage + "index.html")) {
    handleFormSubmit();
  } else if (currentPage.endsWith(config.thankYouPage)) {
    setBackToReferrer();
  }
})();