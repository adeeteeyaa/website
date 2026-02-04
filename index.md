---
layout: default
title: Home
---

Hi there and thank you for visiting my little spot on the internet! This website serves as a little window into who I am, what I do and what I think about.

Below you will find information about my education, work experience, publications, skillset and a little about things I do outside of work.

# Education
As of
{% assign day = site.time | date: "%-d" %} {% case day %} {% when '1' or '21' or '31' %}{{ day }}st {% when '2' or '22' %}{{ day }}nd {% when '3' or '23' %}{{ day }}rd {% else %}{{ day }}t {% endcase %} {{ site.time | date: " %B %Y" }},
 I have two degrees.
<div class="grid">
{% for item in site.data.education %}
  <div class="grid-item">
    <div class="grid-item-header">
      <div class="grid-item-logo">
        <img src="{{ item.logo }}" alt="{{ item.school }}">
      </div>
      <div class="grid-item-title">
        <h4>
          {% if item.url %}
            <a href="{{ item.url }}" class="stretched-link" target="_blank">{{ item.school }}</a>
          {% else %}
            {{ item.school }}
          {% endif %}
        </h4>
        <div class="grid-item-subtext">{{ item.degree }}</div>
        <div class="grid-item-subtext">{{ item.major }}</div>
        <div class="grid-item-subtext">
          <span><i class="fa-solid fa-location-dot"></i> {{ item.location }}</span>
          <span class="grid-item-subtext-divider">|</span>
          <span>{{ item.duration }}</span>
        </div>
      </div>
    </div>
  </div>
  {% endfor %}   
</div>

# Work
Professionally speaking, I have spent the last {% assign start_year = 2017 %}{% assign start_month = 8 %}{% assign start_day = 23 %}{% comment %} Get current date components as numbers {% endcomment %}{% assign current_year = "now" | date: "%Y" | plus: 0 %}{% assign current_month = "now" | date: "%m" | plus: 0 %}{% assign current_day = "now" | date: "%d" | plus: 0 %}{% comment %} Calculate raw year difference {% endcomment %}{% assign age = current_year | minus: start_year %} {% comment %} Subtract 1 if we haven't reached August 23rd yet this year {% endcomment %} {% if current_month < start_month %} {% assign age = age | minus: 1 %}{% elsif current_month == start_month and current_day < start_day %}{% assign age = age | minus: 1 %}{% endif %}{{ age }} years or so working closely on local and wide-area wireless communication systems - particularly Wi-Fi and 5G. While my job has always been in and around the Wi-Fi standard, I did complete a thesis in Virginia Tech focusing on the 3GPP 5G (and beyond) standard.
<div class="grid">
{% for item in site.data.work %}
  <div class="grid-item">
    <div class="grid-item-header">
      <div class="grid-item-logo">
        <img src="{{ item.logo }}" alt="{{ item.company }}">
      </div>
      <div class="grid-item-title">
        <h4>
          {% if item.url %}
            <a href="{{ item.url }}" class="stretched-link" target="_blank">{{ item.company }}</a>
          {% else %}
            {{ item.company }}
          {% endif %}
        </h4>
        <div class="grid-item-subtext">{{ item.designation }}</div>
        <div class="grid-item-subtext">
          <span><i class="fa-solid fa-location-dot"></i> {{ item.location }}</span>
          <span class="grid-item-subtext-divider">|</span>
          <span>{{ item.duration }}</span>
        </div>
      </div>
    </div>
    {% if item.body %}
        <div class="grid-item-body">
                <p>
                    {{ item.body | markdownify }}
                </p>
        </div>
    {% endif %}
  </div>
  {% endfor %}   
</div>

# Patents
<div class="grid">
{% for item in site.data.patents %}
  <div class="grid-item">
    <div class="grid-item-header">
      <div class="grid-item-title">
        <h4>
          {% if item.url %}
            <a href="{{ item.url }}" class="stretched-link" target="_blank">{{ item.title }}</a>
          {% else %}
            {{ item.title }}
          {% endif %}
        </h4>
        <div class="grid-item-subtext">{{ item.authors | markdownify }}</div>
        {% if item.patent-number and item.application-number %}
            <div class="grid-item-subtext"><i>
                <span>{{ item.patent-number }}, {{ item.application-number }}</span>
            </i></div>
        {% endif %}
        <div class="grid-item-subtext"><i>{{ item.publisher }}</i></div>
        <div class="grid-item-subtext"><i>{{ item.status }}</i></div>
      </div>
    </div>
  </div>
  {% endfor %}   
</div>

# Publications
<div class="grid">
{% for item in site.data.publications %}
  <div class="grid-item">
    <div class="grid-item-header">
      <div class="grid-item-title">
        <h4>
          {% if item.url %}
            <a href="{{ item.url }}" class="stretched-link" target="_blank">{{ item.title }}</a>
          {% else %}
            {{ item.title }}
          {% endif %}
        </h4>
        <div class="grid-item-subtext">{{ item.authors | markdownify }}</div>
        <div class="grid-item-subtext"><i>{{ item.publisher }}</i></div>
        <div class="grid-item-subtext"><i>{{ item.status }}</i></div>
      </div>
    </div>
  </div>
  {% endfor %}   
</div>

# Sides
When I'm not working, I like to spend a lot of time working on finding a way to organize my life, tinkering with software and hardware, working on cars and a little bit of photography and content creation with my wife.

# Life
Outside of work, I live in the city of San Jose in California, United States of America along with my wonderful wife.

# History
## 1996 to 2007: Al Ain
I was born in 1996 to two amazing dentists and raised in the United Arab Emirates (UAE) in a (at the time) tiny city called Al Ain, which was basically an oasis in the emirate of Abu Dhabi. Just like most cities in the UAE, Al Ain looks nothing like it did back in 1996-2007, the time that I lived there.