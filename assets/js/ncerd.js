/* NCERD UNN — site script v2 (no dependencies) */
(function(){
  'use strict';
  var d=document, root=d.documentElement;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce) root.classList.add('motion');
  var $=function(s,c){return (c||d).querySelector(s);}, $$=function(s,c){return [].slice.call((c||d).querySelectorAll(s));};

  /* ---------- Page transitions ---------- */
  if(!reduce){
    d.addEventListener('click',function(e){
      var a=e.target.closest('a'); if(!a) return;
      var href=a.getAttribute('href')||'';
      if(a.target==='_blank'||e.metaKey||e.ctrlKey||e.shiftKey||href.charAt(0)==='#'||/^(mailto|tel|https?):/.test(href)) return;
      if(!/\.html(#.*)?$/.test(href)) return;
      e.preventDefault(); d.body.classList.add('leaving');
      setTimeout(function(){location.href=href;},220);
    });
    window.addEventListener('pageshow',function(){d.body.classList.remove('leaving');});
  }

  /* ---------- Header, progress, back-to-top ---------- */
  var head=$('.site-head'), prog=$('.progress'), top=$('.to-top'), lastY=0;
  function onScroll(){
    var y=window.scrollY||0, max=d.documentElement.scrollHeight-innerHeight, p=max>0?y/max:0;
    if(head&&!head.classList.contains('static')){
      head.classList.toggle('solid',y>40);
      if(!d.body.classList.contains('menu-open')){
        if(y>600&&y>lastY+4) head.classList.add('hide');
        else if(y<lastY-4||y<=600) head.classList.remove('hide');
      }
    }
    if(prog) prog.style.setProperty('--p',p.toFixed(4));
    if(top){top.classList.toggle('show',y>700);top.style.setProperty('--p',p.toFixed(4));}
    lastY=y;
  }
  addEventListener('scroll',onScroll,{passive:true});
  if(top) top.addEventListener('click',function(){scrollTo({top:0,behavior:reduce?'auto':'smooth'});});

  /* ---------- Mobile menu ---------- */
  var btn=$('.menu-btn'), nav=$('#nav');
  function setMenu(open){
    nav.classList.toggle('open',open); btn.setAttribute('aria-expanded',open);
    btn.querySelector('.lbl').textContent=open?'Close':'Menu';
    d.body.classList.toggle('menu-open',open); head.classList.toggle('menu-on',open); head.classList.remove('hide');
  }
  if(btn&&nav){
    btn.addEventListener('click',function(){setMenu(!nav.classList.contains('open'));});
    d.addEventListener('keydown',function(e){if(e.key==='Escape'&&nav.classList.contains('open')){setMenu(false);btn.focus();}});
  }

  /* ---------- Reveal on scroll ---------- */
  $$('[data-stagger]').forEach(function(g){
    [].forEach.call(g.children,function(c,i){c.classList.add('reveal');c.style.setProperty('--i',i%8);});
  });
  var watch=$$('.reveal,.reveal-scale,.reveal-clip,[data-count],[data-w]');
  function countUp(el){
    var end=parseFloat(el.getAttribute('data-count')), from=end>1000?end-60:0, t0=null, dur=1600;
    if(reduce){el.textContent=end;return;}
    requestAnimationFrame(function step(t){if(!t0)t0=t;var k=Math.min((t-t0)/dur,1),e=1-Math.pow(1-k,4);el.textContent=Math.round(from+(end-from)*e);if(k<1)requestAnimationFrame(step);});
  }
  function activate(el){
    el.classList.add('in');
    if(el.hasAttribute('data-count')) countUp(el);
    if(el.hasAttribute('data-w')) el.style.width=el.getAttribute('data-w');
  }
  if('IntersectionObserver' in window&&!reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){activate(en.target);io.unobserve(en.target);}});},{rootMargin:'0px 0px -6% 0px',threshold:.06});
    watch.forEach(function(el){io.observe(el);});
  } else watch.forEach(activate);


  /* ---------- Portrait fallback ---------- */
  $$('.portrait img,.leader .ph img').forEach(function(img){
    function fail(){img.parentNode.classList.add('noimg');}
    img.addEventListener('error',fail); if(img.complete&&img.naturalWidth===0) fail();
  });
  var yr=$('#yr'); if(yr) yr.textContent=new Date().getFullYear();

  /* ---------- Live sun over Nsukka ---------- */
  var sky=$('#sky');
  if(sky){
    var LAT=6.85667,LON=7.39583,TZ=1,rad=Math.PI/180,NS='http://www.w3.org/2000/svg',first=true;
    var solar=function(date){
      var jd=date.getTime()/864e5+2440587.5,t=(jd-2451545)/36525;
      var L0=(280.46646+t*(36000.76983+t*.0003032))%360, M=357.52911+t*(35999.05029-.0001537*t), e=.016708634-t*(.000042037+.0000001267*t);
      var C=Math.sin(M*rad)*(1.914602-t*(.004817+.000014*t))+Math.sin(2*M*rad)*(.019993-.000101*t)+Math.sin(3*M*rad)*.000289;
      var lam=L0+C-.00569-.00478*Math.sin((125.04-1934.136*t)*rad);
      var eps=23+(26+(21.448-t*(46.815+t*(.00059-t*.001813)))/60)/60+.00256*Math.cos((125.04-1934.136*t)*rad);
      var dec=Math.asin(Math.sin(eps*rad)*Math.sin(lam*rad))/rad, y=Math.pow(Math.tan(eps*rad/2),2);
      var eot=4/rad*(y*Math.sin(2*L0*rad)-2*e*Math.sin(M*rad)+4*e*y*Math.sin(M*rad)*Math.cos(2*L0*rad)-.5*y*y*Math.sin(4*L0*rad)-1.25*e*e*Math.sin(2*M*rad));
      return {dec:dec,eot:eot};
    };
    var elev=function(date){var s=solar(date),m=date.getUTCHours()*60+date.getUTCMinutes()+date.getUTCSeconds()/60,ha=(m+s.eot+4*LON)/4-180;
      var cz=Math.sin(LAT*rad)*Math.sin(s.dec*rad)+Math.cos(LAT*rad)*Math.cos(s.dec*rad)*Math.cos(ha*rad);return 90-Math.acos(Math.max(-1,Math.min(1,cz)))/rad;};
    var fmt=function(u){var m=Math.round(((u+TZ*60)%1440+1440)%1440),h=Math.floor(m/60),mm=m%60;return (h<10?'0':'')+h+':'+(mm<10?'0':'')+mm;};
    var dayOf=function(now){var s=solar(now),noon=720-4*LON-s.eot,cosH=(Math.cos(90.833*rad)-Math.sin(LAT*rad)*Math.sin(s.dec*rad))/(Math.cos(LAT*rad)*Math.cos(s.dec*rad)),H=Math.acos(cosH)/rad;return {rise:noon-4*H,noon:noon,set:noon+4*H};};
    var mk=function(n,a){var x=d.createElementNS(NS,n);for(var k in a)x.setAttribute(k,a[k]);return x;};
    var draw=function(){
      var now=new Date(),dd=dayOf(now),base=Date.UTC(now.getUTCFullYear(),now.getUTCMonth(),now.getUTCDate());
      var W=sky.clientWidth||1200,H=sky.clientHeight||800,small=W<760;
      var h1=d.querySelector('.hero h1'),hr=h1?h1.getBoundingClientRect().right-sky.getBoundingClientRect().left:W*.5,x0=small?W*.08:Math.min(W*.62,Math.max(W*.5,hr+40)),x1=W*(small?.92:.97),HZ=small?178:H*.47,top=small?34:H*.13;
      sky.setAttribute('viewBox','0 0 '+W+' '+H);
      var pt=function(min){var e=elev(new Date(base+min*6e4));return [x0+(min-dd.rise)/(dd.set-dd.rise)*(x1-x0),HZ-Math.max(e,0)/90*(HZ-top)];};
      var nowMin=now.getUTCHours()*60+now.getUTCMinutes()+now.getUTCSeconds()/60, up=nowMin>dd.rise&&nowMin<dd.set;
      var pts=[],full='';
      for(var i=0;i<=90;i++){var m=dd.rise+(dd.set-dd.rise)*i/90,p=pt(m);pts.push([m,p]);full+=(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1);}
      while(sky.firstChild) sky.removeChild(sky.firstChild);
      var defs=mk('defs',{});
      defs.innerHTML='<linearGradient id="sunGrad" x1="0" x2="1"><stop offset="0" stop-color="#f39a1c" stop-opacity=".25"/><stop offset="1" stop-color="#f7b552"/></linearGradient><radialGradient id="sunGlow"><stop offset="0" stop-color="#f7b552" stop-opacity=".8"/><stop offset=".4" stop-color="#f39a1c" stop-opacity=".25"/><stop offset="1" stop-color="#f39a1c" stop-opacity="0"/></radialGradient>';
      sky.appendChild(defs);
      sky.appendChild(mk('line',{x1:x0-30,x2:x1+30,y1:HZ,y2:HZ,'class':'horizon'}));
      sky.appendChild(mk('path',{d:full,'class':'arc'}));
      var done=mk('path',{'class':'arc-done'}), glow=mk('circle',{r:small?46:110,'class':'glow halo'}), sun=mk('circle',{r:small?9:12,'class':'sun'});
      sky.appendChild(done); if(up){sky.appendChild(glow);sky.appendChild(sun);}
      if(!small){
        var a=mk('text',{x:x0,y:HZ-12,'class':'tick'});a.textContent='Sunrise '+fmt(dd.rise);sky.appendChild(a);
        var b=mk('text',{x:x1,y:HZ-12,'class':'tick','text-anchor':'end'});b.textContent='Sunset '+fmt(dd.set);sky.appendChild(b);
      }
      var target=up?nowMin:(nowMin>=dd.set?dd.set:dd.rise);
      var render=function(u){var s='';for(var j=0;j<pts.length&&pts[j][0]<=u;j++)s+=(s?'L':'M')+pts[j][1][0].toFixed(1)+' '+pts[j][1][1].toFixed(1);
        var p=pt(u);s+=(s?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1);done.setAttribute('d',s);
        if(up){sun.setAttribute('cx',p[0]);sun.setAttribute('cy',p[1]);glow.setAttribute('cx',p[0]);glow.setAttribute('cy',p[1]);}};
      var wasFirst=first;
      if(first&&!reduce&&target>dd.rise){var t0=null;render(dd.rise+.01);setTimeout(function(){requestAnimationFrame(function tick(t){if(!t0)t0=t;var k=Math.min((t-t0)/2600,1),e=1-Math.pow(1-k,3);render(dd.rise+(target-dd.rise)*e);if(k<1)requestAnimationFrame(tick);});},700);}
      else render(Math.max(target,dd.rise+.01));
      first=false;
      var e=elev(now), deg=$('#sun-deg'), cap=$('#sun-cap');
      if(deg) deg.innerHTML=up?Math.round(e)+'<small>°</small>':'Night';
      if(cap) cap.textContent=up?'Sun elevation above the Centre':(nowMin>=dd.set?'The sun has set over Nsukka':'Before sunrise over Nsukka');
      $('#sun-rise').textContent=fmt(dd.rise); $('#sun-noon').textContent=fmt(dd.noon); $('#sun-set').textContent=fmt(dd.set);
      var pct=Math.max(0,Math.min(1,(nowMin-dd.rise)/(dd.set-dd.rise))), meter=$('#sun-meter');
      if(meter) setTimeout(function(){meter.style.width=(pct*100).toFixed(1)+'%';},wasFirst&&!reduce?1000:0);
      var dl=$('#sun-day'); if(dl){var mins=Math.round(dd.set-dd.rise);dl.textContent=Math.floor(mins/60)+' h '+(mins%60)+' min of daylight today. '+Math.round(pct*100)+'% has passed.';}
    };
    draw(); setInterval(draw,60000);
    var rt; addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(draw,200);});
  }

  /* ---------- Technology showcase (tabs with autoplay) ---------- */
  var sc=$('.showcase');
  if(sc){
    var tabs=$$('.tab',sc), panels=$$('.panel',sc), cur=0, timer=null, DUR=6500, visible=false;
    sc.style.setProperty('--dur',DUR+'ms');
    var schedule=function(){clearTimeout(timer);if(reduce||!visible||sc.classList.contains('paused'))return;timer=setTimeout(function(){show(cur+1);},DUR);};
    var show=function(i,focus){
      cur=(i+tabs.length)%tabs.length;
      tabs.forEach(function(t,j){var on=j===cur;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;var b=t.querySelector('.bar');if(b){b.style.animation='none';void b.offsetWidth;b.style.animation='';}});
      panels.forEach(function(p,j){p.hidden=j!==cur;p.classList.remove('show');if(j===cur){void p.offsetWidth;p.classList.add('show');}});
      if(focus) tabs[cur].focus();
      if(innerWidth<960&&visible){var tl=tabs[cur].parentNode;tl.scrollTo({left:tabs[cur].offsetLeft-24,behavior:reduce?'auto':'smooth'});}
      schedule();
    };
    tabs.forEach(function(t,i){
      t.addEventListener('click',function(){sc.classList.add('paused');show(i);});
      t.addEventListener('keydown',function(e){var k=e.key;if(k==='ArrowDown'||k==='ArrowRight'){e.preventDefault();sc.classList.add('paused');show(cur+1,true);}if(k==='ArrowUp'||k==='ArrowLeft'){e.preventDefault();sc.classList.add('paused');show(cur-1,true);}});
    });
    sc.addEventListener('mouseenter',function(){sc.classList.add('paused');clearTimeout(timer);});
    sc.addEventListener('mouseleave',function(){sc.classList.remove('paused');schedule();});
    if(reduce) sc.classList.add('paused');
    if('IntersectionObserver' in window){new IntersectionObserver(function(es){visible=es[0].isIntersecting;if(visible)schedule();else clearTimeout(timer);},{threshold:.3}).observe(sc);}
    show(0);
  }

  /* ---------- Horizontal timeline ---------- */
  var track=$('.hs-track'), prev=$('.hs-prev'), next=$('.hs-next'), hbar=$('.hs-bar i');
  function hsUpdate(){
    if(!track) return;
    var max=track.scrollWidth-track.clientWidth, p=max>0?track.scrollLeft/max:1, vis=Math.min(1,track.clientWidth/track.scrollWidth);
    if(hbar) hbar.style.transform='translateX('+(p*(1-vis)*100)+'%) scaleX('+vis+')';
    if(prev) prev.disabled=track.scrollLeft<4; if(next) next.disabled=track.scrollLeft>max-4;
  }
  if(track){
    var stepBy=function(dir){var c=track.querySelector('.moment');track.scrollBy({left:dir*(c.offsetWidth+16),behavior:reduce?'auto':'smooth'});};
    if(prev) prev.addEventListener('click',function(){stepBy(-1);});
    if(next) next.addEventListener('click',function(){stepBy(1);});
    track.addEventListener('scroll',hsUpdate,{passive:true}); addEventListener('resize',hsUpdate);
    var down=false,sx=0,sl=0;
    track.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;down=true;sx=e.clientX;sl=track.scrollLeft;track.classList.add('drag');});
    addEventListener('pointermove',function(e){if(down)track.scrollLeft=sl-(e.clientX-sx);});
    addEventListener('pointerup',function(){if(down){down=false;track.classList.remove('drag');}});
    hsUpdate();
  }

  /* ---------- Projects: status, area, search ---------- */
  var grid=$('#proj-grid');
  if(grid){
    var cards=$$('.proj',grid), st='all', area='all', q='', cnt=$('#proj-count'), empty=$('#proj-empty');
    var seg=$('.seg'), pill=seg.querySelector('.pill');
    var movePill=function(){var b=seg.querySelector('[aria-pressed="true"]');pill.style.width=b.offsetWidth+'px';pill.style.transform='translateX('+b.offsetLeft+'px)';};
    var apply=function(){
      var n=0;
      cards.forEach(function(c){
        var ok=(st==='all'||c.dataset.status===st)&&(area==='all'||c.dataset.area===area)&&(!q||c.textContent.toLowerCase().indexOf(q)>-1);
        var was=!c.hidden; c.hidden=!ok;
        if(ok){n++; if(!was&&!reduce){c.classList.remove('enter');void c.offsetWidth;c.style.animationDelay=Math.min(n,12)*30+'ms';c.classList.add('enter');}}
      });
      cnt.textContent='Showing '+n+' of '+cards.length+' projects'; empty.hidden=n>0;
    };
    $$('button',seg).forEach(function(b){b.addEventListener('click',function(){$$('button',seg).forEach(function(x){x.setAttribute('aria-pressed','false');});b.setAttribute('aria-pressed','true');st=b.dataset.filter;movePill();apply();});});
    $$('.area-card').forEach(function(b){b.addEventListener('click',function(){var on=b.getAttribute('aria-pressed')==='true';$$('.area-card').forEach(function(x){x.setAttribute('aria-pressed','false');});if(!on){b.setAttribute('aria-pressed','true');area=b.dataset.area;}else area='all';apply();});});
    $('#proj-q').addEventListener('input',function(e){q=e.target.value.trim().toLowerCase();apply();});
    var rs=$('#proj-reset'); if(rs) rs.addEventListener('click',function(){q='';$('#proj-q').value='';area='all';$$('.area-card').forEach(function(x){x.setAttribute('aria-pressed','false');});$$('button',seg)[0].click();});
    addEventListener('resize',movePill); if(d.fonts&&d.fonts.ready) d.fonts.ready.then(movePill); movePill(); apply();
  }

  /* ---------- News filter ---------- */
  var ng=$('#news-grid');
  if(ng){
    var posts=$$('.post',ng);
    $$('.chip').forEach(function(c){c.addEventListener('click',function(){
      $$('.chip').forEach(function(x){x.setAttribute('aria-pressed','false');}); c.setAttribute('aria-pressed','true');
      var f=c.dataset.filter, k=0;
      posts.forEach(function(p){var ok=f==='all'||p.dataset.type===f;p.hidden=!ok;if(ok&&!reduce){p.classList.remove('enter');void p.offsetWidth;p.style.animationDelay=(k++*60)+'ms';p.classList.add('enter');}});
    });});
  }

  /* ---------- Contact form ---------- */
  var form=$('#enquiry');
  if(form){
    form.addEventListener('submit',function(e){
      e.preventDefault(); var ok=true;
      $$('[required]',form).forEach(function(inp){
        var f=inp.closest('.field'), bad=!inp.value.trim()||(inp.type==='email'&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value));
        f.classList.toggle('invalid',bad); if(bad&&ok){inp.focus();ok=false;}
      });
      if(!ok) return;
      var v=function(id){return $('#'+id).value.trim();};
      var subject='['+v('f-topic')+'] '+v('f-subject');
      var body=v('f-msg')+'\n\n'+v('f-name')+'\n'+v('f-email')+(v('f-org')?'\n'+v('f-org'):'')+(v('f-phone')?'\n'+v('f-phone'):'');
      location.href='mailto:ncerdunn@yahoo.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
      $('#form-ok').classList.add('show');
    });
    $$('input,textarea',form).forEach(function(i){i.addEventListener('input',function(){i.closest('.field').classList.remove('invalid');});});
  }

  onScroll();
})();
