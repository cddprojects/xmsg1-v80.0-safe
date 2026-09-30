"""Generates the static pages in ../site from shared header/footer partials."""
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"

NAV = [("index.html","Home"),("services.html","Services"),("jobs.html","Job Types"),
       ("knowledge-hub.html","Knowledge Hub"),("about.html","About Us")]

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
    cur = ' aria-current="page"' if fname=="contact.html" else ""
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
<button class="menu-btn" aria-expanded="false" aria-controls="nav-list">Menu</button>
<ul id="nav-list">{nav}<li><a class="cta" href="contact.html"{cur}>Contact Us</a></li></ul>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{LOGO}Work<em>Nest</em> SG</a>
<p style="margin-top:1rem;max-width:32ch">Independent information on part time jobs, work from home jobs, remote jobs and freelance jobs in Singapore.</p></div>
<div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="jobs.html">Job types</a></li><li><a href="knowledge-hub.html">Knowledge Hub</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
<div><h4>Resources</h4><ul><li><a href="scam-check.html">Job scam checker</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="https://www.scamshield.gov.sg" rel="noopener">ScamShield</a></li><li><a href="https://www.mom.gov.sg" rel="noopener">Ministry of Manpower</a></li><li><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="privacy.html">Privacy &amp; PDPA</a></li></ul></div>
</div>
<div class="legal"><p>WorkNest SG is an information website only. We are not an employment agency, do not hold an MOM Employment Agency licence, and do not recruit, screen, place or introduce candidates or publish vacancies. Guides are general information, not legal advice; confirm details with MOM or CPF Board. Scam helpline: <strong>1799</strong>.</p>
<p>&copy; 2026 WorkNest SG. Demo brand for illustration.</p></div>
</div></footer>
<script src="js/main.js"></script>
</body></html>'''
    (OUT/fname).write_text(html, encoding="utf-8")

def head(eyebrow, h1, lede=""):
    return f'<div class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{"<p class=lede>"+lede+"</p>" if lede else ""}</div></div>'

def svc(n,t,d): return f'<div class="type reveal"><span class="n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
IC.update({
 "laptop":icon('<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>'),
 "globe":icon('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 "wallet":icon('<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M3 10h18M16 15h2"/>'),
 "pen2":icon('<path d="M4 20l4-1 11-11-3-3L5 16z"/>'),
 "check":icon('<path d="M5 12l4 4 10-10"/>'),
 "x":icon('<path d="M6 6l12 12M18 6L6 18"/>'),
})

def jobtile(cls,ic,t,d,href):
    return f'<a class="jt {cls} reveal" href="{href}"><span class="ic">{IC[ic]}</span><h3>{t}</h3><p>{d}</p><span class="go">Explore &rarr;</span></a>'

IC.update({
 "laptop":icon('<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>'),
 "globe":icon('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 "wallet":icon('<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M3 10h18M16 15h2"/>'),
 "pen2":icon('<path d="M4 20l4-1 11-11-3-3L5 16z"/>'),
 "check":icon('<path d="M5 12l4 4 10-10"/>'),
 "x":icon('<path d="M6 6l12 12M18 6L6 18"/>'),
 "book":icon('<path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 21V5"/>'),
})

def jobtile(cls,ic,t,d,href):
    return f'<a class="jt {cls} reveal" href="{href}"><span class="ic">{IC[ic]}</span><h3>{t}</h3><p>{d}</p><span class="go">Read the guide &rarr;</span></a>'

# ---------------- HOME
page("index.html","Part Time Jobs & Work From Home Jobs in Singapore: Guides | WorkNest SG",
"Independent guides to part time job Singapore, work from home jobs Singapore, remote job Singapore, online jobs and freelance jobs, plus how to make money at home safely. Information only.",f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Singapore flexible work guide</span>
<h1>Part-time, work from home &amp; remote jobs in Singapore, <span>explained.</span></h1>
<p class="lede">WorkNest SG is an information website. We explain part time jobs, work from home in Singapore, online work and freelance jobs in plain English, and show you how to spot scams. We do not recruit or place candidates.</p>
<div class="btn-row"><a class="btn btn-warm" href="jobs.html">Explore job types</a><a class="btn btn-ghost" href="scam-check.html">Check a job offer</a></div>
<ul class="kw" aria-label="Popular topics"><li><a href="jobs.html#part-time">part time job Singapore</a></li><li><a href="jobs.html#work-from-home">work from home jobs</a></li><li><a href="jobs.html#remote">remote job Singapore</a></li><li><a href="jobs.html#online">online jobs</a></li><li><a href="jobs.html#freelance">freelance jobs</a></li><li><a href="jobs.html#make-money-at-home">make money at home</a></li></ul>
</div>
<div class="mock" aria-hidden="true">
<div class="mc mc-a"><span class="ic">{IC["check"]}</span><div><b>Before you accept an offer</b><small>Company can be verified</small></div><span class="pill ok">Checklist</span></div>
<div class="mc mc-b"><span class="ic">{IC["laptop"]}</span><div><b>Work from home jobs</b><small>What the role really involves</small></div><span class="pill">Guide</span></div>
<div class="mc mc-c"><span class="ic">{IC["shield"]}</span><div><b>Red flag</b><small>Asked to pay a deposit</small></div><span class="pill warm">Stop</span></div>
<div class="mc mc-d"><span class="ic">{IC["book"]}</span><div><b>Free to read</b><small>No sign-up, no fees</small></div></div>
<p class="cap">Illustration only</p>
</div></div></section>

<div class="strip"><div class="marquee"><ul><li>Part time job</li><li>Work from home jobs</li><li>Remote job Singapore</li><li>Online jobs</li><li>Freelance jobs</li><li>Work from home in Singapore</li><li>Online work from home</li><li>Make money at home</li></ul><ul aria-hidden="true"><li>Part time job</li><li>Work from home jobs</li><li>Remote job Singapore</li><li>Online jobs</li><li>Freelance jobs</li><li>Work from home in Singapore</li><li>Online work from home</li><li>Make money at home</li></ul></div></div>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Job types explained</span><h2>Flexible jobs in Singapore, from part-time to fully remote.</h2><p class="lede">Know what each kind of work involves, what to ask, and who it suits, before you apply anywhere.</p></div>
<div class="jgrid">
{jobtile("c1","clock","Part time job Singapore","Retail, admin, F&amp;B, tutoring and events. How hours, pay and CPF usually work.","jobs.html#part-time")}
{jobtile("c2","home","Work from home jobs Singapore","Support, data entry, virtual assistant and content roles you can do from home.","jobs.html#work-from-home")}
{jobtile("c3","globe","Remote job Singapore","Marketing, design, tech and specialist roles with location freedom.","jobs.html#remote")}
{jobtile("c4","laptop","Online jobs","Online tutoring, moderation, research and e-commerce support, and how to check they are real.","jobs.html#online")}
{jobtile("c5","pen2","Freelance jobs","Project-based work, plus what being self-employed means for CPF and tax.","jobs.html#freelance")}
{jobtile("c6","brief","Contract and temp","Fixed-term cover and seasonal work, and what to ask about contracts.","jobs.html#contract")}
</div></div></section>

<section class="alt" id="make-money-at-home"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Make money at home, the safe way</span><h2>Online work from home is real. So are the scams.</h2><p class="lede">Searching "make money at home" brings up genuine employers and fake offers side by side. Here is how to tell them apart.</p></div>
<div class="vs">
<div class="vs-col good reveal"><h3><span class="ic">{IC["check"]}</span>Genuine work from home job</h3><ul><li>You apply, or a named recruiter contacts you</li><li>Pay, hours and duties are clear before you start</li><li>A real company you can verify</li><li>Interviews by video or phone, a written offer</li><li>You are never asked to pay to get the job</li></ul></div>
<div class="vs-col bad reveal"><h3><span class="ic">{IC["x"]}</span>Likely scam</h3><ul><li>Unsolicited WhatsApp or Telegram message</li><li>"Earn hundreds a day" for liking or rating</li><li>Deposits, training fees or account top-ups</li><li>Pressure to reply fast and keep it secret</li><li>Requests for Singpass, OTP or bank logins</li></ul></div>
</div>
<div class="btn-row"><a class="btn btn-primary" href="scam-check.html">Check an offer</a><a class="btn btn-ghost" href="article-job-scams.html">Read: 7 signs of a scam</a></div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">How to use this site</span><h2>Look for flexible work with your eyes open.</h2></div>
<ol class="steps">
<li class="reveal"><b>1</b><h3>Learn the job type</h3><p>Read what part-time, work from home, remote or freelance really means.</p></li>
<li class="reveal"><b>2</b><h3>Check the employer</h3><p>Verify the company, and check any agency on MOM's Employment Agency directory.</p></li>
<li class="reveal"><b>3</b><h3>Search official channels</h3><p>Use trusted portals such as MyCareersFuture or the employer's own careers page.</p></li>
<li class="reveal"><b>4</b><h3>Know your rights</h3><p>Understand CPF, contracts and flexible work requests before you sign.</p></li>
</ol></div></section>

<section class="dark"><div class="wrap split">
<div><span class="eyebrow">Why read WorkNest SG</span><h2>Independent and free to read.</h2>
<p>We are not a recruitment agency and do not hold an MOM Employment Agency licence. That means we do not sell placements, take fees or collect applications. We simply explain things clearly and point you to official sources.</p>
<div class="btn-row"><a class="btn btn-warm" href="about.html">About us</a></div></div>
<div class="stats" style="margin-top:0"><div><b>6</b>job types explained</div><div><b>20+</b>glossary terms</div><div><b>1</b>scam checker</div></div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Knowledge Hub</span><h2>Real-life reads for real-life pressures.</h2></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">Life &amp; Money</span><span>5 min read</span></div><h3><a href="article-rising-costs.html">When the rent goes up and your pay does not</a></h3><p>How a part time job or work from home income can ease the squeeze.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Life &amp; Money</span><span>5 min read</span></div><h3><a href="article-childcare-caregiving.html">Childcare or caregiving costs eating your pay?</a></h3><p>Options to explore before you decide.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Scams</span><span>6 min read</span></div><h3><a href="article-job-scams.html">Seven signs a work-from-home offer is a scam</a></h3><p>Protect yourself while you look for online work.</p></article>
</div><div class="btn-row"><a class="btn btn-ghost" href="knowledge-hub.html">See all guides</a></div></div></section>

<section class="cta-band"><div class="wrap"><h2>Start with the basics.</h2><p class="lede">Explore the job types, then read the guides before you apply anywhere.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-warm" href="jobs.html">Explore job types</a><a class="btn btn-ghost-light" href="knowledge-hub.html">Knowledge Hub</a></div></div></section>
''')

# ---------------- JOBS
def jobsec(id_,alt,eyebrow,h2,intro,roles,suit,check):
    rl="".join(f"<li>{r}</li>" for r in roles)
    sl="".join(f"<li>{r}</li>" for r in suit)
    cl="".join(f"<li>{r}</li>" for r in check)
    return f'''<section id="{id_}"{' class="alt"' if alt else ''}><div class="wrap">
<div class="head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lede">{intro}</p></div>
<div class="cols3"><div><h3>Typical roles</h3><ul>{rl}</ul></div><div><h3>Suits you if</h3><ul>{sl}</ul></div><div><h3>Ask before you accept</h3><ul>{cl}</ul></div></div>
</div></section>'''

jobs_body=head("Job types","Part-time, work from home, remote and freelance jobs in Singapore.","An overview of common flexible work and what to check for each. WorkNest SG is an information website: we do not list vacancies or recruit. To find openings, see the official channels at the bottom of this page.")
jobs_body+=jobsec("part-time",False,"Part time job Singapore","Part time jobs in Singapore","Roles with fewer than 35 contracted hours a week, usually as an employee with a written contract.",
 ["Retail and F&amp;B service crew","Admin and office assistants","Tutors and education centre helpers","Event and promotion staff","Customer service associates"],
 ["You study, parent or care for family","You want a second income","You are returning to work gradually"],
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
jobs_body+='''<section id="make-money-at-home"><div class="wrap"><div class="head"><span class="eyebrow">Make money at home</span><h2>Ways to make money at home, honestly.</h2><p class="lede">Legitimate options are ordinary jobs done from home: part-time employment, freelance projects or contract work. If an offer promises easy money for almost no work, treat it as a scam.</p></div>
<div class="btn-row"><a class="btn btn-primary" href="scam-check.html">Use the scam checker</a><a class="btn btn-ghost" href="article-job-scams.html">Read the guide</a></div></div></section>
<section class="alt" id="where-to-look"><div class="wrap"><div class="head"><span class="eyebrow">Where to look</span><h2>Find real openings through official channels.</h2><p class="lede">We do not run listings, so use trusted sources.</p></div>
<div class="types">
<div class="type"><span class="n">01</span><h3><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></h3><p>The government job portal, with filters and salary information.</p></div>
<div class="type"><span class="n">02</span><h3>Employer careers pages</h3><p>Apply directly on the official website of a company you have verified.</p></div>
<div class="type"><span class="n">03</span><h3><a href="https://www.mom.gov.sg" rel="noopener">MOM Employment Agency directory</a></h3><p>Confirm that any recruiter or agency holds a valid licence before you share details.</p></div>
</div></div></section>'''
page("jobs.html","Part Time, Work From Home, Remote & Freelance Jobs in Singapore | WorkNest SG",
"Guides to part time job Singapore, work from home jobs Singapore, remote job Singapore, online jobs, work from home in Singapore and freelance jobs: what to expect and what to ask.",jobs_body)

# ---------------- SERVICES
page("services.html","Services | Free Guides on Part Time & Work From Home Jobs | WorkNest SG","Free information services: job type guides, a job scam checker, a recruitment glossary and Knowledge Hub for part time job Singapore, work from home jobs and remote work.",
head("Services","Free tools and guides for flexible job seekers.","WorkNest SG is an information website. Everything here is free to use, with no sign-up.")+f'''
<section><div class="wrap">
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["laptop"]}</div><h3>Job type guides</h3><p>Plain-English explainers on part time job Singapore, work from home jobs, remote, online and freelance work.</p><a class="more" href="jobs.html">Read the guides &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["shield"]}</div><h3>Job scam checker</h3><p>Tick the red flags in an offer and get guidance on what to do next.</p><a class="more" href="scam-check.html">Check an offer &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>Recruitment glossary</h3><p>Decode PMET, CPF, JD, WFH, EP and other Singapore job-ad terms.</p><a class="more" href="glossary.html">Search terms &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Knowledge Hub</h3><p>Articles on cost of living, caregiving, career breaks, rights at work and scams.</p><a class="more" href="knowledge-hub.html">Read articles &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["check"]}</div><h3>Offer question list</h3><p>The questions to ask about hours, pay, CPF and contract before accepting any job.</p><a class="more" href="jobs.html">See per-job questions &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["globe"]}</div><h3>Signposting</h3><p>Links to official sources: MOM, CPF Board, MyCareersFuture, ScamShield and more.</p><a class="more" href="jobs.html#where-to-look">Where to look &rarr;</a></article>
</div></div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">What we do not do</span><h2>Clear boundaries.</h2>
<ul><li>We are not an employment agency and hold no MOM Employment Agency licence.</li><li>We do not recruit, screen, place or introduce candidates.</li><li>We do not publish job vacancies or accept applications.</li><li>We do not charge fees or ask for money, ever.</li><li>We do not give legal or financial advice.</li></ul></div>
<div><span class="eyebrow">Why it matters</span><h2>Anyone who says otherwise is not us.</h2><p>If someone uses our name to offer you a job, ask for a fee, or request your bank or Singpass details, it is a scam. Report it and contact us.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Contact Us</a></div></div>
</div></section>''')

# ---------------- KNOWLEDGE HUB
posts=[
("life","Life & Money","article-rising-costs.html","When the rent goes up and your pay does not","Many households feel squeezed by Singapore living costs. Here is how flexible work can help, and how to choose it wisely.","5 min",True),
("scam","Scams","article-job-scams.html","Seven signs a work-from-home offer is a scam","Fake tasks, upfront fees and messaging-app interviews. Learn the pattern and what to do if you engaged.","6 min",False),
("life","Life & Money","article-childcare-caregiving.html","Childcare or caregiving costs eating your pay?","Working around school runs and caring duties is a real trade-off. Options to explore before you decide.","5 min",False),
("life","Life & Money","article-restart.html","Starting again after a break, retrenchment or illness","Gaps are more common than you think. How to talk about them and take the first small step.","5 min",False),
("life","Life & Money","#","Is the commute costing you more than you think?","Time and money add up. How remote and hybrid roles change the picture.","4 min",False),
("basics","Basics","article-work-modes.html","Part-time, remote, hybrid, freelance: what each really means","The words in a job ad describe different things: hours, place and employment status.","5 min",False),
("rights","Rights","#","Asking for flexible work: how requests are handled","An overview of the national guidelines on formal flexible work arrangement requests.","5 min",False),
("rights","Rights","#","Part-time employees and CPF: the basics","When CPF contributions apply and how to read your payslip.","4 min",False),
("career","Career","#","Building a CV for remote roles","Show self-management, written communication and tool familiarity.","4 min",False),
("career","Career","#","Interviewing over video: a calm checklist","Setup, timing and questions worth asking about hybrid expectations.","3 min",False),
("gig","Freelance","#","Freelancing vs platform work in Singapore","Independent contractor, self-employed and platform worker are not the same. Know the differences.","6 min",False),
("basics","Basics","#","Reading a Singapore job ad like an insider","Salary ranges, JD, notice period, probation and what they signal.","5 min",False),
]
cards=""
for cat,label,href,t,d,m,feat in posts:
    link = f'<a href="{href}">{t}</a>' if href!="#" else f'<a href="#" aria-disabled="true">{t}</a>'
    cards+=f'<article class="post{" feature" if feat else ""}" data-cat="{cat}"><div><div class="meta"><span class="cat">{label}</span><span>{m} read</span>{"<span>Coming soon</span>" if href=="#" else ""}</div><h3>{link}</h3><p>{d}</p></div>{"<div style=\"align-self:end\"><a class=\"btn btn-warm\" href=\""+href+"\">Read now</a></div>" if feat else ""}</article>'
page("knowledge-hub.html","Knowledge Hub | WorkNest SG","Blog-style guides on part-time, remote, hybrid and freelance work in Singapore.",
head("Knowledge Hub","Real-life reads on part time jobs, work from home and money in Singapore.","Warm, plain-English guides on the pressures that push people towards flexible work, and how to handle them.")+f'''
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" data-filter="all" aria-pressed="true">All</button>
<button class="chip" data-filter="life" aria-pressed="false">Life &amp; Money</button>
<button class="chip" data-filter="scam" aria-pressed="false">Scams</button>
<button class="chip" data-filter="basics" aria-pressed="false">Basics</button>
<button class="chip" data-filter="rights" aria-pressed="false">Rights</button>
<button class="chip" data-filter="career" aria-pressed="false">Career</button>
<button class="chip" data-filter="gig" aria-pressed="false">Freelance</button></div>
<div class="posts">{cards}</div></div></section>''')

# ---------------- ARTICLES
def article(fname,title,desc,cat,body):
    page(fname,title+" | WorkNest SG",desc,f'''{head(cat,title)}
<section><div class="wrap article">{body}
<p style="margin-top:2.5rem"><a href="knowledge-hub.html">&larr; Back to Knowledge Hub</a></p></div></section>''')

article("article-job-scams.html","Seven signs a work-from-home offer is a scam","How to recognise fake remote and part-time job offers in Singapore.","Scams",'''
<p class="lede">Scammers favour part-time and remote jobs because the promise of easy, flexible income is hard to resist. These are the patterns to look for.</p>
<h2>1. You did not apply</h2><p>An unsolicited WhatsApp, Telegram or SMS offering a job is a major red flag. Legitimate employers rarely cold-message strangers with pay figures.</p>
<h2>2. Pay is too good for the work</h2><p>Hundreds of dollars a day to "like" videos, boost ratings or complete simple tasks does not match how real businesses pay.</p>
<h2>3. You must pay first</h2><p>Deposits, "training fees", equipment costs or topping up an account to "unlock" tasks are how the scam takes your money.</p>
<h2>4. The interview happens only on a chat app</h2><p>No company email, no video call, no named hiring manager, and no verifiable business in ACRA records.</p>
<h2>5. Pressure and secrecy</h2><p>"Reply in one hour", "do not tell anyone" and "limited slots" are designed to stop you from checking.</p>
<h2>6. They ask for sensitive details</h2><p>Never share Singpass, OTPs, banking logins or a full NRIC photo before a verified offer. Your bank account may be misused for money mule activity.</p>
<h2>7. The job is not on official channels</h2><p>Check whether the employer and role appear on MyCareersFuture or the company's official website.</p>
<div class="callout"><p><strong>If you have engaged:</strong> stop all payments, keep screenshots, call your bank, and contact the Police. For advice, call the ScamShield helpline at 1799. Try our <a href="scam-check.html">scam checker</a>.</p></div>''')

article("article-work-modes.html","Part-time, remote, hybrid, freelance: what each really means","Definitions of common flexible work terms in Singapore.","Basics",'''
<p class="lede">Job ads mix up three separate ideas: how many hours you work, where you work, and your legal status. Untangling them is the first step.</p>
<h2>Hours: part-time vs full-time</h2><p>Under Singapore's Part-Time Employment Regulations, a part-time employee is contracted to work fewer than 35 hours a week. Part-timers are still employees with a contract, and many protections apply on a pro-rated basis. Check MOM for the current rules.</p>
<h2>Place: remote, hybrid, on-site</h2><ul><li><strong>Remote / WFH:</strong> you work away from the employer's premises, often from home.</li><li><strong>Hybrid:</strong> a mix. Ask how many office days are required and whether they are fixed.</li><li><strong>On-site:</strong> you work at a workplace or client location.</li></ul>
<h2>Status: employee, contractor, platform worker</h2><p>Employees have a contract of service. Freelancers and contractors have a contract for services and arrange their own CPF and taxes. Platform workers, such as ride-hail and delivery workers, have their own framework under the Platform Workers Act.</p>
<div class="callout"><p>Questions to ask any employer: Is this an employment contract? What are my weekly hours? How is pay calculated? Is CPF payable? What is the notice period?</p></div>
<p>Unsure about a term? Search our <a href="glossary.html">glossary</a>.</p>''')


article("article-rising-costs.html","When the rent goes up and your pay does not","How flexible work can ease cost-of-living pressure in Singapore.","Life & Money",'''
<p class="lede">If every month feels tighter than the last, you are not imagining it, and you are not alone. Housing, groceries, transport and family costs weigh on many households here.</p>
<h2>Why a second income can help</h2><p>You may not be able to change your rent, but you may be able to change your income. Part-time, remote or contract work can add to what you earn without demanding a rigid full-time schedule.</p>
<h2>Choose the arrangement that suits your budget</h2><ul><li><strong>Part-time:</strong> predictable hours, usually as an employee with a contract.</li><li><strong>Remote or hybrid:</strong> fewer commuting hours and costs.</li><li><strong>Freelance or contract:</strong> can pay more per hour but less predictable, and you handle your own CPF and tax.</li></ul>
<h2>Look at the whole picture</h2><p>Compare the take-home pay against the extra costs: transport, meals out and childcare. Ask how pay is calculated and how often you are paid.</p>
<div class="callout"><p>If money is very tight, also explore government support. SupportGoWhere (supportgowhere.gov.sg) lists schemes you may qualify for. Beware of anyone promising fast money for an upfront fee.</p></div>
<p>Explore flexible options in our <a href="jobs.html">job types guide</a>.</p>''')

article("article-childcare-caregiving.html","Childcare or caregiving costs eating your pay?","Weighing work against childcare and caregiving in Singapore.","Life & Money",'''
<p class="lede">For many parents and caregivers the question is not whether you want to work, but whether the numbers and the hours make sense.</p>
<h2>Start with your real hours</h2><p>Write down the hours you can truly commit each week, including the school run, meals and appointments. A role that fits those hours is worth more than a higher rate that does not.</p>
<h2>Ask about flexibility early</h2><ul><li>Are hours fixed or can you choose slots?</li><li>Can some work be done from home?</li><li>What happens if a child or parent falls ill?</li></ul>
<h2>Do the sums honestly</h2><p>Subtract childcare, transport and other work-related costs from your expected pay. Sometimes fewer hours in a well-matched role beats more hours in a stressful one.</p>
<h2>Be kind to yourself</h2><p>Choosing to work part-time, or to pause, is not a failure. It is a decision you can revisit as your family changes.</p>
<p>Explore roles with flexible hours in our <a href="jobs.html">job types guide</a>.</p>''')

article("article-restart.html","Starting again after a break, retrenchment or illness","Restarting work after a career gap in Singapore.","Life & Money",'''
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
terms=[("Part-time employee","Employee contracted for fewer than 35 hours per week in Singapore."),
("WFH","Work from home. Sometimes written as remote or home-based."),
("Hybrid","A schedule that splits time between office and remote work."),
("Flexi-hours","Flexible start and end times, often around core hours."),
("FWA","Flexible work arrangement: flexi-time, flexi-place or flexi-load."),
("Freelancer","Self-employed person paid per project or task, responsible for own CPF and tax."),
("Platform worker","Person who gets work via an online platform, such as ride-hail or delivery, covered by the Platform Workers Act."),
("Gig","A short-term, task-based job."),
("CPF","Central Provident Fund. A mandatory savings scheme for employed citizens and PRs."),
("PMET","Professionals, Managers, Executives and Technicians."),
("EP / S Pass","Employment Pass and S Pass. Work passes for foreign professionals and mid-skilled workers."),
("SkillsFuture","National movement offering skills training credit and courses."),
("WSG","Workforce Singapore, an agency supporting jobseekers and career transitions."),
("MyCareersFuture","Government job portal operated by GovTech and WSG."),
("JD","Job description, listing duties and requirements."),
("Notice period","Time you or your employer must give before ending employment."),
("Probation","Initial trial period at the start of employment."),
("Contract / temp","Fixed-term employment, often through an agency."),
("AWS / 13th month","Annual wage supplement; often a bonus month paid at year end."),
("Money mule","Person whose bank account is used to move scam proceeds, often unknowingly. It is a criminal offence."),
("ScamShield","Government app and 1799 helpline that filters scam messages and provides advice.")]
tl="".join(f'<div class="term"><dt>{a}</dt><dd>{b}</dd></div>' for a,b in terms)
page("glossary.html","Singapore Recruitment Glossary | WorkNest SG","Definitions of Singapore recruitment, part-time, remote and hybrid work keywords.",
head("Glossary","Recruitment keywords, decoded.")+f'''
<section><div class="wrap" style="max-width:860px">
<label for="glossary-search" class="eyebrow">Search terms</label>
<input id="glossary-search" class="search" type="search" placeholder="Try &quot;CPF&quot; or &quot;hybrid&quot;" autocomplete="off">
<dl class="glossary">{tl}</dl><p id="glossary-empty" hidden>No matches. <a href="contact.html">Ask us to add it.</a></p></div></section>''')

# ---------------- FAQ
faqs=[("Are you a recruitment agency or job board?","No. WorkNest SG is an information website only. We do not hold an MOM Employment Agency licence, recruit or place candidates, publish vacancies or accept applications."),
("Do you charge fees?","No. Everything on this site is free. If anyone using our name asks you for money, it is a scam."),
("How do I find a part time job in Singapore?","Search official channels such as MyCareersFuture and employers' own careers pages. Our part-time guide lists what to ask before you accept."),
("Are there genuine work from home jobs in Singapore?","Yes. Customer support, admin, content and many specialist roles can be done from home. Genuine employers pay you for defined work and never ask you to pay to start."),
("How can I make money at home safely?","Focus on ordinary jobs done from home: part-time employment, freelance projects or contract work. Avoid offers that promise high pay for tasks like liking or rating."),
("What is the difference between remote and work from home?","Work from home usually means working from home on agreed hours. Remote means location flexibility, sometimes with an overseas team. Ask which applies."),
("Are online jobs real?","Many are, such as online tutoring, moderation or support. Check who pays you, get terms in writing and never pay a fee to get started."),
("What are freelance jobs and do they include CPF?","Freelancers are self-employed. You choose your clients and manage your own CPF contributions, tax and admin. See CPF Board and IRAS for current rules."),
("Is a part-time job entitled to CPF?","Employees, including part-timers, generally receive CPF contributions subject to age, residency and pay. See CPF Board for current rates."),
("Can I request remote or hybrid work from my employer?","Employees can submit a formal flexible work arrangement request and employers are expected to consider it fairly under national guidelines. Approval is not guaranteed."),
("How do I check that a recruiter is licensed?","Search the Employment Agency directory on the MOM website before sharing personal details.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html","FAQ | Part Time & Work From Home Jobs in Singapore | WorkNest SG","Answers about part time job Singapore, work from home jobs, remote jobs, online work, freelance jobs and how to make money at home safely.",
head("FAQ","Quick answers.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Still stuck? <a href="contact.html">Contact us</a>.</p></div></section>')

# ---------------- ABOUT
page("about.html","About Us | WorkNest SG","WorkNest SG is an independent information website about part-time, work from home, remote and freelance work in Singapore.",
head("About Us","Clear information for people looking for flexible work.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>Why we exist</h2><p>Living in Singapore is expensive, and many people are stretched between bills, family and work that will not bend. Searching for a part time job or work from home in Singapore also means wading through confusing terms and, too often, scams.</p>
<p>WorkNest SG explains it plainly. We cover part-time, work from home, remote, online and freelance work, what to ask, what your rights are and how to stay safe, always pointing to the official source.</p></div>
<div class="reveal"><h2>Our principles</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Information only</h3><p>We do not recruit, place or advise on individual cases.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Official sources first</h3><p>We link to MOM, CPF Board, MyCareersFuture and ScamShield so you can verify.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Free and safe</h3><p>No fees, no sign-ups, and no collection of your sensitive details.</p></div></div></div></div>
</div></section>
<section class="dark"><div class="wrap"><span class="eyebrow">At a glance</span><h2>What you will find</h2>
<div class="stats"><div><b>6</b>job types explained</div><div><b>20+</b>glossary terms</div><div><b>5</b>articles and growing</div><div><b>SG</b>focused</div></div></div></section>
<section><div class="wrap"><p class="notice" style="max-width:70ch">WorkNest SG is an information website. It is not an employment agency, does not hold an MOM Employment Agency licence, and does not recruit or place candidates. Content is general information, not legal, financial or employment advice.</p><div class="btn-row"><a class="btn btn-primary" href="contact.html">Get in touch</a></div></div></section>''')

# ---------------- CONTACT
page("contact.html","Contact Us | WorkNest SG","Contact WorkNest SG with a question, correction or topic suggestion about part time job Singapore, work from home jobs and remote work.",
head("Contact Us","Questions, corrections or topic ideas?","We are an information website and cannot find or place jobs, but we read every message. Please do not include NRIC, bank or Singpass details.")+f'''
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>A question about part time jobs</option><option>A question about work from home or remote jobs</option><option>Online jobs or freelance work</option><option>I think I saw a scam</option><option>Suggest an article</option><option>Correction or feedback</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send</button>
<p class="notice">Demo form: no data is sent anywhere. Connect a backend or form service before launch.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1"><h3>Thanks, we have noted it.</h3><p>In a live site we would reply within a few working days.</p></div>
</div>
<div><h2>Other ways</h2><ul class="contact-list">
<li><b>Email</b>hello@worknest.example</li>
<li><b>Hours</b>Mon to Fri, 9am to 6pm (SGT)</li>
<li><b>Looking for a job?</b>We do not list vacancies. Try <a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a>.</li>
<li><b>Suspected scam?</b>Call the ScamShield helpline on 1799 and report to the Police.</li></ul></div>
</div></section>''')

# ---------------- PRIVACY
page("privacy.html","Privacy & PDPA | WorkNest SG","How WorkNest SG handles personal data under Singapore's PDPA.",
head("Privacy &amp; PDPA","Privacy notice")+'''
<section><div class="wrap article">
<p>This is a template. Have it reviewed before launch.</p>
<h2>What we collect</h2><p>Only what you submit through the contact form: name, email and message. The scam checker runs in your browser and stores nothing.</p>
<h2>How we use it</h2><p>To reply to your enquiry. We do not sell personal data.</p>
<h2>Your rights</h2><p>Under Singapore's Personal Data Protection Act you may request access to or correction of your data, or withdraw consent, by emailing our Data Protection Officer at dpo@worknest.example.</p>
<h2>Cookies</h2><p>This site sets no tracking cookies. Fonts are loaded from Google Fonts.</p></div></section>''')
print("built")
