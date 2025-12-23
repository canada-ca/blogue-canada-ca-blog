---
altLangPage: /2025/12/17/ai-answers
date: 2025-12-17
dateModified: 2025-12-22
description: "Chaque jour, des milliers de personnes se tournent vers le gouvernement du Canada (GC) pour obtenir de l'aide relativement aux services essentiels."
title: "Réponses IA : Mise à l'essai à l'échelle de l'organisation pour Canada.ca"
---
<p>Chaque jour, des milliers de personnes se tournent vers le gouvernement du Canada (GC) pour obtenir de l'aide relativement aux services essentiels. De nombreuses personnes ne peuvent ni téléphoner aux bureaux du gouvernement ni s'y rendre en personne pendant les heures d'ouverture. C'est pourquoi il est essentiel que le libre-service en ligne soit efficace.</p>

<h2>Comment les outils existants aident les utilisateurs</h2>
<p>L'<a href="https://conception.canada.ca/configurations-conception-communes/outil-retroaction.html">outil Rétroaction GC</a> est utilisé par de nombreuses équipes du GC pour améliorer le contenu et les services qu'elles offrent sur Canada.ca. L'outil recueille quotidiennement plus de 3000 questions et réponses de personnes qui parcourent des pages relatives aux demandes d'immigration, aux prestations d'emploi, à la gestion de comptes d'impôt, etc. Bien que les équipes continuent d'améliorer Canada.ca, ces améliorations ne peuvent à elles seules relever entièrement le défi que représente le fait d'aider les gens à s'y retrouver dans la vaste gamme de contenus et de services Web du GC.</p>

<h2>Comment fonctionne Réponses IA</h2>
<p>Cet été, le SNC a mis à l'essai une nouvelle approche&nbsp;: Réponses IA. Ce service fondé sur l'IA offre aux utilisateurs des réponses courtes dans un langage clair (dont le contenu provient exclusivement de sites Web du GC, avec des liens fiables qui guident les utilisateurs vers les étapes suivantes). Ce billet de blogue présente les résultats de la mise à l'essai de Réponses IA, y compris les principales constatations et ce que nous avons appris.</p>

<h2>Ce que nous avons mis à l'essai</h2>
<p>Sur la <a href="https://www.canada.ca/fr/gouvernement/ouvrir-session-dossier-compte-en-ligne.html"> page d'ouverture de session de Canada.ca</a>, nous avons effectué une mise à l'essai de 19 jours dans le cadre de laquelle nous avons invité les utilisateurs à essayer le nouveau service de Réponses IA (du 18 au 26 juin et du 15 au 25 juillet 2025).</p>
<p>Le contenu des réponses provenait exclusivement de Canada.ca, de sites Web se terminant par &laquo;&nbsp;gc.ca&nbsp;&raquo; et de sites avec une adresse URL autorisée par le gouvernement fédéral. Toutes les questions qui contenaient des renseignements personnels permettant d'identifier la personne ont été bloquées afin de protéger la vie privée de l'utilisateur.</p>
<p>Le concept était simple&nbsp;: permettre aux utilisateurs de poser des questions dans leurs propres mots et de recevoir instantanément des réponses précises dont le contenu provenait de sites Web du gouvernement.</p>
<div class="col-md-8 mrgn-tp-lg">
<div class="row">
        <figure><img alt="Capture d'écran de la page « Se connecter à un dossier ou un compte en ligne du gouvernement du Canada »." class="img-responsive" src="/images/reponses-ia/se-connecter.jpg">
            <figcaption class="well mrgn-tp-0 mrgn-bttm-lg">
                <p><strong>Capture d'écran de la page &laquo;&nbsp;Se connecter à un dossier ou un compte en ligne du gouvernement du Canada&nbsp;&raquo;.</strong></p>
                <p>Une page montrant les options d'ouverture de session et une fenêtre contextuelle invitant les utilisateurs à essayer le nouveau service de Réponses IA.</p>
            </figcaption>
        </figure>
</div>
</div>
<div class="clearfix"></div>
<details>
    <summary>L'approche technique</summary>
    <p>Notre architecture indépendante du modèle utilise le modèle GPT-4.1 d'Azure Canada avec des invites propres aux ministères pour 10 institutions&nbsp;: RCAANC, ARC, EDSC, FIN, SC, IRCC, SAC, ASPC, SPAC et SCT.</p>
    <p>Comme le contenu Web change fréquemment, le système effectue des recherches et télécharge des pages précises pour répondre aux questions, plutôt que d'extraire à l'avance du contenu Web. Ce système d'IA repose sur les renseignements fournis sur les sites Web du GC (<a href="https://reponses-ia.alpha.canada.ca/fr/about">À propos de Réponses IA</a>).</p>
    <p>L'équipe de produit de Réponses IA a mis au point un système d'IA agentive (les utilisateurs interagissent avec un agent spécialisé) avec une invite détaillée pour faire en sorte que les réponses soient claires, concises et utiles. Nous avons intégré des systèmes d'évaluation par des experts humains et des systèmes de notation par l'IA, et avons fait en sorte de bloquer les renseignements personnels permettant d'identifier l'utilisateur afin de protéger sa vie privée.</p>
</details>
<h2>Participation à la mise à l'essai</h2>
<p>Le taux de participation à la mise à l'essai a dépassé nos attentes&nbsp;: 1 227 sessions d'utilisateurs, 32 ministères et des questions portant sur plus de 120 tâches gouvernementales. Une tâche est la raison pour laquelle les utilisateurs consultent le contenu&nbsp;: il peut s'agir d'obtenir des réponses, comme se renseigner sur un sujet, ou d'effectuer une transaction, comme s'inscrire à un programme.</p>

<ul>
    <li><a href="https://conception.canada.ca/sondage/rediger-taches.html#quest-ce-quune-t%C3%A2che">Choisir et rédiger des tâches&nbsp;: Qu’est-ce qu’une tâche?</a></li>
</ul>
<p>La répartition des questions témoigne des priorités des utilisateurs&nbsp;:</p>
<ul>
    <li><strong>42&nbsp;% (635 questions) concernaient les services d'IRCC&nbsp;:</strong> immigration, permis de travail et visas.</li>
    <li><strong>25&nbsp;% (377 questions) concernaient les services d'EDSC&nbsp;:</strong> connexion et inscription à Mon dossier Service Canada, assurance-emploi, Régime de pensions du Canada et recherche d'emploi.</li>
    <li><strong>22&nbsp;% (332 questions) concernaient les services de l'ARC&nbsp;:</strong> accès au compte et questions liées à l'impôt ou aux entreprises.</li>
</ul>
<p>Même les services gouvernementaux les moins utilisés ont généré plusieurs questions par sujet, et ce pour de nombreux ministères, ce qui indique que les utilisateurs ont un grand intérêt pour les interactions avec le gouvernement assistées par l'IA.</p>
<div class="col-md-8 mrgn-tp-lg">
<div class="row">
        <figure><img alt="Capture d'écran de la page du service Réponses IA." class="img-responsive" src="/images/reponses-ia/reponses-IA.png">
            <figcaption class="well mrgn-tp-0 mrgn-bttm-lg">
                <p><strong>Capture d'écran de la page du service Réponses IA.</strong></p>
                <p>La page explique que l'outil peut aider les utilisateurs à trouver des réponses à leurs questions sur les services et les renseignements offerts sur Canada.ca.</p>
            </figcaption>
        </figure>
</div>
</div>
<h2>Quatre principales constatations</h2>
<p><strong>Une exactitude qui répond aux normes organisationnelles&nbsp;:</strong> Nous avons obtenu un taux d'exactitude de 95&nbsp;% pour les questions en anglais et de 94&nbsp;% pour les questions en français. L'exactitude des réponses a été vérifiée au moyen d'une évaluation par des experts de 800 questions d'essai, réalisée en collaboration avec les ministères et les organismes partenaires du GC. Cette cohérence entre les deux langues officielles est rare dans les applications d'IA, car le français présente généralement un taux d'erreur plus élevé de 20&nbsp;%.</p>
<p><strong>Une véritable valeur ajoutée, selon les utilisateurs&nbsp;:</strong> 88&nbsp;% des commentaires des utilisateurs étaient positifs. Il est important de noter que 22&nbsp;% des répondants ont déclaré qu'ils n'avaient plus besoin d'appeler les bureaux gouvernementaux ou de s'y rendre en personne, tandis que 52&nbsp;% ont indiqué qu'ils avaient passé moins de temps à effectuer des recherches et à lire.</p>
<p><strong>Une portée de l'utilisation inattendue&nbsp;:</strong> Même si le service était offert sur une page d'ouverture de session, 50&nbsp;% des questions étaient liées aux 20 principaux services gouvernementaux nommés dans le <a href="https://conception.canada.ca/sondage/index.html">Sondage sur la réussite des tâches du GC</a>. Les utilisateurs ont posé des questions sur un large éventail de sujets, des permis de travail aux cotisations au Régime de pensions du Canada, en passant par l'accès à leur compte d'impôt. Cette mise à l'essai a révélé une forte demande pour de l'aide offerte par l'IA dans l'ensemble des services gouvernementaux.</p>
<p><strong>Une capacité multilingue&nbsp;:</strong> Outre l'anglais et le français, le système a traité des questions dans 19 autres langues. Ces questions représentaient 8,4&nbsp;% de toutes les requêtes. Le taux d'exactitude était plus faible pour ces langues, mais nous avons depuis apporté des améliorations à la traduction et à la recherche.</p>

<h2>Ce que nous avons appris</h2>
<p><strong>Les requêtes courtes doivent être traitées différemment&nbsp;:</strong> En juin, 12&nbsp;% des questions comptaient seulement un mot ou deux et nécessitaient une clarification. Nous avons remédié à ce problème en juillet en bloquant les requêtes très courtes, en fournissant des instructions sur l'utilisation efficace de l'outil et en proposant une autre option de recherche.</p>
<p><strong>Les limites de longueur sont importantes&nbsp;:</strong> Nous avons réduit la longueur maximale des questions de 400 à 260 caractères après avoir constaté que les questions plus longues prêtaient souvent à confusion ou comportaient des tentatives de manipulation du système.</p>
<p><strong>Les lacunes dans le contenu deviennent visibles&nbsp;:</strong> Les partenaires du GC s'affairent maintenant à combler les lacunes et à corriger les erreurs dans le contenu en ligne que les questions des utilisateurs ont mises en lumière. Les interactions avec l'IA sont donc devenues un outil de diagnostic pour l'amélioration des services.</p>
<p><strong>Les mesures de sécurité fonctionnent&nbsp;:</strong> Malgré les inquiétudes concernant les risques liés à l'IA, les experts ont constaté qu'aucune réponse préjudiciable n'a été donnée et que toutes les tentatives de manipulation du système ont été infructueuses au cours de la mise à l'essai.</p>

<h2>Pourquoi est-ce important?</h2>
<p>Cet essai a démontré qu'il est possible d'offrir de l'aide fondée sur l'IA efficace à l'échelle de l'organisation pour l'ensemble des services du GC, tout en respectant les normes d'exactitude et de sécurité.</p>
<p>Grâce à une <strong>conception flexible et fondée sur un agent conversationnel</strong>, le produit est évolutif et prêt à répondre aux besoins futurs en matière d'IA.</p>
<p>Plus important encore, il a montré que nous pouvons répondre aux besoins des utilisateurs là où ils se trouvent en leur fournissant une aide immédiate et précise directement sur Canada.ca.</p>
<ul>
    <li>Ce service fait gagner du temps et réduit le nombre d'appels téléphoniques et de visites aux bureaux, ce qui permet à ces modes de prestation de se concentrer sur les besoins plus complexes des personnes en matière de services.</li>
    <li>Pour un gouvernement numérique, il ne s'agit pas seulement d'une mise à niveau technique, mais d'une amélioration considérable des services du gouvernement pour les personnes qui y ont recours tous les jours.</li>
</ul>

<h2>Prochaines étapes</h2>

<p>Nous améliorons la traduction et les requêtes de recherche conçues par l'IA, et élargissons les essais à d'autres pages de Canada.ca. L'objectif est que les utilisateurs reçoivent les renseignements les plus récents et les plus précis possibles, quelle que soit la langue qu'ils utilisent.</p>
<p>Voici des exemples d'amélioration&nbsp;:</p>
<ul>
    <li>Les questions qui ne sont pas rédigées en anglais ou en français sont traduites en anglais avant que la recherche ne soit effectuée (l'IA utilise les résultats de la recherche pour aider à trouver des renseignements à jour).</li>
    <li>Les questions des utilisateurs sont transformées en requêtes de recherche plus courtes au besoin.</li>
</ul>
<p>Nous étudions également la possibilité d'intégrer des outils ministériels personnalisés et évaluons les applications possibles pour les agents des centres d'appel et les équipes des médias sociaux.</p>

<h2>En savoir plus</h2>
<p>L'équipe de Réponses IA publiera bientôt des billets de blogue sur la conception, la sécurité et les opérations de Réponses IA afin de permettre de mieux comprendre ce service expérimental. Nous espérons que notre travail aidera les équipes de développement de l'IA dans tout le secteur public à déployer des applications sûres et efficaces.</p>

<p><a href="https://reponses-ia.alpha.canada.ca/fr">Visiter le site de la mise à l'essai de Réponses IA</a>.</p>