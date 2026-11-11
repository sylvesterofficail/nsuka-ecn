"""Custom line illustrations for research-unit cards (ECN green palette)."""
import os
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'units')
os.makedirs(OUT, exist_ok=True)

L = '#8fd3a8'   # light line
M = '#3fae6f'   # mid green
F = '#0e5a33'   # fill green
W = '#ffffff'

def wrap(body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b3a24"/><stop offset="1" stop-color="#03190f"/></linearGradient>
  <radialGradient id="glow" cx=".78" cy=".2" r=".6"><stop offset="0" stop-color="#00692f" stop-opacity=".55"/><stop offset="1" stop-color="#00692f" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>
</defs>
<rect width="600" height="450" fill="url(#bg)"/><rect width="600" height="450" fill="url(#glow)"/><rect width="600" height="450" fill="url(#grid)"/>
<g fill="none" stroke="{L}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
{body}
</g></svg>'''

def sun(cx, cy, r=26):
    rays = ''.join(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy}" transform="rotate({a} {cx} {cy}) translate(0 -{r+12})" stroke="{L}"/>' for a in range(0, 360, 45))
    rays = ''.join(f'<path d="M{cx} {cy-r-10} v-14" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45))
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{F}"/>{rays}'

ART = {}

# 1 Solar thermal: thermosyphon water heater on a roof
ART['solar-thermal'] = sun(110, 90) + f'''
<path d="M150 360 L300 250 L560 250 L560 360 Z" fill="{F}" fill-opacity=".35"/>
<path d="M300 250 L560 250"/>
<g transform="translate(330 140)">
  <path d="M0 110 L60 0 L210 0 L150 110 Z" fill="{F}"/>
  <path d="M15 82 L165 82 M30 55 L180 55 M45 28 L195 28"/>
  <path d="M40 110 L100 0 M80 110 L140 0 M120 110 L180 0" stroke-opacity=".5"/>
  <rect x="70" y="-46" width="150" height="38" rx="19" fill="{F}"/>
  <path d="M82 -27 h126" stroke-opacity=".5"/>
  <path d="M150 110 v40 M10 110 v40"/>
</g>
<path d="M60 380 H560" stroke-opacity=".4"/>'''

# 2 Biomass and biogas: fixed-dome digester with inlet, outlet and gas line
ART['biomass'] = f'''
<path d="M40 330 H560" stroke-opacity=".5"/>
<path d="M190 330 C190 230 410 230 410 330" fill="{F}"/>
<path d="M210 330 C215 265 385 265 390 330" stroke-opacity=".5"/>
<path d="M190 330 V380 H410 V330" stroke-opacity=".7"/>
<path d="M120 300 L120 330 M100 300 H160 L190 360" />
<path d="M480 300 V330 M450 300 H510 M410 360 L450 300"/>
<path d="M300 245 V170 H430 V130"/>
<circle cx="430" cy="118" r="12" fill="{F}"/>
<path d="M418 100 C420 88 430 84 430 72 C440 84 442 90 442 100" fill="{M}" fill-opacity=".5"/>
<g transform="translate(70 120)"><path d="M0 120 C10 60 60 20 120 10 C110 70 70 110 0 120 Z" fill="{F}"/><path d="M0 120 C40 80 70 50 120 10"/></g>
<g transform="translate(140 150) scale(.6)"><path d="M0 120 C10 60 60 20 120 10 C110 70 70 110 0 120 Z" fill="{F}"/><path d="M0 120 C40 80 70 50 120 10"/></g>'''

# 3 Photovoltaics: ground-mounted array
def panel(x, y):
    s = f'<g transform="translate({x} {y})"><path d="M0 90 L40 0 L200 0 L160 90 Z" fill="{F}"/>'
    s += '<path d="M10 67 L170 67 M20 45 L180 45 M30 22 L190 22" stroke-opacity=".55"/>'
    s += '<path d="M40 90 L80 0 M80 90 L120 0 M120 90 L160 0" stroke-opacity=".55"/>'
    s += '<path d="M60 90 v40 M140 90 v40"/></g>'
    return s
ART['pv'] = sun(500, 80, 22) + panel(60, 200) + panel(250, 200) + panel(150, 290) + f'<path d="M30 420 H580" stroke-opacity=".4"/>'

# 4 Energy management and environment: meter gauge + cookstove
ART['energy-mgmt'] = f'''
<g transform="translate(400 150)"><path d="M-110 40 A110 110 0 0 1 110 40" stroke-width="10" stroke="{F}"/>
<path d="M-110 40 A110 110 0 0 1 40 -62" stroke="{M}" stroke-width="10"/>
<path d="M0 40 L60 -40" stroke="{W}" stroke-width="4"/><circle cx="0" cy="40" r="10" fill="{L}"/>
<path d="M-95 40 h12 M95 40 h-12 M0 -55 v12 M-67 -27 l9 9 M67 -27 l-9 9" /></g>
<g transform="translate(90 220)">
  <path d="M20 60 H200 L185 170 H35 Z" fill="{F}"/>
  <rect x="0" y="40" width="220" height="22" rx="6" fill="{F}"/>
  <path d="M85 170 V200 M135 170 V200"/>
  <rect x="80" y="110" width="60" height="40" rx="6" />
  <path d="M100 140 C100 125 110 122 110 112 C120 122 122 128 120 140" fill="{M}" fill-opacity=".6"/>
  <path d="M40 40 C40 -10 180 -10 180 40" fill="{F}" fill-opacity=".6"/>
  <path d="M90 -20 c-10 -15 10 -25 0 -40 M130 -20 c-10 -15 10 -25 0 -40" stroke-opacity=".6"/>
</g>
<path d="M40 420 H560" stroke-opacity=".4"/>'''

# 5 Wind and meteorology: turbine + anemometer + clouds
ART['wind'] = f'''
<g transform="translate(410 150)"><path d="M-6 0 L-14 270 H14 L6 0 Z" fill="{F}"/>
<circle r="14" fill="{L}"/>
<path d="M0 -12 C10 -60 14 -100 4 -130 C-8 -100 -10 -60 0 -12 Z" fill="{F}"/>
<path d="M0 -12 C10 -60 14 -100 4 -130 C-8 -100 -10 -60 0 -12 Z" fill="{F}" transform="rotate(120)"/>
<path d="M0 -12 C10 -60 14 -100 4 -130 C-8 -100 -10 -60 0 -12 Z" fill="{F}" transform="rotate(240)"/></g>
<g transform="translate(160 250)"><path d="M0 0 V170"/><path d="M-60 0 H60"/>
<circle cx="-60" cy="-8" r="14" fill="{F}"/><circle cx="60" cy="-8" r="14" fill="{F}"/><circle cx="0" cy="-8" r="6" fill="{L}"/>
<path d="M-20 60 H20 V100 H-20 Z" fill="{F}"/></g>
<path d="M60 120 H210 M90 150 H260 M40 180 H170" stroke-opacity=".5"/>
<path d="M30 420 H570" stroke-opacity=".4"/>'''

# 6 Fossil energy: briquettes and coal
def briq(x, y, r=34):
    holes = ''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="5"/>' for dx, dy in [(0,0),(-14,-10),(14,-10),(-14,10),(14,10)])
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{F}"/>{holes}'
ART['fossil'] = f'''
<path d="M40 380 L170 200 L250 290 L330 170 L560 380 Z" fill="{F}" fill-opacity=".4"/>
<path d="M40 380 L170 200 L250 290 L330 170 L560 380"/>
''' + briq(300, 330) + briq(372, 330) + briq(444, 330) + briq(336, 270) + briq(408, 270) + f'''
<path d="M100 400 L130 370 L170 380 L160 410 Z" fill="{F}"/><path d="M180 410 L200 385 L235 395 L225 415 Z" fill="{F}"/>
<path d="M30 420 H570" stroke-opacity=".4"/>'''

# 7 Energy information and manpower development: board with chart, books, cap
ART['information'] = f'''
<rect x="230" y="70" width="320" height="210" rx="10" fill="{F}"/>
<path d="M260 240 L330 180 L380 210 L450 130 L520 160" stroke="{W}" stroke-width="3"/>
<path d="M260 250 H520 M260 100 V250" stroke-opacity=".5"/>
<path d="M390 280 V330 M330 330 H450"/>
<g transform="translate(70 270)"><rect x="0" y="40" width="150" height="26" rx="4" fill="{F}"/><rect x="12" y="14" width="130" height="26" rx="4" fill="{F}"/><rect x="0" y="-12" width="140" height="26" rx="4" fill="{F}"/></g>
<g transform="translate(140 170)"><path d="M-70 0 L0 -35 L70 0 L0 35 Z" fill="{F}"/><path d="M-40 15 V50 C-20 70 20 70 40 50 V15"/><path d="M70 0 V45"/></g>
<path d="M30 420 H570" stroke-opacity=".4"/>'''

# 8 Design and production workshops: gear, wrench, workbench
def gear(cx, cy, r, n=10):
    import math
    pts = []
    for i in range(n*2):
        a = math.pi*2*i/(n*2)
        rr = r if i % 2 == 0 else r*0.8
        a2 = a + math.pi/(n*2)
        pts.append((cx+rr*math.cos(a), cy+rr*math.sin(a)))
        pts.append((cx+rr*math.cos(a2), cy+rr*math.sin(a2)))
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
    return f'<path d="{d}" fill="{F}"/><circle cx="{cx}" cy="{cy}" r="{r*0.32:.0f}"/>'
ART['workshop'] = gear(420, 150, 90, 12) + gear(290, 240, 55, 9) + f'''
<path d="M60 330 H560 M90 330 V410 M530 330 V410" stroke-width="3"/>
<rect x="60" y="310" width="500" height="20" rx="4" fill="{F}"/>
<g transform="translate(140 220) rotate(-35)"><path d="M0 0 h120" stroke-width="12" stroke="{F}"/><path d="M0 0 h120" /><path d="M120 -18 a18 18 0 1 1 0 36 l-10 -10 v-16 z" fill="{F}"/></g>'''

# 9 Laboratories: flasks, beakers, microscope
ART['labs'] = f'''
<path d="M40 380 H560" stroke-width="3"/>
<g transform="translate(110 200)"><path d="M30 0 V60 L-10 170 H110 L70 60 V0" fill="{F}"/><path d="M20 0 H80"/><path d="M5 130 H95" stroke-opacity=".6"/></g>
<g transform="translate(250 260)"><path d="M0 0 V110 Q0 120 10 120 H80 Q90 120 90 110 V0" fill="{F}"/><path d="M0 50 H90" stroke-opacity=".6"/><path d="M-6 0 H96"/></g>
<g transform="translate(430 130)">
  <path d="M-60 250 H70" stroke-width="4"/><path d="M0 250 V200 C0 170 40 160 50 130" />
  <rect x="20" y="20" width="34" height="110" rx="6" transform="rotate(-25 37 75)" fill="{F}"/>
  <path d="M-30 200 H50" /><circle cx="10" cy="225" r="16" fill="{F}"/>
</g>
<circle cx="150" cy="150" r="8" fill="{M}"/><circle cx="170" cy="120" r="5" fill="{M}"/><circle cx="160" cy="95" r="3.5" fill="{M}"/>'''

# 10 Research library: shelves of books and an open book
ART['library'] = f'''
<path d="M60 120 H330 M60 230 H330 M60 340 H330" stroke-width="3"/>
<rect x="80" y="60" width="26" height="60" fill="{F}"/><rect x="112" y="70" width="22" height="50" fill="{F}"/><rect x="140" y="55" width="30" height="65" fill="{F}"/><path d="M180 120 L200 68 L222 74 L204 120" fill="{F}"/><rect x="235" y="65" width="24" height="55" fill="{F}"/><rect x="266" y="75" width="40" height="45" fill="{F}"/>
<rect x="80" y="170" width="34" height="60" fill="{F}"/><rect x="120" y="180" width="22" height="50" fill="{F}"/><rect x="150" y="165" width="28" height="65" fill="{F}"/><rect x="186" y="175" width="26" height="55" fill="{F}"/><rect x="220" y="168" width="30" height="62" fill="{F}"/><rect x="258" y="182" width="48" height="48" fill="{F}"/>
<rect x="84" y="282" width="30" height="58" fill="{F}"/><rect x="122" y="290" width="26" height="50" fill="{F}"/><rect x="156" y="278" width="34" height="62" fill="{F}"/><rect x="200" y="288" width="24" height="52" fill="{F}"/><rect x="232" y="280" width="30" height="60" fill="{F}"/>
<g transform="translate(460 250)"><path d="M0 -10 C-40 -40 -90 -40 -120 -25 V90 C-90 75 -40 75 0 105 Z" fill="{F}"/><path d="M0 -10 C40 -40 90 -40 120 -25 V90 C90 75 40 75 0 105 Z" fill="{F}"/><path d="M0 -10 V105"/><path d="M-95 5 C-70 -5 -40 -2 -20 10 M-95 30 C-70 20 -40 23 -20 35 M20 10 C40 -2 70 -5 95 5 M20 35 C40 23 70 20 95 30" stroke-opacity=".7"/></g>
<path d="M30 420 H570" stroke-opacity=".4"/>'''

for k, v in ART.items():
    with open(os.path.join(OUT, f'{k}.svg'), 'w') as f:
        f.write(wrap(v))
print('wrote', len(ART))
