"""Generates the static pages in ../site from shared header/footer partials."""
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"

NAV = [("index.html","Home"),("services.html","Services"),("knowledge-hub.html","Knowledge Hub"),
       ("scam-check.html","Scam Check"),("glossary.html","Glossary"),("about.html","About Us")]

LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="oklch(37% .075 178)"/><path d="M16 6l8 3v6c0 5-3.4 8.6-8 11-4.600-2.400-8-6-8-11V9z" fill="oklch(97.6% .009 88)"/><path d="M12.500 16l2.700 2.700 4.500-5" stroke="oklch(60% .19 32)" stroke-width="2.400" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

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
<a class="brand" href="index.html">{LOGO}SG<em>Safer</em></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav-list">Menu</button>
<ul id="nav-list">{nav}<li><a class="cta" href="contact.html"{cur}>Contact Us</a></li></ul>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{LOGO}SG<em>Safer</em></a>
<p style="margin-top:1rem;max-width:32ch">Plain-English guidance on part-time, remote and hybrid work in Singapore.</p></div>
<div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="knowledge-hub.html">Knowledge Hub</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
<div><h4>Stay safe</h4><ul><li><a href="scam-check.html">Job scam checker</a></li><li><a href="https://www.scamshield.gov.sg" rel="noopener">ScamShield</a></li><li><a href="https://www.mom.gov.sg" rel="noopener">Ministry of Manpower</a></li><li><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="privacy.html">Privacy &amp; PDPA</a></li></ul></div>
</div>
<div class="legal"><p>SG Safer is an informational resource, not a job board, employment agency or legal adviser. Rules change; always confirm details with MOM, CPF Board or a qualified professional. Scam helpline: <strong>1799</strong>.</p>
<p>&copy; 2026 SG Safer. Demo brand for illustration.</p></div>
</div></footer>
<script src="js/main.js"></script>
</body></html>'''
    (OUT/fname).write_text(html, encoding="utf-8")

def head(eyebrow, h1, lede=""):
    return f'<div class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{"<p class=lede>"+lede+"</p>" if lede else ""}</div></div>'

# ---------------- HOME
page("index.html","SG Safer | Part-time, remote & hybrid work guide for Singapore",
"Plain-English guides on part-time, remote, hybrid and freelance work in Singapore: your rights, the jargon, and how to spot job scams.",f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Singapore work guide</span>
<h1>Flexible work, <span>without the guesswork.</span></h1>
<p class="lede">Part-time, remote, hybrid or freelance: understand what the listing really means, know your rights, and spot a scam before it costs you.</p>
<div class="btn-row"><a class="btn btn-primary" href="knowledge-hub.html">Read the Knowledge Hub</a><a class="btn btn-ghost" href="scam-check.html">Check a job offer</a></div>
</div>
<aside class="modes" aria-label="Ways of working">
<h2>Four ways people work flexibly here</h2>
<div class="mode"><i class="dot"></i><div><b>Part-time</b><small>Fewer than 35 hours a week</small></div><span class="tag">Employee</span></div>
<div class="mode"><i class="dot"></i><div><b>Remote / WFH</b><small>Work from anywhere agreed</small></div><span class="tag">Location</span></div>
<div class="mode"><i class="dot"></i><div><b>Hybrid</b><small>Split between office and home</small></div><span class="tag">Location</span></div>
<div class="mode"><i class="dot"></i><div><b>Freelance / gig</b><small>Project or platform based</small></div><span class="tag">Self-employed</span></div>
</aside></div></section>
<div class="strip"><ul><li>Part-time</li><li>Remote</li><li>Hybrid</li><li>Freelance</li><li>Internships</li><li>Contract &amp; temp</li><li>Returning to work</li></ul></div>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">What you will find here</span><h2>Everything a flexible worker asks first.</h2></div>
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Rights and rules</h3><p>Part-time terms, CPF, leave, and flexible work requests explained without legalese.</p><a class="more" href="knowledge-hub.html">Browse guides &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["shield"]}</div><h3>Scam awareness</h3><p>Fake job offers target flexible-work seekers. Run any offer through our red-flag checklist.</p><a class="more" href="scam-check.html">Open the checker &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>Recruitment glossary</h3><p>PMET, EP, S Pass, WFH, JD, notice period. Decode the keywords in every listing.</p><a class="more" href="glossary.html">Search terms &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["brief"]}</div><h3>For employers</h3><p>Designing a flexible role? Get a neutral sounding board on wording, expectations and compliance.</p><a class="more" href="services.html">See services &rarr;</a></article>
</div></div></section>

<section class="alt"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Why SG Safer</span><h2>Built around Singapore, not generic advice.</h2>
<p class="lede">Local terms, local agencies, local rules. Every guide points you to the official source so you can verify for yourself.</p></div>
<div class="reveal"><div class="types">
<div class="type" style="grid-template-columns:auto 1fr"><span class="n">01</span><div><h3>Official sources first</h3><p>MOM, CPF Board, WSG, ScamShield and MyCareersFuture.</p></div></div>
<div class="type" style="grid-template-columns:auto 1fr"><span class="n">02</span><div><h3>Plain English</h3><p>Short paragraphs, defined jargon, no fluff.</p></div></div>
<div class="type" style="grid-template-columns:auto 1fr"><span class="n">03</span><div><h3>No listings, no fees</h3><p>We do not sell jobs or ask for money from seekers.</p></div></div>
</div></div></div></section>

<section class="dark"><div class="wrap split">
<div><span class="eyebrow">Latest reading</span><h2>Start with the guide people share most.</h2>
<p>Seven signs a work-from-home offer is a scam, and what to do next.</p>
<div class="btn-row"><a class="btn btn-warm" href="article-job-scams.html">Read the guide</a></div></div>
<div><p style="font-size:1.15rem">"Easy money, no experience, chat on Telegram." If that sounds like a message you received, you are the target. Learn the pattern in five minutes.</p></div>
</div></section>
<section><div class="wrap" style="text-align:center;max-width:720px"><h2>Questions about flexible work?</h2><p class="lede" style="margin-inline:auto">Send us a message and we will point you to the right official resource.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="contact.html">Contact Us</a><a class="btn btn-ghost" href="faq.html">Read the FAQ</a></div></div></section>
''')

# ---------------- SERVICES
def svc(n,t,d): return f'<div class="type reveal"><span class="n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
page("services.html","Services | SG Safer","Guidance for job seekers and employers on part-time, remote, hybrid and freelance arrangements in Singapore.",
head("Services","Guidance for seekers and employers.","We do not place candidates or charge job seekers. We explain, review and signpost.")+f'''
<section><div class="wrap">
<div class="head"><span class="eyebrow">For job seekers</span><h2>Understand the offer before you accept it.</h2></div>
<div class="types">
{svc("01","Offer and contract explainer","Send the terms you received (with personal details removed) and get a checklist of what to clarify: hours, pay basis, CPF, leave and notice.")}
{svc("02","Scam-risk review","We walk through a suspicious message or listing against known scam patterns and tell you where to verify and report.")}
{svc("03","Flexible-work toolkit","Templates for asking your employer about remote, hybrid or reduced hours, with talking points aligned to national guidelines.")}
{svc("04","Returning-to-work roadmap","A starter path for caregivers and career-returners: part-time routes, skills funding schemes and where to get free career coaching.")}
</div></div></section>
<section class="alt"><div class="wrap">
<div class="head"><span class="eyebrow">For employers</span><h2>Design flexible roles that attract the right people.</h2></div>
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["pen"]}</div><h3>Job ad wording review</h3><p>Clear titles, work-mode labels and pay information that reduce mismatches and scam look-alikes.</p></article>
<article class="tile reveal"><div class="ic">{IC["split"]}</div><h3>Hybrid policy outline</h3><p>A neutral framework covering core hours, in-office days, equipment and how requests are handled.</p></article>
<article class="tile reveal"><div class="ic">{IC["shield"]}</div><h3>Compliance signposting</h3><p>An orientation on part-time contracts, CPF and platform-worker rules, pointing you to official guidance.</p></article>
<article class="tile reveal"><div class="ic">{IC["clock"]}</div><h3>Team workshops</h3><p>Short sessions on managing remote and part-time colleagues fairly and productively.</p></article>
</div>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Discuss your needs</a></div></div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">How it works</span><h2>Three steps.</h2></div>
<div class="types">
{svc("1","Tell us the situation","Use the contact form. Please never send NRIC, bank or Singpass details.")}
{svc("2","We reply with a plan","Usually a short written response with sources and next steps.")}
{svc("3","You decide","Everything is informational. Confirm decisions with MOM, CPF Board or a professional.")}
</div></div></section>''')

# ---------------- KNOWLEDGE HUB
posts=[
("scam","Scams","article-job-scams.html","Seven signs a work-from-home offer is a scam","Fake tasks, upfront fees and messaging-app interviews. Learn the pattern and what to do if you engaged.","6 min",True),
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
page("knowledge-hub.html","Knowledge Hub | SG Safer","Blog-style guides on part-time, remote, hybrid and freelance work in Singapore.",
head("Knowledge Hub","Guides for flexible workers in Singapore.","Short, sourced articles. Two are published; the rest are outlined and coming soon.")+f'''
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" data-filter="all" aria-pressed="true">All</button>
<button class="chip" data-filter="scam" aria-pressed="false">Scams</button>
<button class="chip" data-filter="basics" aria-pressed="false">Basics</button>
<button class="chip" data-filter="rights" aria-pressed="false">Rights</button>
<button class="chip" data-filter="career" aria-pressed="false">Career</button>
<button class="chip" data-filter="gig" aria-pressed="false">Freelance</button></div>
<div class="posts">{cards}</div></div></section>''')

# ---------------- ARTICLES
def article(fname,title,desc,cat,body):
    page(fname,title+" | SG Safer",desc,f'''{head(cat,title)}
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

# ---------------- SCAM CHECK
flags=["I was contacted first, on WhatsApp, Telegram, WeChat or SMS, without applying.",
"The pay is very high for simple tasks (liking, rating, boosting, data entry).",
"I was asked to pay a fee, deposit or top up an account.",
"There is no company email, website or verifiable business registration.",
"I am being rushed or told to keep it secret.",
"They asked for Singpass, OTP, banking details or full NRIC copies early on.",
"The interview was text-only, or I was asked to lend or open a bank account."]
lis="".join(f'<li><label><input type="checkbox"> <span>{f}</span></label></li>' for f in flags)
page("scam-check.html","Job Scam Checker | SG Safer","Tick the red flags in a job offer and get guidance.",
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
page("glossary.html","Singapore Recruitment Glossary | SG Safer","Definitions of Singapore recruitment, part-time, remote and hybrid work keywords.",
head("Glossary","Recruitment keywords, decoded.")+f'''
<section><div class="wrap" style="max-width:860px">
<label for="glossary-search" class="eyebrow">Search terms</label>
<input id="glossary-search" class="search" type="search" placeholder="Try &quot;CPF&quot; or &quot;hybrid&quot;" autocomplete="off">
<dl class="glossary">{tl}</dl><p id="glossary-empty" hidden>No matches. <a href="contact.html">Ask us to add it.</a></p></div></section>''')

# ---------------- FAQ
faqs=[("Are you a job board or agency?","No. SG Safer is informational only. We do not list vacancies, place candidates or take fees from job seekers."),
("Where can I find real part-time or remote jobs?","Start with MyCareersFuture and reputable, licensed employment agencies. Check agencies against the MOM licensed list."),
("Is a part-time job entitled to CPF?","Employees, including part-timers, generally receive CPF contributions subject to age, residency and pay. See CPF Board for current rates."),
("Can I request remote or hybrid work?","Employees can submit a formal flexible work arrangement request and employers are expected to consider it fairly under national guidelines. Approval is not guaranteed."),
("A recruiter asked me to pay a fee. Is that normal?","Be careful. Licensed agencies cannot charge job seekers more than the legal limits, and upfront payment to unlock a job is a scam hallmark."),
("How do I report a scam?","Call your bank first if money moved, then report to the Police. The ScamShield 1799 helpline can advise."),
("Can I send you my contract?","Remove NRIC, address and bank details first. We provide informational feedback, not legal advice.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html","FAQ | SG Safer","Frequently asked questions about flexible work in Singapore.",
head("FAQ","Quick answers.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Still stuck? <a href="contact.html">Contact us</a>.</p></div></section>')

# ---------------- ABOUT
page("about.html","About Us | SG Safer","SG Safer helps Singapore workers and employers understand flexible work and avoid job scams.",
head("About Us","We make flexible work easier to understand, and harder to fake.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>Why we exist</h2><p>Flexible work is growing in Singapore, and so are scams built around it. People juggling caregiving, studies or a career change deserve clear answers, not another listing feed.</p>
<p>SG Safer explains terms, rules and risks in plain English and points to the official source every time.</p></div>
<div class="reveal"><h2>What we believe</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Clarity over hype</h3><p>No "earn $500 a day" claims. Just what the rules and evidence say.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Verify everything</h3><p>We cite official sources so you can check us too.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Neutral by design</h3><p>We do not sell placements, so we have no reason to nudge you.</p></div></div></div></div>
</div></section>
<section class="dark"><div class="wrap"><span class="eyebrow">Focus areas</span><h2>What we cover</h2>
<div class="stats"><div><b>4</b>work modes explained</div><div><b>20+</b>glossary terms</div><div><b>7</b>scam red flags</div><div><b>0</b>fees for job seekers</div></div></div></section>
<section><div class="wrap"><p class="notice" style="max-width:70ch">SG Safer is a demonstration brand and website concept. Content is general information and not legal, financial or employment advice.</p><div class="btn-row"><a class="btn btn-primary" href="contact.html">Get in touch</a></div></div></section>''')

# ---------------- CONTACT
page("contact.html","Contact Us | SG Safer","Contact SG Safer with questions about flexible work in Singapore.",
head("Contact Us","Ask us anything about flexible work.","We reply with guidance and sources. Please do not include NRIC, bank or Singpass details.")+f'''
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">I am a</label><select id="topic"><option>Job seeker</option><option>Employer</option><option>Student / returner</option><option>Other</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send message</button>
<p class="notice">Demo form: no data is sent anywhere. Connect a backend or form service before launch.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1"><h3>Thanks, message noted.</h3><p>In a live site we would reply within a few working days.</p></div>
</div>
<div><h2>Other ways</h2><ul class="contact-list">
<li><b>Email</b>hello@sgsafer.example</li>
<li><b>Hours</b>Mon to Fri, 9am to 6pm (SGT)</li>
<li><b>Scam emergency</b>Call your bank and the ScamShield helpline 1799. We are not an emergency service.</li>
<li><b>Official help</b><a href="https://www.mom.gov.sg" rel="noopener">MOM</a>, <a href="https://www.cpf.gov.sg" rel="noopener">CPF Board</a>, <a href="https://www.wsg.gov.sg" rel="noopener">WSG</a></li></ul></div>
</div></section>''')

# ---------------- PRIVACY
page("privacy.html","Privacy & PDPA | SG Safer","How SG Safer handles personal data under Singapore's PDPA.",
head("Privacy &amp; PDPA","Privacy notice")+'''
<section><div class="wrap article">
<p>This is a template. Have it reviewed before launch.</p>
<h2>What we collect</h2><p>Only what you submit through the contact form: name, email and message. The scam checker runs in your browser and stores nothing.</p>
<h2>How we use it</h2><p>To reply to your enquiry. We do not sell personal data.</p>
<h2>Your rights</h2><p>Under Singapore's Personal Data Protection Act you may request access to or correction of your data, or withdraw consent, by emailing our Data Protection Officer at dpo@sgsafer.example.</p>
<h2>Cookies</h2><p>This site sets no tracking cookies. Fonts are loaded from Google Fonts.</p></div></section>''')
print("built")
