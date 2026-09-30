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
<p style="margin-top:1rem;max-width:32ch">Singapore talent resourcing agency for part time jobs, work from home jobs, remote jobs and freelance jobs.</p></div>
<div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="jobs.html">Job types</a></li><li><a href="for-talent.html">For job seekers</a></li><li><a href="for-employers.html">For employers</a></li><li><a href="knowledge-hub.html">Knowledge Hub</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
<div><h4>Resources</h4><ul><li><a href="scam-check.html">Job scam checker</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="https://www.scamshield.gov.sg" rel="noopener">ScamShield</a></li><li><a href="https://www.mom.gov.sg" rel="noopener">Ministry of Manpower</a></li><li><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="privacy.html">Privacy &amp; PDPA</a></li></ul></div>
</div>
<div class="legal"><p>WorkNest SG is a demonstration brand. EA Licence No.: [placeholder, required for a real agency]. Guides are general information, not legal advice; confirm details with MOM or CPF Board. Scam helpline: <strong>1799</strong>.</p>
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

# ---------------- HOME
page("index.html","Part Time Jobs & Work From Home Jobs in Singapore | WorkNest SG",
"WorkNest SG is a Singapore talent resourcing agency. Find part time job Singapore, work from home jobs, remote job Singapore, online jobs and freelance jobs. Free for job seekers.",f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Singapore talent resourcing agency</span>
<h1>Part-time, work from home &amp; remote jobs <span>in Singapore.</span></h1>
<p class="lede">We screen you, match you and introduce you to employers hiring flexible talent. Whether you want a part time job, work from home in Singapore, online work or freelance jobs, WorkNest SG is free for job seekers.</p>
<div class="btn-row"><a class="btn btn-warm" href="contact.html">Join our talent pool</a><a class="btn btn-ghost" href="jobs.html">Browse job types</a></div>
<ul class="kw" aria-label="Popular searches"><li><a href="jobs.html#part-time">part time job Singapore</a></li><li><a href="jobs.html#work-from-home">work from home jobs</a></li><li><a href="jobs.html#remote">remote job Singapore</a></li><li><a href="jobs.html#online">online jobs</a></li><li><a href="jobs.html#freelance">freelance jobs</a></li><li><a href="jobs.html#make-money-at-home">make money at home</a></li></ul>
</div>
<div class="mock" aria-hidden="true">
<div class="mc mc-a"><div class="av">A</div><div><b>Sample candidate profile</b><small>Available 20 hrs a week &middot; Singapore</small></div><span class="pill ok">Screened</span></div>
<div class="mc mc-b"><span class="ic">{IC["laptop"]}</span><div><b>Work from home</b><small>Customer support, part-time</small></div><span class="pill">Matched</span></div>
<div class="mc mc-c"><span class="ic">{IC["clock"]}</span><div><b>Video interview</b><small>Thursday, 2:00 pm</small></div><span class="pill warm">Booked</span></div>
<div class="mc mc-d"><span class="ic">{IC["wallet"]}</span><div><b>Fees for you</b><small>Always $0</small></div></div>
<p class="cap">Illustration only</p>
</div></div></section>

<div class="strip"><div class="marquee"><ul><li>Part time job</li><li>Work from home jobs</li><li>Remote job Singapore</li><li>Online jobs</li><li>Freelance jobs</li><li>Work from home in Singapore</li><li>Online work from home</li><li>Make money at home</li></ul><ul aria-hidden="true"><li>Part time job</li><li>Work from home jobs</li><li>Remote job Singapore</li><li>Online jobs</li><li>Freelance jobs</li><li>Work from home in Singapore</li><li>Online work from home</li><li>Make money at home</li></ul></div></div>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Jobs we place</span><h2>Flexible jobs in Singapore, from part-time to fully remote.</h2><p class="lede">Pick the kind of work you want. We will tell you honestly what it involves and match you to employers who are hiring.</p></div>
<div class="jgrid">
{jobtile("c1","clock","Part time job Singapore","Retail, admin, F&amp;B, tutoring, events and more, with hours that fit around your day.","jobs.html#part-time")}
{jobtile("c2","home","Work from home jobs Singapore","Customer support, data entry, virtual assistants and content roles you can do from home.","jobs.html#work-from-home")}
{jobtile("c3","globe","Remote job Singapore","Marketing, design, tech and specialist roles with location freedom.","jobs.html#remote")}
{jobtile("c4","laptop","Online jobs","Online tutoring, moderation, research and e-commerce support, worked entirely online.","jobs.html#online")}
{jobtile("c5","pen2","Freelance jobs","Project-based design, writing, video and bookkeeping work you can pick up on your terms.","jobs.html#freelance")}
{jobtile("c6","brief","Contract and temp","Fixed-term cover and seasonal peaks, a smart way back into work.","jobs.html#contract")}
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
<div class="head reveal"><span class="eyebrow">How it works</span><h2>From sign-up to interview in four steps.</h2></div>
<ol class="steps">
<li class="reveal"><b>1</b><h3>Join the talent pool</h3><p>Tell us the work you want, your hours and your experience. Two minutes.</p></li>
<li class="reveal"><b>2</b><h3>We screen you</h3><p>A short friendly interview and quick checks, so employers can trust your profile.</p></li>
<li class="reveal"><b>3</b><h3>We match you</h3><p>We put you forward to employers hiring the kind of flexible role you asked for.</p></li>
<li class="reveal"><b>4</b><h3>You interview</h3><p>We prepare you, schedule the interview and stay in touch after you start.</p></li>
</ol></div></section>

<section class="dark"><div class="wrap split">
<div><span class="eyebrow">Why job seekers choose us</span><h2>Free for you. Honest with you.</h2>
<p>We are paid by employers, never by candidates. You see the role, pay range and work mode before any interview, and we introduce you only with your consent.</p>
<div class="btn-row"><a class="btn btn-warm" href="contact.html">Join our talent pool</a></div></div>
<div class="stats" style="margin-top:0"><div><b>$0</b>fees for job seekers</div><div><b>6</b>types of flexible work</div><div><b>4</b>simple steps</div></div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Knowledge Hub</span><h2>Real-life reads for real-life pressures.</h2></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">Life &amp; Money</span><span>5 min read</span></div><h3><a href="article-rising-costs.html">When the rent goes up and your pay does not</a></h3><p>How a part time job or work from home income can ease the squeeze.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Life &amp; Money</span><span>5 min read</span></div><h3><a href="article-childcare-caregiving.html">Childcare or caregiving costs eating your pay?</a></h3><p>Options to explore before you decide.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Scams</span><span>6 min read</span></div><h3><a href="article-job-scams.html">Seven signs a work-from-home offer is a scam</a></h3><p>Protect yourself while you look for online work.</p></article>
</div><div class="btn-row"><a class="btn btn-ghost" href="knowledge-hub.html">See all guides</a></div></div></section>

<section class="cta-band"><div class="wrap"><h2>Ready for work that fits your life?</h2><p class="lede">Join the WorkNest SG talent pool. It is free, friendly and takes two minutes.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-warm" href="contact.html">Join our talent pool</a><a class="btn btn-ghost-light" href="faq.html">Read the FAQ</a></div></div></section>
''')

# ---------------- JOBS
def jobsec(id_,alt,eyebrow,h2,intro,roles,suit,check):
    rl="".join(f"<li>{r}</li>" for r in roles)
    sl="".join(f"<li>{r}</li>" for r in suit)
    cl="".join(f"<li>{r}</li>" for r in check)
    return f'''<section id="{id_}"{' class="alt"' if alt else ''}><div class="wrap">
<div class="head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lede">{intro}</p></div>
<div class="cols3"><div><h3>Typical roles</h3><ul>{rl}</ul></div><div><h3>Suits you if</h3><ul>{sl}</ul></div><div><h3>Ask before you accept</h3><ul>{cl}</ul></div></div>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Join our talent pool</a></div></div></section>'''

jobs_body=head("Job types","Part-time, work from home, remote and freelance jobs in Singapore.","An overview of the flexible work we place people into, and what to check for each. This site is not a job board, so there are no live listings here. Join our talent pool and we will match you.")
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
<div class="btn-row"><a class="btn btn-primary" href="scam-check.html">Use the scam checker</a><a class="btn btn-ghost" href="article-job-scams.html">Read the guide</a></div></div></section>'''
page("jobs.html","Part Time, Work From Home, Remote & Freelance Jobs in Singapore | WorkNest SG",
"Explore part time job Singapore, work from home jobs Singapore, remote job Singapore, online jobs, work from home in Singapore and freelance jobs. What to expect and what to ask.",jobs_body)

# ---------------- SERVICES
page("services.html","Services | Talent Resourcing for Flexible Jobs in Singapore | WorkNest SG","Talent resourcing services in Singapore: screening, matching and placement for part time jobs, work from home jobs, remote roles and freelance jobs.",
head("Services","We screen, match and place flexible talent.","WorkNest SG is a talent resourcing agency. We connect job seekers with employers hiring part-time, work from home, remote, online and freelance talent.")+f'''
<section><div class="wrap">
<div class="head"><span class="eyebrow">For job seekers</span><h2>Free, from sign-up to start date.</h2></div>
<div class="types">
{svc("01","Talent pool registration","Tell us the work you want: part time job, work from home, remote or freelance. We record your skills, hours and pay expectations.")}
{svc("02","Initial screening","A short, friendly interview plus identity, eligibility and reference checks, so employers can shortlist you with confidence.")}
{svc("03","Job matching","We match you to employers we work with who are hiring the flexible roles you want, and put you forward with your consent.")}
{svc("04","Profile and interview readiness","Practical help with your CV and interview preparation, including video interviews, so you are ready to be hired.")}
{svc("05","Placement follow-up","We check in after you start to help settle hours, expectations and any questions.")}
</div><div class="btn-row"><a class="btn btn-warm" href="contact.html">Join our talent pool</a><a class="btn btn-ghost" href="jobs.html">See job types</a></div></div></section>
<section class="alt"><div class="wrap">
<div class="head"><span class="eyebrow">For employers</span><h2>Flexible talent, already screened.</h2></div>
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Initial screening</h3><p>Structured first-round interviews and checks against your role brief.</p></article>
<article class="tile reveal"><div class="ic">{IC["split"]}</div><h3>Shortlisting</h3><p>A short list with a written profile per candidate.</p></article>
<article class="tile reveal"><div class="ic">{IC["laptop"]}</div><h3>Flexible workforce</h3><p>Part-time, remote, hybrid, freelance and contract talent.</p></article>
<article class="tile reveal"><div class="ic">{IC["shield"]}</div><h3>Verification</h3><p>Identity, eligibility and reference checks with candidate consent.</p></article>
</div><div class="btn-row"><a class="btn btn-primary" href="for-employers.html">Employer details</a></div></div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">Our promise</span><h2>Clear terms on both sides.</h2></div>
<div class="types">
{svc("-","Job seekers pay nothing","No fees, deposits or training charges. We are funded by employer clients.")}
{svc("-","Consent first","We only share your profile with an employer after you agree.")}
{svc("-","Transparent","Role, pay range and work mode are shared before any interview.")}
</div></div></section>''')

# ---------------- FOR EMPLOYERS
page("for-employers.html","For Employers | Hire Part-Time & Remote Talent in Singapore | WorkNest SG","Hire part-time, work from home, remote and freelance talent in Singapore. We handle screening and shortlisting.",
head("For Employers","Hire flexible talent without the screening backlog.","We turn a long applicant list into a short, verified shortlist.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>What you get</h2>
<ul><li>A written role brief agreed before we start</li><li>Structured screening interview for every shortlisted candidate</li><li>Availability, eligibility and reference verification</li><li>A one-page profile and recommendation per candidate</li><li>Interview scheduling with your team</li><li>Follow-up after start date</li></ul></div>
<div class="reveal"><h2>What we screen</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Fit for the schedule</h3><p>Availability, reliability and realistic commitments.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Skills and experience</h3><p>Relevant experience tested with role-specific questions.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Remote readiness</h3><p>Communication, tools, self-management and a suitable work setup.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Eligibility</h3><p>Right to work in Singapore and, where relevant, work pass status.</p></div></div></div></div>
</div></section>
<section class="alt"><div class="wrap"><div class="btn-row" style="margin-top:0"><a class="btn btn-primary" href="contact.html">Send us a role brief</a></div></div></section>''')

# ---------------- FOR JOB SEEKERS
page("for-talent.html","For Job Seekers | Find Part Time & Work From Home Jobs in Singapore | WorkNest SG","How WorkNest SG helps job seekers find a part time job Singapore, work from home jobs, remote roles, online jobs and freelance jobs. Free for candidates.",
head("For Job Seekers","Get screened once. Get introduced to employers who are hiring.","Free for job seekers. Part-time, work from home, remote, online and freelance.")+f'''
<section><div class="wrap">
<div class="types">
{svc("01","Join the talent pool","Two minutes: your skills, hours and the kind of work you want.")}
{svc("02","Friendly screening","A short conversation and checks so employers can trust your profile.")}
{svc("03","We match and introduce","With your consent, we put you forward to employers hiring flexible roles.")}
{svc("04","Interview and start","We prepare you, schedule the interview and check in once you start.")}
</div></div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">Who joins us</span><h2>Whatever season of life you are in.</h2>
<ul><li>Parents balancing school runs and childcare costs</li><li>Caregivers looking after ageing parents</li><li>Students topping up allowance and fees</li><li>People restarting after a break or retrenchment</li><li>Mature workers wanting fewer hours</li><li>Anyone whose single income is stretched</li></ul></div>
<div><h2>Looking out for you</h2><p>When money is tight, fake "easy income" offers are especially cruel. We never charge job seekers or ask for bank logins. Learn the signs with our <a href="scam-check.html">scam checker</a> and <a href="glossary.html">glossary</a>.</p>
<div class="btn-row"><a class="btn btn-warm" href="contact.html">Join our talent pool</a></div></div>
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
<p>Want to talk it through? <a href="contact.html">Book a free chat</a> with our team.</p>''')

article("article-childcare-caregiving.html","Childcare or caregiving costs eating your pay?","Weighing work against childcare and caregiving in Singapore.","Life & Money",'''
<p class="lede">For many parents and caregivers the question is not whether you want to work, but whether the numbers and the hours make sense.</p>
<h2>Start with your real hours</h2><p>Write down the hours you can truly commit each week, including the school run, meals and appointments. A role that fits those hours is worth more than a higher rate that does not.</p>
<h2>Ask about flexibility early</h2><ul><li>Are hours fixed or can you choose slots?</li><li>Can some work be done from home?</li><li>What happens if a child or parent falls ill?</li></ul>
<h2>Do the sums honestly</h2><p>Subtract childcare, transport and other work-related costs from your expected pay. Sometimes fewer hours in a well-matched role beats more hours in a stressful one.</p>
<h2>Be kind to yourself</h2><p>Choosing to work part-time, or to pause, is not a failure. It is a decision you can revisit as your family changes.</p>
<p>Our team can help you find roles that respect your schedule. <a href="contact.html">Say hello</a>.</p>''')

article("article-restart.html","Starting again after a break, retrenchment or illness","Restarting work after a career gap in Singapore.","Life & Money",'''
<p class="lede">Gaps in a CV are common: caring for family, retrenchment, health, study or simply needing a rest. Employers see them more often than you might fear.</p>
<h2>Say it simply and honestly</h2><p>One or two calm sentences are enough: what happened, what you learned or did during that time, and what you want next.</p>
<h2>Restart small</h2><p>Part-time or contract work can rebuild confidence, references and recent experience without the pressure of jumping straight back to full time.</p>
<h2>Freshen your profile</h2><ul><li>Update your CV with recent skills, courses or volunteering.</li><li>Ask a former colleague for a short reference.</li><li>Look into SkillsFuture options to top up relevant skills.</li></ul>
<div class="callout"><p>Take the first step at a pace that feels right. There is no deadline on starting again.</p></div>
<p>We would be glad to help. <a href="for-talent.html">See how it works</a>.</p>''')

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
faqs=[("Are you a job board?","No. WorkNest SG is a talent resourcing agency. We screen and match job seekers with employers, rather than publish open listings."),
("Do job seekers pay you?","No. Our services are paid by employer clients. Be cautious of anyone who asks a job seeker for fees or deposits."),
("How do I find a part time job in Singapore?","Join our talent pool. We screen your profile, match you to employers hiring part-time roles and introduce you with your consent. You can also check MyCareersFuture."),
("Are there genuine work from home jobs in Singapore?","Yes. Customer support, admin, content and many specialist roles can be done from home. Genuine employers pay you for defined work and never ask you to pay to start."),
("How can I make money at home safely?","Focus on ordinary jobs done from home: part-time employment, freelance projects or contract work. Avoid offers that promise high pay for tasks like liking or rating."),
("What is the difference between remote and work from home?","Work from home usually means working from home on agreed hours. Remote means location flexibility, sometimes with an overseas team. Ask which applies."),
("Are online jobs real?","Many are, such as online tutoring, moderation or support. Check who pays you, get terms in writing and never pay a fee to get started."),
("What are freelance jobs and do they include CPF?","Freelancers are self-employed. You choose your clients and manage your own CPF contributions, tax and admin. See CPF Board and IRAS for current rules."),
("Is a part-time job entitled to CPF?","Employees, including part-timers, generally receive CPF contributions subject to age, residency and pay. See CPF Board for current rates."),
("Can I request remote or hybrid work from my employer?","Employees can submit a formal flexible work arrangement request and employers are expected to consider it fairly under national guidelines. Approval is not guaranteed."),
("What does initial screening include?","A short interview, skills and availability checks, and with your consent, eligibility and reference verification.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html","FAQ | Part Time & Work From Home Jobs in Singapore | WorkNest SG","Answers about part time job Singapore, work from home jobs, remote jobs, online work, freelance jobs and how to make money at home safely.",
head("FAQ","Quick answers.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Still stuck? <a href="contact.html">Contact us</a>.</p></div></section>')

# ---------------- ABOUT
page("about.html","About Us | WorkNest SG","WorkNest SG is a Singapore talent resourcing agency connecting job seekers with part-time, work from home, remote and freelance roles.",
head("About Us","We believe work should make life easier, not harder.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>Why we exist</h2><p>Living in Singapore is expensive, and many capable people are stretched between bills, family and work that will not bend. Many employers, meanwhile, want flexible talent but have no time to screen applicants properly.</p>
<p>WorkNest SG is a talent resourcing agency built for the middle. We screen job seekers, match them with employers hiring part-time, work from home, remote, online and freelance talent, and introduce them properly.</p></div>
<div class="reveal"><h2>How we work</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Structured, not scattershot</h3><p>Every candidate goes through the same criteria, so introductions are fair.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Job seeker first</h3><p>Free for job seekers, consent before introductions, no pressure.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Safe by default</h3><p>Verified employers, screened talent and open advice on avoiding job scams.</p></div></div></div></div>
</div></section>
<section class="dark"><div class="wrap"><span class="eyebrow">At a glance</span><h2>What we offer</h2>
<div class="stats"><div><b>6</b>types of flexible work</div><div><b>4</b>simple steps</div><div><b>$0</b>fees for job seekers</div><div><b>SG</b>focused</div></div></div></section>
<section><div class="wrap"><p class="notice" style="max-width:70ch">WorkNest SG is a demonstration brand. Figures shown are placeholders. A real agency in Singapore must hold a valid Employment Agency licence from MOM and display its licence number.</p><div class="btn-row"><a class="btn btn-primary" href="contact.html">Get in touch</a></div></div></section>''')

# ---------------- CONTACT
page("contact.html","Contact Us | Join Our Talent Pool | WorkNest SG","Join the WorkNest SG talent pool or send an employer role brief. Part time job, work from home jobs and remote job Singapore.",
head("Contact Us","Join our talent pool, or say hello.","Tell us the work you want, or the role you need to fill. Please do not include NRIC, bank or Singpass details.")+f'''
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">I am looking for</label><select id="topic"><option>Part time job</option><option>Work from home job</option><option>Remote job</option><option>Online job</option><option>Freelance work</option><option>I am an employer hiring</option></select></div>
<div class="field"><label for="msg">Tell us a little</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send</button>
<p class="notice">Demo form: no data is sent anywhere. Connect a backend or form service before launch.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1"><h3>Thanks, we have noted it.</h3><p>In a live site we would reply within one or two working days.</p></div>
</div>
<div><h2>Other ways</h2><ul class="contact-list">
<li><b>Email</b>hello@worknest.example</li>
<li><b>Hours</b>Mon to Fri, 9am to 6pm (SGT)</li>
<li><b>Job seekers</b>Always free. We will never ask you for money.</li>
<li><b>Employers</b>Send a role brief with hours, work mode, pay range and start date.</li></ul></div>
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
