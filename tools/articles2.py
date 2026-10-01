MOM="https://www.mom.gov.sg"
SRC={
"mom":("Ministry of Manpower: Labour market statistics",MOM+"/resources-and-tools/statistics"),
"momfwa":("Tripartite Guidelines on Flexible Work Arrangement Requests (TAFEP)","https://www.tafep.sg"),
"sf":("SkillsFuture Singapore","https://www.skillsfuture.gov.sg"),
"wsg":("Workforce Singapore","https://www.wsg.gov.sg"),
"mcf":("MyCareersFuture","https://www.mycareersfuture.gov.sg"),
"sd":("Singapore Department of Statistics","https://www.singstat.gov.sg"),
"cpf":("CPF Board","https://www.cpf.gov.sg"),
}
def stats(items):
    return '<div class="statrow">'+"".join(f'<div class="stat"><b>{n}</b><span>{t}</span></div>' for n,t in items)+'</div>'
for k,v in {
"article-sectors-hiring.html":["mom","wsg","sd"],
"article-in-demand-roles.html":["mom","mcf","wsg"],
"article-why-second-income.html":["mom","sd","cpf"],
"article-remote-work-trend.html":["momfwa","mom"],
"article-upskilling-2026.html":["sf","wsg"],
"article-read-labour-data.html":["mom","sd","mcf"],
}.items(): SOURCES[k]=[SRC[x] for x in v]

TAKE.update({
"article-sectors-hiring.html":["Healthcare, technology, finance, professional services and logistics are the sectors most often cited in official labour reports.","Growth is uneven: some roles are scarce while others are crowded.","Read the latest quarterly MOM report before choosing a direction.","Skills travel between sectors more than job titles do."],
"article-in-demand-roles.html":["Roles in demand cluster around care, data, digital, finance and operations.","Many of these roles have part-time, contract or remote versions.","Pay ranges vary widely, so check recent listings and official salary data.","Short courses can be a bridge into an adjacent role."],
"article-why-second-income.html":["Part time job Singapore options let you add income without leaving your main role.","Work from home jobs and freelance jobs save commuting time.","A second income works best when hours, tax and CPF are understood up front.","Treat any online earnings claim with care. Pay depends on the work."],
"article-remote-work-trend.html":["Formal flexible work requests are now part of national guidelines.","Remote job Singapore listings range from fully remote to hybrid.","Work from home in Singapore is usually agreed in hours and place.","Employers can still decline a request, with reasons."],
"article-upskilling-2026.html":["SkillsFuture credits and subsidies can lower the cost of courses.","Pick training tied to a role you can actually see advertised.","Short, stackable courses suit people who work part time.","Check that a course is approved before paying."],
"article-read-labour-data.html":["Unemployment and job vacancy figures tell different stories.","Look at the sector and role, not just the headline number.","Wage figures are medians, not promises.","Use official publications first, commentary second."],
})
EXTRA.update({
"article-sectors-hiring.html":([("Where do I find the latest sector figures?","The Ministry of Manpower publishes quarterly labour market reports, and Workforce Singapore shares industry transformation updates."),("Does a growing sector mean easy hiring?","Not always. Competition depends on the role, skills and experience asked for.")],[("article-in-demand-roles.html","Top in-demand roles"),("article-read-labour-data.html","How to read labour data"),("article-upskilling-2026.html","Upskilling in Singapore")]),
"article-in-demand-roles.html":([("Can in-demand roles be done part-time or remotely?","Some can, especially analysis, content, support and project work. Ask the employer what is possible."),("Do I need a degree?","Requirements vary. Many employers now list skills and certifications alongside or instead of degrees.")],[("article-sectors-hiring.html","Sectors to watch"),("article-upskilling-2026.html","Upskilling in Singapore"),("remote-jobs-singapore.html","Remote jobs guide")]),
"article-why-second-income.html":([("How many hours does a second income take?","It depends on your target and rate. Try our <a href='make-money-at-home-singapore.html'>hours calculator</a>."),("Do I need to tell my main employer?","Check your employment contract. Some contracts require approval for outside work.")],[("part-time-jobs-singapore.html","Part time job guide"),("work-from-home-jobs-singapore.html","Work from home jobs guide"),("freelance-jobs-singapore.html","Freelance jobs guide")]),
"article-remote-work-trend.html":([("Can I ask to work from home?","Yes, you can submit a formal flexible work arrangement request. See our step-by-step guide."),("Are remote roles open to Singapore residents?","Many are. Check which time zone, entity and payroll apply.")],[("article-flexible-work-request.html","How to ask for flexible work"),("remote-jobs-singapore.html","Remote jobs guide"),("article-remote-cv.html","A CV for remote roles")]),
"article-upskilling-2026.html":([("Who can use SkillsFuture Credit?","Singapore citizens aged 25 and above have an opening credit. Check SkillsFuture for the latest amounts and any mid-career top-ups."),("Can I study while working part time?","Many courses are modular and part-time, designed for working adults.")],[("article-in-demand-roles.html","Top in-demand roles"),("article-restart.html","Starting again after a break"),("article-remote-cv.html","A CV for remote roles")]),
"article-read-labour-data.html":([("What is the difference between job vacancies and openings you see online?","Official figures count vacancies reported by employers. Listings online may be duplicated or already filled."),("Where are the official tables?","The MOM Manpower Research and Statistics pages and SingStat publish them.")],[("article-sectors-hiring.html","Sectors to watch"),("article-in-demand-roles.html","Top in-demand roles"),("glossary.html","Glossary")]),
})

article("article-sectors-hiring.html","Which sectors are hiring in Singapore right now","A plain-language read of the industries that official labour reports keep pointing to, and what it means for your next career move.","Industry trends",f'''
<p class="lede">Singapore's job market is not moving in one direction. A few sectors keep growing, others are reshaping, and the roles inside each are changing fast. Here is the big picture.</p>
{stats([("5","sectors most often highlighted: healthcare, tech, finance, professional services, logistics"),("Quarterly","how often MOM publishes labour market reports"),("35 hrs","the line between part-time and full-time")])}
<h2>Healthcare and care services</h2><p>An ageing population keeps demand steady for nurses, allied health, eldercare and community care staff. Many roles offer part-time and shift-based options.</p>
<h2>Technology and digital</h2><p>Data, cybersecurity, cloud and AI-related work keep appearing in national skills reports. Remote and contract arrangements are common here.</p>
<h2>Finance and professional services</h2><p>Compliance, risk, analytics and advisory roles continue to be needed, with a growing mix of hybrid arrangements.</p>
<h2>Logistics, engineering and the green economy</h2><p>Supply chain, advanced manufacturing and sustainability roles are part of Singapore's industry transformation plans.</p>
<h2>What this means for you</h2><p>Whether you want a main career move or a part time job Singapore employers offer alongside it, look at which skills sit behind a sector rather than the job title. Adjacent skills move across sectors more easily than most people expect.</p>
<div class="callout"><p>Figures change each quarter. Always confirm with the latest MOM and Workforce Singapore publications listed below.</p></div>''')

article("article-in-demand-roles.html","Top in-demand roles in Singapore now","The kinds of roles employers are asking for, across care, data, digital, finance and operations, and how to read the trend.","In-demand roles",f'''
<p class="lede">Job titles come and go, but the skills employers keep asking for fall into a few clear groups.</p>
{stats([("Care","nursing, allied health, eldercare"),("Data","analysts, engineers, AI support"),("Digital","product, marketing, cybersecurity"),("Ops","logistics, projects, compliance")])}
<h2>Care and health roles</h2><p>Nurses, therapists, care associates and community support staff appear consistently in manpower plans.</p>
<h2>Data and technology roles</h2><p>Data analysts, software engineers, cloud and security specialists. Many are open to remote job Singapore arrangements or contract work.</p>
<h2>Digital marketing and content</h2><p>Performance marketing, SEO, content and design. Freelance jobs and project-based work are common routes in.</p>
<h2>Finance, compliance and operations</h2><p>Risk, audit, project coordination and supply chain roles are steady across industries.</p>
<h2>How to use this list</h2><ul><li>Check recent listings on MyCareersFuture for the real salary range.</li><li>Look at the skills section, not only the title.</li><li>Ask whether part-time, hybrid or contract options exist.</li></ul>
<p>Looking at the types of work behind these roles? See our <a href="jobs.html">job types</a> overview.</p>''')

article("article-why-second-income.html","Why a second income is on more Singaporeans' minds","A part time job, work from home jobs and freelance jobs are common ways people add income. Here is why the idea keeps growing.","Second income",f'''
<p class="lede">More people are looking at a part time job on top of a main role, or a freelance project on weekends. The reasons are practical.</p>
{stats([("<35 hrs","part-time contracted hours per week"),("3","common routes: part-time, freelance, online"),("1","income that rarely fits every cost")])}
<h2>Costs are the main push</h2><p>Housing, childcare, healthcare and daily expenses all weigh on households. A second income gives breathing room without changing your main career.</p>
<h2>Flexible options have widened</h2><p>Part time job Singapore listings, work from home jobs, work from home in Singapore arrangements, online jobs, online work from home options and freelance jobs make it easier to fit extra work around a schedule. Many people also look into how to make money at home through ordinary paid work done remotely.</p>
<h2>Skills become a second career test</h2><p>A side role is also a low-risk way to try a new field, build a portfolio, or restart after a break.</p>
<h2>What to settle first</h2><ul><li>Your realistic weekly hours.</li><li>Tax and CPF treatment for employee or self-employed work.</li><li>Whether your main contract allows outside work.</li></ul>
<p>Compare the types in our <a href="make-money-at-home-singapore.html">work-at-home routes guide</a>.</p>''')

article("article-remote-work-trend.html","Remote, hybrid and flexible work: where Singapore stands","How flexible work requests, remote roles and hybrid schedules have become part of normal employment conversations.","Industry trends",f'''
<p class="lede">Flexible work has moved from a perk to a standard conversation between employees and employers.</p>
{stats([("2024","year national flexible work guidelines took effect"),("2 months","time for an employer to reply to a formal request"),("3","forms: flexi-place, flexi-time, flexi-load")])}
<h2>What changed</h2><p>Employers are now expected to have a process for considering flexible work requests. This does not guarantee approval, but it gives you a clear way to ask.</p>
<h2>Remote and hybrid in practice</h2><p>Remote job Singapore roles range from fully remote to a fixed number of office days. Work from home in Singapore usually means agreed hours with a Singapore employer.</p>
<h2>What employers look for</h2><p>Clear communication, reliable output, and a suitable workspace. A short trial with a review date often helps.</p>
<p>Ready to ask? Read <a href="article-flexible-work-request.html">how to submit a flexible work request</a>.</p>''')

article("article-upskilling-2026.html","Upskilling in Singapore: what is available and what is worth it","SkillsFuture credits, subsidies and short courses, and how to choose training tied to roles employers actually want.","Education & skills",f'''
<p class="lede">Training can open a new path, but only if it connects to roles you can see advertised.</p>
{stats([("$500","opening SkillsFuture Credit for citizens 25+"),("$4,000","SkillsFuture Level-Up credit for citizens 40+"),("Modular","courses designed for working adults")])}
<h2>Start from the role, not the course</h2><p>Pick two or three job ads you would like, list the skills they ask for, then match courses to the gaps.</p>
<h2>Funding to check</h2><p>SkillsFuture Credit, mid-career support and course subsidies reduce costs. Amounts and eligibility are updated, so check SkillsFuture before you pay.</p>
<h2>Short courses and part-time study</h2><p>Many programmes are modular and offered in evenings or online, which suits people already working part time.</p>
<h2>Avoid</h2><ul><li>Paying for unapproved courses.</li><li>Training promises that guarantee a job or income.</li></ul>
<p>Looking to restart? See <a href="article-restart.html">starting again after a break</a>.</p>''')

article("article-read-labour-data.html","How to read Singapore's labour market data","A quick guide to unemployment, job vacancies and wage figures, so you can read official reports like a pro.","Career advice",f'''
<p class="lede">Headlines compress a lot. Here is what the main labour figures actually measure.</p>
{stats([("Unemployment","share of the labour force looking for work"),("Vacancies","openings reported by employers"),("Median wage","the middle, not the average")])}
<h2>Unemployment rate</h2><p>Shows how many people are looking for work. It is low in Singapore, but it does not show underemployment or mismatches.</p>
<h2>Job vacancies</h2><p>Counts openings employers report. It is different from the number of listings you see online.</p>
<h2>Wages</h2><p>Medians help you see the middle of the range. Individual pay depends on experience and employer.</p>
<h2>A simple routine</h2><ul><li>Read the summary of the latest MOM report.</li><li>Check the sector table for your field.</li><li>Compare with recent listings.</li></ul>
<p>See also <a href="article-sectors-hiring.html">which sectors are hiring</a>.</p>''')
