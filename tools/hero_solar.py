import os
W,H=1600,700
out=[]
out.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#062b1a"/><stop offset=".55" stop-color="#0b3a24"/><stop offset="1" stop-color="#03190f"/></linearGradient>
<radialGradient id="sun" cx=".74" cy=".36" r=".38"><stop offset="0" stop-color="#9fdcb5" stop-opacity=".55"/><stop offset=".35" stop-color="#2e9d5c" stop-opacity=".25"/><stop offset="1" stop-color="#00692f" stop-opacity="0"/></radialGradient>
<linearGradient id="cell" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#145c3a"/><stop offset="1" stop-color="#062b1a"/></linearGradient>
<linearGradient id="glint" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9fdcb5" stop-opacity="0"/><stop offset=".5" stop-color="#9fdcb5" stop-opacity=".35"/><stop offset="1" stop-color="#9fdcb5" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<rect width="{W}" height="{H}" fill="url(#sun)"/>
<circle cx="1184" cy="252" r="46" fill="#9fdcb5" fill-opacity=".85"/>
<path d="M0 330 C 220 300 420 320 640 305 C 900 288 1150 318 1600 300 L1600 360 L0 360 Z" fill="#0a3320"/>
<path d="M0 352 L1600 352" stroke="#8fd3a8" stroke-opacity=".25"/>
''')
# perspective rows of panels from horizon (y=360) to bottom
import math
rows=7
for r in range(rows):
    t=(r+1)/rows
    y=360+ (H-360)*(t**1.6)
    ph=14+70*(t**1.4)           # panel height
    pw=60+190*(t**1.4)          # panel width
    gap=pw*0.12
    skew=ph*0.55
    lw=0.6+1.6*t
    op=0.35+0.6*t
    x=-pw*(0.3 if r%2 else 0.8)
    while x< W+pw:
        x0,y0=x,y
        pts=f'{x0:.1f},{y0:.1f} {x0+pw:.1f},{y0:.1f} {x0+pw-skew:.1f},{y0-ph:.1f} {x0-skew:.1f},{y0-ph:.1f}'
        out.append(f'<polygon points="{pts}" fill="url(#cell)" stroke="#8fd3a8" stroke-opacity="{op:.2f}" stroke-width="{lw:.2f}"/>')
        # cell grid
        for k in range(1,4):
            yy=y0-ph*k/4; xs=x0-skew*k/4
            out.append(f'<line x1="{xs:.1f}" y1="{yy:.1f}" x2="{xs+pw:.1f}" y2="{yy:.1f}" stroke="#8fd3a8" stroke-opacity="{op*0.45:.2f}" stroke-width="{lw*0.6:.2f}"/>')
        for k in range(1,6):
            xa=x0+pw*k/6
            out.append(f'<line x1="{xa:.1f}" y1="{y0:.1f}" x2="{xa-skew:.1f}" y2="{y0-ph:.1f}" stroke="#8fd3a8" stroke-opacity="{op*0.45:.2f}" stroke-width="{lw*0.6:.2f}"/>')
        # glint
        out.append(f'<polygon points="{x0+pw*0.15:.1f},{y0:.1f} {x0+pw*0.32:.1f},{y0:.1f} {x0+pw*0.32-skew:.1f},{y0-ph:.1f} {x0+pw*0.15-skew:.1f},{y0-ph:.1f}" fill="url(#glint)" opacity="{0.4*t:.2f}"/>')
        # legs
        out.append(f'<line x1="{x0+pw*0.25:.1f}" y1="{y0:.1f}" x2="{x0+pw*0.25:.1f}" y2="{y0+ph*0.45:.1f}" stroke="#8fd3a8" stroke-opacity="{op*0.6:.2f}" stroke-width="{lw:.2f}"/>')
        out.append(f'<line x1="{x0+pw*0.75:.1f}" y1="{y0:.1f}" x2="{x0+pw*0.75:.1f}" y2="{y0+ph*0.45:.1f}" stroke="#8fd3a8" stroke-opacity="{op*0.6:.2f}" stroke-width="{lw:.2f}"/>')
        x+=pw+gap
out.append('</svg>')
p=os.path.join(os.path.dirname(__file__),'..','assets','images','hero-solar.svg')
open(p,'w').write('\n'.join(out)); print(os.path.getsize(p))
