---
altLangPage: /2025/12/17/reponses-ia 
date: 2025-12-17
description: "Every day, thousands of people turn to the Government of Canada (GC) seeking help with essential services."
title: "AI Answers: Enterprise-scale trial for Canada.ca"
---
<p>Every day, thousands of people turn to the Government of Canada (GC) seeking help with essential services. Many cannot call or visit government offices during business hours, making effective online self-service critical.</p>

<p>The <a href="https://design.canada.ca/common-design-patterns/page-feedback.html" target="_blank" rel="noreferrer noopener">GC Feedback tool</a> is being used by many teams to improve their <a href="http://canada.ca" target="_blank" rel="noreferrer noopener">Canada.ca</a> content and services. The tool captures over 3,000 daily questions and answers from people navigating immigration applications, employment benefits, tax account management, and more. While GC teams continue to improve <a href="http://canada.ca">Canada.ca</a>, these improvements alone cannot fully address the challenge of helping people navigate the vast array of GC web content and services.</p>

<p>This summer, CDS tested a new approach: <a href="https://ai-answers.alpha.canada.ca/en" target="_blank" rel="noreferrer noopener">AI Answers</a>. It's an AI-based service that provides people with short, plain-language responses (sourced exclusively from GC websites, with authoritative links to guide users to their next steps). This blog highlights the AI Answers trial results, including key findings and what we learned.</p>

<h2>What we tested:</h2>

<ul class="lst-spcd-2">
    <li>On the <a href="https://www.canada.ca/en/government/sign-in-online-account.html" target="_blank" rel="noreferrer noopener">Canada.ca Sign in page</a>, we ran a 19-day trial inviting users to try the new AI Answers service (from June 18 to 26 and July 15 to 25, 2025).
        <ul>
            <li>Answers are sourced exclusively from Canada.ca, gc.ca, and authorized federal government URLs. Any questions that contain personal identifying information are blocked to protect the user's privacy.</li>
        </ul>
    </li>
    <li>The concept was straightforward: let users ask questions in their own words and receive accurate, government-sourced answers instantly.</li>
</ul>

<div class="col-md-8 mrgn-tp-lg">
        <figure><img alt="Screenshot of the Government of Canada online account sign-in page." class="img-responsive" src="/images/ai-answers/Sign-In.jpg">
            <figcaption class="well mrgn-tp-lg mrgn-bttm-lg">
                <p><strong>Screenshot of the Government of Canada online account sign-in.</strong></p>
                <p>A page showing the login options and a pop up inviting users to try the new AI Answers Service.</p>
            </figcaption>
        </figure>
</div>
<div class="clearfix"></div>

<details>
    <summary>The technical approach</summary>
    <p>Our model-independent architecture used Azure Canada GPT 4.1 with department-specific prompts for 10 institutions: CIRNAC, CRA, ESDC, FIN, HC, IRCC, ISC, PHAC, PSPC, and TBS.</p>
    <p>Since web content changes frequently, the system uses search and downloads specific pages to answer questions, rather than pre-scraping web content. This AI system relies on information provided on GC websites (<a href="https://ai-answers.alpha.canada.ca/en/about">learn more about AI Answers</a>).</p>
    <p>The AI Answers product team built a detailed agentic system (users 'chat with a specialized agent) prompt to make sure that answers are clear, concise, and helpful. We built in both human expert evaluation and AI scoring systems, with blocking of personal identifying information to protect user privacy.</p>
</details>

<h2>Trial participation:</h2>

<ul>
    <li>Trial participation exceeded our expectations: 1,227 user sessions, spanning 32 departments, with questions covering 120+ government tasks. <a href="https://design.canada.ca/survey/writing-tasks.html#what-is-a-task" target="_blank" rel="noreferrer noopener">Tasks are what people come to the content to do</a>: That can mean getting answers, like learning about a subject, or performing a transaction, like applying for a program.</li>
</ul>

<p>The question distribution revealed user priorities:</p>

<ul>
    <li><strong>42% (635 questions) on IRCC services:</strong> immigration, work permits, and visas.</li>
    <li><strong>25% (377 questions) on ESDC services:</strong> My Service Canada Account sign-in and registration, employment insurance, CPP, and job searches.</li>
    <li><strong>22% (332 questions) on CRA services:</strong> account access, and tax and business questions.</li>
    <li>Even less-commonly used government services generated multiple questions per topic across many departments, suggesting broad user interest in AI-assisted government interactions.</li>
</ul>

<div class="col-md-8 mrgn-tp-lg">
        <figure><img alt="Screenshot of the AI Answers service page." class="img-responsive" src="/images/ai-answers/AI-Answers-679x1024.png">
            <figcaption class="well mrgn-tp-lg mrgn-bttm-lg">
                <p><strong>Screenshot of the AI Answers service page.</strong></p>
                <p>The page explains that the tool can help users find answers to their questions about Canada.ca services and information.</p>
            </figcaption>
        </figure>
</div>



<h2>4 key findings:</h2>

<ol class="lst-spcd-2">
    <li><strong>Accuracy that meets enterprise standards:</strong> We achieved a 95% accuracy rate on English questions and 94% on French. This was verified through an expert evaluation of 800 trial questions, completed with GC departments and agency partners. This consistency across both official languages is rare in AI applications, where French typically shows 20% higher error rates.</li>
    <li><strong>Users found genuine value:</strong> 88% of user feedback was positive. Importantly, 22% of feedback respondents said they no longer needed to call government offices or visit in person, while 52% reported saving time on searching and reading.</li>
    <li><strong>Unexpected breadth of use:</strong> Despite launching from a <a href="https://www.canada.ca/en/government/sign-in-online-account.html" target="_blank" rel="noreferrer noopener">sign-in page</a>, 50% of questions were related to the top 20 government services identified in the <a href="https://design.canada.ca/survey/" target="_blank" rel="noreferrer noopener">GC Task Success Survey</a>. Users asked about everything from work permits, to Contributions to the Canada Pension Plan (CPP) benefits, to tax account access. This revealed a strong demand for AI help across the full spectrum of government services.</li>
    <li><strong>Multilingual capability:</strong> Beyond English and French, the system handled questions in 19 other languages, representing 8.4% of all queries. While accuracy was lower for these languages, we've since implemented translation and search improvements.</li>
</ol>

<h2>What we learned</h2>

<ul class="lst-spcd-2">
    <li><strong>Short queries need different handling:</strong> In June, 12% of questions were just 1-2 words, requiring clarification. We addressed this in July by blocking very short queries, providing instruction on effective use and offering a search alternative.</li>
    <li><strong>Length limits matter:</strong> We reduced the maximum question length from 400 to 260 characters after finding longer questions were often confusing or included attempts to manipulate the system.</li>
    <li><strong>Content gaps become visible:</strong> GC partners are now addressing online content gaps and errors that user questions had revealed, turning AI interactions into a diagnostic tool for service improvement.</li>
    <li><strong>Safety measures work:</strong> Despite concerns about AI risks, expert reviewers found no harmful responses were given, and no attempts to manipulate the system were successful during the trial.</li>
</ul>

<h2>Why this matters:</h2>

<ul class="lst-spcd-2">
    <li>This trial demonstrates that enterprise-scale AI assistance can work across the full breadth of GC services, while maintaining accuracy and safety standards.
        <ul>
            <li>The product's flexible, chat agent-based design makes it scalable and ready for future AI needs.</li>
        </ul>
    </li>
    <li>More importantly, it shows we can meet users where they are by providing immediate, accurate assistance right on <a href="http://canada.ca">Canada.ca</a>.
        <ul>
            <li>This saves time and reduces the need for phone calls and office visits, allowing those service channels to focus on people's more complex service needs.</li>
            <li>For a digital government, that's not just a technical upgrade, but a meaningful service improvement for people using government services every day.</li>
        </ul>
    </li>
</ul>

<h2>Next steps</h2>

<ul class="lst-spcd-2">
    <li>We have made improvements to AI-crafted search queries and translation, while expanding testing across additional Canada.ca pages. The goal is to make sure that people receive the latest, most accurate information possible, no matter which language they use.
        <ul>
            <li><strong>Improvement examples:</strong>
                <ul>
                    <li>Translating questions that are not in English or French into English before searching (the AI uses the search results to help it find up-to-date information).</li>
                    <li>Another improvement is to transform the users question into a shorter search query.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>We're also exploring integrating custom departmental tools and evaluating potential applications for call-centre agents and social media teams.</li>
</ul>

<h2>Want to learn more?</h2>

<p>In the near future, our team will publish a few blog posts about the design, safety, and operations of AI Answers to give you deeper insight into this experimental service. We hope that our work helps AI development teams across the public sector deploy safe and effective applications.</p>

<p>You can also <a href="https://ai-answers.alpha.canada.ca/en" target="_blank" rel="noreferrer noopener">visit the AI Answers trial site</a>.</p>