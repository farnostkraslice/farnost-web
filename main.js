(function(){
  // ---------- hlavička ----------
  const header=document.querySelector('header');
  const onScrollHeader=()=>header.classList.toggle('scrolled',scrollY>30);

  // mobilní menu
  const menu=document.getElementById('menu'),burger=document.querySelector('.burger');
  burger.addEventListener('click',()=>{const o=menu.classList.toggle('open');burger.setAttribute('aria-expanded',o)});
  menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>menu.classList.remove('open')));

  // aktivní stránka v menu
  const page=document.body.dataset.page;
  menu.querySelectorAll('a[data-page]').forEach(a=>{if(a.dataset.page===page)a.classList.add('active')});

  // ---------- objevování při scrollu ----------
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
  // pojistka: co je vidět hned na první obrazovce (nebo když prohlížeč observer nespustí), se ukáže vždy
  const showVisible=()=>document.querySelectorAll('.reveal:not(.in)').forEach(el=>{const r=el.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0){el.classList.add('in');io.unobserve(el)}});
  requestAnimationFrame(showVisible);setTimeout(showVisible,600);addEventListener('load',showVisible);
  addEventListener('scroll',()=>{clearTimeout(showVisible.t);showVisible.t=setTimeout(showVisible,200)},{passive:true});

  // ---------- kostelík v úvodu: nakreslí se linkou, pak se vybarví; kliknutím se rozsvítí okna ----------
  const hc=document.querySelector('.hero-church');
  if(hc){
    hc.querySelectorAll('.hc-line').forEach(p=>p.style.setProperty('--len',Math.ceil(p.getTotalLength()+2)));
    requestAnimationFrame(()=>requestAnimationFrame(()=>hc.classList.add('in')));
    const b=document.getElementById('light');
    if(b)b.addEventListener('click',()=>{const lit=hc.classList.toggle('lit');document.body.classList.toggle('lit',lit);b.setAttribute('aria-pressed',lit);b.textContent=lit?'Zhasnout':'Rozsvítit kostel'});
  }

  // ---------- kutálející se tvary, které se dole složí do kostelíka z loga ----------
  // Díly jsou během stránky skryté. V poslední sekci (data-line="end") se jeden po druhém
  // přikutálí z okrajů (střídavě zleva a zprava) a složí se do kostelíka.
  // ?kostel=hotovo ukáže rovnou složený kostelík (pro kontrolu).
  const layer=document.getElementById('shapes');
  const DONE=/kostel=hotovo|line=full/.test(location.search)||matchMedia('(prefers-reduced-motion: reduce)').matches;
  // b = výřez dílu v souřadnicích loga, d = tvar, side = odkud se přikutálí, o = pořadí skládání
  const PARTS=[
    {b:[92,548,492,1101],d:'M92,1101V817L287,676V630H249V606H287V548H312V606H349V630H312V670L492,817V1101Z M241,879a59,59 0 1,0 118,0a59,59 0 1,0 -118,0Z',side:'L',f:.36,o:0},
    {b:[523,733,623,1101],d:'M523,817L623,733V1101H523Z',side:'R',f:.66,o:1},
    {b:[937,733,1038,1101],d:'M937,733L1038,817V1101H937Z',side:'L',f:.8,o:2},
    {b:[648,45,912,1101],d:'M648,1101V466L767,179V127H730V103H767V45H792V103H829V127H792V179L912,466V1101Z M717,587V524.5a14.5,14.5 0 0 1 29,0V587ZM766,587V524.5a14.5,14.5 0 0 1 29,0V587ZM815,587V524.5a14.5,14.5 0 0 1 29,0V587ZM741,679V617.5a14.5,14.5 0 0 1 29,0V679ZM790,679V617.5a14.5,14.5 0 0 1 29,0V679ZM746,729a34,34 0 1,0 68,0a34,34 0 1,0 -68,0Z',side:'R',f:.3,o:3},
    {b:[344,670,623,798],d:'M344,670H623V701L504,798Z',side:'L',f:.6,o:4},
  ];
  let G=null; // geometrie přepočítaná při změně velikosti
  if(layer){
    PARTS.forEach(p=>{
      const [x1,y1,x2,y2]=p.b;
      p.el=document.createElement('div');p.el.className='shape';
      p.el.innerHTML=`<svg viewBox="${x1} ${y1} ${x2-x1} ${y2-y1}"><path fill-rule="evenodd" d="${p.d}"/></svg>`;
      layer.appendChild(p.el);
    });
  }
  // ---------- modrý farář z geometrických tvarů, který po složení vběhne do kostela ----------
  const REDUCED=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let priest=null,door=null,priestPlayed=false,anims=[];
  if(layer){
    door=document.createElement('div');door.className='church-door';layer.appendChild(door);
    priest=document.createElement('div');priest.className='farar zprava';
    priest.innerHTML=`<svg viewBox="0 0 40 60" aria-hidden="true"><g class="pr-bob">
      <rect class="pr-leg pr-l" x="13.5" y="44" width="5.5" height="15" rx="2.5"/>
      <rect class="pr-leg pr-r" x="21" y="44" width="5.5" height="15" rx="2.5"/>
      <rect class="pr-arm pr-arm-b" x="11" y="21" width="5" height="17" rx="2.5"/>
      <polygon class="pr-body" points="13,19 27,19 32,48 8,48"/>
      <rect class="pr-collar" x="17" y="19" width="6" height="4" rx="1"/>
      <rect class="pr-arm" x="24" y="21" width="5" height="17" rx="2.5"/>
      <circle class="pr-head" cx="20" cy="10.5" r="8"/>
      <rect class="pr-cross" x="19" y="27" width="2" height="9"/><rect class="pr-cross" x="16.5" y="29.5" width="7" height="2"/>
    </g></svg>`;
    layer.appendChild(priest);
  }
  function resetPriest(){
    anims.forEach(a=>a.cancel());anims=[];priestPlayed=false;
    if(!priest||!G)return;
    priest.classList.remove('running');priest.style.opacity=0;door.style.opacity=0;
    priest.style.width=G.pw+'px';priest.style.height=G.ph+'px';
    door.style.width=G.door.w+'px';door.style.height=G.door.h+'px';
    door.style.transform=`translate(${G.door.x-G.door.w/2}px,${G.door.y-G.door.h}px)`;
  }
  function playPriest(){
    if(!priest||!G||REDUCED)return;
    priestPlayed=true;
    // pomalejší běh: ~2,5–4 s k dveřím, pak ještě chvíli vchází dovnitř
    const y=G.door.y-G.ph, x0=G.px0-G.pw/2, x1=G.door.x-G.pw/2, run=Math.max(2600,Math.abs(x1-x0)*11), enter=1100, total=run+enter;
    const T=(x,k)=>`translate(${x}px,${y}px) scale(${k})`;
    priest.style.opacity=1;priest.classList.add('running');
    anims.push(door.animate([{opacity:0},{opacity:1,offset:.2},{opacity:1,offset:.85},{opacity:0}],{duration:total+1600,delay:300,fill:'forwards'}));
    const a=priest.animate([
      {transform:T(x0,1),opacity:0},
      {transform:T(x0+(x1-x0)*.05,1),opacity:1,offset:.06},
      {transform:T(x1,1),opacity:1,offset:run/total},
      {transform:T(x1,.92),opacity:.9,offset:(run+enter*.4)/total},
      {transform:T(x1,.72),opacity:0}
    ],{duration:total,delay:600,easing:'ease-in-out',fill:'forwards'});
    a.onfinish=()=>priest.classList.remove('running');
    anims.push(a);
  }
  const ease=t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;
  const clamp=v=>Math.max(0,Math.min(1,v));
  function buildShapes(){
    if(!layer)return;
    const spot=document.querySelector('.church-spot');
    if(!spot){layer.style.display='none';G=null;return}
    layer.style.height='0px';
    const W=document.documentElement.clientWidth, H=document.documentElement.scrollHeight;
    layer.style.height=H+'px';
    const mobile=W<860;
    let top=0,n=spot;while(n){top+=n.offsetTop;n=n.offsetParent}
    const sh=spot.offsetHeight, sc=Math.min((sh-40)/1056,(W-40)/946);   // kostelík se vždy vejde do vyhrazeného místa
    const cx=W/2, base=top+sh-20;
    const gutter=mobile?14:Math.max(70,(W-1180)/2*0.6);
    const rs=mobile?.5:.62;                                // díly jsou při kutálení menší
    PARTS.forEach(p=>{
      const [x1,y1,x2,y2]=p.b, w=(x2-x1)*sc, h=(y2-y1)*sc;
      p.w=w;p.h=h;p.el.style.width=w+'px';p.el.style.height=h+'px';
      p.tx=cx+((x1+x2)/2-565)*sc; p.ty=base+((y1+y2)/2-1101)*sc;
      p.r=Math.max(w,h)*rs/2;                              // „poloměr“ pro výpočet otáčení
      p.ex=p.side==='L'?gutter:W-gutter;
    });
    const maxS=H-innerHeight;
    // složeno, když je spodek kostelíka v ~80 % výšky okna (nebo na konci stránky, pokud tam nejde dojet)
    const S1=Math.max(0,Math.min(maxS-6,base-innerHeight*0.8)), S0=Math.max(0,S1-innerHeight*0.7);
    G={W,H,mobile,rs,S0,S1,startY:document.querySelector('[data-line]').offsetHeight*0.35};
    // dveře ve věži kostelíka (pod kulatým okénkem) a farář, který k nim přiběhne
    G.door={x:cx+(780-565)*sc,y:base,w:74*sc,h:128*sc};          // dveře ve věži
    G.ph=Math.max(36,G.door.h*1.3);G.pw=G.ph*40/60;
    G.px0=Math.min(W-G.pw,cx+(1038-565)*sc+(mobile?110:260));  // farář přibíhá zprava
    resetPriest();
    drawShapes();
  }
  function drawShapes(){
    if(!G)return;
    // díly jsou skryté; až v poslední sekci se přikutálí z okrajů a složí do kostelíka
    const s=scrollY, span=G.S1-G.S0, step=span*0.1, dur=Math.max(1,span-step*4);
    let all=true;
    PARTS.forEach(p=>{
      let t=DONE?1:(span>0?clamp((s-G.S0-p.o*step)/dur):(s>=G.S1?1:0));
      const e=ease(t), dir=p.side==='L'?1:-1;
      const sx=p.ex, dist=Math.abs(p.tx-sx);
      const x=sx+(p.tx-sx)*e;
      const y=p.ty-Math.sin(Math.PI*e)*(G.mobile?30:60);          // malý oblouk při doskoku
      const rot=-dir*(1-e)*(dist/p.r)*57.2958;                    // kutálení, na místě skončí rovně
      const k=G.rs+(1-G.rs)*e;
      if(t<1)all=false;
      p.el.style.transform=`translate(${(x-p.w/2).toFixed(1)}px,${(y-p.h/2).toFixed(1)}px) rotate(${rot.toFixed(1)}deg) scale(${k.toFixed(3)})`;
      p.el.style.opacity=clamp(t*5);
    });
    layer.classList.toggle('done',all);
    if(all&&!priestPlayed)playPriest();
    else if(!all&&priestPlayed&&!DONE)resetPriest();
  }
  let raf=0,rt;
  addEventListener('scroll',()=>{onScrollHeader();if(!raf)raf=requestAnimationFrame(()=>{raf=0;drawShapes()})},{passive:true});
  const relayout=()=>{clearTimeout(rt);rt=setTimeout(buildShapes,150)};
  addEventListener('resize',relayout);
  addEventListener('load',buildShapes);
  if(document.fonts)document.fonts.ready.then(buildShapes);
  document.querySelectorAll('img').forEach(i=>i.addEventListener('load',relayout));
  buildShapes();onScrollHeader();

  // ---------- akce (content/akce.json) – proběhlé se skryjí samy ----------
  const esc=t=>String(t??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const lists=document.querySelectorAll('[data-akce]');
  if(lists.length){
    fetch('content/akce.json',{cache:'no-cache'}).then(r=>r.ok?r.json():Promise.reject(r.status)).then(data=>{
      const today=new Date();today.setHours(0,0,0,0);
      const items=(data.akce||[]).filter(a=>a.nazev&&a.datum&&new Date(a.datum+'T00:00')>=today).sort((a,b)=>a.datum.localeCompare(b.datum));
      const card=a=>{
        const d=new Date(a.datum+'T00:00');
        const mon=d.toLocaleDateString('cs-CZ',{month:'short'}).replace('.','');
        const wd=d.toLocaleDateString('cs-CZ',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
        const popis=(a.popis||'').split(/\n\s*\n/).map(p=>`<p>${esc(p).replace(/\n/g,'<br>')}</p>`).join('');
        const img=a.plakat?String(a.plakat).replace(/^(?!\/|https?:)/,'/'):'';
        return `<article class="akce reveal in${img?' has-plakat':''}">
          ${img?`<a class="akce-plakat" href="${esc(img)}" target="_blank" rel="noopener" aria-label="Plakát: ${esc(a.nazev)} (otevřít ve velkém)"><img src="${esc(img)}" alt="Plakát – ${esc(a.nazev)}" loading="lazy"></a>`:''}
          <div class="akce-date"><strong>${d.getDate()}</strong><span>${esc(mon)}</span></div>
          <p class="when">${esc(wd)}${a.cas?' · '+esc(a.cas):''}</p>
          <h3>${esc(a.nazev)}</h3>
          ${a.misto?`<p class="where">${esc(a.misto)}</p>`:''}
          ${a.perex?`<div class="desc"><p>${esc(a.perex)}</p></div>`:''}
          ${popis?`<details><summary>Více informací</summary><div class="desc">${popis}</div></details>`:''}
        </article>`};
      lists.forEach(list=>{
        list.innerHTML=items.length?items.map(card).join(''):'<p class="empty">Momentálně nemáme vypsané žádné akce. Sledujte nás na Facebooku a Instagramu.</p>';
        list.querySelectorAll('details').forEach(x=>x.addEventListener('toggle',relayout));
      });
      relayout();
    }).catch(()=>{lists.forEach(l=>l.innerHTML='<p class="empty">Akce se nepodařilo načíst. Zkuste stránku obnovit.</p>')});
  }

  // ---------- pořad měsíce (content/porad.json, mění administrace) ----------
  const porad=document.querySelector('[data-porad]');
  if(porad){
    fetch('content/porad.json',{cache:'no-cache'}).then(r=>r.ok?r.json():Promise.reject()).then(d=>{
      if(d.soubor)porad.href=d.soubor;
      if(d.nazev)porad.querySelector('[data-porad-nazev]').textContent=d.nazev;
    }).catch(()=>{});
  }

  // ---------- dar: QR platba (formát SPD, české banky) ----------
  const qrBox=document.getElementById('qr');
  if(qrBox&&window.qrcode){
    const IBAN='CZ7908000000000860622379';
    const btns=[...document.querySelectorAll('.amounts button')],own=document.getElementById('own');
    let amount=500;
    const render=()=>{
      const am=amount>0?`AM:${amount.toFixed(2)}*`:'';
      const spd=`SPD*1.0*ACC:${IBAN}*${am}CC:CZK*MSG:DAR FARNOSTI KRASLICE*`;
      const q=qrcode(0,'M');q.addData(spd);q.make();
      qrBox.innerHTML=q.createSvgTag({cellSize:4,margin:0,scalable:true});
      const lab=document.getElementById('qr-amount');
      if(lab)lab.textContent=amount>0?amount.toLocaleString('cs-CZ')+' Kč':'částku zadáte v bance';
    };
    btns.forEach(b=>b.addEventListener('click',()=>{
      btns.forEach(x=>x.setAttribute('aria-pressed',x===b));own.value='';
      amount=+b.dataset.am;render();
    }));
    own.addEventListener('input',()=>{
      btns.forEach(x=>x.setAttribute('aria-pressed',false));
      amount=Math.max(0,Math.round(+own.value.replace(/\s/g,'').replace(',','.')||0));render();
    });
    render();
  }
  // ---------- platba tábora: QR kód s pevnou částkou a jménem dítěte ve zprávě ----------
  const qrT=document.getElementById('qr-tabor');
  if(qrT&&window.qrcode){
    const IBAN='CZ7908000000000860622379', am=+qrT.dataset.amount||0, jm=document.getElementById('tabor-jmeno');
    const clean=t=>t.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[*]/g,' ').toUpperCase().trim().slice(0,40);
    const nar=document.getElementById('tabor-narozeni'), vsLab=document.getElementById('tabor-vs');
    // variabilní symbol = datum narození DDMMRRRR (přijme i „15. 3. 2015“ nebo „15032015“)
    const toVS=t=>{
      const m=t.match(/^\s*(\d{1,2})\s*[.\/ -]\s*(\d{1,2})\s*[.\/ -]\s*(\d{4})\s*$/);
      if(m)return m[1].padStart(2,'0')+m[2].padStart(2,'0')+m[3];
      const d=t.replace(/\D/g,'');return d.length===8?d:'';
    };
    const renderT=()=>{
      const msg=('TABOR 2027 '+clean(jm.value)).trim(), vs=toVS(nar.value);
      vsLab.textContent=vs?'VS: '+vs:'VS: datum narození';
      const q=qrcode(0,'M');q.addData(`SPD*1.0*ACC:${IBAN}*AM:${am.toFixed(2)}*CC:CZK*${qrT.dataset.due?'DT:'+qrT.dataset.due+'*':''}${vs?'X-VS:'+vs+'*':''}MSG:${msg}*`);q.make();
      qrT.innerHTML=q.createSvgTag({cellSize:4,margin:0,scalable:true});
    };
    jm.addEventListener('input',renderT);nar.addEventListener('input',renderT);renderT();
  }
  document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>{
    const t=b.dataset.copy,old=b.textContent;
    (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>{b.textContent='Zkopírováno ✓';setTimeout(()=>b.textContent=old,1800)}).catch(()=>{});
  }));

  // ---------- online přihláška na tábor (Netlify Forms → e-mail pořadatelům) ----------
  document.querySelectorAll('form[data-netlify]').forEach(form=>{
    const ok=form.querySelector('.form-ok'),err=form.querySelector('.form-err'),inv=form.querySelector('.form-invalid'),btn=form.querySelector('button[type=submit]');
    form.addEventListener('submit',e=>{
      e.preventDefault();
      [ok,err,inv].forEach(x=>x&&(x.hidden=true));
      form.classList.add('tried');
      if(!form.checkValidity()){inv.hidden=false;const f=form.querySelector(':invalid');if(f){f.focus({preventScroll:true});f.scrollIntoView({block:'center',behavior:'smooth'})}return}
      btn.disabled=true;
      fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(form)).toString()})
        .then(r=>{if(!r.ok)throw r.status;ok.hidden=false;form.reset();form.classList.remove('tried')})
        .catch(()=>{err.hidden=false})
        .finally(()=>{btn.disabled=false;relayout()});
    });
  });

  // ---------- mapa: Google Mapy se načtou až po kliknutí ----------
  document.querySelectorAll('.map-load').forEach(b=>b.addEventListener('click',()=>{
    const f=document.createElement('iframe');
    f.src=b.dataset.src;f.title='Mapa – farnost Kraslice';f.loading='lazy';f.referrerPolicy='no-referrer-when-downgrade';
    b.replaceWith(f);
  }));
})();
