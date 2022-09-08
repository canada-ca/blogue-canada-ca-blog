---
altLangPage: /2022/09/23/presentation-bouton-contextuel-se-connecter
date: 2022-09-23
dateModified: 2022-09-29
description: "To improve findability for this important top task, the global header component of Canada.ca now includes the option of adding a contextual Sign in button on pages where people are likely looking to sign in to an account."
title: "Introducing the contextual Sign in button"
---
Every day, over a million visitors come to Canada.ca to access government services. For many of these services, people must sign in to an authenticated government account.

To improve findability for this important top task, the global header component of Canada.ca now includes the option of adding a contextual Sign in button on pages where people are likely looking to sign in to an account.

[Contextual Sign in button - Canada.ca design pattern](https://design.canada.ca/common-design-patterns/contextual-signin.html)

> “Making the sign-in experience of users easier and improving the overall end-to-end experience of accessing government services are key to ensuring that the GC’s digital transformation keeps users’ needs at the forefront.” - [Canada’s Digital Ambition 2022](https://www.canada.ca/en/government/system/digital-government/government-canada-digital-operations-strategic-plans/canada-digital-ambition.html)

## Consistent placement for improved findability

On pages that include the Sign in button, the consistent placement, as part of the header, creates a learning effect. As more programs and services use this component, people will begin to recognize where on a page they can expect to find the access point to the account (or accounts) associated with the content they’re reading. Improving findability is a first step to improving task success.

{% include components/gc-complex-img.html
   alt="A long description can be found after the image"
   file="2022-09-23-sign-in-01.png"
   caption=""
   summary="Detailed description"
   content="<p>The Sign in button appears in the top right corner of the screen, below the divider line that separates the Government of Canada signature, language toggle and search bar from the breadcrumb and the page content.</p>"
%}

## Consistent label: “Sign in,” not “Log in”

There are well over 50 separate Government of Canada accounts that require people to register and sign in to access their data. Terminology matters. A standardized approach to labeling improves both recognition and clarity.

In 2018, the Treasury Board of Canada Secretariat Office of the Chief Information Officer (OCIO) made the decision to use “Sign in” as the label for access to GCKey and Sign-in partner authenticated services.

This decision was based on these considerations:

1. Usage: Analysis showed that more accounts across Canada.ca were using Sign in for their authenticated interactions, including some of the most used accounts from CRA, IRCC, and Service Canada, so many people were already familiar with that label and were looking for it
2. Call to action: Using a verb to initiate an action improves task success
   - in English, “sign in” uses a verb, while “login” is a noun
   - in French, “se connecter” is a verb, while “connexion” is a noun

Also, when discussing terminology for authenticated services, it’s important to note that “Register” (“S’inscrire” in French) is the standard label for setting up an account, not “Sign up.” “Sign up” is too similar to “Sign in.” It’s better for the terms to be very distinct as the 2 terms may often appear close together.

## When to customize the button label

In mobile view, we recommend using the generic label “Sign in.” This ensures that the button doesn’t spread over multiple lines to accommodate lengthy label text on a small screen.

For medium and large screens, the label field allows up to 25 characters. In these formats, you can customize the label with additional descriptive text, such as “Sign in to [account name],” if being more specific works better in the context of the page.

If you’re adding the button on a page where there may be multiple accounts that a person could want to sign in to, it may make sense to use the generic “Sign in” label to direct people to a chooser page. The header of a chooser page shouldn’t include the Sign in button component. Instead, the body of the page should provide access to each of the relevant accounts.

Once you add the Sign in button on a page or group of pages, watch traffic patterns and feedback to gain insights on how people are using it. This may provide cues as to when to customize the label or where the button may be more or less effective.

## Final word

Canada.ca is the source for Canadians to access services from the Government of Canada. Everyone needs clear paths to task success.

When we use consistent terminology across the ecosystem, it helps people feel confident that they are on the right path. Improved confidence increases trust and provides a better overall user experience. It requires that we, as content designers, pay attention to even the smallest details, right down to the label text for buttons.

## Learn more
- [Choosing the right button for task success](https://blog.canada.ca/2020/12/17/choosing-buttons.html)
- [Contextual Sign in button - Canada.ca design pattern](https://design.canada.ca/common-design-patterns/contextual-signin.html)
- [GCWeb (WET): Authentication patterns](https://wet-boew.github.io/GCWeb/sites/authentication/authentication-en.html)
- [Ask a UXpert: Why is consistency important in design?](https://www.youtube.com/watch?v=UHUluiMe0cA&t=51s)
- [Guideline on Defining Authentication Requirements](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=26262)
- [Labelling study: which words work best
](https://blog.canada.ca/2020/10/02/labelling-study)
