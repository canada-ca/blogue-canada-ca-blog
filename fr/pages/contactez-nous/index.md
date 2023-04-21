---
altLangPage: "contact-us.html"
breadcrumbs: false
contextualFooter:
  title: ""
dateModified: 2023-04-18
description: "Contactez le Bureau de la transformation numérique au sujet du système de conception Canada.ca."
nomenu: true
nositesearch: true
noReportProblem: true
script: ./gc-referrer.js
share: false
showFeedback: false
title: "Contactez le Bureau de la transformation numérique"
---
Communiquez avec nous pour poser des questions sur la conception du site Canada.ca ou pour nous faire part de vos suggestions à ce sujet.

<div class="row">
  <div class="col-md-8">
    <details class="mrgn-tp-lg">
      <summary>La protection des renseignements personnels</summary>
      <p class="mrgn-tp-lg">Nous recueillons les informations personnelles que vous soumettez au moyen du présent formulaire permettant de communiquer avec nous en vertu de <cite>la Loi sur la gestion des finances publiques</cite>, afin de pouvoir vous répondre. Les renseignements demandés sont fournis sur une base volontaire. Les renseignements personnels recueillis seront mis à la disposition du personnel du programme chargé de l'administration du site web et seront utilisés et protégés conformément à <cite>la Loi sur la protection des renseignements personnels</cite> et tel qu’il est indiqué dans le fichier de renseignements personnels POU 914 - Communications publiques. En vertu de <cite>la Loi sur la protection des renseignements personnels</cite>, qui protège vos renseignements personnels, vous avez le droit de consulter ces renseignements et de demander que des corrections y soient apportées. Si vous avez des questions à propos des présents renseignements sur la protection des renseignements personnels, veuillez communiquer avec le coordinateur/la coordonnatrice de l’accès à l’information et de la protection des renseignements personnels (AIPRP) du SCT. Si la réponse du SCT à vos préoccupations en matière de protection des renseignements personnels ne vous satisfait pas, vous pouvez communiquer avec le Commissariat à la protection de la vie privée.</p>
      <h2>Coordonnées</h2>
      <p>Coordonnateur/Coordonnatrice de l’AIPRP du Conseil du Trésor</p>
      <ul>
        <li>Téléphone&nbsp;: 1-866-312-1511</li>
        <li>Courriel&nbsp;: <a href="mailto:ATIP.AIPRP@tbs-sct.gc.ca">ATIP.AIPRP@tbs-sct.gc.ca</a></li>
      </ul>
      <p>Autres coordonnées</p>
      <ul>
        <li><a href="https://www.priv.gc.ca/fr/communiquer-avec-le-commissariat/">Commissariat à la protection de la vie privée du Canada</a></li>
      </ul>
      <h2>Références</h2>
      <ul>
        <li><a href="https://laws-lois.justice.gc.ca/fra/lois/p-21/index.html"><cite>Loi sur la protection des renseignements personnels</cite></a></li>
        <li><a href="https://www.canada.ca/fr/secretariat-conseil-tresor/services/acces-information-protection-reseignements-personnels/acces-information/renseignements-programmes-fonds-renseignements/fichiers-renseignements-personnels-ordinaires.html#pou914">Fichier de renseignements personnels POU 914 - Communications publiques</a></li>
      </ul>
    </details>
  </div>
</div>

<div class="wb-frmvld row">
  <form action="/contactez-nous/merci.html" method="post" id="contact-dto" class="mrgn-tp-lg col-md-8 gc-font-2019" netlify>
    <input type="hidden" value="" name="referer" id="referrer">
    <div class="wb-fieldflow" data-wb-fieldflow='{"noForm": true, "renderas":"radio", "gcChckbxrdio":true}'>
      <p>Souhaitez-vous que nous communiquions avec vous au sujet de vos commentaires?</p>
      <ul>
        <li data-wb-fieldflow='{"action": "query", "name": "feedback_type", "value": "feedback_type1"}'>Non</li>
        <li data-wb-fieldflow='[
          {"action": "toggle", "toggle": "#email_request_other", "live":true },
          {"action": "query", "name": "feedback_type", "value": "feedback_type3" }
          ]'>Oui, je suis à l’aise de fournir mon adresse courriel à des fins de communication seulement.</li>
      </ul>
    </div>
    <div id="email_request_other" class="hidden">
      <div class="form-group">
        <label for="email1"><span class="field-name">Courriel</span></label>
        <p>Votre courriel ne sera utilisée que pour vous contacter. Elle ne sera pas partagée.</p>
        <div class="row">
          <div class="col-md-8">
            <input class="form-control input-lg full-width" id="email1" name="email1" type="email" autocomplete="email" />
          </div>
        </div>
      </div>
    </div>
    <div class="form-group">
      <label for="subject1"><span class="field-name">Objet (255 caractères maximum)</span></label>
      <input class="form-control full-width" id="subject1" name="subject1" type="text" data-rule-minlength="2">
    </div>         
    <div class="form-group">
      <label for="message" class="required gc-font-2019"><span class="field-name">Message</span> <strong class="required" aria-hidden="true">(obligatoire)</strong></label>
      <div>
        <textarea class="form-control full-width required" rows="6" id="message" name="message"></textarea>
      </div>
    </div>
    <ul class="list-unstyled list-inline mrgn-tp-lg">
      <li> <button type="submit" class="btn btn-lg btn-primary">Soumettre</button> </li>
      <li><button type="reset" class="btn btn-lg btn-link">Annuler</button></li>
    </ul>
  </form>
</div>
