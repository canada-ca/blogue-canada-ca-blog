---
altLangPage: /2025/12/17/reponses-ia 
date: 2025-12-17
dateModified: 2025-12-22
description: "Every day, thousands of people turn to the Government of Canada (GC) seeking help with essential services."
title: "AI Answers: Enterprise-scale trial for Canada.ca"
---
<p>Every day, thousands of people turn to the Government of Canada (GC) seeking help with essential services. Many cannot call or visit government offices during business hours, making effective online self-service critical.</p>

<h2>How existing tools support users</h2>
<p>The <a href="https://design.canada.ca/common-design-patterns/page-feedback.html">GC Feedback tool</a> is being used by many GC teams to improve their Canada.ca content and services. The tool captures over 3,000 daily questions and answers from people navigating immigration applications, employment benefits, tax account management, and more. While teams continue to improve Canada.ca, these improvements alone cannot fully address the challenge of helping people navigate the vast array of GC web content and services.</p>

<h2>How AI Answers works</h2>
<p>This summer, CDS tested a new approach: AI Answers. It's an AI-based service that provides people with short, plain-language responses (sourced exclusively from GC websites, with authoritative links to guide users to their next steps). This blog highlights the AI Answers trial results, including key findings and what we learned.</p>

<h2>What we tested</h2>
<p>On the <a href="https://www.canada.ca/en/government/sign-in-online-account.html">Canada.ca Sign in page</a>, we ran a 19-day trial inviting users to try the new AI Answers service (from June 18 to 26 and July 15 to 25, 2025).</p>

<p>Answers were sourced exclusively from Canada.ca, gc.ca, and authorized federal government URLs. Any questions that contained personal identifying information were blocked to protect the user's privacy.</p>

<p>The concept was straightforward: let users ask questions in their own words and receive accurate, government-sourced answers instantly.</p>

<div class="col-md-8 mrgn-tp-lg">
<div class="row">
        <figure><img alt="Screenshot of the Government of Canada online account sign-in page." class="img-responsive" src="/images/ai-answers/sign-in.jpg">
            <figcaption class="well mrgn-tp-0 mrgn-bttm-lg">
                <p><strong>Screenshot of the Government of Canada online account sign-in.</strong></p>
                <p>A page showing the login options and a pop up inviting users to try the new AI Answers Service.</p>
            </figcaption>
        </figure>
</div>
</div>
<div class="clearfix"></div>
<details>
    <summary>The technical approach</summary>
    <p>Our model-independent architecture uses Azure Canada GPT 4.1 with department-specific prompts for 10 institutions: CIRNAC, CRA, ESDC, FIN, HC, IRCC, ISC, PHAC, PSPC, and TBS.</p>
    <p>Since web content changes frequently, the system uses search and downloads specific pages to answer questions, rather than pre-scraping web content. This AI system relies on information provided on GC websites (<a href="https://ai-answers.alpha.canada.ca/en/about">learn more about AI Answers</a>).</p>
    <p>The AI Answers product team built a detailed agentic system (users interact with a specialized agent) prompt to make sure that answers are clear, concise, and helpful. We built in both human expert evaluation and AI scoring systems, with blocking of personal identifying information to protect user privacy.</p>
</details>

<h2>Trial participation</h2>

<p>Trial participation exceeded our expectations: 1,227 user sessions, spanning 32 departments, with questions covering 120+ government tasks. Tasks are what people come to the content to do: That can mean getting answers, like learning about a subject, or performing a transaction, like applying for a program.</p>

<ul>
    <li><a href="https://design.canada.ca/survey/writing-tasks.html#what-is-a-task">Choosing and writing tasks: What is a task</a></li>
</ul>

<p>The question distribution revealed user priorities:</p>

<ul>
    <li><strong>42% (635 questions) on IRCC services:</strong> immigration, work permits, and visas</li>
    <li><strong>25% (377 questions) on ESDC services:</strong> My Service Canada Account sign-in and registration, employment insurance, CPP, and job searches</li>
    <li><strong>22% (332 questions) on CRA services:</strong> account access, and tax and business questions</li>
</ul>

<p>Even less-commonly used government services generated multiple questions per topic across many departments, suggesting broad user interest in AI-assisted government interactions.</p>

<div class="col-md-8 mrgn-tp-lg">
<div class="row">
        <figure><img alt="Screenshot of the AI Answers service page." class="img-responsive" src="/images/ai-answers/AI-answers.png">
            <figcaption class="well mrgn-tp-0 mrgn-bttm-lg">
                <p><strong>Screenshot of the AI Answers service page.</strong></p>
                <p>The page explains that the tool can help users find answers to their questions about Canada.ca services and information.</p>
            </figcaption>
        </figure>
</div>
</div>



<h2>Four key findings</h2>

<p><strong>Accuracy that meets enterprise standards:</strong> We achieved a 95% accuracy rate on English questions and 94% on French. This was verified through an expert evaluation of 800 trial questions, completed with GC departments and agency partners. This consistency across both official languages is rare in AI applications, where French typically shows 20% higher error rates.</p>
<p><strong>Users found genuine value:</strong> 88% of user feedback was positive. Importantly, 22% of feedback respondents said they no longer needed to call government offices or visit in person, while 52% reported saving time on searching and reading.</p>
<p><strong>Unexpected breadth of use:</strong> Despite launching from a sign-in page, 50% of questions were related to the top 20 government services identified in the <a href="https://design.canada.ca/survey/">GC Task Success Survey</a>. Users asked about a wide range of subjects, from work permits, to contributions to the Canada Pension Plan (CPP) benefits, to tax account access. This revealed a strong demand for AI help across the full spectrum of government services.</p>
<p><strong>Multilingual capability:</strong> Beyond English and French, the system handled questions in 19 other languages, representing 8.4% of all queries. While accuracy was lower for these languages, we've since implemented translation and search improvements.</p>

<h2>What we learned</h2>

<p><strong>Short queries need different handling:</strong> In June, 12% of questions were just 1-2 words, requiring clarification. We addressed this in July by blocking very short queries, providing instruction on effective use and offering a search alternative.</p>
<p><strong>Length limits matter:</strong> We reduced the maximum question length from 400 to 260 characters after finding longer questions were often confusing or included attempts to manipulate the system.</p>
<p><strong>Content gaps become visible:</strong> GC partners are now addressing online content gaps and errors that user questions had revealed, turning AI interactions into a diagnostic tool for service improvement.</p>
<p><strong>Safety measures work:</strong> Despite concerns about AI risks, expert reviewers found no harmful responses were given, and no attempts to manipulate the system were successful during the trial.</p>

<h2>Why this matters</h2>

<p>This trial demonstrates that enterprise-scale AI assistance can work across the full breadth of GC services, while maintaining accuracy and safety standards.</p>

<p>The product's <strong>flexible, chat agent-based design</strong> makes it scalable and ready for future AI needs.</p>
   
<p>More importantly, it shows we can meet users where they are by providing immediate, accurate assistance right on Canada.ca.</p>
<ul>
    <li>This saves time and reduces the need for phone calls and office visits, allowing those service channels to focus on people's more complex service needs.</li>
    <li>For a digital government, that's not just a technical upgrade, but a meaningful service improvement for people using government services every day.</li>
</ul>

<h2>Next steps</h2>

<p>We are making improvements to AI-crafted search queries and translation, and expanding testing across additional Canada.ca pages. The goal is to make sure that people receive the latest, most accurate information possible, no matter which language they use.</p>
<p>Improvement examples:</p>
<ul>
    <li>Translating questions that are not in English or French into English before searching (the AI uses the search results to help it find up-to-date information).</li>
    <li>Transforming user questions into shorter search queries when needed.</li>
</ul>
<p>We're also exploring integrating custom departmental tools and evaluating potential applications for call-centre agents and social media teams.</p>

<h2>Learn more</h2>

<p>In the near future, the AI Answers team will publish blog posts about the design, safety, and operations of AI Answers to give deeper insight into this experimental service. We hope that our work helps AI development teams across the public sector deploy safe and effective applications.</p>

<p><a href="https://ai-answers.alpha.canada.ca/en">Visit the AI Answers trial site</a>.</p>