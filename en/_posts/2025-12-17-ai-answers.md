---
altLangPage: /2025/12/17/reponses-ia
date: 2025-12-17
dateModified: 2026-06-16
description: "Every day, thousands of people turn to the Government of Canada (GC) seeking help with essential services."
latestChanges:
  - term: 2026-06-16
    definition: "Added Trial 2 and Trial 3 results, and new section: Trial results at a glance."
  - term: 2025-12-17
    definition: "Original publication with Trial 1 results (1,763 questions, 94% accuracy)."
title: "AI Answers: Enterprise-scale trials for Canada.ca"
---

## On this page

* [How existing tools support users](#how-existing-tools-support-users)
* [How AI Answers works](#how-ai-answers-works)
* [Trial results at a glance](#trial-results-at-a-glance)
* [Trial 1 results](#trial-1-results)
* [Four key findings](#four-key-findings)
* [Trial 2 results](#trial-2-results)
* [Trial 3: Partner Beta](#trial-3-partner-beta)
* [Why this matters](#why-this-matters)
* [Learn more](#learn-more)
* [Latest changes](#latest-changes)

Every day, thousands of people turn to the Government of Canada (GC) seeking help with essential services. Many cannot call or visit government offices during business hours, making effective online self-service critical.

## How existing tools support users

The [GC Feedback tool](https://design.canada.ca/common-design-patterns/page-feedback.html) is being used by many GC teams to improve their Canada.ca content and services. The tool captures over 3,000 daily questions and answers from people navigating immigration applications, employment benefits, tax account management, and more. While teams continue to improve Canada.ca, these improvements alone cannot fully address the challenge of helping people navigate the vast array of GC web content and services.

## How AI Answers works

Starting in the summer of 2025, the Canada.ca Experience Office tested a new approach: AI Answers. It's an AI-based service that provides people with short, plain-language responses (sourced exclusively from GC websites, with authoritative links to guide users to their next steps). This blog highlights the AI Answers trial results, including key findings and what we learned.

## Trial results at a glance

<table class="table table-bordered table-striped mrgn-bttm-lg">
  <thead class="bg-primary">
    <tr>
      <th>Metric</th>
      <th>Trial 1 (Jun-Jul 2025)</th>
      <th>Trial 2 (Oct-Nov 2025)</th>
      <th>Beta Trial 3 (Dec 2025-Jan 2026)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Questions</th>
      <td class="text-right">1,763</td>
      <td class="text-right">2,866</td>
      <td class="text-right">3,222</td>
    </tr>
    <tr>
      <th>Answer accuracy</th>
      <td class="text-right">94%</td>
      <td class="text-right">95%</td>
      <td class="text-right"><strong>96.7%</strong></td>
    </tr>
    <tr>
      <th>Web pages</th>
      <td class="text-right">2</td>
      <td class="text-right">12</td>
      <td class="text-right">112</td>
    </tr>
    <tr>
      <th>Institutions sourced</th>
      <td class="text-right">32</td>
      <td class="text-right">60</td>
      <td class="text-right">56</td>
    </tr>
  </tbody>
  <tfoot>
    <tr class="info">
      <th>Cumulative total:</th>
      <td colspan="3" class="text-right"><strong>7,851 questions across all trials, with 30% expert-evaluated</strong></td>
    </tr>
  </tfoot>
</table>

{% include components/gc-complex-img.html
  alt="Screenshot of the Government of Canada online account sign-in."
  file="/images/ai-answers/Sign-In.jpg"
  caption="<b>Screenshot of the Government of Canada online account sign-in.</b><br>A page showing the login options and a pop up inviting users to try the new AI Answers Service."
  summary="AI Answers technical approach"
  content="<p>Our model-independent architecture uses Azure Canada GPT 4.1 with department-specific prompts for 10 institutions: Crown-Indigenous Relations and Northern Affairs (<span class='text-uppercase'>cirnac</span>), Canada Revenue Agency (CRA), Employment and Social Development Canada (ESDC), Department of Finance (<span class='text-uppercase'>fin</span>), Health Canada (HC), Immigration and Citizenship Canada (IRCC), Indigenous Services Canada (<span class='text-uppercase'>isc</span>), Public Health Agency of Canada (<span class='text-uppercase'>phac</span>), Public Services and Procurement Canada (PSPC), and Treasury Board of Canada Secretariat (TBS).</p>
    <p>Since web content changes frequently, the system uses search and downloads specific pages to answer questions, rather than pre-scraping web content. This AI system relies on information provided on GC websites.</p>
    <p>The AI Answers product team built a detailed agentic system (users interact with a specialized agent) prompt to make sure that answers are clear, concise, and helpful. We built in both human expert evaluation and AI scoring systems, with blocking of personal identifying information to protect user privacy.</p>"
%}

## Trial 1 results

### Participation  (June 18 to 26 and July 15 to 25, 2025)

Trial participation exceeded our expectations: 1,227 user sessions, spanning 32 departments, with questions covering 120+ government tasks. Tasks are what people come to the content to do: That can mean getting answers, like learning about a subject, or performing a transaction, like applying for a program.

The question distribution revealed user priorities:

* **42% (635 questions) on IRCC services:** immigration, work permits, and visas
* **25% (377 questions) on ESDC services:** My Service Canada Account sign in and registration, Employment Insurance (EI), Canada Pension Plan (CPP), and job searches
* **22% (332 questions) on CRA services:** account access, and tax and business questions

Even less-commonly used government services generated multiple questions per topic across many departments, suggesting broad user interest in AI-assisted government interactions.

{% include components/gc-complex-img.html
  alt="Screenshot of the AI Answers service page."
  file="/images/ai-answers/AI-answers.png"
  summary="Image description: AI Answers"
  content="<p>A screenshot of an AI Answers page on Canada.ca, showing a typical exchange between a user and the AI Answers service.</p>
          <p>The Canada.ca header, which displays the Government of Canada identifier, is at the top of the page. The page title is “AI Answers” followed by the text “Get answers to your Canada.ca questions.” Beneath this, a disclaimer states that answers provided by the AI service are for information only, not official advice, and that improvements are ongoing.</p>
          <p>A collapsible link labeled “Privacy and AI terms of use” appears below.</p>
          <p>A user-submitted question is shown in a light blue chat bubble.The question is:</p>
          <ul>
            <li>“I have direct deposit for my income tax refunds. However, OAS keeps sending me payments by cheque. They ask me to sign up for direct deposit. I wrote back saying I already have direct deposit, but the OAS cheques keep coming.”</li>
          </ul>
          <p>Below the question, an AI Answer’s response appears in a white panel.The response is:</p>
          <ul>
            <li>“Direct deposit information is not automatically shared between the CRA and OAS programs. To receive OAS payments by direct deposit, you need to sign up separately for OAS direct deposit. You can set up or change direct deposit for OAS using the instructions on the Government of Canada direct deposit page. After you sign up, it may take one or two payment cycles for direct deposit to begin.”</li>
          </ul>
          <p>Below the AI response, there is a disclaimer: “AI can make mistakes, always check your answer.”</p>
          <p>Below this, a section titled “Check your answer and take the next step” includes a link to a Canada.ca webpage about direct deposit for government payments.</p>
          <p>At the very bottom, a Chat ID is displayed as a string of letters and numbers.</p>"
%}

## Four key findings

**Accuracy that meets enterprise standards:** We achieved a 95% accuracy rate on English questions and 94% on French. This was verified through an expert evaluation of 800 trial questions, completed with GC departments and agency partners. This consistency across both official languages is rare in AI applications, where French typically shows 20% higher error rates.

**Users found genuine value:** 88% of user feedback was positive. Importantly, 22% of feedback respondents said they no longer needed to call government offices or visit in person, while 52% reported saving time on searching and reading.

**Unexpected breadth of use:** Despite launching from a sign-in page, 50% of questions were related to the top 20 government services identified in the [GC Task Success Survey](https://design.canada.ca/survey/). Users asked about a wide range of subjects, from work permits, to contributions to the Canada Pension Plan (CPP) benefits, to tax account access. This revealed a strong demand for AI help across the full spectrum of government services.

**Multilingual capability:** Beyond English and French, the system handled questions in 19 other languages, representing 8.4% of all queries. While accuracy was lower for these languages, we've since implemented translation and search improvements.

## Trial 2 results

### Participation  (October 22, 2025 to 12pm ET on November 7, 2025)

For trial 2, we expanded testing beyond the Sign-in page. The invitation was displayed to randomly-selected visitors on 12 Canada.ca pages: Sign in, All services, Contact, Change address, Departments, and GCkey help (in both English and French).

Over 16.5 days, this generated 2,866 questions in 1,983 user sessions, significantly more than Trial 1. The broader entry points brought a wider range of topics:

* **38% (1,111) on IRCC services:** immigration, work permits, and visa questions continued to dominate
* **18% (468) on ESDC services:** Employment Insurance (EI), Canada Pension Plan (CPP), and Service Canada account questions
* **14% (309) on CRA services:** tax accounts, business numbers, and filing questions
* **12% (462) about the AI Answers service itself:** users curious about how the tool works

Notably, 112 answers came from CBSA pages—90 of those specifically about the CBSA Assessment and Revenue Management (CARM). Answers were sourced across 60 different federal institutions.

### Trial 2 key findings

**Accuracy held steady at 95%:** Expert evaluation of 994 questions (35% of total, up from 13% in Trial 1) showed continued strong performance. Answer errors dropped from 6% to 5%. The proportion of "golden" answers (fully correct and useful) increased from 66% to 80.5%.

**Positive feedback remained high at 77%:** 21% of the people who responded with a thumbs-up ‘Yes’ to ‘Was this helpful?’ went on to respond that it saved them a call (11%) or a visit (10%).

**Budget 2025 tested real-time capability:** When Budget 2025 was announced on November 4, we added a custom Finance Canada scenario prompt within the hour. The team tested questions and refined URLs immediately after the Budget pages were launched. All public Budget questions asked about the announcement received clear, accurate answers, demonstrating the system can handle breaking government news.

**Enterprise breadth confirmed:** With answers sourced from 60 institutions, the trial confirmed this is genuinely an enterprise solution that works across the full scope of federal services.

### What we learned from Trial 2

**Multilingual questions work:** Trial 2 included scoring of 94 answers to questions asked and answered in 22 non-official languages. The score distribution was similar to the distribution for just English and French answers. This follows naturally since the AI Answers system translates the question into English in order to answer it, then translates back into the original language to display the answer. These scores confirmed the system's potential to serve Canadian and international visitors in the language of their choice.

**Users didn’t always answer clarifying questions:** Some users didn't appear to scroll down to answer clarifying questions the AI asked. We added a scroll indicator to signal there's more content below.

**Users want to know about AI Answers:** There were many questions about the system itself. After the trial, the Canada.ca Experience Office team added an [About AI Answers page](https://ai-answers.alpha.canada.ca/en/about) and enabled the AI Answers system to download and read it to answer questions about itself.

## Trial 3: Partner Beta

### Trial 3 participation (December 2, 2025 to January 9, 2026)

The first Beta trial was run in collaboration with four federal department partners. They placed banners on 112 Canada.ca English and French pages inviting visitors to beta-test AI Answers. Service Canada’s Principal Publisher team provided custom banners for this trial. Pages with the banner included:

* **Employment and Social Development Canada (ESDC):** All Employment Insurance pages
* **Treasury Board Secretariat (TBS):** Public service pay and pensions, and Working for the government pages
* **Indigenous Services Canada (ISC):** Indian Status pages
* **Health Canada (HC):** Flu and measles pages

Along with banner tests on the Canada.ca Contact page, this generated 3,222 questions, our largest trial yet. Partner team members evaluated at least 25% of questions related to their content during and after the trial ended.

Click-through rates to AI Answers varied by page type: the Contact page had the highest rate at 2.0%, while EI pages averaged 0.5% and health pages ranged from 0.03% to 0.04% of visitors trying the AI Answers beta test.

### Trial 3 key findings

**Accuracy reached 96.7%:** Expert and AI-assisted evaluation of a sample of 1,155 questions (36% of total) measured errors and accuracy.  English accuracy was 96.9% and French was 96.1%, maintaining the rare consistency across official languages that we've seen throughout testing.

**AI auto-evaluation scoring performance improved:** Accuracy analysis included 174 auto-evaluations of similar answers to similar questions.

**Partner evaluation revealed content insights:** Each partner discovered issues with their own web content through the evaluation process. ESDC found outdated information about how to submit forms to Service Canada and a content gap for employee Records of Employment. TBS discovered content gaps and instructions that weren't written in plain language.

**Positive feedback held at 65%:** Even with the shift to more complex partner topics, user satisfaction remained strong.

### What we learned from Trial 3

**Bottom banners outperform top banners:** Testing on the Contact page showed that bottom sticky banners achieved 2.0% click-through (201 clicks in 9,971 visits) compared to 0.8% for top banners (71 clicks in 8,772 visits), 2.5x more effective. Users appear more likely to try AI assistance after they've scanned the page content first. Banners will be positioned at the bottom of the page in future.

**Follow-up questions need work:** Questions asked as follow-ups in the same session were 2% more likely to contain errors. We're investigating causes and possible solutions.

**Citation specificity matters:** The most common "Needs improvement" feedback was that citations pointed to topic pages rather than the specific destination page users needed. Partners want more precise citation links.

**AI as a diagnostic tool:** Partners reported that the evaluation process itself was valuable. It revealed content problems their web communications teams hadn't noticed. Several teams began content improvement work based on issues AI Answers surfaced. As one insight noted: “AI Answers generated confusing responses when the source content was unclear, reinforcing the importance of regular website maintenance.”

## Why this matters

These trials demonstrate that enterprise-scale AI assistance can work across the full breadth of Government of Canada services, while maintaining accuracy and safety standards.

The product's **flexible, chat agent-based design** makes it scalable and ready for future AI needs.

More importantly, it shows we can meet users where they are by providing immediate, accurate assistance right on Canada.ca.

* This saves time and reduces the need for phone calls and office visits, allowing those service channels to focus on people's more complex service needs.
* For a digital government, that's not just a technical upgrade, but a meaningful service improvement for people using government services every day.

## Learn more

 As we work towards a wider roll-out in 2026, we hope that our work helps AI development teams across the public sector deploy safe and effective applications.

## Latest changes

{% include components/latest-changes.html  items=page.latestChanges %}
