"""Generates the static pages in ../site from shared header/footer partials."""
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"

NAV = [("index.html","Home"),("knowledge-hub.html","Knowledge Hub"),("jobs.html","Job Types"),
       ("services.html","Services"),("about.html","About Us"),("contact.html","Contact Us")]

LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="oklch(37% .075 178)"/><path d="M6 16.500L16 7l10 9.500" stroke="oklch(97.6% .009 88)" stroke-width="2.400" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.500 15v9h13v-9" fill="oklch(97.6% .009 88)"/><circle cx="16" cy="19.500" r="2.400" fill="oklch(60% .19 32)"/></svg>'

def icon(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
IC = {
 "clock":icon('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "home":icon('<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>'),
 "split":icon('<path d="M4 6h16M4 12h10M4 18h16"/>'),
 "shield":icon('<path d="M12 3l8 3v6c0 5-3.400 8-8 10-4.600-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>'),
 "doc":icon('<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
 "pen":icon('<path d="M4 20l4-1 11-11-3-3L5 16z"/>'),
 "brief":icon('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3"/>'),
 "chat":icon('<path d="M4 5h16v11H9l-5 4z"/>'),
}

def page(fname, title, desc, body, extra_head=""):
    nav = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    cur = ' aria-current="page"' if fname=="join.html" else ""
    html = f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1f5a4f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="index.html">{LOGO}Work<em>Nest</em> SG</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav-list" aria-label="Open menu"><span class="bars" aria-hidden="true"></span></button>
<ul id="nav-list">{nav}</ul>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{LOGO}Work<em>Nest</em> SG</a>
<p style="margin-top:1rem;max-width:32ch">Independent articles on Singapore careers, industries and skills, including part time job and work from home information.</p></div>
<div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="jobs.html">Job types</a></li><li><a href="knowledge-hub.html">Knowledge Hub</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="privacy.html">Privacy Policy</a></li><li><a href="disclaimer.html">Disclaimer</a></li></ul></div>
</div>
<div class="legal"><p>WorkNest SG is an information website. We are independent and not affiliated with any government agency. We do not recruit or place candidates or publish vacancies. Guides are general information, not legal advice; please confirm details with MOM or CPF Board. Scam helpline: <strong>1799</strong>.</p>
<p>&copy; 2026 WorkNest SG &middot; 22 Orchard Road, #03-01, Singapore 238885 &middot; +65 8396 3756 &middot; support@worknestsg.com</p></div>
</div></footer>
<script src="js/main.js"></script>
</body></html>'''
    (OUT/fname).write_text(html, encoding="utf-8")

def head(eyebrow, h1, lede=""):
    return f'<div class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{"<p class=lede>"+lede+"</p>" if lede else ""}</div></div>'

def svc(n,t,d): return f'<div class="type reveal"><span class="n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
IC.update({
 "book":icon('<path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 21V5"/>'),
 "laptop":icon('<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>'),
 "globe":icon('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 "wallet":icon('<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M3 10h18M16 15h2"/>'),
 "pen2":icon('<path d="M4 20l4-1 11-11-3-3L5 16z"/>'),
 "check":icon('<path d="M5 12l4 4 10-10"/>'),
 "x":icon('<path d="M6 6l12 12M18 6L6 18"/>'),
})

def jobtile(cls,ic,t,d,facts,href):
    return f'<a class="jt {cls} reveal" href="{href}"><span class="ic">{IC[ic]}</span><h3>{t}</h3><p>{d}</p><span class="facts">{facts}</span><span class="go">Read the guide &rarr;</span></a>'

KW = ["part time job","work from home jobs","work from home jobs Singapore","remote job Singapore","part time job Singapore","work from home in Singapore","make money at home","online jobs","online work from home","freelance jobs"]
kwul = "".join(f"<li>{k}</li>" for k in KW)

IMG={
"article-sectors-hiring.html":("sectors-hiring.jpg","Bar chart and city skyline illustrating sectors hiring in Singapore"),
"article-in-demand-roles.html":("in-demand-roles.jpg","Role cards for care, data and digital jobs"),
"article-why-second-income.html":("second-income.jpg","Two streams of coins merging, illustrating a side income"),
"article-remote-work-trend.html":("remote-growth.jpg","Rising line chart with a home office and city"),
"article-upskilling-2026.html":("upskilling.jpg","Steps with books and certificates, illustrating upskilling"),
"article-read-labour-data.html":("labour-data.jpg","Charts and magnifying glass illustrating labour data"),
"article-rising-costs.html":("rising-costs.jpg","Calculator, coins, house key and laptop on a desk, illustrating household costs and a side income"),
"article-childcare-caregiving.html":("childcare-caregiving.jpg","Parent and child at a table with a laptop, backpack and clock, illustrating work around family"),
"article-restart.html":("restart.jpg","A figure taking a first step on a path towards a sunrise over a city, illustrating restarting work"),
"article-work-modes.html":("work-modes.jpg","Icons for part-time, work from home, remote and freelance work connected together"),
"article-job-scams.html":("job-scams.jpg","Magnifying glass over a job listing with a checklist, shield and warning sign"),
"article-flexible-work-request.html":("flexible-work-request.jpg","Calendar, laptop and speech bubble illustrating a request for flexible work"),
"article-part-time-cpf.html":("part-time-cpf.jpg","Payslip, piggy bank and calculator illustrating checking contributions on a payslip"),
"article-read-job-ad.html":("read-job-ad.jpg","Job advertisement with highlighted phrases, magnifying glass and sticky notes"),
"article-remote-cv.html":("remote-cv.jpg","Laptop showing a CV with webcam, headset and coffee on a home desk"),
}
def thumb(href,lazy=True):
    if href not in IMG: return ""
    f,alt=IMG[href]
    return f'<a class="thumb" href="{href}" tabindex="-1" aria-hidden="true"><img src="img/{f}" alt="" width="1280" height="720"{" loading=\"lazy\"" if lazy else ""}></a>'
# ---------------- HOME
EXC={
"article-sectors-hiring.html":"Healthcare, technology, finance and logistics keep growing, while roles inside each are changing fast...",
"article-in-demand-roles.html":"Job titles change, but the skills employers keep asking for fall into clear groups...",
"article-why-second-income.html":"More people add a part time job or freelance work alongside their main role...",
"article-remote-work-trend.html":"Flexible work has moved from a perk to a standard conversation between employers and employees...",
"article-upskilling-2026.html":"Training only pays off when it connects to roles you can actually see advertised...",
"article-read-labour-data.html":"Unemployment, vacancies and wages each measure something different. The real story is in combining them...",
"article-rising-costs.html":"If every month feels tighter than the last, you are not imagining it...",
"article-childcare-caregiving.html":"The question is not whether you want to work, but whether the hours make sense...",
"article-restart.html":"Gaps in a CV are common, and a calm, simple explanation is usually enough...",
"article-remote-cv.html":"A remote employer cannot watch you work, so your CV must show you deliver independently...",
"article-flexible-work-request.html":"Treat your request as a proposal: describe the arrangement, show the work gets done...",
"article-part-time-cpf.html":"Part-time employees are still employees, and your payslip is the quickest place to check CPF...",
"article-work-modes.html":"Job ads mix up three ideas: hours, where you work, and your legal status...",
"article-read-job-ad.html":"Two job ads can look alike yet describe very different roles. The small print decides...",
"article-job-scams.html":"Scammers favour part-time and remote jobs because easy, flexible income is hard to resist...",
}
def card(href,label,t,d,m="5 min"):
    return f'<article class="post reveal">{thumb(href)}<div class="meta"><span class="cat">{label}</span><span>{m} read</span></div><h3><a href="{href}">{t}</a></h3><p>{EXC.get(href,d)}</p></article>'
def tile_s(href,t,d): return f'<a class="mini reveal" href="{href}"><b>{t}</b><span>{d}</span></a>'
page("index.html","Singapore Careers & Job Market Trends: Part Time Job, Work From Home Jobs | WorkNest SG",
"Independent Singapore career and industry publication: sectors hiring, in-demand roles, upskilling, and why a part time job, work from home jobs or freelance jobs are growing as a side income.",f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Singapore careers, industries and skills</span>
<h1>What is changing in Singapore's job market. <span>And what it means for your career.</span></h1>
<p class="lede">Articles on in-demand roles, hiring sectors and upskilling, plus why a part time job, work from home jobs or freelance jobs are becoming a common side income. Sourced from official publications and updated regularly.</p>
<div class="btn-row"><a class="btn btn-primary" href="knowledge-hub.html">Read more articles</a><a class="btn btn-ghost" href="#second-income">Why a side income</a></div>
</div>
<a class="lead-card" href="article-sectors-hiring.html"><img src="img/sectors-hiring.jpg" alt="" width="1280" height="720"><span class="cat">Lead story &middot; Industry trends</span><h2>Singapore Hiring Outlook: Sectors Driving Job Demand</h2><span class="go">Read the article &rarr;</span></a>
</div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">The big picture</span><h2>Four shifts shaping careers in Singapore.</h2></div>
<ol class="shifts">
<li class="reveal"><span class="no">01</span><h3>Sectors</h3><p>Care, technology, finance and logistics keep appearing in national reports.</p></li>
<li class="reveal"><span class="no">02</span><h3>Skills</h3><p>Employers increasingly describe roles by skills, not only job titles.</p></li>
<li class="reveal"><span class="no">03</span><h3>Flexibility</h3><p>Formal flexible work guidelines make remote and hybrid requests routine.</p></li>
<li class="reveal"><span class="no">04</span><h3>Side income</h3><p>Part-time, online and freelance work help many households close the gap.</p></li>
</ol>
<p class="src-note">Sources: Ministry of Manpower, Workforce Singapore, SkillsFuture Singapore.</p>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Latest reads</span><h2>Career paths, roles and skills.</h2></div>
<div class="posts">
{card("article-in-demand-roles.html","In-demand roles","In-Demand Roles in Singapore: Skills Employers Are Seeking","Care, data, digital, finance and operations: the skills behind the titles.")}
{card("article-why-second-income.html","Side income","The Rise of Side Income in Singapore: Trends and Considerations","A part time job, work from home or freelance work: why it keeps growing.")}
{card("article-upskilling-2026.html","Education &amp; skills","Upskilling in Singapore: Funding, Courses and Career Impact","SkillsFuture credits and short courses tied to real roles.")}
{card("article-remote-work-trend.html","Industry trends","Flexible Work in Singapore: The Shift Towards Remote and Hybrid Models","What national guidelines changed for remote job Singapore roles.")}
{card("article-read-labour-data.html","Career advice","Reading Singapore's Labour Market Data: A Practical Guide","Unemployment, vacancies and wages, explained.","4 min")}
{card("article-rising-costs.html","Life &amp; money","Cost of Living and Household Income: The Case for Flexible Work","How flexible work can help household budgets.")}
</div>
<p class="after-tiles"><a href="knowledge-hub.html">Read more &rarr;</a></p>
</div></section>

<section class="alt" id="second-income"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Side income</span><h2>Why part-time work is helping more people add a side income.</h2></div>
<div class="reveal"><p class="lede">With living costs up, many in Singapore pair their main job with a part time job Singapore employers offer, online work from home, or freelance jobs.</p>
<p>Flexible options such as work from home jobs Singapore, work from home in Singapore arrangements and remote job Singapore roles save commuting time. Many readers also ask how to make money at home through ordinary paid work. Pay depends on the role and hours, and is never guaranteed.</p>
<p><a href="article-why-second-income.html">Read the article &rarr;</a></p></div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Work types explained</span><h2>The six common ways people work flexibly.</h2></div>
<div class="minis">
{tile_s("part-time-jobs-singapore.html","Part time job","Under 35 hours a week")}
{tile_s("work-from-home-jobs-singapore.html","Work from home jobs","Agreed hours, at home")}
{tile_s("remote-jobs-singapore.html","Remote job Singapore","Location flexible")}
{tile_s("online-jobs-singapore.html","Online jobs","Flexible sessions")}
{tile_s("freelance-jobs-singapore.html","Freelance jobs","Paid per project")}
{tile_s("make-money-at-home-singapore.html","Earn from home","Routes compared")}
</div></div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Rights &amp; money</span><h2>Practical reads.</h2></div>
<div class="posts">
{card("article-flexible-work-request.html","Rights","Requesting Flexible Work: A Step-by-Step Guide","A step-by-step guide to a formal request.")}
{card("article-part-time-cpf.html","Rights","Part-Time Employment and CPF","Check your payslip.","4 min")}
{card("article-remote-cv.html","Career","Preparing a CV for Remote and Home-Based Roles","Show you can deliver independently.","4 min")}
</div></div></section>

<section id="contact-us"><div class="wrap split">
<div><span class="eyebrow">Contact</span><h2>Questions or topic suggestions?</h2><p class="lede">Send us a message. We read everything, and use your feedback to decide what to cover next.</p></div>
<div><form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send</button></form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Thank you for your message.</h3><p>Your email app should now be open with your message ready to send. Just press send when you are ready.</p><p class="ok-sub">If nothing opened, no worries. You can write to us at support@worknestsg.com and we will be glad to hear from you.</p></div></div>
</div></section>
''')

# ---------------- JOBS
GUIDE={k:f'<div class="btn-row"><a class="btn btn-primary" href="{v}">Read the full guide</a></div>' for k,v in {"part-time":"part-time-jobs-singapore.html","work-from-home":"work-from-home-jobs-singapore.html","remote":"remote-jobs-singapore.html","online":"online-jobs-singapore.html","freelance":"freelance-jobs-singapore.html"}.items()}
def jobsec(id_,alt,eyebrow,h2,intro,roles,suit,check):
    rl="".join(f"<li>{r}</li>" for r in roles)
    sl="".join(f"<li>{r}</li>" for r in suit)
    cl="".join(f"<li>{r}</li>" for r in check)
    return f'''<section id="{id_}"{' class="alt"' if alt else ''}><div class="wrap">
<div class="head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lede">{intro}</p></div>
<div class="cols3"><div><h3>Typical roles</h3><ul>{rl}</ul></div><div><h3>Suits you if</h3><ul>{sl}</ul></div><div><h3>Ask before you accept</h3><ul>{cl}</ul></div></div>
{GUIDE.get(id_,"")}</div></section>'''

jobs_body=head("Job types","Part-time, work from home, remote and freelance jobs in Singapore.","Explore the common kinds of flexible work in Singapore, what each involves, and what to check before you say yes.")
jobs_body+='''<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">At a glance</span><h2>Six job types compared.</h2><p class="lede">A quick summary. Details vary by employer, so always check the terms.</p></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Job type</th><th>Typical hours</th><th>Where</th><th>Usual status</th><th>CPF</th></tr></thead><tbody>
<tr><td><a href="#part-time">Part time job Singapore</a></td><td>Under 35 hrs a week</td><td>On-site or home</td><td>Employee</td><td>Generally applies*</td></tr>
<tr><td><a href="#work-from-home">Work from home jobs</a></td><td>Agreed hours</td><td>Home</td><td>Usually employee</td><td>Generally applies*</td></tr>
<tr><td><a href="#remote">Remote job Singapore</a></td><td>Full or part</td><td>Anywhere</td><td>Employee or contractor</td><td>Depends on status</td></tr>
<tr><td><a href="#online">Online jobs</a></td><td>Flexible slots</td><td>Online</td><td>Varies</td><td>Depends on status</td></tr>
<tr><td><a href="#freelance">Freelance jobs</a></td><td>You decide</td><td>Anywhere</td><td>Self-employed</td><td>You manage your own</td></tr>
<tr><td><a href="#contract">Contract and temp</a></td><td>Fixed term</td><td>Varies</td><td>Employee, often via agency</td><td>Generally applies*</td></tr>
</tbody></table></div><p class="notice">*For employees, subject to age, residency and pay. Check CPF Board for current rules. Earnings vary and are not guaranteed.</p></div></section>'''
jobs_body+=jobsec("part-time",False,"Part time job Singapore","Part time jobs in Singapore","Roles with fewer than 35 contracted hours a week, usually as an employee with a written contract.",
 ["Retail and F&amp;B service crew","Admin and office assistants","Tutors and education centre helpers","Event and promotion staff","Customer service associates"],
 ["You study, parent or care for family","You want a side income","You are returning to work gradually"],
 ["Weekly hours and shift pattern","How pay is calculated and paid","CPF and leave entitlements","Notice period"])
jobs_body+=jobsec("work-from-home",True,"Work from home jobs Singapore","Work from home jobs in Singapore","Roles you do from home with agreed hours, common for service and admin work. Work from home in Singapore does not have to mean freelancing.",
 ["Customer support by chat or email","Data entry and back-office admin","Virtual assistants","Content and social media support","Transcription and translation"],
 ["You need to be home for family","You want to save commute time and cost","You have a quiet space and reliable internet"],
 ["Is it an employee contract or freelance?","Who provides equipment?","Expected response times and hours","How performance is measured"])
jobs_body+=jobsec("remote",False,"Remote job Singapore","Remote jobs in Singapore","Roles where your location is flexible. Some are with Singapore companies, some are with overseas teams that need Singapore hours.",
 ["Digital marketing and SEO","Graphic and web design","Software and QA","Account and project management","Recruitment coordination"],
 ["You have specialist skills","You are self-directed","You are comfortable with written communication"],
 ["Which time zone and core hours","Who is the employer, and is it a Singapore entity?","Pay currency and payment method","Tax and CPF treatment"])
jobs_body+=jobsec("online",True,"Online jobs","Online jobs and online work from home","Work delivered entirely online, from live teaching to moderating and research. Legitimate online work is paid by a verifiable company for defined work.",
 ["Online tutoring","Community and chat moderation","Online research and data labelling","E-commerce listing and order support","Virtual event support"],
 ["You want flexible slots","You enjoy screen-based work","You can commit to reliable schedules"],
 ["Who pays you and when","Whether any equipment or registration fee is requested (a red flag)","Training provided","Trial-period terms"])
jobs_body+=jobsec("freelance",False,"Freelance jobs","Freelance jobs in Singapore","Project-based work where you are self-employed. You choose your clients but handle your own CPF contributions, tax and admin.",
 ["Design, illustration and branding","Copywriting and translation","Video and photo editing","Bookkeeping and admin support","Web and app development"],
 ["You want control of your schedule","You have a portfolio or specialist skill","You can manage irregular income"],
 ["Scope, deadlines and revision limits","Payment terms and deposits from the client","Contract for services in writing","Your own tax obligations"])
jobs_body+=jobsec("contract",True,"Contract and temp","Contract and temporary jobs","Fixed-term roles for project cover, seasonal peaks or maternity cover. A practical way to rebuild recent experience.",
 ["Admin and operations cover","Seasonal retail and logistics","Project coordinators","Customer service surge teams"],
 ["You want a defined end date","You are restarting after a break","You want to try a company or industry"],
 ["Contract length and renewal","Whether it is employed via an agency","Leave and CPF","Conversion to permanent"])
jobs_body+='''<section id="make-money-at-home"><div class="wrap"><div class="head"><span class="eyebrow">Earning from home</span><h2>Working from home: the main routes.</h2><p class="lede">People who want to make money at home usually choose a part-time job, freelance projects or contract work. Each is covered above. Earnings vary by role, skills and hours, and are never guaranteed.</p></div>
<div class="btn-row"><a class="btn btn-primary" href="make-money-at-home-singapore.html">Compare the routes</a><a class="btn btn-ghost" href="#part-time">Part-time jobs</a><a class="btn btn-ghost" href="article-work-modes.html">Read: what each term means</a></div></div></section>
<section class="alt" id="where-to-look"><div class="wrap"><div class="head"><span class="eyebrow">Where to look</span><h2>Find real openings through official channels.</h2><p class="lede">Current openings are posted on these trusted sources.</p></div>
<div class="types">
<div class="type"><span class="n">01</span><h3><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></h3><p>The government job portal, with filters and salary information.</p></div>
<div class="type"><span class="n">02</span><h3>Employer careers pages</h3><p>Apply directly on the official website of a company you have verified.</p></div>
<div class="type"><span class="n">03</span><h3><a href="https://www.mom.gov.sg" rel="noopener">MOM Employment Agency directory</a></h3><p>Confirm that any recruiter or agency holds a valid licence before you share details.</p></div>
</div></div></section>'''
page("jobs.html","Part Time, Work From Home, Remote & Freelance Jobs in Singapore | WorkNest SG",
"Guides to part time job Singapore, work from home jobs Singapore, remote job Singapore, online jobs, work from home in Singapore and freelance jobs: what to expect and what to ask.",jobs_body)

# ---------------- SERVICES
page("services.html","Services | Guides & Tools for Part Time and Work From Home Jobs | WorkNest SG","Free guides and tools for job seekers: part time job Singapore, work from home jobs, remote job Singapore, online jobs and freelance jobs, plus a weekly hours calculator.",
head("Services","What we publish.","Free articles, guides and tools on Singapore careers and flexible work, with no sign-up.")+f'''
<section><div class="wrap">
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["laptop"]}</div><h3>In-depth job type guides</h3><p>Roles, a sample week, how to start, and what to check on contracts, pay and CPF for six kinds of flexible work.</p><a class="more" href="jobs.html">Browse job types &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["wallet"]}</div><h3>Hours calculator</h3><p>Enter the extra income you want and an hourly rate to see roughly how many hours a week that needs.</p><a class="more" href="make-money-at-home-singapore.html">Work it out &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Knowledge Hub</h3><p>Articles on your rights, CPF, job ads, CVs and the cost of living.</p><a class="more" href="knowledge-hub.html">Read articles &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>Recruitment glossary</h3><p>PMET, CPF, JD, WFH, EP and more, in plain English.</p><a class="more" href="glossary.html">Search terms &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["globe"]}</div><h3>Where to look</h3><p>Links to official sources for current openings and your rights.</p><a class="more" href="jobs.html#where-to-look">See sources &rarr;</a></article>
</div></div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">Get in touch</span><h2>Questions or ideas?</h2><p>Tell us what you would like covered, or point out anything we should correct.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Contact Us</a></div></div>
</div></section>''')

# ---------------- KNOWLEDGE HUB
posts=[
("trends","Industry trends","article-sectors-hiring.html","Singapore Hiring Outlook: Sectors Driving Job Demand","The industries official labour reports keep pointing to, and what it means for your next move.","5 min",True),
("roles","In-demand roles","article-in-demand-roles.html","In-Demand Roles in Singapore: Skills Employers Are Seeking","Care, data, digital, finance and operations: the skills behind the titles.","5 min",False),
("second","Side income","article-why-second-income.html","The Rise of Side Income in Singapore: Trends and Considerations","Why part-time, online and freelance work keep growing.","5 min",False),
("trends","Industry trends","article-remote-work-trend.html","Flexible Work in Singapore: The Shift Towards Remote and Hybrid Models","How guidelines made flexible work requests normal.","4 min",False),
("edu","Education & skills","article-upskilling-2026.html","Upskilling in Singapore: Funding, Courses and Career Impact","SkillsFuture credits and short courses tied to real roles.","5 min",False),
("career","Career advice","article-read-labour-data.html","Reading Singapore's Labour Market Data: A Practical Guide","Unemployment, vacancies and wages, explained.","4 min",False),
("second","Side income","article-rising-costs.html","Cost of Living and Household Income: The Case for Flexible Work","How flexible work can help household budgets.","5 min",False),
("second","Side income","article-childcare-caregiving.html","Balancing Work and Caregiving: Costs and Options for Families","Options to explore before you decide.","5 min",False),
("career","Career advice","article-restart.html","Returning to Work After a Career Break: A Practical Approach","How to talk about gaps and take the first step.","5 min",False),
("career","Career advice","article-remote-cv.html","Preparing a CV for Remote and Home-Based Roles","Show you can deliver independently.","4 min",False),
("rights","Rights & money","article-flexible-work-request.html","Requesting Flexible Work: A Step-by-Step Guide","A step-by-step guide to a formal request.","5 min",False),
("rights","Rights & money","article-part-time-cpf.html","Part-Time Employment and CPF: What to Verify on Your Payslip","Is CPF actually being paid, and correctly?","4 min",False),
("career","Career advice","article-work-modes.html","Part-Time, Remote, Hybrid and Freelance Work: Key Definitions","The words in a job ad describe different things.","5 min",False),
("career","Career advice","article-read-job-ad.html","Reading Job Advertisements for Flexible Roles","The details that decide whether a role fits.","4 min",False),
("scam","Scams","article-job-scams.html","Recognising Fraudulent Remote Work Offers: Seven Warning Signs","How to spot fake offers.","6 min",False),
]
cards=""
for cat,label,href,t,d,m,feat in posts:
    body_=f'<div><div class="meta"><span class="cat">{label}</span><span>{m} read</span></div><h3><a href="{href}">{t}</a></h3><p>{EXC.get(href,d)}</p>{"<a class=\"btn btn-warm\" href=\""+href+"\">Read now</a>" if feat else ""}</div>'
    cards+=f'<article class="post{" feature" if feat else ""}" data-cat="{cat}">{thumb(href, not feat)}{body_}</article>'
page("knowledge-hub.html","Knowledge Hub | WorkNest SG","Articles on Singapore career paths, industry trends, in-demand roles, upskilling and part time job Singapore options.",
head("Knowledge Hub","Articles on Singapore careers, industries and skills.","Industry trends, in-demand roles, education and the rise of the side income, with sources.")+f'''
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" data-filter="all" aria-pressed="true">All</button>
<button class="chip" data-filter="trends" aria-pressed="false">Industry trends</button>
<button class="chip" data-filter="roles" aria-pressed="false">In-demand roles</button>
<button class="chip" data-filter="edu" aria-pressed="false">Education &amp; skills</button>
<button class="chip" data-filter="second" aria-pressed="false">Side income</button>
<button class="chip" data-filter="career" aria-pressed="false">Career advice</button>
<button class="chip" data-filter="rights" aria-pressed="false">Rights &amp; money</button>
<button class="chip" data-filter="scam" aria-pressed="false">Scams</button></div>
<div class="posts">{cards}</div></div></section>''')

# ---------------- ARTICLES
TAKE={}
EXTRA={}
SOURCES={}
def article(fname,title,desc,cat,body):
    tk=TAKE.get(fname)
    box=("<div class=\"takeaways\"><h2>Key takeaways</h2><ul>"+"".join(f"<li>{t}</li>" for t in tk)+"</ul></div>") if tk else ""
    body=body.replace("</p>","</p>"+box,1) if box else body
    ex=EXTRA.get(fname)
    if ex:
        body+="<h2>Common questions</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in ex[0])
        body+='<h2>Keep reading</h2><ul>'+"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in ex[1])+'</ul>'
    src=SOURCES.get(fname)
    if src:
        body+='<h2>Sources</h2><ul class="sources">'+"".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t,u in src)+'</ul>'
    body='<p class="byline">Last reviewed October 2026</p>'+body
    hero=""
    if fname in IMG:
        f,alt=IMG[fname]
        hero=f'<div class="wrap article"><figure class="hero-img"><img src="img/{f}" alt="{alt}" width="1280" height="720"></figure></div>'
    page(fname,title+" | WorkNest SG",desc,f'''{head(cat,title)}
{hero}<section style="padding-top:2rem"><div class="wrap article">{body}
<p style="margin-top:2.5rem"><a href="knowledge-hub.html">&larr; Back to Knowledge Hub</a></p></div></section>''')


EXTRA.update({
"article-job-scams.html":([("What should I do if I already replied?","Stop replying, do not send money, keep screenshots and speak to your bank. Call the ScamShield helpline on 1799 for advice."),("How can I check a job is real?","Look for the role on the company's own website or MyCareersFuture, and contact the company using details you found yourself.")],[("part-time-jobs-singapore.html","Part time job guide"),("online-jobs-singapore.html","Online jobs guide"),("scam-check.html","Scam checker")]),
"article-work-modes.html":([("Is part-time the same as freelance?","No. Part-time employees have a contract of service and are employees. Freelancers are self-employed."),("Can a job be both remote and part-time?","Yes. Hours and location are separate. A role can be part-time and remote, or full-time and on-site.")],[("part-time-jobs-singapore.html","Part time job guide"),("remote-jobs-singapore.html","Remote jobs guide"),("freelance-jobs-singapore.html","Freelance jobs guide")]),
"article-rising-costs.html":([("How many hours would I need for a meaningful side income?","It depends on the rate and your target. Try our <a href='make-money-at-home-singapore.html'>hours calculator</a>."),("Is a side income taxable?","Income from employment and freelance work is generally taxable and must be declared. Check IRAS.")],[("make-money-at-home-singapore.html","Make money at home"),("part-time-jobs-singapore.html","Part time job guide"),("article-part-time-cpf.html","Part-Time Employment and CPF")]),
"article-childcare-caregiving.html":([("Are there jobs that fit school hours?","Some part-time and work from home roles offer hours that work around school. Ask early about flexibility."),("Can I ask my current employer for changed hours?","You can make a formal flexible work request. See our guide on how to do it.")],[("article-flexible-work-request.html","How to ask for flexible work"),("work-from-home-jobs-singapore.html","Work from home jobs guide"),("part-time-jobs-singapore.html","Part time job guide")]),
"article-restart.html":([("How long a gap is too long?","There is no fixed limit. Employers care more about what you can do now and how you explain the gap."),("Should I take part-time work first?","Part-time or contract work can help rebuild confidence and recent experience, and many people use it as a first step.")],[("part-time-jobs-singapore.html","Part time job guide"),("article-remote-cv.html","A CV for remote roles"),("article-read-job-ad.html","How to read a job ad")]),
"article-flexible-work-request.html":([("Can my employer say no?","Yes. Employers can decline a request but are expected to give reasons in writing. See the MOM guidelines."),("Should I offer a trial?","A trial period with a review date can make it easier for an employer to say yes.")],[("article-work-modes.html","What each work mode means"),("work-from-home-jobs-singapore.html","Work from home jobs guide"),("remote-jobs-singapore.html","Remote jobs guide")]),
"article-part-time-cpf.html":([("Do part-time workers get an itemised payslip?","Employees should receive an itemised payslip. Check MOM for the current requirements."),("Do freelancers get CPF from clients?","No. Freelancers are self-employed. Check CPF Board for MediSave obligations.")],[("part-time-jobs-singapore.html","Part time job guide"),("freelance-jobs-singapore.html","Freelance jobs guide"),("glossary.html","Glossary")]),
"article-read-job-ad.html":([("What does 'up to' salary mean?","It is the top of the range, not a guaranteed amount. Ask what most people in the role are paid."),("What is a probation period?","An initial trial period after you start, during which the notice period may differ. Check your contract.")],[("glossary.html","Glossary"),("part-time-jobs-singapore.html","Part time job guide"),("article-part-time-cpf.html","Part-Time Employment and CPF")]),
"article-remote-cv.html":([("Should I mention my time zone?","Yes. State your location, hours and any overlap you can commit to."),("Do I need a portfolio?","A small portfolio helps for creative, technical and content roles, but it is not required for every job.")],[("remote-jobs-singapore.html","Remote jobs guide"),("work-from-home-jobs-singapore.html","Work from home jobs guide"),("online-jobs-singapore.html","Online jobs guide")]),
})

TAKE.update({
"article-job-scams.html":["Genuine employers do not ask you to pay to start work.","Be careful with unsolicited chat-app offers and pay that seems too good.","Verify the company and the listing on official sources.","Never share Singpass, OTP or bank logins. Call 1799 if unsure."],
"article-work-modes.html":["Hours, place and status are three different things in a job ad.","Part-time in Singapore means fewer than 35 contracted hours a week.","Freelancers manage their own CPF and tax.","Ask about hours, pay basis, CPF, contract type and notice period."],
"article-rising-costs.html":["Part-time, remote or freelance work are common ways to add income.","Compare take-home pay with extra costs like transport and childcare.","Ask how and when you are paid.","Check government support schemes if money is very tight."],
"article-childcare-caregiving.html":["Start with the hours you can truly commit.","Ask about flexibility before accepting.","Subtract childcare and work costs from expected pay.","You can revisit your decision as circumstances change."],
"article-restart.html":["Career gaps are common and easier to explain than people expect.","Keep the explanation short and honest.","Part-time or contract work can be a gentle restart.","Refresh your CV, references and skills."],
})
article("article-job-scams.html","Recognising Fraudulent Remote Work Offers: Seven Warning Signs","How to recognise fake remote and part-time job offers in Singapore.","Scams",'''
<p class="lede">Scammers favour part-time and remote jobs because the promise of easy, flexible income is hard to resist. These are the patterns to look for.</p>
<h2>1. You did not apply</h2><p>An unsolicited WhatsApp, Telegram or SMS offering a job is a major red flag. Legitimate employers rarely cold-message strangers with pay figures.</p>
<h2>2. Pay is too good for the work</h2><p>Hundreds of dollars a day to "like" videos, boost ratings or complete simple tasks does not match how real businesses pay.</p>
<h2>3. You must pay first</h2><p>Deposits, "training fees", equipment costs or topping up an account to "unlock" tasks are how the scam takes your money.</p>
<h2>4. The interview happens only on a chat app</h2><p>No company email, no video call, no named hiring manager, and no verifiable business in ACRA records.</p>
<h2>5. Pressure and secrecy</h2><p>"Reply in one hour", "do not tell anyone" and "limited slots" are designed to stop you from checking.</p>
<h2>6. They ask for sensitive details</h2><p>Never share Singpass, OTPs, banking logins or a full NRIC photo before a verified offer. Your bank account may be misused for money mule activity.</p>
<h2>7. The job is not on official channels</h2><p>Check whether the employer and role appear on MyCareersFuture or the company's official website.</p>
<div class="callout"><p><strong>If you have engaged:</strong> stop all payments, keep screenshots, call your bank, and contact the Police. For advice, call the ScamShield helpline at 1799. Try our <a href="scam-check.html">scam checker</a>.</p></div>''')

article("article-work-modes.html","Part-Time, Remote, Hybrid and Freelance Work: Key Definitions","Definitions of common flexible work terms in Singapore.","Basics",'''
<p class="lede">Job ads mix up three separate ideas: how many hours you work, where you work, and your legal status. Untangling them is the first step.</p>
<h2>Hours: part-time vs full-time</h2><p>Under Singapore's Part-Time Employment Regulations, a part-time employee is contracted to work fewer than 35 hours a week. Part-timers are still employees with a contract, and many protections apply on a pro-rated basis. Check MOM for the current rules.</p>
<h2>Place: remote, hybrid, on-site</h2><ul><li><strong>Remote / WFH:</strong> you work away from the employer's premises, often from home.</li><li><strong>Hybrid:</strong> a mix. Ask how many office days are required and whether they are fixed.</li><li><strong>On-site:</strong> you work at a workplace or client location.</li></ul>
<h2>Status: employee, contractor, platform worker</h2><p>Employees have a contract of service. Freelancers and contractors have a contract for services and arrange their own CPF and taxes. Platform workers, such as ride-hail and delivery workers, have their own framework under the Platform Workers Act.</p>
<div class="callout"><p>Questions to ask any employer: Is this an employment contract? What are my weekly hours? How is pay calculated? Is CPF payable? What is the notice period?</p></div>
<p>Unsure about a term? Search our <a href="glossary.html">glossary</a>.</p>''')


article("article-rising-costs.html","Cost of Living and Household Income: The Case for Flexible Work","How flexible work can ease cost-of-living pressure in Singapore.","Life & Money",'''
<p class="lede">If every month feels tighter than the last, you are not imagining it, and you are not alone. Housing, groceries, transport and family costs weigh on many households here.</p>
<h2>Why a side income can help</h2><p>You may not be able to change your rent, but you may be able to change your income. Part-time, remote or contract work can add to what you earn without demanding a rigid full-time schedule.</p>
<h2>Choose the arrangement that suits your budget</h2><ul><li><strong>Part-time:</strong> predictable hours, usually as an employee with a contract.</li><li><strong>Remote or hybrid:</strong> fewer commuting hours and costs.</li><li><strong>Freelance or contract:</strong> can pay more per hour but less predictable, and you handle your own CPF and tax.</li></ul>
<h2>Look at the whole picture</h2><p>Compare the take-home pay against the extra costs: transport, meals out and childcare. Ask how pay is calculated and how often you are paid.</p>
<div class="callout"><p>If money is very tight, also explore government support. SupportGoWhere (supportgowhere.gov.sg) lists schemes you may qualify for. Beware of anyone promising fast money for an upfront fee.</p></div>
<p>Explore flexible options in our <a href="jobs.html">job types guide</a>.</p>''')

article("article-childcare-caregiving.html","Balancing Work and Caregiving: Costs and Options for Families","Weighing work against childcare and caregiving in Singapore.","Life & Money",'''
<p class="lede">For many parents and caregivers the question is not whether you want to work, but whether the numbers and the hours make sense.</p>
<h2>Start with your real hours</h2><p>Write down the hours you can truly commit each week, including the school run, meals and appointments. A role that fits those hours is worth more than a higher rate that does not.</p>
<h2>Ask about flexibility early</h2><ul><li>Are hours fixed or can you choose slots?</li><li>Can some work be done from home?</li><li>What happens if a child or parent falls ill?</li></ul>
<h2>Do the sums honestly</h2><p>Subtract childcare, transport and other work-related costs from your expected pay. Sometimes fewer hours in a well-matched role beats more hours in a stressful one.</p>
<h2>Be kind to yourself</h2><p>Choosing to work part-time, or to pause, is not a failure. It is a decision you can revisit as your family changes.</p>
<p>Explore roles with flexible hours in our <a href="jobs.html">job types guide</a>.</p>''')

article("article-restart.html","Returning to Work After a Career Break: A Practical Approach","Restarting work after a career gap in Singapore.","Life & Money",'''
<p class="lede">Gaps in a CV are common: caring for family, retrenchment, health, study or simply needing a rest. Employers see them more often than you might fear.</p>
<h2>Say it simply and honestly</h2><p>One or two calm sentences are enough: what happened, what you learned or did during that time, and what you want next.</p>
<h2>Restart small</h2><p>Part-time or contract work can rebuild confidence, references and recent experience without the pressure of jumping straight back to full time.</p>
<h2>Freshen your profile</h2><ul><li>Update your CV with recent skills, courses or volunteering.</li><li>Ask a former colleague for a short reference.</li><li>Look into SkillsFuture options to top up relevant skills.</li></ul>
<div class="callout"><p>Take the first step at a pace that feels right. There is no deadline on starting again.</p></div>
<p>See our <a href="jobs.html">job types guide</a> for a gentle place to start.</p>''')

# ---------------- SCAM CHECK
flags=["I was contacted first, on WhatsApp, Telegram, WeChat or SMS, without applying.",
"The pay is very high for simple tasks (liking, rating, boosting, data entry).",
"I was asked to pay a fee, deposit or top up an account.",
"There is no company email, website or verifiable business registration.",
"I am being rushed or told to keep it secret.",
"They asked for Singpass, OTP, banking details or full NRIC copies early on.",
"The interview was text-only, or I was asked to lend or open a bank account."]
lis="".join(f'<li><label><input type="checkbox"> <span>{f}</span></label></li>' for f in flags)
page("scam-check.html","Job Scam Checker | WorkNest SG","Tick the red flags in a job offer and get guidance.",
head("Scam Check","Does this offer look off?","Tick anything that matches. Nothing is stored or sent anywhere.")+f'''
<section><div class="wrap split">
<div><ul class="check" id="scam-check">{lis}</ul>
<div class="result" id="scam-result" hidden role="status" aria-live="polite"><h3></h3><p></p></div></div>
<div><h2>Verify, do not trust.</h2><ol>
<li>Look up the company in ACRA's business records.</li>
<li>Search for the role on MyCareersFuture or the company's own site.</li>
<li>Contact the company using details you found yourself.</li>
<li>Install the ScamShield app to filter scam SMS and calls.</li></ol>
<div class="callout"><p>Lost money or shared bank details? Call your bank immediately and report to the Police. For advice, call <strong>1799</strong>.</p></div>
<p class="notice">This checker is indicative only. A clean result does not guarantee an offer is genuine.</p></div>
</div></section>''')

# ---------------- GLOSSARY
terms=[("Base pay","The fixed part of your pay, before commission, bonuses or allowances."),
("Commission-only","Pay depends entirely on results, with no guaranteed base."),
("Ad hoc","One-off or irregular work, with no commitment on either side."),
("Retainer","A regular fee paid to a freelancer to stay available for an agreed amount of work."),
("Flexi-hours","Flexible start and end times, often around core hours."),
("FWA","Flexible work arrangement: flexi-time, flexi-place or flexi-load."),
("Core hours","Hours when you must be available, even in flexible or remote roles."),
("Hybrid","A schedule that splits time between office and remote work."),
("Freelancer","Self-employed person paid per project or task, responsible for own tax and contributions."),
("Platform worker","Person who gets work via an online platform, such as ride-hail or delivery."),
("Gig","A short-term, task-based job."),
("Contract / temp","Fixed-term employment, sometimes through an agency."),
("Probation","Initial trial period at the start of employment."),
("Notice period","Time you or your employer must give before ending employment."),
("Training bond","An agreement to stay for a set period after training, or repay costs."),
("PMET","Professionals, Managers, Executives and Technicians."),
("Money mule","Person whose bank account is used to move scam proceeds, often unknowingly. It is a criminal offence.")]
tl="".join(f'<div class="term"><dt>{a}</dt><dd>{b}</dd></div>' for a,b in terms)
page("glossary.html","Singapore Recruitment Glossary | WorkNest SG","Definitions of Singapore recruitment, part-time, remote and hybrid work keywords.",
head("Glossary","Job-ad terms, explained.")+f'''
<section><div class="wrap" style="max-width:860px">
<label for="glossary-search" class="eyebrow">Search terms</label>
<input id="glossary-search" class="search" type="search" placeholder="Try &quot;CPF&quot; or &quot;hybrid&quot;" autocomplete="off">
<dl class="glossary">{tl}</dl><p id="glossary-empty" hidden>No matches. <a href="contact.html">Ask us to add it.</a></p></div></section>''')

# ---------------- FAQ
faqs=[("Does WorkNest SG list jobs?","We share information about job types in Singapore. For current openings, see MyCareersFuture and employers' own careers pages."),
("Is WorkNest SG free?","Yes. All guides and tools are free to read with no sign-up. Never pay anyone to get a job."),
("How do I find a part time job in Singapore?","Search official channels such as MyCareersFuture and employers' own careers pages. Our part-time guide lists what to ask before you accept."),
("Are there genuine work from home jobs in Singapore?","Yes. Customer support, admin, content and many specialist roles can be done from home. Genuine employers pay you for defined work and never ask you to pay to start."),
("How can I make money at home?","Most people do it through ordinary jobs done from home: part-time employment, freelance projects or contract work. Earnings vary by role, skills and hours, and are not guaranteed."),
("What is the difference between remote and work from home?","Work from home usually means working from home on agreed hours. Remote means location flexibility, sometimes with an overseas team. Ask which applies."),
("Are online jobs real?","Many are, such as online tutoring, moderation or support. Check who pays you, get terms in writing and never pay a fee to get started."),
("What are freelance jobs and do they include CPF?","Freelancers are self-employed. You choose your clients and manage your own CPF contributions, tax and admin. See CPF Board and IRAS for current rules."),
("Can I request remote or hybrid work from my employer?","Employees can submit a formal flexible work arrangement request and employers are expected to consider it fairly under national guidelines. Approval is not guaranteed."),
("How do I check that a recruiter is licensed?","Search the Employment Agency directory on the MOM website before sharing personal details.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html","FAQ | Part Time & Work From Home Jobs in Singapore | WorkNest SG","Answers about part time job Singapore, work from home jobs, remote jobs, online work, freelance jobs and how to make money at home.",
head("FAQ","Quick answers.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Still stuck? <a href="contact.html">Contact us</a>.</p></div></section>')

# ---------------- ABOUT
page("about.html","About Us | WorkNest SG","WorkNest SG shares practical, sourced information on part time job Singapore, work from home jobs, remote job Singapore, online jobs and freelance jobs.",
head("About Us","Information on flexible work in Singapore.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>Who this is for</h2><p>WorkNest SG is an independent publication on Singapore career paths, industry trends and skills. It is for anyone planning their next move, or looking at a part time job, work from home in Singapore, online work or freelance jobs as a side income. We are not affiliated with any government agency.</p>
<p>You have limited hours, real bills and no time to sift through jargon. So each guide tells you what the work involves, what it usually looks like week to week, and what to check before you agree to anything.</p></div>
<div class="reveal"><h2>How we write our guides</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>From your point of view</h3><p>Every guide answers the questions a job seeker asks: hours, pay basis, CPF, contract and how to start.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Checked against official sources</h3><p>We link to MOM, CPF Board, IRAS and MyCareersFuture so you can confirm details yourself.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Reviewed and dated</h3><p>Guides show when they were last reviewed, so you know how current they are.</p></div></div></div></div>
</div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">What you will find</span><h2>Articles, job type guides and tools.</h2></div>
<div class="btn-row"><a class="btn btn-primary" href="jobs.html">Browse job types</a><a class="btn btn-ghost" href="knowledge-hub.html">Knowledge Hub</a></div></div></section>
<section><div class="wrap"><p class="notice" style="max-width:70ch">WorkNest SG shares general information about jobs in Singapore. It is not legal, financial or employment advice. Find us at 22 Orchard Road, #03-01, Singapore 238885.</p></div></section>''')

# ---------------- CONTACT
page("contact.html","Contact Us | WorkNest SG","Contact WorkNest SG with a question, correction or topic suggestion about part time job Singapore, work from home jobs and remote work.",
head("Contact Us","Questions, corrections or topic ideas?","Send us a question, a correction or an idea for a guide. We read every message. Please do not include NRIC, bank or Singpass details.")+f'''
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>A question about part time jobs</option><option>A question about work from home or remote jobs</option><option>Online jobs or freelance work</option><option>Report a problem or concern</option><option>Suggest an article</option><option>Correction or feedback</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send</button>
<p class="notice">Sending opens your email app with your message ready to send to support@worknestsg.com.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Thank you for your message.</h3><p>Your email app should now be open with your message ready to send. Just press send when you are ready.</p><p class="ok-sub">If nothing opened, no worries. You can write to us at support@worknestsg.com and we will be glad to hear from you.</p></div>
</div>
<div><h2>Other ways</h2><ul class="contact-list">
<li><b>Email</b>support@worknestsg.com</li>
<li><b>Phone</b>+65 8396 3756</li>
<li><b>Address</b>22 Orchard Road, #03-01, Singapore 238885</li>
</ul></div>
</div></section>''')



# ---------------- DISCLAIMER
page("disclaimer.html","Disclaimer | WorkNest SG","Disclaimer for WorkNest SG, an information website about part time, work from home, remote and freelance work in Singapore.",
head("Disclaimer","Disclaimer")+'''
<section><div class="wrap article">
<h2>Information only</h2><p>WorkNest SG publishes general information about part-time, work from home, remote, online, freelance and contract work in Singapore. We are not an employment agency, we do not publish job vacancies, and we do not recruit, screen, place or introduce candidates.</p>
<h2>No earnings or job guarantees</h2><p>Nothing on this site promises employment or a level of income. Pay, hours and conditions differ between employers and roles, and change over time.</p>
<h2>Not professional advice</h2><p>Content is not legal, financial, tax or employment advice. Rules on CPF, employment terms and flexible work can change. Please confirm details with the Ministry of Manpower, CPF Board, IRAS or a qualified professional.</p>
<h2>Third-party links</h2><p>We link to official and third-party websites for reference. We do not control their content and are not responsible for it.</p>
<h2>Accuracy</h2><p>We aim to keep information accurate and up to date, but we cannot guarantee that every detail is current. If you spot an error, please <a href="contact.html">contact us</a>.</p>
</div></section>''')

# ---------------- PRIVACY
page("privacy.html","Privacy Policy | WorkNest SG","How WorkNest SG collects, uses, discloses and protects personal data in accordance with Singapore's Personal Data Protection Act 2012 (PDPA).",
head("Privacy Policy","Privacy Policy","Last updated: 1 October 2026")+'''
<section><div class="wrap article">
<p>WorkNest SG ("we", "us", "our") respects your privacy and is committed to protecting your personal data in accordance with Singapore's Personal Data Protection Act 2012 ("PDPA"). This policy explains how we collect, use, disclose and protect personal data when you use this website.</p>
<p>By using this website or submitting your personal data to us, you acknowledge that you have read and understood this policy.</p>

<h2>1. Who we are</h2>
<p>WorkNest SG is an independent information website on Singapore careers, industries and skills. We publish articles and tools only. We are not an employment agency, we do not publish job vacancies, and we do not recruit, screen or place candidates.</p>

<h2>2. Personal data we collect</h2>
<p>We collect personal data only when you choose to give it to us, for example when you send a message through our contact form or email us. This may include:</p>
<ul><li>your name;</li><li>your email address;</li><li>the contents of your message, and any other information you choose to include.</li></ul>
<p>Please do not send sensitive information such as your NRIC number, Singpass details, OTPs, bank account details or passwords. We will never ask for them.</p>
<p>The hours calculator and the scam checker run entirely in your browser. The information you enter into them is not sent to us or stored.</p>

<h2>3. Technical data</h2>
<p>Our web server may automatically log standard technical information such as your IP address, browser type and the pages requested, for security and to keep the site running.</p>

<h2>4. How we use your personal data</h2>
<p>We use your personal data only for the following purposes:</p>
<ul><li>to respond to your questions, feedback or correction requests;</li><li>to consider topic suggestions you send us;</li><li>to maintain the security and proper functioning of this website;</li><li>to comply with applicable laws and regulatory requirements.</li></ul>
<p>We do not use your personal data for direct marketing unless you have given us your consent. We do not sell your personal data.</p>

<h2>5. Disclosure of personal data</h2>
<p>We do not disclose your personal data to third parties except:</p>
<ul><li>to service providers who help us operate the website and handle email, and who are required to protect your data;</li><li>where required or authorised by law, such as by a court order or a regulatory or law enforcement authority;</li><li>with your consent.</li></ul>

<h2>6. Transfer of personal data outside Singapore</h2>
<p>Some of our service providers may store or process data outside Singapore. Where this happens, we take reasonable steps to ensure that your personal data receives a standard of protection comparable to that required under the PDPA.</p>

<h2>7. Protection and retention</h2>
<p>We take reasonable security measures to protect personal data in our possession against unauthorised access, collection, use, disclosure, copying, modification or disposal. No method of transmission over the internet is completely secure, so we cannot guarantee absolute security.</p>
<p>We keep your personal data only as long as it is needed for the purposes in section 4 or as required by law. When it is no longer needed, we delete it or anonymise it.</p>

<h2>8. Your rights</h2>
<p>Under the PDPA you may:</p>
<ul><li>ask for access to the personal data we hold about you, and information on how it has been used or disclosed in the past year;</li><li>ask us to correct personal data that is inaccurate or incomplete;</li><li>withdraw your consent to our collection, use or disclosure of your personal data.</li></ul>
<p>To make a request, email our Data Protection Officer at the address below. We may need to verify your identity first, and we will respond within a reasonable time. If you withdraw consent, we will explain the likely consequences, and we may not be able to continue to deal with your enquiry.</p>

<h2>9. Third-party websites</h2>
<p>Our articles may link to websites run by others, including government agencies. We are not responsible for their privacy practices. Please read their policies before giving them your personal data.</p>

<h2>10. Children</h2>
<p>This website is intended for a general audience and is not directed at children. If you believe a child has given us personal data, please contact us and we will delete it.</p>

<h2>11. Changes to this policy</h2>
<p>We may update this policy from time to time. The latest version will always be on this page, with the date it was last updated.</p>

<h2>12. Contact our Data Protection Officer</h2>
<p>If you have questions, a request or a complaint about how we handle personal data, please contact:</p>
<ul><li><strong>Data Protection Officer, WorkNest SG</strong></li><li>Email: support@worknestsg.com</li><li>Phone: +65 8396 3756</li><li>Address: 22 Orchard Road, #03-01, Singapore 238885</li></ul>
<p>If you are not satisfied with our response, you may contact the Personal Data Protection Commission at <a href="https://www.pdpc.gov.sg" rel="noopener">www.pdpc.gov.sg</a>.</p>
</div></section>''')

# ---------------- THANK YOU
page("thank-you.html","Thank You | WorkNest SG","Thank you for contacting WorkNest SG.",
head("Thank you","Thanks for getting in touch.","We have received your message and will reply by email as soon as we can.")+'''
<section><div class="wrap" style="max-width:720px">
<p>In the meantime, you are welcome to keep reading our latest articles on Singapore careers, industries and skills.</p>
<div class="btn-row"><a class="btn btn-primary" href="knowledge-hub.html">Read more articles</a><a class="btn btn-ghost" href="index.html">Back to home</a></div>
<p class="notice" style="margin-top:2rem">Need to add something? Email support@worknestsg.com or call +65 8396 3756.</p>
</div></section>''',extra_head='<meta name="robots" content="noindex">')
exec(open(pathlib.Path(__file__).with_name("articles2.py"),encoding="utf-8").read())
exec(open(pathlib.Path(__file__).with_name("jobpages.py"),encoding="utf-8").read())
print("built")
