---
altLangPage: /index
page: 2019-01-29
dateModified: 2021-03-19
description: Evidence and insights from the Canada.ca team.
layout: default
title: Canada.ca blog
---

{%- assign locales = site.data.locales.index -%}
<p>{{ locales.intro[ page.lang ] }}</p>
<section class="followus">
	<h2>{{ locales.followus[ page.lang ] }}</h2>
	<ul>
		<li><a href="{{ site.baseurl }}/{{ locales.feedurl[ page.lang ] }}" class="rss" rel="external"><span class="wb-inv">{{ locales.feed[ page.lang ] }}</span></a></li>
		<li><a href="{{ site.baseurl }}/pages/{{ locales.signupurl[ page.lang ] }}" class="email" rel="external"><span class="wb-inv">{{ locales.signup[ page.lang ] }}</span></a></li>
		<li><a href="https://twitter.com/{{ locales.twitterhandle[ page.lang ] }}" class="twitter" rel="external"><span class="wb-inv">Twitter</span></a></li>
	</ul>
</section>
<h2 class="wb-inv">{{ locales.newest[ page.lang ] }}</h2>
<div class="row wb-eqht-grd main-card mrgn-tp-lg">
{%- assign posts = site.posts | where: "lang", page.lang -%}
{%- if posts.size > 0 -%}
	{%- for post in posts limit:3 -%}
	<div class="col-md-4">
		<div class="hght-inhrt">
			<div class="hidden-xs hidden-sm">
				<img src="/images/thumbs/{{ post.date | date: "%F" }}.png" alt="{{ post.title }}" class="img-responsive mrgn-bttm-md thumbnail">
			</div>
			<h3><a href="{{ post.url | remove_first: '/' | remove_first: page.lang }}" class="stretched-link">{{ post.title }}</a></h3>
			<p>{{ post.description }}</p>
			<p class="small"><time datetime="{{ post.date | date: "%F" }}" class="nowrap">[{% include locale-date.html date=post.date format="%-d %B %Y" %}]</time></p>
		</div>
	</div>
	{%- endfor -%}
{%- endif -%}
</div>
<h2>{{ locales.searchblog[ page.lang ] }}</h2>
<div class="wb-filter">
	<section id="patterns" class="grouped">
		<ul class="list-unstyled">
			{%- for post in posts -%}
			<li>
				<h2 class="h3"><a href="{{ post.url | remove_first: '/' | remove_first: page.lang }}">{{ post.title }}</a></h2>
				<p>{{ post.description }}</p>
				<p class="small"><time datetime="{{ post.date | date: "%F" }}" class="nowrap">[{% include locale-date.html date=post.date format="%-d %B %Y" %}]</time></p>
			</li>
			{%- endfor -%}
		</ul>
	</section>
</div>