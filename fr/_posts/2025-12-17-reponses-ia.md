---
altLangPage: /2025/12/17/ai-answers
date: 2025-12-17
dateModified: 2026-06-15
description: "Chaque jour, des milliers de personnes se tournent vers le gouvernement du Canada (GC) pour obtenir de l'aide relativement aux services essentiels."
latestChanges:
  - term: 2026-06-12
    definition: "Ajout des résultats des essais 2 et 3 et d’une nouvelle section&nbsp;: Les résultats des essais en un coup d’œil."
  - term: 2025-12-17
    definition: "Publication originale avec les résultats de l’essai 1 (1 763 questions, 94&nbsp;% d’exactitude)."
title: "Réponses IA&nbsp;: Mise à l'essai à l'échelle de l'organisation pour Canada.ca"
---

## Sur cette page

* [Comment les outils existants aident les utilisateurs](#comment-les-outils-existants-aident-les-utilisateurs)
* [Comment fonctionne Réponses IA](#comment-fonctionne-réponses-ia)
* [Les résultats des essais en un coup d’œil](#les-résultats-des-essais-en-un-coup-dœil)
* [Résultats de l’essai 1](#résultats-de-lessai-1)
* [Quatre principales constatations](#quatre-principales-constatations)
* [Résultats de l’essai 2](#résultats-de-lessai-2)
* [Résultats de l’essai bêta 3](#essai-3-partenaires-de-lessai-bêta)
* [Pourquoi est-ce important?](#pourquoi-est-ce-important)
* [En savoir plus](#en-savoir-plus)
* [Derniers changements](#derniers-changements)

Chaque jour, des milliers de personnes se tournent vers le gouvernement du Canada (GC) pour obtenir de l’aide relativement aux services essentiels. De nombreuses personnes ne peuvent ni téléphoner aux bureaux du gouvernement ni s’y rendre en personne pendant les heures d’ouverture. C’est pourquoi il est essentiel que le libre-service en ligne soit efficace.

## Comment les outils existants aident les utilisateurs

L’outil [Rétroaction GC](https://conception.canada.ca/configurations-conception-communes/outil-retroaction.html) est utilisé par de nombreuses équipes pour améliorer le contenu et les services qu’elles offrent sur Canada.ca. L’outil recueille quotidiennement plus de 3 000 questions et réponses de personnes qui parcourent des pages relatives aux demandes d’immigration, aux prestations d’emploi, à la gestion de comptes d’impôt, etc. Bien que les équipes du GC continuent d’améliorer Canada.ca, ces améliorations ne peuvent à elles seules relever entièrement le défi que représente le fait d’aider les gens à s’y retrouver dans la vaste gamme de contenus et de services Web du GC.

## Comment fonctionne Réponses IA

À l’été 2025, le Bureau de l’Expérience Canada.ca a mis à l’essai une nouvelle approche&nbsp;: Réponses IA. Ce service fondé sur l’IA offre aux utilisateurs des réponses courtes dans un langage clair (dont le contenu provient exclusivement de sites Web du GC, avec des liens fiables qui guident les utilisateurs vers les étapes suivantes). Ce billet de blogue présente les résultats de la mise à l’essai de Réponses IA, y compris les principales constatations et ce que nous avons appris.

## Les résultats des essais en un coup d’œil

<table class="table table-bordered table-striped mrgn-bttm-lg">
  <thead class="bg-primary">
    <tr>
      <th>Paramètre</th>
      <th>Essai 1 (juin à juil. 2025)</th>
      <th>Essai 2 (oct. à nov. 2025)</th>
      <th>Essai bêta 3 (déc. 2025 à janv. 2026)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Questions</th>
      <td class="text-right">1 763</td>
      <td class="text-right">2 866</td>
      <td class="text-right">3 222</td>
    </tr>
    <tr>
      <th>Exactitude de la réponse</th>
      <td class="text-right">94&nbsp;%</td>
      <td class="text-right">95&nbsp;%</td>
      <td class="text-right"><strong>96,7&nbsp;%</strong></td>
    </tr>
    <tr>
      <th>Pages Web</th>
      <td class="text-right">2</td>
      <td class="text-right">12</td>
      <td class="text-right">112</td>
    </tr>
    <tr>
      <th>Institutions sources</th>
      <td class="text-right">32</td>
      <td class="text-right">60</td>
      <td class="text-right">56</td>
    </tr>
  </tbody>
  <tfoot>
    <tr class="info">
      <th><strong>Total cumulé&nbsp;:</strong></th>
      <td colspan="3">7 851 questions pour l'ensemble des essais, dont 30&nbsp;% ont été évaluées par des experts</td>
    </tr>
  </tfoot>
</table>

{% include components/gc-complex-img.html
  alt="Une page montrant les options d’ouverture de session et une fenêtre contextuelle invitant les utilisateurs à essayer le nouveau service de Réponses IA."
  file="/images/reponses-ia/se-connecter.jpg"
  summary="Approche technique des réponses générées par l’IA"
  content="<p>Notre architecture indépendante du modèle utilise le modèle GPT-4.1 d’Azure Canada avec des invites propres aux ministères pour 10 institutions&nbsp;: Relations Couronne-Autochtones et Affaires du Nord Canada (RCAANC), Agence du revenu du Canada (ARC), Emploi et Développement social Canada (EDSC), Ministère des Finances (<span class='text-uppercase'>fin</span>), Santé Canada (SC), Immigration, Réfugiés et Citoyenneté Canada (IRCC), Services aux Autochtones Canada (<span class='text-uppercase'>sac</span>), Agence de la santé publique du Canada (ASPC), Services publics et Approvisionnement Canada (<span class='text-uppercase'>spac</span>) et Secrétariat du Conseil du Trésor du Canada (SCT).</p>
    <p>Comme le contenu Web change fréquemment, le système effectue des recherches et télécharge des pages précises pour répondre aux questions, plutôt que d’extraire à l’avance du contenu Web. Ce système d’IA repose sur les renseignements fournis sur des sites Web du gouvernement du Canada.</p>
    <p>L’équipe responsable du produit Réponses IA a mis au point un système d’IA agentive (les utilisateurs interagissent avec un agent spécialisé) avec une invite détaillée pour faire en sorte que les réponses soient claires, concises et utiles. Nous avons intégré des systèmes d’évaluation par des experts humains et des systèmes de notation par l’IA, en plus de bloquer les renseignements personnels afin de protéger la vie privée des utilisateurs.</p>"
%}

## Résultats de l’essai 1

### Participation (du 18 au 26 juin et du 15 au 25 juillet 2025)

Le taux de participation à l’essai a dépassé nos attentes&nbsp;: 1 227 sessions d’utilisateurs, couvrant 32 ministères et des questions portant sur plus de 120 tâches gouvernementales. Une tâche est la raison pour laquelle les utilisateurs consultent le contenu&nbsp;: cela peut être pour obtenir des réponses, par exemple se renseigner sur un sujet, ou effectuer une démarche, comme s’inscrire à un programme.

La répartition des questions témoigne des priorités des utilisateurs

* **42&nbsp;% (635 questions) concernaient les services d’IRCC&nbsp;:** immigration, permis de travail et visas.
* **25&nbsp;% (377 questions) concernaient les services d’EDSC&nbsp;:** connexion et inscription à Mon dossier Service Canada, assurance-emploi, Régime de pensions du Canada et recherche d’emploi.
* **22&nbsp;% (332 questions) concernaient les services de l’ARC&nbsp;:** accès au compte et questions liées à l’impôt ou aux entreprises.

Même les services gouvernementaux les moins utilisés ont généré plusieurs questions par sujet, et ce, pour de nombreux ministères, ce qui indique que les utilisateurs ont un grand intérêt pour les interactions avec le gouvernement assistées par l’IA.

{% include components/gc-complex-img.html
  alt="Capture d’écran de la page du service Réponses IA."
  file="/images/reponses-ia/Reponses-IA.png"
  summary="Description de l'image&nbsp; Réponses IA"
  content="<p>Capture d'écran d'une page &laquo;&nbsp;Réponses IA&nbsp;&raquo; sur Canada.ca, illustrant un échange type entre un utilisateur et le service &laquo;&nbsp;Réponses IA&nbsp;&raquo;.</p>
           <p>L'en-tête de Canada.ca, qui affiche l'identifiant du gouvernement du Canada, se trouve en haut de la page. Le titre de la page est &laquo;&nbsp;Réponses IA&nbsp;&raquo;, suivi du texte &laquo;&nbsp;Obtenez des réponses à vos questions sur Canada.ca.&nbsp;&raquo;. En dessous, une clause de non-responsabilité précise que les réponses fournies par le service d’IA sont données à titre informatif uniquement, qu’il ne s’agit pas de conseils officiels, et que des améliorations sont en cours.</p>
           <p>Un lien repliable intitulé &laquo;&nbsp;Confidentialité et conditions d’utilisation de l’IA&nbsp;&raquo; apparaît en dessous.</p>
           <p>Une question soumise par un utilisateur est affichée dans une bulle de discussion bleu clair. La question est la suivante&nbsp;:</p>
            <ul>
              <li>&laquo;&nbsp;Je reçois mes retours d'impôt par dépôt direct. Cependant, la SV continue de m’envoyer des chèques. On me demande de m’inscrire au dépôt direct. J’ai répondu en disant que j’y étais déjà inscrit, mais les chèques continuent d’arriver.&nbsp;&raquo;</li>
            </ul>
            <p>Sous la question, la réponse de l’IA apparaît dans un encadré blanc. La réponse est la suivante&nbsp;:</p>
            <ul>
              <li>&laquo;&nbsp;Le dépôt direct pour les remboursements d’impôt de l’ARC est distinct de celui de la SV, vos renseignements ne sont pas partagés. Pour cesser les chèques de SV[PM1], mettez à jour vos renseignements de dépôt direct SV [PM2] dans Mon dossier Service Canada. Si vous ne pouvez pas utiliser Mon dossier Service Canada, communiquez avec le centre d’appels de la SV au 1-800-277-9914 pour mettre à jour vos coordonnés bancaires. Après avoir changé vos renseignements de dépôt SV[PM3], gardez l’ancien compte ouvert jusqu’à ce qu’un nouveau paiement soit versé dans le nouveau.&nbsp;&raquo;</li>
            </ul>
            <p>En dessous, une section intitulée &laquo;&nbsp;Continuez avec ce lien :&nbsp;&raquo; comprend un lien vers une page Web de Canada.ca consacrée aux renseignements personnels.</p>
            <p>Ce lien est suivi d’une mise en garde&nbsp;: &laquo;&nbsp;L’IA peut faire des erreurs, vérifiez la réponse ou posez une question de suivi ci-dessous.&nbsp;&raquo;</p>
            <p>Tout en bas, un ID de chat s'affiche sous la forme d'une suite de lettres et de chiffres.</p>"
%}

## Quatre principales constatations

**Une exactitude qui répond aux normes organisationnelles&nbsp;:** Nous avons obtenu un taux d’exactitude de 95&nbsp;% pour les questions en anglais et de 94&nbsp;% pour les questions en français. L’exactitude des réponses a été vérifiée au moyen d’une évaluation par des experts de 800 questions d’essai, réalisée en collaboration avec des ministères et organismes fédéraux partenaires. Cette cohérence entre les deux langues officielles est rare dans les applications d’IA, car le français présente généralement un taux d’erreur plus élevé de 20&nbsp;%.

**Une véritable valeur ajoutée, selon les utilisateurs&nbsp;:** 88&nbsp;% des commentaires des utilisateurs étaient positifs. Il est important de noter que 22&nbsp;% des répondants ont déclaré qu’ils n’avaient plus besoin d’appeler les bureaux gouvernementaux ou de s’y rendre en personne, tandis que 52&nbsp;% ont indiqué qu’ils avaient passé moins de temps à effectuer des recherches et à lire.

**Une portée de l’utilisation inattendue&nbsp;:** Même si le service était offert sur une page d’ouverture de session, 50&nbsp;% des questions étaient liées aux 20 principaux services gouvernementaux nommés dans le [Sondage sur la réussite des tâches du GC](https://conception.canada.ca/sondage/index.html). Les utilisateurs ont posé des questions sur un large éventail de sujets, tels que les permis de travail, les cotisations au Régime de pensions du Canada, ou encore l’accès à leur compte d’impôt. Cette mise à l’essai a révélé une forte demande pour de l’aide offerte par l’IA dans l’ensemble des services gouvernementaux.

**Une capacité multilingue&nbsp;:** Outre l’anglais et le français, le système a traité des questions dans 19 autres langues. Ces questions représentaient 8,4&nbsp;% de toutes les requêtes. Le taux d’exactitude était plus faible pour ces langues, mais nous avons depuis apporté des améliorations à la traduction et à la recherche.

## Résultats de l’essai 2

### Participation  (du 22 octobre au 7 novembre 2025 à 12 h HE)

Pour l’essai 2, nous avons étendu les essais au-delà de la page d’ouverture de session. L’invitation a été affichée sur 12 pages du site Canada.ca à l’intention de visiteurs sélectionnés de manière aléatoire&nbsp;: Ouverture de session, Tous les services, Coordonnées, Changement d’adresse, Ministères, et Aide ayant trait à CléGC (en anglais et en français).

En 16,5 jours, 2 866 questions ont été posées au cours de 1 983 sessions d’utilisateurs, ce qui est beaucoup plus que lors de l’essai 1\. Les points d’entrée plus larges ont permis d’élargir l’éventail des sujets abordés&nbsp;:

* **38&nbsp;% (1 111) concernaient les services d’IRCC&nbsp;:** les questions sur l’immigration, les permis de travail et les visas demeurent les plus fréquentes.
* **18&nbsp;% (468) concernaient les services d’EDSC&nbsp;:** assurance-emploi, RPC et questions sur Mon dossier Service Canada.
* **14&nbsp;% (309) concernaient les services de l’ARC&nbsp;:** comptes d’impôt, numéros d’entreprise et questions sur la déclaration de revenus.
* **12&nbsp;% (462) concernaient le service Réponses IA&nbsp;:** utilisateurs curieux de savoir comment l’outil fonctionne.

Notons que 112 réponses provenaient des pages de l’Agence des services frontaliers du Canada (ASFC), dont 90 concernaient plus précisément la Gestion des cotisations et des recettes de l’ASFC (GCRA). Dans l’ensemble, les réponses provenaient de 60 institutions fédérales différentes.

### Principales constatations de l’essai 2

**Le taux d’exactitude est resté stable à 95&nbsp;%&nbsp;:** l’évaluation par des experts de 994 questions (35&nbsp;% du total, comparativement à 13&nbsp;% lors de l’essai 1) a montré que le rendement restait élevé. Le taux d’erreur dans les réponses est passé de 6&nbsp;% à 5&nbsp;%. La proportion de réponses « en or » (entièrement correctes et utiles) est passée de 66&nbsp;% à 80,5&nbsp;%.

**La rétroaction positive est restée élevée (77&nbsp;%)&nbsp;:** 21&nbsp;% des personnes qui ont répondu avec un pouce levé en guise de « oui » à la question « Cela vous a-t-il été utile? » ont ensuite indiqué que cela leur avait évité un appel (11&nbsp;%) ou une visite (10&nbsp;%).

**Le budget de 2025 a mis à l’essai la capacité en temps réel&nbsp;:** lorsque le budget de 2025 a été annoncé le 4 novembre, nous avons ajouté une requête personnalisée du ministère des Finances du Canada dans l’heure qui a suivi. L’équipe a mis à l’essai les questions et a peaufiné les URL immédiatement après le lancement des pages du budget. Toutes les questions concernant le budget public posées à propos de l’annonce ont reçu des réponses claires et précises, ce qui prouve que le système est capable de gérer les nouvelles de dernière heure du gouvernement.

**L’ampleur est confirmée&nbsp;:** grâce aux réponses provenant de 60 institutions, l’essai a permis de confirmer qu’il s’agit véritablement d’une solution à l’échelle de l’organisation qui fonctionne pour l’ensemble des services fédéraux.

### Ce que nous avons appris de l’essai 2

**Les questions multilingues fonctionnent&nbsp;:** l’essai 2 comprenait la notation de 94 réponses fournies à des questions posées dans 22 langues non officielles. L’attribution des notes est semblable à celle des réponses en anglais et en français. Cela va de soi puisque le système Réponses IA traduit la question en anglais afin d’y répondre, puis retraduit dans la langue d’origine pour afficher la réponse. Les notes accordées ont confirmé la capacité du système à servir les visiteurs canadiens et étrangers dans la langue de leur choix.

**Les utilisateurs n’ont pas toujours répondu aux questions d’éclaircissement&nbsp;:** certains utilisateurs ne semblaient pas faire défiler la page pour répondre aux questions d’éclaircissement posées par l’IA. Nous avons ajouté un indicateur de défilement pour signaler qu’il y a du contenu plus bas sur la page.

**Les utilisateurs veulent en savoir plus sur Réponses IA&nbsp;:** de nombreuses questions ont été posées au sujet du système. Après l’essai, l’équipe du Bureau de l’Expérience Canada.ca a ajouté [une page À propos de Réponses IA](https://reponses-ia.alpha.canada.ca/fr/a-propos) pour permettre au système de Réponses IA de la télécharger et d’en tenir compte pour répondre à des questions à son propre sujet.

## Essai 3&nbsp;: partenaires de l’essai bêta

### Participation à l’essai 3 (du 2 décembre 2025 au 9 janvier 2026)

Le premier essai bêta a été mené en collaboration avec quatre ministères fédéraux partenaires. Ils ont placé des bannières sur 112 pages anglaises et françaises de Canada.ca, invitant les visiteurs à mettre à l’essai Réponses IA. L’équipe de l’éditeur principal de Service Canada a fourni des bannières personnalisées pour cet essai. Pages intégrant la bannière&nbsp;:

* **Emploi et Développement social Canada (EDSC)&nbsp;:** toutes les pages de l’assurance-emploi
* **Secrétariat du Conseil du Trésor (SCT)&nbsp;:** pages sur la rémunération et la pension dans la fonction publique, et pages Travailler au gouvernement
* **Services aux Autochtones Canada (SAC)&nbsp;:** pages sur le statut d’Indien
* **Santé Canada (SC)&nbsp;:** pages sur la grippe et la rougeole

Avec les essais de bannières sur la page Coordonnées de Canada.ca, cela a généré 3 222 questions – notre plus grand essai à ce jour. Les membres des équipes partenaires ont évalué au moins 25&nbsp;% des questions concernant leur contenu pendant et après l’essai.

Les taux de clics à Réponses IA varient selon le type de page&nbsp;: la page de Coordonnées présente le taux le plus élevé (2,0&nbsp;%), tandis que les pages sur l’assurance-emploi affichent une moyenne de 0,5&nbsp;% et les pages sur la santé varient entre 0,03&nbsp;% et 0,04&nbsp;% des visiteurs qui ont essayé l’essai bêta de Réponses IA.

### Principales constatations de l’essai 3

**Le taux d’exactitude a atteint 96,7&nbsp;%&nbsp;:** l’évaluation d’un échantillon de 1 155 questions (36&nbsp;% du total) par des experts et par l’IA a permis de mesurer le taux d’erreur et d’exactitude. En anglais, le taux d’exactitude était de 96,9&nbsp;% et, en français, il s’établissait à 96,1&nbsp;%, ce qui maintient la cohérence entre les langues officielles (ce qui est rare) que nous avons observée tout au long des essais.

**Amélioration du rendement de la notation de l’auto-évaluation de l’IA&nbsp;:** L’analyse de l’exactitude comprenait 174 auto-évaluations de réponses semblables à des questions semblables.

**L’évaluation par les partenaires a permis d’obtenir des renseignements sur le contenu&nbsp;:** chaque partenaire a découvert des problèmes liés à son propre contenu Web au cours du processus d’évaluation. EDSC a trouvé des renseignements obsolètes sur la manière de soumettre les formulaires à Service Canada et une lacune dans le contenu portant sur les relevés d’emploi des employés. Le SCT a découvert des lacunes dans son contenu et des instructions qui n’étaient pas rédigées en langage clair.

**La rétroaction positive se maintient à 65&nbsp;%&nbsp;:** même avec le passage à des sujets plus complexes, la satisfaction des utilisateurs est restée élevée.

### Ce que nous avons appris de l’essai 3

**Le rendement des bannières au bas des pages est supérieur à celui des bannières en haut des pages&nbsp;:** les essais effectués sur la page Coordonnées ont montré que les bannières fixes au bas des pages atteignaient un taux de clics de 2,0&nbsp;% (201 clics sur 9 971 visites), par rapport à 0,8&nbsp;% pour les bannières en haut des pages (71 clics sur 8 772 visites), soit une efficacité 2,5 fois supérieure. Les utilisateurs semblent plus enclins à essayer le soutien de l’IA après avoir parcouru le contenu de la page. Les bannières seront dorénavant placées au bas des pages.

**Les questions de suivi doivent être améliorées&nbsp;:** les questions de suivi posées au cours d’une même session étaient 2&nbsp;% plus susceptibles de contenir des erreurs. Nous étudions les causes et les solutions possibles.

**Le renvoi précis à la source est important&nbsp;:** la remarque la plus fréquente concernant les « améliorations nécessaires » concerne les renvois à des pages thématiques plutôt qu’à la page précise de la source dont les utilisateurs ont besoin. Les partenaires veulent des liens plus précis de renvois à la source.

**L’IA comme outil de diagnostic&nbsp;:** Les partenaires ont mentionné que le processus d’évaluation comme tel était utile. Il a révélé des problèmes de contenu que leurs équipes de communication Web n’avaient pas remarqués. Plusieurs équipes ont commencé à travailler à l’amélioration du contenu en fonction des problèmes soulevés par Réponses IA. À ce propos, nous avons reçu le commentaire suivant&nbsp;: « Les réponses de l’IA ont généré des réponses floues lorsque le contenu source n’était pas clair, ce qui fait ressortir l’importance d’une maintenance régulière du site Web ».

## Pourquoi est-ce important?

Ces essais démontrent que l’assistance au moyen de l’IA à l’échelle de l’organisation peut fonctionner dans l’ensemble des services du gouvernement du Canada, tout en respectant les normes d’exactitude et de sécurité.

La **flexibilité du produit, dont la conception est fondée sur un agent conversationnel**, le rend évolutif et prêt à répondre aux besoins futurs en matière d’IA.

Cela vient surtout montrer que nous pouvons répondre aux besoins des utilisateurs là où ils se trouvent en leur offrant une assistance immédiate et précise, directement sur Canada.ca.

* Cela fait gagner du temps et réduit le nombre d’appels téléphoniques et de visites au bureau, ce qui permet au personnel des différents modes de prestation de services de se concentrer sur les besoins plus complexes des personnes.
* Pour un gouvernement numérique, il ne s’agit pas seulement d’une mise à jour technique, mais d’une amélioration importante des services pour les personnes qui les utilisent chaque jour.

## En savoir plus

Alors que nous travaillons à un déploiement plus vaste en 2026, nous espérons que notre travail aidera les équipes de développement de l’IA dans l’ensemble du secteur public à déployer des applications sûres et efficaces.

## Derniers changements

{% include components/latest-changes.html  items=page.latestChanges %}
