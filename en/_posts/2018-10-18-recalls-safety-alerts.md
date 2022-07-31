---
altLangPage: "/2018/10/18/rappels-avis-securite"
date:   2018-10-18
description: Of the top 100 tasks on Canada.ca, getting recalls and safety alerts is &#35;8. It gets nearly 7 million annual visits, 71% of which are via mobile. For food-related alerts, that jumps to a whopping 84%.
title:  "Recalls and safety alerts: An optimization project to better protect Canadians"
---

[Of the top 100 tasks on Canada.ca](https://www.canada.ca/en/government/about/top-tasks-for-canada-ca.html), getting recalls and safety alerts is #8. It gets nearly 7 million annual visits, 71% of which are via mobile. For food-related alerts, that jumps to a whopping 84%.

In the existing system, Canadians can search for recalls and safety information in four categories:

* Consumer products
* Vehicles
* Food
* Health products

The content is currently managed and populated by three partner departments:

* [Health Canada](https://www.canada.ca/en/health-canada.html)
* [Transport Canada](https://www.tc.gc.ca/eng/menu.htm)
* [Canadian Food Inspection Agency](http://www.inspection.gc.ca/eng/1297964599443/1297965645317)

## If 7 million people are using the system, we better make sure it works

The unfortunate reality is that the existing system for recalls and safety alerts is old and unreliable. The database and technical infrastructure is a patchwork of servers that often fails and needs constant maintenance. This is a serious problem for Canadians who rely on it for timely and accurate safety information.

In June of 2018, the web team at Health Canada, along with representatives from Transport Canada and Canadian Food Inspection Agency, began working with the Digital Transformation Office from the Treasury Board Secretariat to optimize recalls and safety alerts.

On top of the infrastructure challenges, discovery research and usability testing found that Canadians face several problems when using the system:

* design, content and writing style were not responsive or mobile-friendly
* search issues and lack of filters caused many task failures
* overall sense of uncertainty – people weren’t getting clear answers for what to do

With those issues in mind, the Digital Transformation Office and the project team designed new prototypes for a search solution and content pages. The goal was to increase task findability and completion rates by 20% for each.

## New prototypes

Considering 71% of people are coming to the system via mobile, designing for mobile first was the obvious focus for the new prototypes.

The new search solution:

* adopted the Canada.ca search engine
* added auto-complete to the search field and filters
* improved the layout, search result headings and short description of the results
* presented results in chronological order
* changed the main categories to:
  * Food and allergies
  * Vehicles
  * Health
  * Products

The new content pages:

* clarified page titles: “product, issue, status”
* added summaries at the top of pages with a clear “what to do”
* used clear headings, font and spacing to make pages easier to scan
* simplified language throughout
* applied responsive design to make pages and lists easier to use
* added links to product brand and category
* grouped together similar products affected by a recall so users don’t need to leave the page to find out if their product is affected

After a second round of validation testing with Canadians on the new prototypes, the results were impressive. Task findability increased from 51% to 75% (up 24% points), and task completion increased from 54% to 87% (up 34% points).
{% include components/gc-complex-img.html
   alt="Image of two phones showing EpiPen information update page, labelled 'Before' and 'After'."
   file="recalls-rappels/beforeafter-epipen.jpg"
   caption="EpiPen shortage information update at baseline and after redesign for validation"
   summary="Detailed description"
   content="<p>Image of two phones, labelled &quot;Before&quot; and &quot;After&quot;.</p>
    <p>The first phone shows how dense and crowded the original safety alert looked on mobile. An arrow points to the text with the annotation &quot;Pinch and zoom - Canadians use phones for recalls&quot;.</p>
    <p>The second phone shows how the redesigned prototype text is much shorter and has more white space. You can see that 3 bullets immediately tell you the product, the issue and what to do. An arrow points to the text with the annotation &quot;Answers not information - Highlight what to do&quot;.</p>"
%}

## Next steps

Now that we know how to present recalls and safety alerts so that Canadians can easily find and understand them, we’re moving on to the operational side of the project.

Health Canada, Transport Canada and Canadian Food Inspection Agency are working together to define our technical and operational needs, and build a system that will be reliable for Canadians for years to come. The goal is to release incremental improvements quickly based on what we learned, with a final recalls and safety alerts system rolled out by summer of 2019.

## We want to hear from you
Let us know what you think about task management. Email us at [dto.btn@tbs-sct.gc.ca](mailto:dto.btn@tbs-sct.gc.ca) or tweet using the hashtag #Canadadotca.

## Learn more

* [Project summary: Recalls and safety alerts]( {{ "/research-summaries/recalls-research-summary" | prepend: site.urlalt[ page.lang ] }} )
