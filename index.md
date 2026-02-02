---
layout: default
title: Home
---

Hi there and thank you for visiting my little spot on the internet! This website serves as a little window into who I am, what I do and what I think about.

Below you will find information about my education, work experience, publications, skillset and a little about things I do outside of work.

# <i class="fa-solid fa-school"></i> Education
As of
{% assign day = site.time | date: "%-d" %} {% case day %} {% when '1' or '21' or '31' %}{{ day }}st {% when '2' or '22' %}{{ day }}nd {% when '3' or '23' %}{{ day }}rd {% else %}{{ day }}t {% endcase %} {{ site.time | date: " %B %Y" }},
 I have two degrees.
<div class="career-grid">
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/vt-logo.png" alt="Virginia Tech">
            </div>
            <div class="header-text">
                <h4>Virginia Tech</h4>
                <div class="experience-meta">Master of Science (with Thesis)</div>
                <div class="experience-meta">Computer Engineering</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Arlington, VA, USA</span>
                    <span class="meta-divider">|</span>
                    <span>Aug 2022 — Sept 2024</span>
                </div>
            </div>
        </div>
    </div>
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/nitk-logo.png" alt="NITK">
            </div>
            <div class="header-text">
                <h4>National Institute of Technology Karnataka</h4>
                <div class="experience-meta">Bachelor of Technology</div>
                <div class="experience-meta">Electrical and Electronics Engineering</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Surathkal, KA, India</span>
                    <span class="meta-divider">|</span>
                    <span>Aug 2022 — Sept 2024</span>
                </div>
            </div>
        </div>
    </div>    
</div>

# <i class="fa-solid fa-briefcase"></i> Work
Professionally speaking, I have spent the last {% assign start_year = 2017 %}{% assign start_month = 8 %}{% assign start_day = 23 %}{% comment %} Get current date components as numbers {% endcomment %}{% assign current_year = "now" | date: "%Y" | plus: 0 %}{% assign current_month = "now" | date: "%m" | plus: 0 %}{% assign current_day = "now" | date: "%d" | plus: 0 %}{% comment %} Calculate raw year difference {% endcomment %}{% assign age = current_year | minus: start_year %} {% comment %} Subtract 1 if we haven't reached August 23rd yet this year {% endcomment %} {% if current_month < start_month %} {% assign age = age | minus: 1 %}{% elsif current_month == start_month and current_day < start_day %}{% assign age = age | minus: 1 %}{% endif %}{{ age }} years or so working closely on local and wide-area wireless communication systems - particularly Wi-Fi and 5G. While my job has always been in and around the Wi-Fi standard, I did complete a thesis in Virginia Tech focusing on the 3GPP 5G (and beyond) standard.

<div class="career-grid">
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/qualcomm-logo.png" alt="Qualcomm">
            </div>
            <div class="header-text">
                <h4>Qualcomm</h4>
                <div class="experience-meta">Senior Engineer</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Santa Clara, CA, USA</span>
                    <span class="meta-divider">|</span>
                    <span>Oct 2024 — Present</span>
                </div>
            </div>
        </div>
        <div class="experience-body">
            <p>
                Wi-Fi 8 and EasyMesh software design, architecture and development - focusing on low-latency and ultra-reliable mobility in IEEE 802.11 wireless local-area networks
            </p>
        </div>
    </div>
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/qualcomm-logo.png" alt="Qualcomm">
            </div>
            <div class="header-text">
                <h4>Qualcomm</h4>
                <div class="experience-meta">Interim Engineering Intern</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Santa Clara, CA, USA</span>
                    <span class="meta-divider">|</span>
                    <span>May 2023 — July 2023</span>
                </div>
            </div>
        </div>
        <div class="experience-body">
            <p>Working on Wi-Fi 8 — focusing on the AP software design and architecture.</p>
        </div>
    </div>  
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/commonwealth-cyber-initiative-logo.png" alt="Commonwealth Cyber Initiative">
            </div>
            <div class="header-text">
                <h4>Commonwealth Cyber Initiative</h4>
                <div class="experience-meta">Graduate Researcher</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Arlington, VA, USA</span>
                    <span class="meta-divider">|</span>
                    <span>Aug 2022 — Sept 2024</span>
                </div>
            </div>
        </div>
        <div class="experience-body">
            <p><u>Focus 1:</u> Design and bringup of the entire CCI xG Testbed infrastructure - focusing on virtualized access to front-haul USRP software-defined radio grid for wireless communication experimentation</p>
            <p><u>Focus 2:</u> Research feasibility of large-scale experimentation platforms for unlicensed spectrum technologies (Wi-Fi, NR-U) in academic research</p>
        </div>
    </div>  
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/qualcomm-logo.png" alt="Qualcomm">
            </div>
            <div class="header-text">
                <h4>Qualcomm</h4>
                <div class="experience-meta">Associate Engineer > Engineer > Senior Engineer</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Bengaluru, KA, India</span>
                    <span class="meta-divider">|</span>
                    <span>Aug 2017 — June 2022</span>
                </div>
            </div>
        </div>
        <div class="experience-body">
            <p>Working on Wi-Fi 8 — focusing on the AP software design and architecture.</p>
        </div>
    </div>  
    <div class="experience-item">
        <div class="experience-header">
            <div class="company-logo">
                <img src="/public/career/iisc-logo.png" alt="Indian Institute of Science">
            </div>
            <div class="header-text">
                <h4>Indian Institute of Science</h4>
                <div class="experience-meta">Research Intern</div>
                <div class="experience-meta">
                    <span><i class="fa-solid fa-location-dot"></i> Bengaluru, KA, India</span>
                    <span class="meta-divider">|</span>
                    <span>May 2016 — August 2016</span>
                </div>
            </div>
        </div>
        <div class="experience-body">
            <p><u>Focus 1:</u> Study high-performance computer architecture for complex workloads</p>
            <p><u>Focus 2:</u> Research the fingerprinting of repetitive instruction flows in program execution using machine learning techniques</p>
        </div>
    </div>  
</div>

# <i class="fa-solid fa-newspaper"></i> Publications
<div class="pub-grid">
  <div class="pub-item">
    <div class="pub-content">
      <h4 class="pub-title">
        <a href="https://doi.org/..." target="_blank">High-Efficiency Wi-Fi 8 MAC Layer Optimizations for AP Architecture</a>
      </h4>
      <div class="pub-authors">
        <strong>Aditya Sathish</strong>, Shwetha Raghavendra Prasanna, et al.
      </div>
      <div class="pub-venue">
        IEEE International Conference on Communications (ICC), 2025
      </div>
    </div>
    <div class="pub-links">
      <a href="/public/papers/wifi8-paper.pdf" class="btn-pub"><i class="fa-solid fa-file-pdf"></i> Google Scholar</a>
      <!-- <a href="#" class="btn-pub"><i class="fa-solid fa-quote-left"></i> Cite</a> -->
    </div>
  </div>
  <div class="pub-item">
    <div class="pub-content">
      <h4 class="pub-title">
        <a href="https://doi.org/..." target="_blank">High-Efficiency Wi-Fi 8 MAC Layer Optimizations for AP Architecture</a>
      </h4>
      <div class="pub-authors">
        <strong>Aditya Sathish</strong>, Shwetha Raghavendra Prasanna, et al.
      </div>
      <div class="pub-venue">
        IEEE International Conference on Communications (ICC), 2025
      </div>
    </div>
    <div class="pub-links">
      <a href="/public/papers/wifi8-paper.pdf" class="btn-pub"><i class="fa-solid fa-file-pdf"></i> Google Scholar</a>
      <!-- <a href="#" class="btn-pub"><i class="fa-solid fa-quote-left"></i> Cite</a> -->
    </div>
  </div>
</div>


# <i class="fa-solid fa-sun"></i> Life
Outside of work, I live in the city of San Jose in California, United States of America along with my wonderful wife.

# History
## 1996 to 2007: Al Ain
I was born in 1996 to two amazing dentists and raised in the United Arab Emirates (UAE) in a (at the time) tiny city called Al Ain, which was basically an oasis in the emirate of Abu Dhabi. Just like most cities in the UAE, Al Ain looks nothing like it did back in 1996-2007, the time that I lived there.