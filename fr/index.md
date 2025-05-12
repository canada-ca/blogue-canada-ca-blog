---
altLangPage: /index
date: 2019-01-29
dateModified: 2021-05-10
description: Validations et perspectives de l’équipe Canada.ca.
layout: default
title: Blogue de Canada.ca
---

{%- assign locales = site.data.locales.index -%}
<p>{{ locales.intro[ page.language ] }}</p>

<h2 class="wb-inv">{{ locales.newest[ page.language ] }}</h2>
<div class="row wb-eqht-grd main-card mrgn-tp-lg">
{%- assign posts = site.posts | where: "language", page.language -%}
{%- if posts.size > 0 -%}
	{%- for post in posts limit:3 -%}
	<div class="col-md-4">
		<div class="hght-inhrt">
			<div class="hidden-xs hidden-sm">
				<img src="/images/thumbs/{{ post.date | date: "%F" }}.png" alt="{{ post.title }}" class="img-responsive mrgn-bttm-md thumbnail">
			</div>
			<h3><a href="{{ post.url | remove_first: '/' | remove_first: page.language }}" class="stretched-link">{{ post.title }}</a></h3>
			<p>{{ post.description }}</p>
			<p class="small"><time datetime="{{ post.date | date: "%F" }}" class="nowrap">[{% include locale-date.html date=post.date format="%-d %B %Y" %}]</time></p>
		</div>
	</div>
	{%- endfor -%}
{%- endif -%}
</div>
<h2>{{ locales.searchblog[ page.language ] }}</h2>
<div class="wb-filter">
	<section id="patterns" class="grouped">
		<ul class="list-unstyled">
			{%- for post in posts -%}
			<li>
				<h2 class="h3"><a href="{{ post.url | remove_first: '/' | remove_first: page.language }}">{{ post.title }}</a></h2>
				<p>{{ post.description }}</p>
				<p class="small"><time datetime="{{ post.date | date: "%F" }}" class="nowrap">[{% include locale-date.html date=post.date format="%-d %B %Y" %}]</time></p>
			</li>
			{%- endfor -%}
		</ul>
	</section>
</div>