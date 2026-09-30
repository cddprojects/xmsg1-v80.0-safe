# Long-form job type guides and extra articles. Executed from build.py (shares its globals).

def _li(items): return "".join(f"<li>{i}</li>" for i in items)

def jobpage(fname,cls,eyebrow,h1,seo_title,seo_desc,intro,facts,roles,week,steps,know,questions,mistakes,faqs,related):
    facts_html="".join(f"<dt>{k}</dt><dd>{v}</dd>" for k,v in facts)
    roles_html="".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in roles)
    week_html="".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in week)
    steps_html="".join(f'<li><b>{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(steps))
    know_html="".join(f'<article class="tile"><h3>{t}</h3><p>{d}</p></article>' for t,d in know)
    faq_html="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
    rel_html="".join(f'<a class="rel" href="{h}"><b>{t}</b><span>{d}</span></a>' for h,t,d in related)
    body=f'''
<div class="page-head jobhero {cls}"><div class="wrap jh-grid">
<div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{intro}</p>
<div class="btn-row"><a class="btn btn-primary" href="join.html">Join our community</a><a class="btn btn-ghost" href="jobs.html">Compare all job types</a></div></div>
<aside class="qf" aria-label="Quick facts"><h2>Quick facts</h2><dl>{facts_html}</dl><p class="rv">Last reviewed September 2026</p></aside>
</div></div>
<section><div class="wrap"><div class="head"><span class="eyebrow">Common roles</span><h2>What people actually do in this kind of work.</h2></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Role</th><th>What it involves</th></tr></thead><tbody>{roles_html}</tbody></table></div></div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">A sample week</span><h2>What it can look like alongside your day.</h2><p class="lede">An illustrative example only. Real schedules depend on the employer.</p></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Day</th><th>Time</th><th>Activity</th></tr></thead><tbody>{week_html}</tbody></table></div></div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">How to get started</span><h2>{len(steps)} steps.</h2></div><ol class="steps">{steps_html}</ol></div></section>
<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">Before you accept</span><h2>What to know about terms, pay and CPF.</h2></div><div class="tiles">{know_html}</div></div></section>
<section><div class="wrap split"><div><h2>Questions to ask</h2><ul class="qlist">{_li(questions)}</ul></div><div><h2>Mistakes to avoid</h2><ul class="qlist bad">{_li(mistakes)}</ul></div></div></section>
<section class="alt"><div class="wrap" style="max-width:860px"><div class="head"><span class="eyebrow">FAQ</span><h2>Common questions.</h2></div>{faq_html}</div></section>
<section><div class="wrap"><div class="head"><span class="eyebrow">Keep reading</span><h2>Related guides.</h2></div><div class="rels">{rel_html}</div>
<p class="notice" style="margin-top:1.5rem">General information only. Earnings, hours and conditions vary by employer and are not guaranteed. Confirm details with <a href="https://www.mom.gov.sg" rel="noopener">MOM</a>, <a href="https://www.cpf.gov.sg" rel="noopener">CPF Board</a> or <a href="https://www.iras.gov.sg" rel="noopener">IRAS</a>.</p></div></section>
<section class="cta-band"><div class="wrap"><h2>Want more guides like this?</h2><p class="lede">Join our community for new guides on flexible work in Singapore.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-warm" href="join.html">Join our community</a><a class="btn btn-ghost-light" href="knowledge-hub.html">Knowledge Hub</a></div></div></section>'''
    page(fname,seo_title,seo_desc,body)

R_FLEX=("article-flexible-work-request.html","How to ask your employer for flexible work","Step-by-step: putting in a request")
R_CPF=("article-part-time-cpf.html","Part-time work and CPF","What to check on your payslip")
R_AD=("article-read-job-ad.html","How to read a Singapore job ad","Decode pay, hours and terms")
R_CV=("article-remote-cv.html","A CV for remote roles","Show you can work independently")
R_MODES=("article-work-modes.html","Part-time, remote, hybrid, freelance","What each really means")
def rel(*ks): return [k for k in ks]

WEEK_NOTE=None

jobpage("part-time-jobs-singapore.html","jh1","Part time job Singapore","Part time jobs in Singapore: roles, hours and what to check",
"Part Time Job Singapore: Roles, Hours, CPF and How to Start | WorkNest SG",
"A practical guide to part time job Singapore: common roles, typical hours, how to start, and what to check on contracts, pay and CPF before you accept.",
"A part time job is the most common way to add a second income in Singapore. In Singapore, an employee contracted for fewer than 35 hours a week is classed as part-time. You still have an employment contract, with many entitlements worked out in proportion to your hours.",
[("Typical hours","Fewer than 35 a week"),("Where","On-site, sometimes from home"),("Usual status","Employee"),("CPF","Generally applies for employees*"),("Good for","Students, parents, caregivers, anyone adding a second income")],
[("Retail and F&amp;B crew","Serving customers, handling payments, restocking and closing. Often shift-based, with evenings and weekends."),("Admin assistant","Filing, data entry, scheduling, answering enquiries. Usually weekday hours."),("Tutor or centre assistant","Teaching or supporting classes, marking, front desk. Peak hours are after school and weekends."),("Events and promotions","Short, project-based shifts at exhibitions or promotions."),("Customer service associate","Handling calls, chat and email enquiries, often in set shifts.")],
[("Tuesday","6pm to 10pm","Evening shift"),("Thursday","6pm to 10pm","Evening shift"),("Saturday","10am to 6pm","Weekend shift"),("Other days","Free","Study, family or your main job")],
[("Work out your real availability","List the days and time slots you can commit to every week, including travel time. Be realistic: reliability matters more than maximum hours."),("Prepare a one-page CV","Lead with reliability, availability and any customer-facing experience. Keep it to one page."),("Search trusted sources","Browse MyCareersFuture and the careers pages of employers you know. Read the full listing, including hours and pay."),("Check the terms","Confirm hours, pay rate, pay date, CPF and leave before you say yes. Ask for it in writing."),("Start and review","After a few weeks, check the hours still suit you. Raise any issues early.")],
[("Hours and contract","You should receive written terms including your hours and pay rate. Part-time employees are covered by the Employment Act, so check the details with MOM."),("Pay","You should get an itemised payslip. Salary is generally due within seven days after the end of the salary period; confirm on the MOM website."),("Leave and CPF","Leave entitlements are pro-rated for part-time employees. CPF contributions apply to employees who are Singapore Citizens or PRs, subject to age and pay. See CPF Board."),("Holding a full-time job","Check your existing contract for limits on outside work and whether you need approval. Work pass holders should check with MOM first.")],
["How many hours a week, and are they fixed or rostered?","What is the hourly or monthly rate, and when is it paid?","Is this an employee contract with CPF?","How much notice do I get for shift changes?","Is there a probation period and what is the notice period?","Who do I contact if my hours need to change?"],
["Accepting without knowing the hours","Not asking whether pay is hourly or monthly","Overcommitting and burning out","Ignoring the terms in your main job's contract"],
[("How many hours is a part time job in Singapore?","An employee contracted to work fewer than 35 hours a week is classed as part-time under Singapore's part-time employment rules."),("Do part-time employees get leave?","Yes, generally on a pro-rated basis. Check the current rules on the MOM website."),("Can I do a part time job and keep my full-time job?","Often yes, but read your full-time contract first. Some employers require approval for outside work.")],
[("article-part-time-cpf.html","Part-time work and CPF","What to check on your payslip"),("article-read-job-ad.html","How to read a Singapore job ad","Decode pay, hours and terms"),("work-from-home-jobs-singapore.html","Work from home jobs","The next guide")])

jobpage("work-from-home-jobs-singapore.html","jh2","Work from home jobs Singapore","Work from home jobs in Singapore: what they involve and how to start",
"Work From Home Jobs Singapore: Roles, Setup and What to Ask | WorkNest SG",
"Guide to work from home jobs Singapore: common roles, a sample week, the setup you need, and what to check on contracts and expectations for work from home in Singapore.",
"Work from home in Singapore usually means doing a defined job from home, on agreed hours, for an employer. It is common in customer support, admin and content. It is different from freelancing, where you are self-employed.",
[("Typical hours","Agreed hours, part or full time"),("Where","From home"),("Usual status","Usually employee"),("CPF","Generally applies for employees*"),("Good for","Parents, caregivers, anyone saving commute time")],
[("Customer support agent","Answering customers by chat, email or phone using company systems."),("Data entry and back-office admin","Updating records, processing forms, checking data accuracy."),("Virtual assistant","Managing calendars, inboxes and bookings for a business or individual."),("Content and social media support","Drafting posts, scheduling, basic graphics, community replies."),("Transcription and translation","Turning audio into text or translating documents, often paid per task.")],
[("Monday to Friday","9am to 1pm","Core support shift from home"),("Wednesday","2pm to 3pm","Team check-in by video"),("Weekend","Free","Fully off")],
[("Set up a workspace","A quiet spot, a reliable internet connection and a laptop are the basics. Ask whether the employer provides equipment."),("List your transferable skills","Communication, accuracy and tools you already use (email, spreadsheets, chat platforms)."),("Search official channels","Use MyCareersFuture and verified employer careers pages. Read whether the role is employee or freelance."),("Ask about expectations","Response times, core hours, tools, supervision and how performance is measured."),("Confirm the terms in writing","Hours, pay, CPF, equipment and notice period.")],
[("Employee or freelance","Employees have a contract of service, CPF and leave. Freelancers are self-employed and manage their own CPF and tax. The role title alone does not tell you which applies."),("Equipment and costs","Ask who provides the laptop and software, and whether you are expected to cover internet or electricity."),("Data and privacy","If you handle customer data, you may need to follow company data protection rules, in line with the PDPA."),("Working hours","Agree core hours and how you record time. Remote work still has defined hours.")],
["Is this an employee role or freelance?","What are my core hours and how is time tracked?","Who provides the equipment and software?","How is pay calculated and when is it paid?","Is there paid training?","Can hours change, and with how much notice?"],
["Assuming work from home means no fixed hours","Not checking whether CPF applies","Using a shared or unsecured device for company data","Skipping the written terms"],
[("Are work from home jobs in Singapore real?","Yes. Many employers hire for support, admin and content roles that can be done from home. Check the employer and the terms as you would for any job."),("What is the difference between work from home and remote?","Work from home usually means working from your home on set hours. Remote can mean any location and sometimes an overseas team. See our remote job guide."),("Do I need my own laptop?","It depends on the employer. Ask before accepting.")],
[("remote-jobs-singapore.html","Remote jobs in Singapore","The wider picture"),("article-work-modes.html","Part-time, remote, hybrid, freelance","What each really means"),("article-flexible-work-request.html","How to ask for flexible work","If you already have a job")])

jobpage("remote-jobs-singapore.html","jh3","Remote job Singapore","Remote jobs in Singapore: skills, employers and what to clarify",
"Remote Job Singapore: Roles, Skills, Time Zones and Tax | WorkNest SG",
"Guide to remote job Singapore: common roles, skills employers look for, time zone and employer-entity questions, and how tax and CPF can differ.",
"A remote job means your location is flexible. Some remote roles are with Singapore companies, others with overseas teams that need overlap with Singapore hours. The details matter more here than in other job types.",
[("Typical hours","Part or full time"),("Where","Anywhere, with agreed overlap hours"),("Usual status","Employee or contractor"),("CPF","Depends on employer and status*"),("Good for","People with specialist skills who are self-directed")],
[("Digital marketing and SEO","Planning campaigns, content, reporting and search optimisation."),("Graphic and web design","Visual assets, layouts and websites for brands."),("Software and QA","Building or testing software with a distributed team."),("Account or project management","Coordinating clients, timelines and deliverables online."),("Customer success","Onboarding and supporting customers of software or online services.")],
[("Monday to Thursday","9am to 5pm","Core hours, with a daily stand-up"),("Friday","9am to 1pm","Shorter day, planning and reporting"),("Weekend","Free","Off")],
[("Show your skills","Build a small portfolio or work sample. Remote employers cannot watch you work, so results matter."),("Target the right roles","Search by skill and by whether the role is open to Singapore-based staff."),("Check who the employer is","Confirm the legal employer, its location and how you will be paid."),("Prepare for video interviews","Test your camera, audio and connection. Have examples of working independently."),("Clarify tax and CPF","Ask how employment, tax and CPF are handled for your situation.")],
[("Employer entity","CPF contributions are tied to employment with a Singapore employer. With an overseas employer or as a contractor, your position can differ. Check with CPF Board and IRAS."),("Time zone","Ask which hours you must be available and how flexible they are."),("Pay","Confirm currency, payment method and timing, and any conversion or bank fees."),("Work passes","If you are on a work pass, extra employment generally needs MOM approval. Check before you start.")],
["Who is my legal employer and where are they based?","Which time zone and core hours apply?","Am I an employee or a contractor?","What currency and payment method?","What equipment and tools are provided?","How will tax and CPF be handled?"],
["Ignoring the time zone overlap","Assuming an overseas contractor role includes CPF","Not keeping a record of income for tax","Skipping written terms"],
[("Are remote jobs in Singapore only for tech workers?","No. Marketing, design, support, project management and content roles are commonly remote."),("Do remote employers need me to be in Singapore?","Some do for tax or legal reasons and some do not. Ask early."),("Do I pay tax on income from an overseas employer?","Tax treatment depends on your situation. Check IRAS or a tax professional.")],
[("freelance-jobs-singapore.html","Freelance jobs in Singapore","If you would rather be self-employed"),("article-remote-cv.html","A CV for remote roles","Show you can work independently"),("online-jobs-singapore.html","Online jobs","Work delivered fully online")])

jobpage("online-jobs-singapore.html","jh4","Online jobs","Online jobs and online work from home in Singapore",
"Online Jobs Singapore: Online Work From Home Roles and What to Check | WorkNest SG",
"Guide to online jobs and online work from home in Singapore: common roles, a sample week, how to start, and questions to ask about pay and terms.",
"Online jobs are roles delivered entirely over the internet, from live teaching to moderating and research. Legitimate online work is paid by an identifiable business for defined work.",
[("Typical hours","Flexible slots or set sessions"),("Where","Online"),("Usual status","Varies: employee or freelance"),("CPF","Depends on status*"),("Good for","People who want flexible slots and enjoy screen-based work")],
[("Online tutor","Teaching students one-to-one or in groups over video."),("Community and chat moderator","Keeping online spaces safe and on-topic."),("Online researcher or data labeller","Finding, checking or tagging information for projects."),("E-commerce support","Listing products, processing orders and answering shop enquiries."),("Virtual event support","Managing chat, registrations and tech at online events.")],
[("Tuesday","7pm to 9pm","Online tutoring sessions"),("Thursday","7pm to 9pm","Online tutoring sessions"),("Sunday","2pm to 5pm","Order and listing support")],
[("Pick a skill to offer","Teaching, writing, research, admin or customer support are all in demand online."),("Prepare your tools","Reliable internet, a quiet space and the software the role needs."),("Look for an identifiable business","You should be able to find who is paying you and how."),("Get the terms in writing","Rate, hours, payment date and whether you are an employee or freelancer."),("Start small and review","Take a trial period or small first batch of work, then decide.")],
[("Who pays you","You should know the business name and how you will be paid before you start."),("Fees","Genuine employers do not ask you to pay to begin work. If a registration or equipment fee is requested, pause and verify."),("Status","Online roles can be employment or freelance. This changes CPF, leave and tax."),("Trial periods","Ask whether the first tasks are paid and on what terms.")],
["Who is the business and how can I verify it?","Am I paid per hour, per task or per month?","When and how is payment made?","Is there any fee for me to start? (There should not be.)","Is this employment or freelance?","What happens if sessions are cancelled?"],
["Paying a fee to get started","Working without knowing who pays you","Ignoring the tax on freelance income","Relying on chat-app messages instead of written terms"],
[("Are online jobs real?","Many are. Online tutoring, moderation and support are established roles. Check the employer and the terms."),("What is online work from home?","Work you do from home over the internet, such as tutoring, support or admin, for a set rate."),("Do online jobs pay CPF?","Only if you are an employee under a contract of service. Freelancers manage their own contributions.")],
[("work-from-home-jobs-singapore.html","Work from home jobs","Set-hours roles from home"),("freelance-jobs-singapore.html","Freelance jobs","Self-employed online work"),("article-read-job-ad.html","How to read a job ad","Decode pay and terms")])

jobpage("freelance-jobs-singapore.html","jh5","Freelance jobs","Freelance jobs in Singapore: how to start and what to know",
"Freelance Jobs Singapore: How to Start, Contracts, Tax and MediSave | WorkNest SG",
"Guide to freelance jobs in Singapore: common freelance roles, how to find clients, contracts, invoicing, tax and MediSave basics.",
"Freelance work is project-based and you are self-employed. You choose your clients and schedule, but you also manage your own contracts, invoices, tax and contributions.",
[("Typical hours","You decide"),("Where","Anywhere"),("Usual status","Self-employed"),("CPF","You manage your own contributions*"),("Good for","People with a portfolio or specialist skill")],
[("Design and branding","Logos, social graphics, layouts and illustrations."),("Writing and translation","Articles, copy, editing and translation."),("Video and photo editing","Editing footage, photos and short-form content."),("Bookkeeping and admin","Recording transactions and organising records for small businesses."),("Web and app development","Building and maintaining websites and small apps.")],
[("Monday","9am to 12pm","Client project A"),("Tuesday to Wednesday","10am to 3pm","Client project B and admin"),("Thursday","Afternoon","Invoicing and finding new clients"),("Friday","Free","Time off or main job")],
[("Choose your niche","Focus on one or two services you can do well and explain in a sentence."),("Build a portfolio","Two or three strong samples are enough to start."),("Decide how to price","Hourly or per-project. Include your time for revisions, admin and tax."),("Find clients","Referrals, your network, online platforms and professional profiles."),("Put it in writing","Use a written agreement covering scope, deadlines, revisions and payment terms."),("Track income for tax","Record every payment. You must declare freelance income.")],
[("Contract for services","Agree scope, deadline, revisions and payment terms in writing. Consider a deposit for larger projects."),("Tax","Income from freelance work is taxable and must be declared to IRAS. Keep records of income and expenses."),("MediSave","Self-employed persons may need to contribute to MediSave depending on their income. Check CPF Board."),("Business registration","Depending on how you trade, you may need to register a business with ACRA. Check ACRA and IRAS.")],
["What exactly is included in the project?","How many revisions are included?","What is the payment schedule and due date?","Who owns the final work?","Is a deposit required?","What is the process if the scope changes?"],
["Working without a written agreement","Underpricing and forgetting admin time","Not tracking income for tax","Taking on too many clients at once"],
[("Do freelancers pay CPF?","Freelancers do not receive employer CPF contributions. Self-employed persons may need to contribute to MediSave depending on income. Check CPF Board."),("Do I need to register a business to freelance?","It depends on how you operate. Check ACRA and IRAS for your situation."),("How do I find freelance clients in Singapore?","Common routes are referrals, professional networks and online platforms.")],
[("remote-jobs-singapore.html","Remote jobs","If you prefer being employed"),("article-work-modes.html","What each term means","Freelance vs employee"),("make-money-at-home-singapore.html","Make money at home","Compare the routes")])

jobpage("make-money-at-home-singapore.html","jh6","Make money at home","How to make money at home in Singapore: the main routes compared",
"Make Money at Home in Singapore: Part-Time, Freelance and Online Work Compared | WorkNest SG",
"Compare the main ways to make money at home in Singapore: part time job, work from home jobs, online work from home and freelance jobs, with a simple calculator.",
"Most people who want to make money at home in Singapore choose one of four routes: a part-time job, a work from home job, online work or freelance projects. Each suits different hours, skills and need for stability.",
[("Routes","Part-time, work from home, online, freelance"),("Time needed","From a few hours a week"),("Best start","Match your hours to the route"),("Earnings","Vary by role and skills, never guaranteed")],
[("Part-time employment","Steady hours and a contract, at a workplace or from home. <a href='part-time-jobs-singapore.html'>Read the guide</a>."),("Work from home job","Defined role and hours, done from home. <a href='work-from-home-jobs-singapore.html'>Read the guide</a>."),("Online work","Tutoring, moderation, research and support. <a href='online-jobs-singapore.html'>Read the guide</a>."),("Freelance projects","Paid per project, you set the schedule. <a href='freelance-jobs-singapore.html'>Read the guide</a>.")],
[("Step 1","Set a monthly target","How much extra income do you want each month?"),("Step 2","Estimate an hourly rate","Use a rate from a real listing or your own quote."),("Step 3","Calculate hours per week","Use the calculator on this page.")],
[("Decide your target","Write down the extra monthly income you need, and your fixed costs."),("Count your free hours","Be honest about how many hours a week you can commit."),("Pick the route","Steady hours suit part-time. Skills and control suit freelance."),("Search official sources","MyCareersFuture and employers' own pages are good places to look."),("Review after a month","Check that hours, pay and energy levels still work.")],
[("Realistic expectations","Earnings depend on the role, your skills and hours. Be sceptical of any offer that promises high pay for little effort."),("Costs","Factor in transport, equipment, internet and any tax on your income."),("Your rights","Employees have contracts, CPF and leave. Freelancers manage their own tax and contributions."),("Balance","A second income should not burn you out. Build in rest.")],
["How many hours can I commit each week?","Do I need steady income or flexible work?","Is this employment or self-employment?","What costs will I have?","How will I record income for tax?","Does my main job allow outside work?"],
["Chasing offers that promise easy money","Ignoring costs and tax","Taking on more hours than you can sustain","Skipping written terms"],
[("What is the easiest way to make money at home in Singapore?","There is no single easiest route. It depends on your skills and hours. Part-time and work from home jobs offer steady hours. Freelance offers control."),("Can I make money at home with no experience?","Some entry-level roles, such as support or admin, do not need extensive experience. Employers vary."),("Do I need to declare income from home?","Yes. Income from employment and freelance work is taxable. Check IRAS.")],
[("part-time-jobs-singapore.html","Part time jobs","Steady hours"),("freelance-jobs-singapore.html","Freelance jobs","Control your schedule"),("article-rising-costs.html","When the rent goes up","Why a second income helps")])

# calculator on make-money page
_p=OUT/"make-money-at-home-singapore.html"
_h=_p.read_text(encoding="utf-8")
_calc='''<section class="alt"><div class="wrap split"><div><span class="eyebrow">Simple calculator</span><h2>How many hours a week would you need?</h2><p class="lede">Enter your own numbers. Nothing is saved or sent, and this is not a promise of income.</p></div>
<form class="fit" id="calc" onsubmit="return false"><div class="field"><label for="c-target">Extra income you want per month ($)</label><input id="c-target" type="number" min="0" inputmode="decimal"></div>
<div class="field"><label for="c-rate">Expected hourly rate ($)</label><input id="c-rate" type="number" min="0" inputmode="decimal"></div>
<div id="c-out" class="fit-out" role="status" aria-live="polite" hidden></div></form></div></section>'''
_h=_h.replace('<section class="alt"><div class="wrap" style="max-width:860px">',_calc+'<section class="alt"><div class="wrap" style="max-width:860px">',1)
_p.write_text(_h,encoding="utf-8")

_h=_p.read_text(encoding="utf-8")
for a,b in [("A sample week","Work it out"),("What it can look like alongside your day.","Three steps to a realistic plan."),("An illustrative example only. Real schedules depend on the employer.","Use the calculator further down for step 3."),("<th>Day</th><th>Time</th><th>Activity</th>","<th>Step</th><th>Action</th><th>Detail</th>")]:
    _h=_h.replace(a,b)
_p.write_text(_h,encoding="utf-8")

TAKE.update({
"article-flexible-work-request.html":["Employees can make a formal flexible work arrangement request.","Be specific about what you want, why, and when it starts.","Offer a trial period to make a yes easier.","Employers should reply in writing and give reasons if they decline."],
"article-part-time-cpf.html":["CPF contributions apply to employees who are citizens or PRs, subject to age and pay.","Your payslip should show your pay and CPF contributions.","Freelancers are not employees, so employer CPF does not apply.","Check the current rates on the CPF Board website."],
"article-read-job-ad.html":["Look for hours, pay basis, work mode and employment type first.","Salary ranges and 'up to' amounts are not the same as guaranteed pay.","Note probation and notice period before you apply.","Check the employer on an official source."],
"article-remote-cv.html":["Show results you delivered independently.","List the remote tools you already use.","Mention time zones and availability clearly.","Keep it to one or two pages."],
})

article("article-flexible-work-request.html","How to ask your employer for flexible work","A step-by-step guide to a flexible work arrangement request in Singapore.","Rights",'''
<p class="lede">If you already have a job and want part-time hours, remote days or flexible timing, you can put in a formal request. Preparing it well makes a yes more likely.</p>
<h2>Know what you are asking for</h2><ul><li><strong>Flexi-place:</strong> working from home or another location some or all of the time.</li><li><strong>Flexi-time:</strong> different start and end times.</li><li><strong>Flexi-load:</strong> fewer hours, such as part-time or job-sharing.</li></ul>
<h2>Step by step</h2><ol><li>Check your contract and any company policy.</li><li>Decide what you want, for how long and from when.</li><li>Explain how the work will still get done, and any handover needed.</li><li>Offer a trial period and a review date.</li><li>Submit the request in writing.</li><li>Follow up politely if you do not hear back.</li></ol>
<h2>What to expect</h2><p>Under national guidelines on flexible work arrangement requests, employers are expected to consider requests fairly, respond in writing within a set period and explain their reasons if they decline. Check the current details on the MOM website.</p>
<div class="callout"><p>A request is not a guarantee. A clear, practical proposal with a trial period is your strongest approach.</p></div>''')

article("article-part-time-cpf.html","Part-time work and CPF: what to check on your payslip","How CPF applies to part-time work in Singapore.","Rights",'''
<p class="lede">Part-time employees are still employees. Whether CPF applies depends on your status, age and pay, not the number of hours alone.</p>
<h2>Who gets CPF contributions</h2><p>CPF contributions apply to employees who are Singapore Citizens or Permanent Residents, subject to age and monthly wages. Foreigners on work passes are generally not covered. Rates change, so check the CPF Board website.</p>
<h2>Reading your payslip</h2><ul><li>Your gross pay and pay period.</li><li>Deductions, including employee CPF contribution where it applies.</li><li>Employer CPF contribution, which is shown separately.</li><li>Net pay.</li></ul>
<h2>What about freelancers?</h2><p>Freelancers are self-employed, so there is no employer CPF contribution. Self-employed persons may need to contribute to MediSave depending on income.</p>
<h2>Questions to ask</h2><ul><li>Am I an employee under a contract of service?</li><li>Will CPF be contributed each month?</li><li>Will I receive an itemised payslip?</li></ul>
<p>See our <a href="part-time-jobs-singapore.html">part time job guide</a> for more.</p>''')

article("article-read-job-ad.html","How to read a Singapore job ad like an insider","How to decode pay, hours and terms in a Singapore job listing.","Basics",'''
<p class="lede">A job ad packs a lot into a few lines. Knowing what to look for saves time and avoids surprises.</p>
<h2>Start with the basics</h2><ul><li><strong>Employment type:</strong> permanent, contract, part-time, freelance or temp.</li><li><strong>Work mode:</strong> on-site, hybrid, remote or work from home.</li><li><strong>Hours:</strong> fixed, shifts or flexible.</li></ul>
<h2>Decode the pay</h2><p>A salary range shows what the employer expects to pay, and where you land depends on experience. "Up to" figures are a ceiling, not a promise. Commission-based pay depends on results. Check whether pay is hourly, monthly or per project.</p>
<h2>Terms worth noting</h2><ul><li><strong>JD:</strong> job description, the duties and requirements.</li><li><strong>Probation:</strong> an initial trial period.</li><li><strong>Notice period:</strong> how long you must give or receive before leaving.</li><li><strong>AWS:</strong> annual wage supplement, often a bonus month.</li></ul>
<h2>Check the employer</h2><p>Confirm the company exists and is the one hiring. Prefer official channels such as MyCareersFuture or the company's careers page. See our <a href="glossary.html">glossary</a> for more terms.</p>''')

article("article-remote-cv.html","A CV for remote and work from home roles","How to tailor a CV for remote and work from home jobs in Singapore.","Career",'''
<p class="lede">Remote employers cannot watch you work, so they look for evidence that you can deliver independently.</p>
<h2>Lead with results</h2><p>Use short bullets that show what you achieved on your own: tickets resolved, campaigns delivered, projects completed on time.</p>
<h2>Show remote skills</h2><ul><li>Tools you already use: email, chat platforms, spreadsheets, video calls, project boards.</li><li>Written communication: clear, brief and polite.</li><li>Time management and reliability.</li></ul>
<h2>Be clear on availability</h2><p>State your hours, time zone and any core hours you can commit to. This helps for part time job and work from home applications.</p>
<h2>Keep it tidy</h2><p>One or two pages, plain formatting and a short summary at the top. Add a link to a portfolio if you have one.</p>
<p>See our <a href="work-from-home-jobs-singapore.html">work from home jobs guide</a> for roles to aim at.</p>''')
