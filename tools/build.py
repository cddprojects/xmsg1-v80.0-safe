"""Generates the static pages in ../site from shared header/footer partials."""
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"

NAV = [("index.html","Home"),("services.html","Services"),("for-employers.html","Employers"),("for-talent.html","Talent"),
       ("knowledge-hub.html","Knowledge Hub"),("about.html","About Us")]

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
<p style="margin-top:1rem;max-width:32ch">Talent resourcing and career consulting for part-time, remote and hybrid work in Singapore.</p></div>
<div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="for-employers.html">For employers</a></li><li><a href="for-talent.html">For talent</a></li><li><a href="knowledge-hub.html">Knowledge Hub</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
<div><h4>Resources</h4><ul><li><a href="scam-check.html">Job scam checker</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="https://www.scamshield.gov.sg" rel="noopener">ScamShield</a></li><li><a href="https://www.mom.gov.sg" rel="noopener">Ministry of Manpower</a></li><li><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="privacy.html">Privacy &amp; PDPA</a></li></ul></div>
</div>
<div class="legal"><p>SG Safer is a demonstration brand. EA Licence No.: [placeholder, required for a real agency]. Guides are general information, not legal advice; confirm details with MOM or CPF Board. Scam helpline: <strong>1799</strong>.</p>
<p>&copy; 2026 SG Safer. Demo brand for illustration.</p></div>
</div></footer>
<script src="js/main.js"></script>
</body></html>'''
    (OUT/fname).write_text(html, encoding="utf-8")

def head(eyebrow, h1, lede=""):
    return f'<div class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{"<p class=lede>"+lede+"</p>" if lede else ""}</div></div>'

def svc(n,t,d): return f'<div class="type reveal"><span class="n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
# ---------------- HOME
page("index.html","SG Safer | Talent resourcing & career consulting in Singapore",
"Singapore talent resourcing for part-time, remote, hybrid and contract roles. We handle initial screening for employers and career consulting for candidates.",f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Talent resourcing &middot; Singapore</span>
<h1>The right people, <span>screened before they reach you.</span></h1>
<p class="lede">SG Safer is a talent resourcing and career consulting practice for flexible work: part-time, remote, hybrid and contract. We do the initial screening for employers and guide candidates to roles that fit.</p>
<div class="btn-row"><a class="btn btn-primary" href="for-employers.html">I am hiring</a><a class="btn btn-ghost" href="for-talent.html">I am looking for work</a></div>
</div>
<aside class="modes" aria-label="What we screen for">
<h2>Roles we resource</h2>
<div class="mode"><i class="dot"></i><div><b>Part-time</b><small>Admin, operations, education, retail, F&amp;B</small></div><span class="tag">Fewer than 35 hrs</span></div>
<div class="mode"><i class="dot"></i><div><b>Remote</b><small>Support, content, data, marketing, virtual assistants</small></div><span class="tag">Location-free</span></div>
<div class="mode"><i class="dot"></i><div><b>Hybrid</b><small>Executives and specialists split across office and home</small></div><span class="tag">Flexible</span></div>
<div class="mode"><i class="dot"></i><div><b>Contract / temp</b><small>Project cover, seasonal peaks, maternity cover</small></div><span class="tag">Fixed term</span></div>
</aside></div></section>
<div class="strip"><ul><li>Initial screening</li><li>Shortlisting</li><li>Career consulting</li><li>Reference checks</li><li>Flexible workforce</li><li>Returning to work</li></ul></div>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">What we do</span><h2>Two sides of one hiring conversation.</h2></div>
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["brief"]}</div><h3>For employers</h3><p>We source, screen and shortlist so your team only meets candidates who match the role, the schedule and the culture.</p><a class="more" href="for-employers.html">How we help employers &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>For candidates</h3><p>One-to-one career consulting: CV and profile review, role matching and interview preparation for flexible work.</p><a class="more" href="for-talent.html">How we help candidates &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["shield"]}</div><h3>Screening you can rely on</h3><p>Identity, work eligibility, experience and reference checks done consistently, with a clear summary for each person.</p><a class="more" href="services.html">See our screening &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Knowledge Hub</h3><p>Guides on flexible work rules, hiring practice and Singapore recruitment terms.</p><a class="more" href="knowledge-hub.html">Read the guides &rarr;</a></article>
</div></div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Our screening process</span><h2>From brief to shortlist in four steps.</h2></div>
<div class="types">
{svc("01","Brief","We clarify the role: hours, work mode, pay range, must-haves and team context.")}
{svc("02","Source","We reach into our talent network and approved channels. No mass blasting.")}
{svc("03","Screen","Structured phone or video interview, skills and availability check, eligibility and reference verification.")}
{svc("04","Shortlist","You receive a concise profile for each candidate with our assessment and a recommendation.")}
</div></div></section>

<section class="dark"><div class="wrap split">
<div><span class="eyebrow">Why flexible-work specialists</span><h2>Part-time and remote hiring has different risks.</h2>
<p>Availability, self-management, communication style and reliability matter more when nobody sits next to the person. Our screening is built around them.</p></div>
<div><div class="stats" style="margin-top:0"><div><b>4</b>screening stages</div><div><b>48h</b>target first shortlist*</div><div><b>1:1</b>candidate consulting</div></div><p class="notice" style="margin-top:1.5rem;color:inherit;opacity:.7">*Illustrative target for demonstration. Update with real service levels.</p></div>
</div></section>
<section><div class="wrap" style="text-align:center;max-width:720px"><h2>Tell us who you need, or where you want to go.</h2><p class="lede" style="margin-inline:auto">A short conversation is all it takes to start.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="contact.html">Contact Us</a><a class="btn btn-ghost" href="services.html">View services</a></div></div></section>
''')

# ---------------- SERVICES
page("services.html","Services | SG Safer","Initial screening, shortlisting, flexible workforce resourcing and career consulting in Singapore.",
head("Services","Screening, shortlisting and career consulting.","Talent resourcing for flexible roles, plus one-to-one guidance for candidates.")+f'''
<section><div class="wrap">
<div class="head"><span class="eyebrow">Talent resourcing</span><h2>For employers hiring flexible talent.</h2></div>
<div class="types">
{svc("01","Initial screening","Structured first-round interviews against your role brief: skills, availability, communication, motivation and expectations on pay and work mode.")}
{svc("02","Candidate shortlisting","A concise, ranked shortlist with a written assessment for each person so your hiring managers spend time only on strong matches.")}
{svc("03","Flexible workforce sourcing","Part-time, remote, hybrid, contract and temporary talent, including seasonal and project cover.")}
{svc("04","Verification and reference checks","Identity, right-to-work eligibility, qualification and reference checks, carried out with candidate consent under PDPA.")}
{svc("05","Role design advice","Help shaping hours, work mode, pay bands and job-ad wording so you attract the right applicants.")}
{svc("06","Onboarding support","Structured check-ins in the first weeks to keep part-time and remote hires engaged and settled.")}
</div><div class="btn-row"><a class="btn btn-primary" href="for-employers.html">Employer details</a></div></div></section>
<section class="alt"><div class="wrap">
<div class="head"><span class="eyebrow">Career consulting</span><h2>For candidates seeking flexible work.</h2></div>
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>CV and profile review</h3><p>Positioning your experience for part-time, remote and hybrid roles.</p></article>
<article class="tile reveal"><div class="ic">{IC["split"]}</div><h3>Role matching</h3><p>We discuss your availability, goals and pay expectations, then match you to suitable openings.</p></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>Interview coaching</h3><p>Practice for video interviews and questions about self-management.</p></article>
<article class="tile reveal"><div class="ic">{IC["clock"]}</div><h3>Career-return support</h3><p>A plan for caregivers, career-switchers and mature workers rejoining the workforce.</p></article>
</div>
<div class="btn-row"><a class="btn btn-primary" href="for-talent.html">Candidate details</a></div></div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">Our promise</span><h2>Clear terms on both sides.</h2></div>
<div class="types">
{svc("-","Candidates pay nothing","Our consulting and placement is funded by employer clients. No fees, deposits or training charges for candidates.")}
{svc("-","Consent first","We only share a candidate profile with an employer after the candidate agrees.")}
{svc("-","Transparent","Role, pay range and work mode are shared before any interview.")}
</div></div></section>''')

# ---------------- FOR EMPLOYERS
page("for-employers.html","For Employers | SG Safer","Outsource initial screening and shortlisting for part-time, remote, hybrid and contract roles in Singapore.",
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
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">Typical roles</span><h2>Where employers use us most.</h2></div>
<div class="tiles">
<article class="tile"><h3>Admin and operations</h3><p>Coordinators, receptionists, data entry, executive assistants.</p></article>
<article class="tile"><h3>Customer support</h3><p>Remote chat and email agents, service ambassadors.</p></article>
<article class="tile"><h3>Marketing and content</h3><p>Social media, design, writing, video editing freelancers.</p></article>
<article class="tile"><h3>Education and services</h3><p>Tutors, centre assistants, admin for SMEs and schools.</p></article>
</div><div class="btn-row"><a class="btn btn-primary" href="contact.html">Send us a role brief</a></div></div></section>''')

# ---------------- FOR TALENT
page("for-talent.html","For Talent | SG Safer","Career consulting for Singapore candidates seeking part-time, remote, hybrid and contract work.",
head("For Talent","Find flexible work that actually fits your life.","One-to-one career consulting, free for candidates.")+f'''
<section><div class="wrap">
<div class="types">
{svc("01","Intro conversation","A 20 to 30 minute call about your experience, availability and what a good role looks like for you.")}
{svc("02","Profile tune-up","Feedback on your CV and online profile, tailored to flexible and remote roles.")}
{svc("03","Screening interview","The same structured screening employers rely on, so you present yourself well.")}
{svc("04","Match and introduce","With your consent, we introduce you to suitable openings and prepare you for the interview.")}
</div></div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">Who we help</span><h2>Flexible work suits many stages of life.</h2>
<ul><li>Students seeking part-time or holiday work</li><li>Caregivers and parents returning to work</li><li>Mid-career switchers</li><li>Mature workers looking for reduced hours</li><li>Professionals building a freelance portfolio</li></ul></div>
<div><h2>Staying safe while job hunting</h2><p>Fake job offers target people looking for flexible work. Legitimate consultants do not charge candidates or ask for bank logins. Learn the signs with our <a href="scam-check.html">scam checker</a> and <a href="glossary.html">glossary</a>.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Book a consultation</a></div></div>
</div></section>''')


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
head("Knowledge Hub","Guides on flexible work and hiring in Singapore.","Short, sourced articles. Two are published; the rest are outlined and coming soon.")+f'''
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
faqs=[("Are you a job board?","No. We are a talent resourcing and career consulting practice. We screen and shortlist for employers and coach candidates, rather than publish open listings."),
("Do candidates pay you?","No. Our services are paid by employer clients. Be cautious of anyone who asks a candidate for fees or deposits."),
("What does initial screening include?","A structured interview against the role brief, skills and availability checks, and, with consent, eligibility and reference verification."),
("How quickly can I get a shortlist?","It depends on the role and market. We agree an expected timeline in the brief. Figures on this demo site are illustrative."),
("What roles do you cover?","Part-time, remote, hybrid, contract and temporary roles, mainly admin, support, marketing, education and operations."),
("Is candidate data protected?","We handle personal data under Singapore's PDPA and only share a profile with an employer after the candidate consents. See our Privacy page."),
("Is a part-time job entitled to CPF?","Employees, including part-timers, generally receive CPF contributions subject to age, residency and pay. See CPF Board for current rates."),
("Can I request remote or hybrid work from my employer?","Employees can submit a formal flexible work arrangement request and employers are expected to consider it fairly under national guidelines. Approval is not guaranteed.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html","FAQ | SG Safer","Frequently asked questions about SG Safer's talent resourcing and career consulting.",
head("FAQ","Quick answers.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Still stuck? <a href="contact.html">Contact us</a>.</p></div></section>')

# ---------------- ABOUT
page("about.html","About Us | SG Safer","SG Safer is a Singapore talent resourcing and career consulting practice focused on flexible work.",
head("About Us","A talent resourcing practice for flexible work.")+f'''
<section><div class="wrap split">
<div class="reveal"><h2>Why we exist</h2><p>Part-time, remote and hybrid roles attract large numbers of applicants, and screening them properly takes time many small teams do not have. At the same time, candidates want honest guidance on roles that fit their lives.</p>
<p>SG Safer sits in the middle. We do the initial screening for employers and act as career consultants for candidates, so both sides meet with confidence.</p></div>
<div class="reveal"><h2>How we work</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Structured, not scattershot</h3><p>Every candidate goes through the same criteria, so comparisons are fair.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Candidate-first ethics</h3><p>Free for candidates, consent before introductions, no pressure.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Safe by default</h3><p>Verified employers, verified talent, and open advice on avoiding job scams.</p></div></div></div></div>
</div></section>
<section class="dark"><div class="wrap"><span class="eyebrow">At a glance</span><h2>What we offer</h2>
<div class="stats"><div><b>2</b>audiences served</div><div><b>4</b>screening stages</div><div><b>0</b>fees for candidates</div><div><b>SG</b>focused</div></div></div></section>
<section><div class="wrap"><p class="notice" style="max-width:70ch">SG Safer is a demonstration brand. Statistics and service levels shown are placeholders. A real agency must hold a valid Employment Agency licence from MOM and display its licence number.</p><div class="btn-row"><a class="btn btn-primary" href="contact.html">Get in touch</a></div></div></section>''')

# ---------------- CONTACT
page("contact.html","Contact Us | SG Safer","Contact SG Safer to brief a role or book a career consultation.",
head("Contact Us","Brief a role, or book a consultation.","Tell us a little and we will reply with next steps. Please do not include NRIC, bank or Singpass details.")+f'''
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="topic">I am</label><select id="topic"><option>An employer hiring</option><option>A candidate seeking work</option><option>Returning to work</option><option>Other</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send message</button>
<p class="notice">Demo form: no data is sent anywhere. Connect a backend or form service before launch.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1"><h3>Thanks, message noted.</h3><p>In a live site we would reply within one or two working days.</p></div>
</div>
<div><h2>Other ways</h2><ul class="contact-list">
<li><b>Email</b>hello@sgsafer.example</li>
<li><b>Hours</b>Mon to Fri, 9am to 6pm (SGT)</li>
<li><b>Employers</b>Send a role brief with hours, work mode, pay range and start date.</li>
<li><b>Candidates</b>Consultations are free. We will never ask you for money.</li></ul></div>
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
