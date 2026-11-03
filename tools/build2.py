#!/usr/bin/env python3
"""NCERD UNN static site generator v2."""
import os, html
from icons import ic
OUT = os.path.join(os.path.dirname(__file__), '..')
NAV = [('index.html','Home'),('about.html','About'),('projects.html','Projects'),
       ('staff-profiles.html','Staff'),('news-events.html','News'),('external-resources.html','Resources')]
SUFFIX = ' | NCERD, University of Nigeria, Nsukka'

def head(title, desc, slug):
    items=''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==slug else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en-NG">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#00692f">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="assets/images/building-1100.webp">
<link rel="icon" href="assets/images/ecn-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/ncerd.css">
<script>document.documentElement.classList.add(matchMedia('(prefers-reduced-motion: reduce)').matches?'rm':'motion')</script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<div class="progress" aria-hidden="true"></div>
<header class="site-head solid static">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="NCERD, University of Nigeria, Nsukka: home">
      <img class="seal" src="assets/images/ecn-logo.png" alt="" width="52" height="52">
      <span><b>NCERD</b><small>National Centre for Energy Research and Development, UNN</small></span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav"><span class="bars"><i></i></span><span class="lbl">Menu</span></button>
    <nav class="nav" id="nav" aria-label="Main">
      <ul>{items}</ul>
      <a class="cta" href="contact-us.html"{' aria-current="page"' if slug=='contact-us.html' else ''}>Contact us {ic('arrow')}</a>
    </nav>
  </div>
</header>
<main id="main">
'''

def foot():
    return f'''</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <img class="seal" src="assets/images/ecn-logo.png" alt="Energy Commission of Nigeria emblem" width="64" height="64">
        <b>National Centre for Energy Research and Development</b>
        <p>University of Nigeria, Nsukka. A research centre of the Energy Commission of Nigeria, working on renewable and alternative energy since 1982.</p>
      </div>
      <div>
        <h2>The Centre</h2>
        <ul><li><a href="about.html">About NCERD</a></li><li><a href="projects.html">Research projects</a></li><li><a href="staff-profiles.html">Staff and leadership</a></li><li><a href="news-events.html">News and events</a></li></ul>
      </div>
      <div>
        <h2>Related sites</h2>
        <ul><li><a href="https://energy.gov.ng" target="_blank" rel="noopener">Energy Commission of Nigeria</a></li><li><a href="https://www.unn.edu.ng" target="_blank" rel="noopener">University of Nigeria</a></li><li><a href="https://ncerd.com.ng" target="_blank" rel="noopener">NCERD conference</a></li><li><a href="external-resources.html">All resources</a></li></ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li class="ci">{ic('phone')}<span><a href="tel:+2348065702570">+234 806 570 2570</a><br><a href="tel:+2348082770823">+234 808 277 0823</a></span></li>
          <li class="ci">{ic('mail')}<a href="mailto:ncerdunn@yahoo.com">ncerdunn@yahoo.com</a></li>
          <li class="ci">{ic('globe')}<a href="https://www.ncerd-unn.gov.ng" target="_blank" rel="noopener">www.ncerd-unn.gov.ng</a></li>
          <li class="ci">{ic('pin')}<span>University of Nigeria, Nsukka, Enugu State</span></li>
        </ul>
      </div>
    </div>
    <div class="wordmark" aria-hidden="true">NCERD</div>
    <div class="foot-base"><span>© <span id="yr">2026</span> National Centre for Energy Research and Development, UNN</span><span>Supervised by the Energy Commission of Nigeria</span></div>
  </div>
</footer>
<button class="to-top" aria-label="Back to top"><svg class="ring" viewBox="0 0 54 54" aria-hidden="true"><circle cx="27" cy="27" r="25"/></svg>{ic('arrow-up')}</button>
<script src="assets/js/ncerd.js" defer></script>
</body>
</html>
'''

def phero(title, lede, crumb, photo=None, stats=None):
    bg=f'<div class="bg"><img src="{photo}" alt="" fetchpriority="high"></div>' if photo else ''
    st=''
    if stats:
        st='<div class="stats-glass glass">'+''.join(f'<div><b data-count="{n}">{n}</b><span>{l}</span></div>' for n,l in stats)+'</div>'
    arc=('<svg class="phero-arc" viewBox="0 0 760 420" aria-hidden="true"><path d="M20 410 C 160 -20, 600 -20, 740 410"/>'
         '<path class="solid" d="M20 410 C 90 190, 220 70, 380 78"/><circle cx="380" cy="78" r="12"/></svg>')
    return f'''<section class="phero{' plain' if not photo else ''}">
  {bg}{arc}
  <div class="wrap in-load">
    <div class="crumbs"><a href="index.html">Home</a>{ic('right')}<span>{crumb}</span></div>
    <h1>{title}</h1>
    <p>{lede}</p>
    {st}
  </div>
</section>
'''

def write(name, title, desc, body):
    with open(os.path.join(OUT,name),'w',encoding='utf-8') as f:
        f.write(head(title,desc,name)+body+foot())

# ---------------- data ----------------
UNITS=[
 ('Solar Thermal','sun','Solar water and air heaters, crop dryers, concentrators and solar refrigeration.','Engr. O.N. Okala'),
 ('Biomass and Biogas','flame','Anaerobic digestion, biofuels, pyrolysis and conversion of agricultural and municipal waste.','Dr. (Mrs.) N.F. Oparaku'),
 ('Photovoltaics','panel','Design, testing and evaluation of PV systems, solar cells and thin films.','Mrs. C.A. Nwanya'),
 ('Energy Management and Environment','gauge','Energy audits, efficiency programmes and cookstove testing at the National Stove Eligibility Laboratory.','Engr. I.F. Okafor'),
 ('Wind and Meteorology','wind','Wind resource measurement and the weather data that underpin system design.','Dr. P.E. Ugwuoke'),
 ('Fossil Energy','mountain','Coal and solid fuel studies, including smokeless briquettes and efficient stoves.','Dr. I.S. Eze'),
 ('Energy Information and Manpower Development','book','Energy data, training programmes and short courses for technicians and graduates.','Dr. C.N. Anyanwu'),
 ('Design and Production Workshops','wrench','Fabrication of prototypes and devices produced on demand.','Mr. Ik Owoh'),
 ('Laboratories','flask','Analytical and test facilities serving every research unit.','Mr. A. Ofomatah'),
]
TECH=[
 ('Solar rice dryer','sun','Solar thermal','A commercial-scale solar rice dryer designed, constructed and installed by the Centre for a rice production company.','2 tonnes','capacity'),
 ('Thermosyphon solar water heater','droplet','Solar thermal','A solar water heater that circulates water naturally, without a pump.','70–80 °C','hot water supply'),
 ('Solar chicken brooders','egg','Solar thermal','Brooders of various sizes that use solar heat in place of electric bulbs for raising chicks.','',''),
 ('Solar incubator','egg','Solar thermal','A solar thermal incubator developed at the Centre for hatching eggs in poultry production.','',''),
 ('Solar refrigerator','snow','Solar thermal','An absorption refrigerator that collects solar heat during the day and converts it to cooling in the evening and night.','',''),
 ('Solar crop and manure dryers','leaf','Solar thermal','Solar dryers for crops, and for poultry waste, cow dung and pig droppings.','',''),
 ('Biogas digesters and cookstoves','flame','Biomass','Biogas digester applications and cookstoves for domestic use, with stove performance tested at the National Stove Eligibility Laboratory.','',''),
 ('Solar PV system','panel','Photovoltaics','A photovoltaic installation at the Centre used for demonstration and research.','1.5 kWp','capacity'),
]
NETWORK=[
 ('NCERD','National Centre for Energy Research and Development','University of Nigeria, Nsukka','Solar and renewable energy','sun',True),
 ('SERC','Sokoto Energy Research Centre','Usmanu Danfodiyo University, Sokoto','Solar and renewable energy','sun',False),
 ('NCEEC','National Centre for Energy Efficiency and Conservation','University of Lagos','Energy efficiency and conservation','gauge',False),
 ('NACHRED','National Centre for Hydropower Research and Development','University of Ilorin','Hydropower','droplet',False),
 ('NCEE','National Centre for Energy and Environment','University of Benin','Energy and environment','leaf',False),
 ('NCPRD','National Centre for Petroleum Research and Development','Abubakar Tafawa Balewa University, Bauchi','Petroleum','mountain',False),
]
TIMELINE=[
 ('1979','Energy Commission Act','Act No. 62 creates the Energy Commission of Nigeria to coordinate the country\'s energy resources.',False),
 ('1980','Centre established','An Act of the National Assembly establishes the Centre at Nsukka, alongside three other research centres.',True),
 ('1982','Full operation','The Centre begins full work on the Nsukka campus, funded directly by the Federal Government.',True),
 ('1988','Under the Commission','Decree No. 12 of 1988, and Decree No. 19 of 1989, charge the Energy Commission with supervising the centres.',False),
 ('2020','4th conference','NCERD hosts the 4th International Conference and Training Workshop with GIZ, alongside solar PV training.',False),
 ('2022','5th conference','The 5th edition is held at the Centre, physically and virtually, on post-COVID-19 energy solutions.',False),
 ('2024','6th edition','A new call for papers opens with a 20-day practical solar PV training workshop.',True),
]

def network():
    out='<div class="net" data-stagger>'
    for ab,n,u,f,i,h in NETWORK:
        pill='<span class="here-pill">You are here</span>' if h else ''
        out+=f'<article class="centre{" here" if h else ""}">{pill}<span class="ab">{ab}</span><h3>{n}</h3><p>{u}</p><div class="focus">{ic(i)}{f}</div></article>'
    return out+'</div>'

def timeline():
    m=''.join(f'<article class="moment{" key" if k else ""}"><time>{y}</time><h3>{t}</h3><p>{d}</p></article>' for y,t,d,k in TIMELINE)
    return f'''<div class="hscroll reveal">
      <div class="hs-track" tabindex="0" aria-label="Timeline of the Centre, scroll sideways">{m}</div>
      <div class="hs-bar"><i></i></div>
    </div>'''

def bento(with_heads=False):
    out='<div class="bento" data-stagger>'
    for k,(n,i,dsc,h) in enumerate(UNITS):
        cls='tile big' if k==0 else ('tile green' if k==1 else ('tile wide' if k==2 else 'tile'))
        cls+=' art'
        artf={'Solar Thermal':'solar-thermal','Biomass and Biogas':'biomass','Photovoltaics':'pv','Energy Management and Environment':'energy-mgmt','Wind and Meteorology':'wind','Fossil Energy':'fossil','Energy Information and Manpower Development':'information','Design and Production Workshops':'workshop','Laboratories':'labs'}[n]
        rings='<svg class="rings" viewBox="0 0 340 340" aria-hidden="true"><circle cx="170" cy="170" r="60"/><circle cx="170" cy="170" r="100"/><circle cx="170" cy="170" r="140"/><circle cx="170" cy="170" r="168"/></svg>' if k==0 else ''
        lead=f'<div class="lead">Unit head: {h}</div>' if with_heads else ''
        out+=f'<article class="{cls}" style="background-image:url(assets/images/units/{artf}.svg)"><h3>{n}</h3><p>{dsc}</p>{lead}</article>'
    return out+'</div>'

def contact_strip():
    return f'''<div class="contact-strip">
      <div class="c-list" data-stagger>
        <a class="c-item" href="tel:+2348065702570"><span class="icon">{ic('phone')}</span><span><small>Call the Centre</small><b>+234 806 570 2570</b></span></a>
        <a class="c-item" href="tel:+2348082770823"><span class="icon">{ic('phone')}</span><span><small>Alternative line</small><b>+234 808 277 0823</b></span></a>
        <a class="c-item" href="mailto:ncerdunn@yahoo.com"><span class="icon">{ic('mail')}</span><span><small>Email</small><b>ncerdunn@yahoo.com</b></span></a>
        <a class="c-item" href="https://www.ncerd-unn.gov.ng" target="_blank" rel="noopener"><span class="icon">{ic('globe')}</span><span><small>Website</small><b>www.ncerd-unn.gov.ng</b></span></a>
        <div class="c-item"><span class="icon">{ic('pin')}</span><span><small>Visit</small><b>University of Nigeria, Nsukka Campus, Enugu State</b></span></div>
      </div>
      <div class="map-card reveal-scale">
        <iframe title="Map of the NCERD complex on the University of Nigeria, Nsukka campus" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=7.3858%2C6.8507%2C7.4058%2C6.8627&amp;layer=mapnik&amp;marker=6.85667%2C7.39583"></iframe>
        <div class="pin"><div><b>NCERD complex</b><span>6°51′24″N, 7°23′45″E</span></div><a class="btn btn-dark" href="https://www.openstreetmap.org/?mlat=6.85667&amp;mlon=7.39583#map=17/6.85667/7.39583" target="_blank" rel="noopener">Get directions {ic('arrow-ur')}</a></div>
      </div>
    </div>'''

def portrait(cls=''):
    return f'''<div class="portrait {cls}">
        <img src="assets/images/leadership/director-ncerd.jpg" alt="Engr. Dr. Izuchukwu Francis Okafor, Acting Director of NCERD" loading="lazy">
        <div class="mono" aria-hidden="true">IFO</div>
      </div>'''


LEADERS=[
 ('l1','minister.jpg','KU','Supervising Minister','Dr. Kingsley Tochukwu Udeh, SAN','','Minister of Innovation, Science and Technology'),
 ('l2','dg-ecn.jpg','MA','Energy Commission of Nigeria','Dr. Mustapha Abdullahi','PhD (Mech. Engrg), MIMechE','DG/CEO, Energy Commission of Nigeria'),
 ('l3','director-ncerd.jpg','IO','The Centre','Engr. Dr. Izuchukwu Francis Okafor','Ph.D.; M.Eng. (Mechanical Engineering); B.Eng. (Mechanical Engineering); SESN; MWEC-NNC; CMNSE; ASME; R.Engr., COREN','Ag. Director, National Centre for Energy Research and Development (NCERD), University of Nigeria, Nsukka'),
]
def leaders():
    out='<div class="leaders" data-stagger>'
    for cls,img,ini,rank,name,cred,role in LEADERS:
        cr=f'<span class="cred">{cred}</span>' if cred else ''
        out+=f'''<article class="leader {cls}"><div class="ph"><img src="assets/images/leadership/{img}" alt="{name}" loading="lazy"><div class="mono" aria-hidden="true">{ini}</div></div><div class="tx"><span class="rank">{rank}</span><b>{name}</b>{cr}<span class="role">{role}</span></div></article>'''
    return out+'</div><p class="source" style="color:var(--ink-3)">Titles as listed on the Energy Commission of Nigeria leadership page, energy.gov.ng.</p>'
# =================================================== HOME
marq_items=[('sun','Solar thermal'),('panel','Photovoltaics'),('flame','Biogas'),('leaf','Biomass'),('wind','Wind'),('droplet','Hydro'),('mountain','Coal'),('gauge','Energy management'),('globe','Environment'),('cap','Training')]
marq=''.join(f'<span>{ic(i)}{t}</span>' for i,t in marq_items)*2

tabs=''.join(f'<button class="tab" role="tab" id="t{k}" aria-controls="p{k}" aria-selected="{"true" if k==0 else "false"}">{ic(i)}<b>{n}</b><span class="bar"></span></button>' for k,(n,i,a,dsc,sv,sl) in enumerate(TECH))
panels=''.join(f'''<div class="panel" role="tabpanel" id="p{k}" aria-labelledby="t{k}"{'' if k==0 else ' hidden'}>
  <svg class="rings" viewBox="0 0 460 460" aria-hidden="true"><circle cx="230" cy="230" r="80"/><circle cx="230" cy="230" r="140"/><circle cx="230" cy="230" r="200"/><circle cx="230" cy="230" r="228"/></svg>
  <div class="art">{ic(i)}</div>
  <span class="tag">{a}</span>
  <h3>{n}</h3>
  <p>{dsc}</p>
  {f'<div class="spec"><b>{sv}</b><span>{sl}</span></div>' if sv else ''}
</div>''' for k,(n,i,a,dsc,sv,sl) in enumerate(TECH))

home=f'''<section class="hero" aria-labelledby="hero-title" style="padding:0">
  <div class="hero-bg"><img src="assets/images/building-2000.webp" srcset="assets/images/building-1100.webp 1100w, assets/images/building-2000.webp 2000w" sizes="100vw" alt="The NCERD building on the Nsukka campus of the University of Nigeria" fetchpriority="high"></div>
  <svg class="sky" id="sky" aria-hidden="true"></svg>
  <div class="hero-main">
    <div class="wrap hero-grid">
      <div>
        <h1 id="hero-title"><span class="line"><span>Energy research</span></span><span class="line"><span>and development</span></span><span class="line"><span class="gold">for Nigeria.</span></span></h1>
        <p class="sub">A research centre of the Energy Commission of Nigeria at the University of Nigeria, Nsukka, working on renewable and alternative energy since 1982.</p>
        <div class="btns">
          <a class="btn btn-gold" href="#units">Explore our research {ic('arrow')}</a>
          <a class="btn btn-glass" href="about.html">About the Centre</a>
        </div>
      </div>
      <aside class="sun-card glass" aria-live="polite" aria-label="Live sun position over the Centre">
        <div class="top"><span>The sun over the Centre</span><span class="live">Live</span></div>
        <div class="deg" id="sun-deg">–</div>
        <div class="cap" id="sun-cap">Sun elevation above the Centre</div>
        <div class="meter"><i id="sun-meter"></i></div>
        <dl><div><dt>Sunrise</dt><dd id="sun-rise">–</dd></div><div><dt>Solar noon</dt><dd id="sun-noon">–</dd></div><div><dt>Sunset</dt><dd id="sun-set">–</dd></div></dl>
        <p class="fine" id="sun-day">Calculated for 6°51′N, 7°23′E, West Africa Time.</p>
      </aside>
    </div>
  </div>
</section>

<section aria-labelledby="intro">
  <div class="wrap statement">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2 id="intro">One of Nigeria's earliest energy research centres, <span class="soft">established by Act of the National Assembly in 1980.</span></h2>
      <p class="lede" style="margin-top:24px">Our mandate covers research, development, dissemination and manpower training across solar, biomass, wind, hydro, geothermal, coal, petroleum, energy management and the environment.</p>
      <a class="link-arrow" href="about.html">Read our story {ic('arrow')}</a>
    </div>
    <div class="stat-grid" data-stagger>
      <div class="stat hl">{ic('scroll')}<b data-count="1980">1980</b><span>Established by Act of the National Assembly</span></div>
      <div class="stat">{ic('layers')}<b data-count="9">9</b><span>Research units</span></div>
      <div class="stat">{ic('clipboard')}<b data-count="37">37</b><span>Published research projects</span></div>
      <div class="stat green">{ic('network')}<b data-count="6">6</b><span>Energy Commission research centres nationwide</span></div>
    </div>
  </div>
</section>

<section class="mist" id="units" aria-labelledby="units-title">
  <div class="wrap">
    <div class="head-row">
      <div class="reveal"><span class="eyebrow">Research units</span><h2 id="units-title">Research units</h2><p class="lede">The units listed in the Centre's published staff directory.</p></div>
      <a class="btn btn-ghost reveal" href="staff-profiles.html">Meet the unit heads {ic('arrow')}</a>
    </div>
    {bento()}
  </div>
</section>

<section class="dark" aria-labelledby="tech-title">
  <div class="wrap">
    <div class="head-row">
      <div class="reveal"><span class="eyebrow">Made at NCERD</span><h2 id="tech-title">Technologies designed and built at the Centre</h2><p class="lede">Devices developed in our workshops, many for rural agriculture and households. Units can be produced on request.</p></div>
    </div>
    <div class="showcase reveal">
      <div class="tabs" role="tablist" aria-label="Technologies">{tabs}</div>
      <div class="panels">{panels}</div>
    </div>
    <p class="source">Sources: Solar Energy Applications in Nigeria (Energy Commission of Nigeria paper, OSTI); papers by NCERD researchers.</p>
  </div>
</section>

<section aria-labelledby="lead-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Leadership</span><h2 id="lead-title">Supervision and leadership</h2><p class="lede">The Centre is supervised by the Energy Commission of Nigeria. The Commission's governing board, as listed on its website, includes the Minister of Innovation, Science and Technology.</p></div><a class="btn btn-ghost reveal" href="staff-profiles.html">Leadership and staff {ic('arrow')}</a></div>
    {leaders()}
  </div>
</section>

<section class="mist" aria-labelledby="pics-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">The Centre</span><h2 id="pics-title">The NCERD complex, Nsukka</h2></div><a class="btn btn-ghost reveal" href="about.html#history">Our history {ic('arrow')}</a></div>
    <div class="gallery" data-stagger>
      <figure><img src="assets/images/building-1100.webp" alt="The NCERD building on the Nsukka campus, with a solar street light in front" loading="lazy"><figcaption>The NCERD building, University of Nigeria, Nsukka campus</figcaption></figure>
      <figure><img src="assets/images/commissioning.webp" alt="Officials and staff at a ribbon-cutting ceremony at the Centre" loading="lazy"><figcaption>A commissioning ceremony at the Centre</figcaption></figure>
      <figure><img src="assets/images/inverter-room.webp" alt="Officials inspecting a solar inverter and battery bank installation" loading="lazy"><figcaption>Solar inverter and battery bank installation</figcaption></figure>
    </div>
  </div>
</section>

<section class="mist" aria-labelledby="hist-title">
  <div class="wrap">
    <div class="head-row">
      <div class="reveal"><span class="eyebrow">Our journey</span><h2 id="hist-title">History of the Centre</h2></div>
      <div class="hs-ctrl reveal"><button class="round hs-prev" aria-label="Previous">{ic('left')}</button><button class="round hs-next" aria-label="Next">{ic('right')}</button></div>
    </div>
    {timeline()}
  </div>
</section>

<section aria-labelledby="conf-title">
  <div class="wrap">
    <article class="feature reveal-clip">
      <div class="ph"><img src="assets/images/commissioning.webp" alt="Officials and staff at a ribbon-cutting ceremony at the Centre" loading="lazy"></div>
      <div class="tx">
        <span class="eyebrow" style="color:var(--gold-300)">Conference and training</span>
        <h2 id="conf-title">Energy for Sustainable Development in Africa</h2>
        <p>Our international conference and training workshop series brings scientists, engineers, social scientists and students to the NCERD complex, with hands-on solar PV training.</p>
        <div class="btns" style="margin-top:12px"><a class="btn btn-gold" href="news-events.html">See news and events {ic('arrow')}</a></div>
      </div>
    </article>
    <div class="editions" data-stagger>
      <article class="edition"><div class="no"><b>4th edition</b><span class="tag">With GIZ</span></div><div class="when">{ic('calendar')}11–13 November 2020</div><p>Held with a professional solar PV training workshop organised with the German Agency for International Cooperation.</p></article>
      <article class="edition"><div class="no"><b>5th edition</b><span class="tag">Hybrid</span></div><div class="when">{ic('calendar')}17–19 May 2022</div><p>On sustainable energy as a solution to post-COVID-19 energy challenges. Proceedings published in 2023.</p></article>
      <article class="edition"><div class="no"><b>6th edition</b><span class="tag gold">Training</span></div><div class="when">{ic('calendar')}2024</div><p>Call for papers, with a 20-day practical solar PV training workshop for engineers, scientists and electricians.</p></article>
    </div>
  </div>
</section>

<section class="dark" aria-labelledby="net-title">
  <div class="wrap">
    <div class="head-row">
      <div class="reveal"><span class="eyebrow">National network</span><h2 id="net-title">Energy Commission of Nigeria research centres</h2><p class="lede">The Energy Commission of Nigeria supervises six research centres, each hosted by a federal university and focused on one part of the energy sector.</p></div>
      <a class="btn btn-glass reveal" href="https://energy.gov.ng" target="_blank" rel="noopener">Visit energy.gov.ng {ic('arrow-ur')}</a>
    </div>
    {network()}
  </div>
</section>

<section aria-labelledby="visit-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Get in touch</span><h2 id="visit-title">Visit or contact the Centre</h2></div><a class="btn btn-green reveal" href="contact-us.html">Send an enquiry {ic('arrow')}</a></div>
    {contact_strip()}
  </div>
</section>
'''
write('index.html','National Centre for Energy Research and Development (NCERD) | University of Nigeria, Nsukka',
 'The National Centre for Energy Research and Development (NCERD), University of Nigeria, Nsukka, is a research centre of the Energy Commission of Nigeria working on renewable and alternative energy since 1982.', home)

# =================================================== ABOUT
FAC=[('flask','Laboratories','Analytical and testing work for every unit'),('thermo','Solar collector test rig','Computerised, with an attached meteorological station'),
     ('panel','Photovoltaic systems','Demonstration and test installations'),('wrench','Mechanical and electrical workshops','Prototype design and production'),
     ('pot','National Stove Eligibility Laboratory','Cookstove performance testing'),('library','Library, seminar room and conference centre','Training, workshops and conferences')]
RES=[('sun','Solar',1),('leaf','Biomass',1),('wind','Wind',1),('droplet','Hydro',1),('globe','Geothermal',1),('mountain','Coal',0),('zap','Petroleum',0),('gauge','Energy management',0),('leaf','Environment',0)]
about=phero('About the Centre','One of Nigeria\'s earliest energy research centres, working on renewable and alternative energy on the Nsukka campus of the University of Nigeria since 1982.','About',
            photo='assets/images/building-2000.webp',stats=[(1980,'Established by Act'),(1982,'Full operation'),(9,'Research units'),(6,'ECN centres')])
about+=f'''
<section aria-labelledby="who">
  <div class="wrap split">
    <div class="photo-stack reveal-scale">
      <div class="a"><img src="assets/images/building-1100.webp" alt="The NCERD building at the University of Nigeria, Nsukka" loading="lazy"></div>
      <div class="b"><img src="assets/images/commissioning.webp" alt="A commissioning ceremony at the Centre" loading="lazy"></div>
      <span class="chip glass">{ic('pin')}Nsukka, Enugu State</span>
    </div>
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2 id="who">A federal research centre on a university campus</h2>
      <p class="lede" style="margin:20px 0">NCERD is hosted by the University of Nigeria, Nsukka, and supervised by the Energy Commission of Nigeria, which lists it as the Commission's centre for research in solar and renewable energy.</p>
      <p>Projects are carried out with staff of the University's departments, including mechanical and agricultural engineering, physics, statistics, economics and sociology, and the Centre welcomes proposals from researchers in every discipline.</p>
      <div class="rchips">{''.join(f'<span class="rchip{"" if r else " nr"}">{ic(i)}{t}</span>' for i,t,r in RES)}</div>
    </div>
  </div>
</section>

<section class="mist" aria-labelledby="vm">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Purpose</span><h2 id="vm">Vision, mission and mandate</h2></div></div>
    <div class="vmm" data-stagger>
      <article class="vcard"><div class="icon">{ic('eye')}</div><h3>Vision</h3><p>A functional, globally comparable and competitive centre for research and development in renewable and alternative energy technologies, responsive to the energy and economic needs of Nigeria and beyond.</p></article>
      <article class="vcard mid"><div class="icon">{ic('target')}</div><h3>Mission</h3><p>To keep the Centre at the forefront of research and development, innovation and knowledge transfer in renewable and alternative energy, energy management and the environment, in support of the Sustainable Development Goals.</p></article>
      <article class="vcard"><div class="icon">{ic('scroll')}</div><h3>Mandate</h3><p>Research, development, dissemination and manpower training across renewable and non-renewable energy, with short courses, diplomas and degree programmes run with UNN departments.</p></article>
    </div>
  </div>
</section>

<section id="history" aria-labelledby="hist-title">
  <div class="wrap">
    <div class="head-row">
      <div class="reveal"><span class="eyebrow">History</span><h2 id="hist-title">Key dates</h2></div>
      <div class="hs-ctrl reveal"><button class="round hs-prev" aria-label="Previous">{ic('left')}</button><button class="round hs-next" aria-label="Next">{ic('right')}</button></div>
    </div>
    {timeline()}
  </div>
</section>

<section class="mist" aria-labelledby="story-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Our story</span><h2 id="story-title">How the Centre began and grew</h2></div></div>
    <div class="facts-list" data-stagger>
      <div class="fact"><b>Our home: the University of Nigeria</b><p>The University was founded by Dr. Nnamdi Azikiwe in 1955 and formally opened on 7 October 1960, as the first land-grant university in Africa. Its Nsukka campus covers 871 hectares of hilly savannah, about 80 km north of Enugu.</p><span class="src">Source: NCERD conference venue page, ncerd.com.ng</span></div>
      <div class="fact"><b>Established in 1980, operating from 1982</b><p>An Act of the National Assembly established the Centre in 1980 along with three other research centres. It started full operation in 1982, funded directly by the Federal Government.</p><span class="src">Sources: energyresearch.unn.edu.ng; unn.edu.ng</span></div>
      <div class="fact"><b>Early research areas</b><p>In its early years the Centre was active in solar, biomass and coal energy utilisation, energy consumption and energy policy studies, working with UNN departments of mechanical and agricultural engineering, physics, statistics, economics and sociology.</p><span class="src">Source: unn.edu.ng</span></div>
      <div class="fact"><b>The first building</b><p>The Centre was first housed in a multi-purpose building with seven offices, a small laboratory, small mechanical and electrical workshops, a library, a seminar room and a conference centre, with a computerised solar collector test rig and an attached meteorological station.</p><span class="src">Source: unn.edu.ng</span></div>
      <div class="fact"><b>Supervision by the Energy Commission</b><p>Decree No. 12 of 1988 and Decree No. 19 of 1989 gave the Energy Commission of Nigeria the legal mandate to supervise the research centres. The Commission now supervises six centres.</p><span class="src">Sources: energyresearch.unn.edu.ng; energy.gov.ng</span></div>
      <div class="fact"><b>Heads of the Centre</b><p>Heads named in published sources include Dr. C.N. Anyanwu (former Acting Director), Dr. P.E. Ugwuoke (Acting Director in the Centre's published directory) and the current Acting Director, Engr. Dr. Izuchukwu Francis Okafor.</p><span class="src">Sources: TEA-LP; energyresearch.unn.edu.ng; energy.gov.ng</span></div>
    </div>
  </div>
</section>

<section aria-labelledby="pics-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">In pictures</span><h2 id="pics-title">The NCERD complex</h2></div></div>
    <div class="gallery" data-stagger>
      <figure><img src="assets/images/building-1100.webp" alt="The NCERD building on the Nsukka campus" loading="lazy"><figcaption>The NCERD building, University of Nigeria, Nsukka campus</figcaption></figure>
      <figure><img src="assets/images/commissioning.webp" alt="Officials and staff at a ribbon-cutting ceremony at the Centre" loading="lazy"><figcaption>A commissioning ceremony at the Centre</figcaption></figure>
      <figure><img src="assets/images/inverter-room.webp" alt="Officials inspecting a solar inverter and battery bank installation" loading="lazy"><figcaption>Solar inverter and battery bank installation</figcaption></figure>
    </div>
  </div>
</section>

<section class="mist" aria-labelledby="fac">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Facilities</span><h2 id="fac">Research, fabrication and training under one roof</h2></div></div>
    <div class="fac" data-stagger>{''.join(f'<div class="fac-item"><span class="icon">{ic(i)}</span><span><b>{t}</b><span>{dsc}</span></span></div>' for i,t,dsc in FAC)}</div>
  </div>
</section>

<section class="dark" aria-labelledby="net-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">National network</span><h2 id="net-title">Part of the Energy Commission's network</h2><p class="lede">The Commission is headquartered at Plot 701C, Central Business District, Abuja.</p></div></div>
    {network()}
  </div>
</section>

<section aria-labelledby="partner">
  <div class="wrap">
    <div class="cta-band reveal-scale">
      <div><h2 id="partner">Work with the Centre</h2><p>We offer technical consultancy, produce our devices on request and train engineers, scientists and technicians. COREN lists NCERD among its renewable energy and energy efficiency training partners.</p></div>
      <div class="btns"><a class="btn btn-gold" href="contact-us.html">Contact us {ic('arrow')}</a><a class="btn btn-glass" href="projects.html">Our projects</a></div>
    </div>
  </div>
</section>
'''
write('about.html','About the Centre'+SUFFIX,'History, vision, mission, mandate and facilities of the National Centre for Energy Research and Development, University of Nigeria, Nsukka.',about)

# =================================================== PROJECTS
P=[
 ('Performance evaluation of a 50 L batch transesterification reactor','bio','done',''),
 ('Synthesis, characterisation and comparative analysis of dye-sensitised solar cells using natural and synthetic dyes with TiO₂ films','pv','done',''),
 ('Characterisation of eight woody biomass samples for fast pyrolysis experiments','bio','done',''),
 ('Design of a water scrubbing unit for biogas purification','bio','done',''),
 ('Improving the onset of flammable gas production from a pumpkin stalk and cow dung blend','bio','done',''),
 ('Biochemical characterisation of biogas microbes from biofuel production using old cabbage leaves','bio','done',''),
 ('Biogas production from the organic fraction of municipal solid waste','bio','done',''),
 ('Fast pyrolysis of eight biomass samples to produce bio-char, bio-oil and non-condensable gases','bio','done',''),
 ('Design and fabrication of an LM35-based thermo-regulator','el','done',''),
 ('Kinetic modelling of biogas production from blends of animal manure','bio','done','PhD work of Mr. I.S. Eze'),
 ('Characterisation of the liquid and solid products of fast pyrolysis of eight biomass samples','bio','done',''),
 ('Biogas production from blends of maize bracts and old cabbage leaf waste','bio','done',''),
 ('Preserving fresh amaranthus and pumpkin vegetables: open air compared with a solar refrigerator','st','done',''),
 ('Drying fresh stockfish under passive and active solar dryers and open sun','st','done',''),
 ('Briquetting of carbonised oil palm empty fruit bunch and palm kernel shells','bio','done',''),
 ('Bioethanol production from locally available starch feedstock','bio','done',''),
 ('Biodiesel production from locally available oil feedstock','bio','done',''),
 ('Growth and characterisation of thin-film nanocrystalline silicon materials and solar cells','pv','done','PhD work of Dr. S.N. Agbo, Delft University of Technology, 2012'),
 ('Building-integrated photovoltaics','pv','done','PhD work of Dr. C.U. Ikedi, University of Nottingham, 2012'),
 ('Design and fabrication of an automatic power changeover','el','done',''),
 ('Design and fabrication of a 1 kVA inverter','el','done','Electronics Laboratory'),
 ("Installation of PV street lights at the Vice-Chancellor's Lodge, UNN",'pv','done',''),
 ('Modelling neem methyl ester yield in a batch biodiesel reactor','bio','done','PhD work of Engr. C.N. Anyanwu'),
 ('Library automation and digitisation of library resources','info','on',''),
 ('Preparation and characterisation of dye-sensitised nanocrystalline solar cells using starch polymer electrolytes','pv','on',''),
 ('Household-scale solar-assisted water treatment system','st','on',''),
 ('Improved design and construction of a fast pyrolysis reactor','bio','on',''),
 ('Photovoltaic applicability of selected metallic selenide and sulphide thin films','pv','on',''),
 ('Biomass pulverising machine for thermo-conversion feedstock','bio','on',''),
 ('Bioenergy production and application from tropical vegetable waste in Nigeria','bio','on',''),
 ('Biogas pressure pump made from locally available materials','bio','on',''),
 ('Optimising anaerobic digestion of the organic fraction of municipal solid waste for biogas','bio','on',''),
 ('Water scrubbing unit for biogas cleaning and bottling in CNG cylinders','bio','on',''),
 ('Metal-organic frameworks for removing carbon dioxide from biogas: preliminary studies','bio','on',''),
 ('Growth and characterisation of PbS thin films and their applications','pv','on',''),
 ('Development of dye-sensitised solar cells','pv','on',''),
 ('Starch as a polymer host and its application in dye-sensitised solar cells','pv','on',''),
]
assert len(P)==37
AREAS=[('bio','Biomass, biogas and biofuels','flame'),('pv','Solar PV and materials','panel'),('st','Solar thermal','sun'),('el','Electronics','cpu'),('info','Information','book')]
AN={k:(n,i) for k,n,i in AREAS}
done=sum(p[2]=='done' for p in P); on=37-done
cnt={k:sum(p[1]==k for p in P) for k,_,_ in AREAS}
area_cards=''.join(f'<button class="area-card" data-area="{k}" aria-pressed="false"><span class="icon">{ic(i)}</span><b data-count="{cnt[k]}">{cnt[k]}</b><span>{n}</span><div class="bar"><i data-w="{cnt[k]/37*100:.1f}%"></i></div></button>' for k,n,i in AREAS)
cards=''
for idx,(t,a,s,n) in enumerate(P,1):
    an,ai=AN[a]; note=f'<span class="note">{n}</span>' if n else ''
    cards+=f'<article class="proj" data-status="{s}" data-area="{a}"><div class="top"><span class="icon">{ic(ai)}</span><span class="n">{idx:02d}</span></div><h3>{t}{note}</h3><div class="foot"><span class="tag">{an}</span><span class="status {s}">{"Completed" if s=="done" else "Ongoing"}</span></div></article>'
projects=phero('Research projects','Thirty-seven projects published by the Centre, from biogas and biofuels to thin-film solar cells and the electronics that keep systems running.','Projects',photo='assets/images/hero-solar.svg',
               stats=[(37,'Projects'),(done,'Completed'),(on,'Ongoing'),(5,'Research areas')])
projects+=f'''
<section aria-labelledby="by-area" style="padding-top:80px">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Browse by area</span><h2 id="by-area">Where our research goes</h2><p class="lede">Select an area to filter the projects below. Biomass, biogas and biofuels make up most of the portfolio.</p></div></div>
    <div class="area-cards" data-stagger>{area_cards}</div>
    <div class="toolbar">
      <div class="seg" role="group" aria-label="Filter by status"><span class="pill" aria-hidden="true"></span>
        <button data-filter="all" aria-pressed="true">All<span class="c">37</span></button>
        <button data-filter="done" aria-pressed="false">Completed<span class="c">{done}</span></button>
        <button data-filter="on" aria-pressed="false">Ongoing<span class="c">{on}</span></button>
      </div>
      <label class="search"><span class="sr">Search projects</span>{ic('search')}<input id="proj-q" type="search" placeholder="Search, for example biogas or thin film" autocomplete="off"></label>
    </div>
    <p class="count" id="proj-count" aria-live="polite">Showing 37 of 37 projects</p>
    <div class="proj-grid" id="proj-grid"><div class="proj-head" aria-hidden="true"><span>No.</span><span class="h-ic"></span><span>Project title</span><span class="h-area">Research area</span><span>Status</span></div>{cards}</div>
    <div class="empty" id="proj-empty" hidden>{ic('search')}<p><b>No projects match that search.</b></p><p>Try a broader word, such as solar or biomass.</p><button class="btn btn-ghost" id="proj-reset">Clear filters</button></div>
    <div class="notebox">{ic('info')}<p>Project titles and status are as published on the Centre's page at energyresearch.unn.edu.ng. For current status or to collaborate on a project, <a href="contact-us.html">contact the Centre</a>.</p></div>
  </div>
</section>
'''
write('projects.html','Research projects'+SUFFIX,'Completed and ongoing research projects of the National Centre for Energy Research and Development, UNN: biogas, biofuels, pyrolysis, solar PV, solar thermal and electronics.',projects)

# =================================================== STAFF
def initials(name):
    ps=[p for p in name.replace('(Mrs.)','').replace('.',' ').split() if p not in ('Mr','Mrs','Dr','Engr','Barr','Prof')]
    return (ps[0][0]+ps[-1][0]).upper()
def person(n,role,unit,i):
    return f'<article class="person"><div class="row"><div class="avatar" aria-hidden="true"><span>{initials(n)}</span></div><div><b>{n}</b><small>{role}</small></div></div><div class="unit">{ic(i)}{unit}</div></article>'
heads=''.join(person(h,'Unit head',n,i) for n,i,_,h in UNITS)
SUP=[('Mrs. H.A. Umeakuka','Administrative Secretary (Acting)','Administration','building'),('Mr. I.O. Imuoh','Unit head','Accounts','coins'),
     ('Mr. P.U. Nwafor','Unit head','Audit','clipboard'),('Mrs. U. Ogwo','Unit head','Library and ICT','library'),('Mr. M.C. Onyia','Unit head','Media','media'),
     ('Mr. O.D. Osondu','Unit head','Business','briefcase'),('Barr. S.O. Abangwu','Unit head','Legal','scale'),('Mrs. G.K. Uka','Unit head','Personnel and Pension','users')]
sup=''.join(person(n,r,u,i) for n,r,u,i in SUP)
staff=phero('Leadership and staff','Research fellows, engineers, technologists and administrators across nine research units and eight support units.','Staff',photo='assets/images/hero-solar.svg',
            stats=[(9,'Research units'),(8,'Support units')])
staff+=f'''
<section aria-labelledby="sup-title" style="padding-top:80px">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">Supervision</span><h2 id="sup-title">Supervision and leadership</h2></div></div>
    {leaders()}
  </div>
</section>
<section aria-labelledby="lead" style="padding-top:0">
  <div class="wrap">
    <div class="lead-card reveal-scale">
      {portrait()}
      <div>
        <span class="tag">Ag. Director, NCERD</span>
        <h2 id="lead" style="margin-top:16px">Engr. Dr. Izuchukwu Francis Okafor</h2>
        <div class="creds"><span>Ph.D.</span><span>M.Eng. (Mechanical Engineering)</span><span>B.Eng. (Mechanical Engineering)</span><span>SESN</span><span>MWEC-NNC</span><span>CMNSE</span><span>ASME</span><span>R.Engr., COREN</span></div>
        <p>He previously headed the Centre's Energy Management and Environment Unit and its National Stove Eligibility Laboratory. His research covers solar thermal systems, CFD modelling and simulation, industrial energy audits and efficiency, solid fuel briquettes, and cookstove design and testing.</p>
        <p style="margin-top:20px"><a class="btn btn-gold" href="mailto:izuchukwu.okafor@unn.edu.ng">{ic('mail')} Email the Director</a></p>
      </div>
    </div>

    <div class="block">
      <div class="group-title reveal"><h2>Heads of research units</h2><span>As listed in the published staff directory</span></div>
      <div class="people" data-stagger>{heads}</div>
    </div>
    <div class="block" style="margin-bottom:0">
      <div class="group-title reveal"><h2>Administration and support</h2><span>As listed in the published staff directory</span></div>
      <div class="people" data-stagger>{sup}</div>
    </div>
    <div class="notebox">{ic('info')}<p>Unit heads are listed as published in the Centre's staff directory on energyresearch.unn.edu.ng, and some posts may have changed since. The Acting Director is as listed by the Energy Commission of Nigeria. Search the <a href="http://www.unn.edu.ng/internals/staff/search?faculty=CENTRE+FOR+ENERGY+RESEARCH+AND+DEVELOPMENT&amp;department=CENTRE+FOR+ENERGY+RESEARCH+AND+DEVELOPMENT&amp;term=a" target="_blank" rel="noopener">full UNN staff directory for the Centre</a>.</p></div>
  </div>
</section>

<section class="mist" aria-labelledby="units-title">
  <div class="wrap">
    <div class="head-row"><div class="reveal"><span class="eyebrow">What each unit does</span><h2 id="units-title">Our research units</h2></div></div>
    {bento(True)}
  </div>
</section>
'''
write('staff-profiles.html','Staff and leadership'+SUFFIX,'Leadership, heads of research units and support units at the National Centre for Energy Research and Development, University of Nigeria, Nsukka.',staff)

# =================================================== NEWS
NEWS=[
 ('Apr','30','2024','conference','Call for papers','6th International Conference and Training Workshop announced','The Centre opened its call for papers for the 6th edition, with the first round of abstracts and full papers due on 30 April 2024.','https://ncerd.com.ng/our-speaker/engr-dr-i-f-okafor-msesn-mnse/','ncerd.com.ng'),
 ('','20 days','2024','training','Training','Practical solar PV training workshop','A full-time course from the solar resource through to PV system design, installation and maintenance. Open to applicants aged 18 to 40 with an engineering or science background, and to electricians.','https://ncerd.com.ng/front-page-features/aim-of-the-conference-training-workshop/','ncerd.com.ng'),
 ('Apr','','2023','publication','Publication','Proceedings of the 5th conference published','Energy Solutions for Attainment of Sustainable Development in Africa, edited by researchers of the Centre including the Acting Director.','https://www.researchgate.net/publication/370202123_Energy_Solutions_for_Attainment_of_Sustainable_Development_in_Africa','ResearchGate'),
 ('May','17–19','2022','conference','Conference','5th International Conference held at NCERD','Held physically and virtually on sustainable energy as a solution to post-COVID-19 energy challenges, with a training workshop from 25 April to 30 May 2022.','https://ncerd.com.ng/','ncerd.com.ng'),
 ('','','2022','training','Training','Solar PV training with COREN and NESP','Solar PV experts from the Centre trained shortlisted participants at NCERD with the Council for the Regulation of Engineering in Nigeria and the Nigerian Energy Support Programme.','https://www.researchgate.net/publication/370202123_Energy_Solutions_for_Attainment_of_Sustainable_Development_in_Africa','ResearchGate'),
 ('','','2022','lecture','Lecture','Director delivers Special Materials Lecture','Engr. Dr. I.F. Okafor spoke at the MSN Special Materials Lecture 2022 on materials for research and development of renewable energy devices.','https://msn.ng/sml/sml2022/','msn.ng'),
 ('Nov','11–13','2020','conference','Conference','4th International Conference and Training Workshop','Held at NCERD alongside professional solar PV training organised with the German Agency for International Cooperation (GIZ).','https://www.unn.edu.ng/author/chiomaokpoko/','unn.edu.ng'),
]
TYPE_IC={'conference':'mic','training':'cap','lecture':'users','publication':'file'}
chips=''.join(f'<button class="chip" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{ic(i)}{v}</button>' for k,v,i in [('all','All','layers'),('conference','Conferences','mic'),('training','Training','cap'),('lecture','Lectures','users'),('publication','Publications','file')])
posts=''
for m,dd,y,typ,label,t,body,url,src in NEWS:
    posts+=f'''<article class="post" data-type="{typ}"><div class="date"><span class="m">{m or label}</span><span class="d">{dd or y}</span><span class="y">{y if dd else '&nbsp;'}</span></div><div><span class="tag">{ic(TYPE_IC[typ])}{label}</span><h3>{t}</h3><p>{body}</p><a class="link-arrow" href="{url}" target="_blank" rel="noopener">Source: {src} {ic('arrow-ur')}</a></div></article>'''
news=phero('News and events','Conferences, training workshops, lectures and publications from the Centre.','News',photo='assets/images/inverter-room.webp')
news+=f'''
<section style="padding-top:80px">
  <div class="wrap">
    <article class="feature reveal-clip" style="margin-bottom:64px">
      <div class="ph"><img src="assets/images/building-1100.webp" alt="The NCERD complex, venue of the training workshops" loading="lazy"></div>
      <div class="tx">
        <span class="eyebrow" style="color:var(--gold-300)">Featured training</span>
        <h2>Learn solar PV design, installation and maintenance</h2>
        <ul class="list">
          <li>{ic('check')}20 days of practical, full-time training at the NCERD complex</li>
          <li>{ic('check')}For engineers, scientists and electricians aged 18 to 40</li>
          <li>{ic('check')}Training manual, materials and certificate included</li>
        </ul>
        <div class="btns"><a class="btn btn-gold" href="mailto:ncerdunn.conference@gmail.com">Apply by email {ic('send')}</a><a class="btn btn-glass" href="https://ncerd.com.ng/front-page-features/aim-of-the-conference-training-workshop/" target="_blank" rel="noopener">Course details</a></div>
      </div>
    </article>
    <div class="head-row" style="margin-bottom:24px"><div class="reveal"><span class="eyebrow">Archive</span><h2>All news and events</h2></div></div>
    <div class="chips" role="group" aria-label="Filter by type">{chips}</div>
    <div class="news-grid" id="news-grid" data-stagger>{posts}</div>
    <div class="notebox">{ic('info')}<p>For announcements not yet listed here, call <a href="tel:+2348065702570">+234 806 570 2570</a> or email <a href="mailto:ncerdunn@yahoo.com">ncerdunn@yahoo.com</a>.</p></div>
  </div>
</section>
'''
write('news-events.html','News and events'+SUFFIX,'Conferences, solar PV training workshops, lectures and publications from the National Centre for Energy Research and Development, UNN.',news)

# =================================================== RESOURCES
G=[
 ('network','Supervising body and network','The Energy Commission of Nigeria and its research centres.',[
   ('Energy Commission of Nigeria','The Centre\'s supervising body','https://energy.gov.ng','energy.gov.ng'),
   ('ECN research centres','The six centres and their areas of research','https://energy.gov.ng/research_centers.php','energy.gov.ng'),
   ('ECN leadership','The Commission\'s management and centre directors','https://energy.gov.ng/team.html','energy.gov.ng'),
   ('Hydropower research centre','National Centre for Hydropower Research and Development, Ilorin','https://nachred.unilorin.edu.ng','unilorin.edu.ng')]),
 ('cap','University of Nigeria','Our host university\'s services.',[
   ('University of Nigeria, Nsukka','The University\'s official website','https://www.unn.edu.ng','unn.edu.ng'),
   ('CBT exams status table','Computer-based test timetable','http://www.unn.edu.ng/cbttimetable/','unn.edu.ng'),
   ('UNN staff directory','Search staff of the Centre','http://www.unn.edu.ng/internals/staff/search?faculty=CENTRE+FOR+ENERGY+RESEARCH+AND+DEVELOPMENT&department=CENTRE+FOR+ENERGY+RESEARCH+AND+DEVELOPMENT&term=a','unn.edu.ng'),
   ('NCERD on unn.edu.ng','The Centre\'s university web page','https://energyresearch.unn.edu.ng','energyresearch.unn.edu.ng'),
   ('NCERD website','The Centre\'s own website','https://www.ncerd-unn.gov.ng','ncerd-unn.gov.ng')]),
 ('mic','Conferences and training','Our conference series and training recognition.',[
   ('NCERD conference website','Energy for Sustainable Development in Africa','https://ncerd.com.ng','ncerd.com.ng'),
   ('Solar PV training workshop','Course content, eligibility and how to apply','https://ncerd.com.ng/front-page-features/aim-of-the-conference-training-workshop/','ncerd.com.ng'),
   ('COREN training partners','NCERD is a renewable energy and energy efficiency training partner','https://coren.gov.ng/training-institutions/','coren.gov.ng')]),
 ('file','Publications','Research outputs from the Centre.',[
   ('Energy Solutions for Attainment of Sustainable Development in Africa','Proceedings of the 5th conference, 2023','https://www.researchgate.net/publication/370202123_Energy_Solutions_for_Attainment_of_Sustainable_Development_in_Africa','researchgate.net'),
   ('Energy technologies for sustainable rural agriculture in Nigeria','Solar brooders, incubators and PV systems developed at NCERD','https://www.researchgate.net/publication/351721263_Deployment_of_energy_technologies_for_sustainable_rural_agricultural_development_in_Nigeria','researchgate.net'),
   ('Renewable energy penetration in South-East Nigeria','Survey by NCERD researchers','https://www.researchgate.net/publication/215909831_Renewable_energy_penetration_in_Nigeria_A_study_of_the_South-East_Zone','researchgate.net')]),
]
grp=''
for i,t,dsc,links in G:
    lc=''.join(f'<a class="lc" href="{u}" target="_blank" rel="noopener"><span class="go">{ic("arrow-ur")}</span><b>{a}</b><span>{b}</span><span class="dom">{dom}</span></a>' for a,b,u,dom in links)
    grp+=f'<div class="res-group"><div class="reveal"><div class="sticky"><div class="icon">{ic(i)}</div><h2>{t}</h2><p class="lede">{dsc}</p></div></div><div class="link-cards" data-stagger>{lc}</div></div>'
res=phero('Resources and links','Official websites, university services, conference pages and publications connected to the Centre.','Resources',photo='assets/images/hero-solar.svg')
res+=f'<section><div class="wrap res-groups">{grp}</div></section>'
write('external-resources.html','Resources and links'+SUFFIX,'Links to the Energy Commission of Nigeria, University of Nigeria services, NCERD conferences, training and publications.',res)

# =================================================== CONTACT
contact=phero('Contact the Centre','Call, email or visit us on the Nsukka campus. We welcome research partnerships, consultancy enquiries and training applications.','Contact',photo='assets/images/building-2000.webp')
contact+=f'''
<section style="padding-top:0">
  <div class="wrap">
    <div class="reach" data-stagger>
      <div class="rcard"><div class="icon">{ic('phone')}</div><h2>Call</h2><a href="tel:+2348065702570">+234 806 570 2570</a><a href="tel:+2348082770823">+234 808 277 0823</a></div>
      <div class="rcard"><div class="icon">{ic('mail')}</div><h2>Email</h2><a href="mailto:ncerdunn@yahoo.com">ncerdunn@yahoo.com</a><small>Conference and training: <a href="mailto:ncerdunn.conference@gmail.com">ncerdunn.conference@gmail.com</a></small></div>
      <div class="rcard"><div class="icon">{ic('pin')}</div><h2>Visit</h2><span class="v">University of Nigeria, Nsukka Campus</span><small>Nsukka, Enugu State, Nigeria</small></div>
    </div>
  </div>
</section>
<section style="padding-top:24px">
  <div class="wrap contact-layout">
    <div class="form-card reveal">
      <span class="eyebrow">Send an enquiry</span>
      <h2>How can we help?</h2>
      <p class="lede">Fill in the form and your email app will open with the message ready to send to the Centre.</p>
      <form id="enquiry" class="form" novalidate>
        <div class="field"><input id="f-name" name="name" autocomplete="name" placeholder=" " required><label for="f-name">Full name</label><span class="err">Enter your name.</span></div>
        <div class="field"><input id="f-email" name="email" type="email" autocomplete="email" placeholder=" " required><label for="f-email">Email address</label><span class="err">Enter an email address like name@example.com.</span></div>
        <div class="field"><input id="f-org" name="org" autocomplete="organization" placeholder=" "><label for="f-org">Organisation (optional)</label></div>
        <div class="field"><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder=" "><label for="f-phone">Phone (optional)</label></div>
        <div class="field full"><select id="f-topic" name="topic"><option>Research partnership</option><option>Technical consultancy</option><option>Training and workshops</option><option>Conference</option><option>Student enquiry</option><option>General enquiry</option></select><label for="f-topic">What is it about?</label></div>
        <div class="field full"><input id="f-subject" name="subject" placeholder=" " required><label for="f-subject">Subject</label><span class="err">Add a short subject.</span></div>
        <div class="field full"><textarea id="f-msg" name="message" placeholder=" " required></textarea><label for="f-msg">Your message</label><span class="err">Write your message.</span></div>
        <div class="actions"><small>Sends to ncerdunn@yahoo.com</small><button class="btn btn-green" type="submit">Open email to send {ic('send')}</button></div>
        <p class="form-ok" id="form-ok" role="status">{ic('check')}Your email app should now be open with your message. Press send there to reach the Centre.</p>
      </form>
    </div>
    <div class="side">
      <div class="map-card reveal-scale">
        <iframe title="Map of the NCERD complex on the University of Nigeria, Nsukka campus" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=7.3858%2C6.8507%2C7.4058%2C6.8627&amp;layer=mapnik&amp;marker=6.85667%2C7.39583"></iframe>
        <div class="pin"><div><b>NCERD complex</b><span>6°51′24″N, 7°23′45″E</span></div><a class="btn btn-dark" href="https://www.openstreetmap.org/?mlat=6.85667&amp;mlon=7.39583#map=17/6.85667/7.39583" target="_blank" rel="noopener">Directions {ic('arrow-ur')}</a></div>
      </div>
      <div class="info reveal">
        <h3>Other contacts</h3>
        <dl>
          <div><dt>Website</dt><dd><a href="https://www.ncerd-unn.gov.ng" target="_blank" rel="noopener">www.ncerd-unn.gov.ng</a></dd></div>
          <div><dt>Director</dt><dd><a href="mailto:izuchukwu.okafor@unn.edu.ng">izuchukwu.okafor@unn.edu.ng</a></dd></div>
          <div><dt>Supervising body</dt><dd><a href="https://energy.gov.ng" target="_blank" rel="noopener">Energy Commission of Nigeria</a>, Plot 701C, Central Business District, Abuja</dd></div>
          <div><dt>Host university</dt><dd><a href="https://www.unn.edu.ng" target="_blank" rel="noopener">University of Nigeria, Nsukka</a></dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>
'''
write('contact-us.html','Contact us'+SUFFIX,'Phone, email, address and map for the National Centre for Energy Research and Development, University of Nigeria, Nsukka.',contact)
print('built v2')
