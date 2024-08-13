---
altLangPage: https://blog.canada.ca/signup.html
date: "2021-03-01"
dateModified: "2024-02-21"
description: Abonnez-vous à notre liste d’envoi pour des renseignements au sujet des ateliers, des événements, des activités de recherche sur les utilisateurs et des tests de convivialité auxquels vous pourriez vouloir participer.
layout: default
pageclass: "cnt-wdth-lmtd"
title: Abonnez-vous à la liste d’envoi du Bureau de la transformation numérique
---
{%- assign locales = site.data.locales.signup -%}
<p>{{ locales.intro[ page.language ] }}</p>
<div class="row">
	<div class="col-md-8">
		<!-- Begin MailChimp Signup Form -->
		<link href="//cdn-images.mailchimp.com/embedcode/classic-10_7.css" rel="stylesheet" type="text/css">
		<style type="text/css">
			#mc_embed_signup {
				clear:left;
				font:20px Helvetica,Arial,sans-serif;
			}

			.hp {
				text-align: left !important;
				color: white !important;
				background-color: #318000 !important;
				border-color: #458259 !important;
			}

			a.hp:visited {
				color: white !important;
				background-color: #318000 !important;
			}

			a.hp:hover {
				color: white !important;
				background-color: #122a01 !important;
			}

			.paddingc {
				padding-left: 0 !important;
			}
		</style>
		<div id="mc_embed_signup">
			<form action="https://canada.us15.list-manage.com/subscribe?u=729a207773f7324e217a1d945&id=8764caedfb" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate paddingc" target="_blank" novalidate>
				<div id="mc_embed_signup_scroll">
					<div class="mc-field-group">
						<label class="wb-inv" for="mce-EMAIL">{{ locales.mce-email[ page.language ] }}</label>
						<input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL" placeholder="{{ locales.mce-email[ page.language ] }}">
					</div>
					<div class="mc-field-group input-group">
						<b>{{ locales.emailtype[ page.language ] }}</b>
						<ul>
							<li>
								<input type="radio" value="html" name="EMAILTYPE" id="mce-EMAILTYPE-0">
								<label for="mce-EMAILTYPE-0">{{ locales.emailtype1[ page.language ] }}</label>
							</li>
							<li>
								<input type="radio" value="text" name="EMAILTYPE" id="mce-EMAILTYPE-1">
								<label for="mce-EMAILTYPE-1">{{ locales.emailtype2[ page.language ] }}</label> {{ locales.emailtype-cmmt[ page.language ] }}
							</li>
						</ul>
					</div>
					<div id="mce-responses" class="clear">
						<div class="response" id="mce-error-response" style="display:none"></div>
						<div class="response" id="mce-success-response" style="display:none"></div>
					</div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
					<div style="position: absolute; left: -5000px;" aria-hidden="true">
						<input type="text" name="b_5700d338d6ab413ebca1099f4_c6bb0b9f64" tabindex="-1" value="">
					</div>
					<div class="clear">
						<input type="submit" value="{{ locales.subscribe[ page.language ] }}" name="subscribe" id="mc-embedded-subscribe" class="button hp">
					</div>
				</div>
			</form>
		</div>
		<script type='text/javascript' src='s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script>
		<script type='text/javascript'>
			( function( $ ) {
				window.fnames = new Array();
				window.ftypes = new Array();
				fnames[ 0 ]='EMAIL';
				ftypes[ 0 ]='email';
				fnames[ 1 ]='FNAME';
				ftypes[ 1 ]='text';
				fnames[ 2 ]='LNAME';
				ftypes[ 2 ]='text';
				fnames[ 3 ]='ADDRESS';
				ftypes[ 3 ]='address';
				fnames[ 4 ]='PHONE';
				ftypes[ 4 ]='phone';
				/*
				* Translated default messages for the $ validation plugin.
				* Locale: FR
				*/
				$.extend( $.validator.messages, {
					required: "Ce champ est requis.",
					remote: "Veuillez remplir ce champ pour continuer.",
					email: "Veuillez entrer une adresse email valide.",
					url: "Veuillez entrer une URL valide.",
					date: "Veuillez entrer une date valide.",
					dateISO: "Veuillez entrer une date valide (ISO).",
					number: "Veuillez entrer un nombre valide.",
					digits: "Veuillez entrer (seulement) une valeur numérique.",
					creditcard: "Veuillez entrer un numéro de carte de crédit valide.",
					equalTo: "Veuillez entrer une nouvelle fois la même valeur.",
					accept: "Veuillez entrer une valeur avec une extension valide.",
					maxlength: $.validator.format("Veuillez ne pas entrer plus de {0} caractères."),
					minlength: $.validator.format("Veuillez entrer au moins {0} caractères."),
					rangelength: $.validator.format("Veuillez entrer entre {0} et {1} caractères."),
					range: $.validator.format("Veuillez entrer une valeur entre {0} et {1}."),
					max: $.validator.format("Veuillez entrer une valeur inférieure ou égale à {0}."),
					min: $.validator.format("Veuillez entrer une valeur supérieure ou égale à {0}.")
				});
			}( jQuery ));
			var $mcj = jQuery.noConflict( true );
		</script>
		<!--End mc_embed_signup-->
		<div class="mce-privacy" style="padding-top: 9px;">
			<a href="#privacy-notice-modal" aria-controls="privacy-notice-modal" class="overlay-lnk light-link wb-lbx" aria-label="{{ locales.privacy-notice[ page.language ] }}">{{ locales.privacy-notice[ page.language ] }}</a>
		</div>
		<section class="mfp-hide modal-dialog modal-content overlay-def" id="privacy-notice-modal">
			<header class="modal-header">
				<h2 class="modal-title">{{ locales.privacy-notice[ page.language ] }}</h2>
			</header>
			<div class="modal-body">
				<p>{{ locales.privacy-notice1[ page.language ] }}</p>
				<p>{{ locales.privacy-notice2[ page.language ] }}</p>
				<p>{{ locales.privacy-notice3[ page.language ] }}</p>
				<p>{{ locales.privacy-notice4[ page.language ] }}</p>
			</div>
		</section>
	</div>
</div>
