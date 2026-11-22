#!/usr/bin/env python3
"""Sestaví HTML stránky webu farnosti Kraslice (společná hlavička, patička, logo).
Texty stránek měň tady a pak spusť:  python3 tools/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------- aktuální „Pořad měsíce“ (farní ohlášky) ----------
# Mění se v administraci (/admin → Pořad měsíce), data jsou v content/porad.json.
# Web si je načítá za běhu, tady jsou jen jako výchozí hodnota v HTML.
import json as _json
_porad = _json.loads((ROOT / "content/porad.json").read_text(encoding="utf-8"))
PORAD_PDF = _porad["soubor"]
PORAD_NAZEV = _porad["nazev"]

FB = "https://www.facebook.com/profile.php?id=61595670185263"
IG = "https://www.instagram.com/farnostkraslice"
MAP = "https://www.google.com/maps?q=Kpt.+Jaro%C5%A1e+321%2F2,+358+01+Kraslice&output=embed"

# ---------- kostelík z loga (souřadnice podle originálu) ----------
CHURCH_D = (
    "M92,1101V817L287,676V630H249V606H287V548H312V606H349V630H312V670L492,817V1101Z"
    "M344,670H623V701L504,798Z"
    "M523,817L623,733V1101H523Z"
    "M648,1101V466L767,179V127H730V103H767V45H792V103H829V127H792V179L912,466V1101Z"
    "M937,733L1038,817V1101H937Z"
)
WINDOWS_D = (
    "M241,879a59,59 0 1,0 118,0a59,59 0 1,0 -118,0Z"
    "M717,587V524.5a14.5,14.5 0 0 1 29,0V587ZM766,587V524.5a14.5,14.5 0 0 1 29,0V587ZM815,587V524.5a14.5,14.5 0 0 1 29,0V587ZM741,679V617.5a14.5,14.5 0 0 1 29,0V679ZM790,679V617.5a14.5,14.5 0 0 1 29,0V679ZM746,729a34,34 0 1,0 68,0a34,34 0 1,0 -68,0Z"
)
VB = "86 40 958 1066"
LOGO = "#F8E9A4"   # barva kostelíka z loga

def church_small():
    # okna jsou průhledná (vyříznutá), ne bílá
    return f'<svg viewBox="{VB}" aria-hidden="true"><path fill="{LOGO}" fill-rule="evenodd" d="{CHURCH_D}{WINDOWS_D}"/></svg>'

ICON_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3z"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21.9 8c-.1-1.6-.4-3-1.6-4.2S17.6 2.2 16 2.1C14.3 2 9.7 2 8 2.1c-1.6.1-3 .4-4.2 1.6S2.2 6.4 2.1 8C2 9.7 2 14.3 2.1 16c.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.7.1 6.3.1 8 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.7.1-6.3.2-8zm-2.2 9.8a3.3 3.3 0 0 1-1.8 1.8c-1.3.5-4.3.4-5.8.4s-4.5.1-5.8-.4a3.3 3.3 0 0 1-1.8-1.8c-.5-1.3-.4-4.3-.4-5.8s-.1-4.5.4-5.8a3.3 3.3 0 0 1 1.8-1.8C7.5 4 10.5 4.1 12 4.1s4.5-.1 5.8.4a3.3 3.3 0 0 1 1.8 1.8c.5 1.3.4 4.3.4 5.8s.1 4.5-.3 5.7z"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
DOWN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v13M6 12l6 6 6-6M5 21h14"/></svg>'
SOC = f'<div class="soc"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ICON_FB}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a></div>'

# Menu ve stejném pořadí jako na původním webu
NAV = [("historie", "historie.html", "Historie"), ("kontakty", "kontakty.html", "Kontakty"),
       ("tabor", "detsky-tabor.html", "Dětský tábor"), ("aktuality", "aktuality.html", "Aktuality"),
       ("porad", "porad-mesice.html", "Pořad měsíce")]

def header():
    items = "".join(f'<li><a href="{h}" data-page="{k}">{t}</a></li>' for k, h, t in NAV)
    return f'''<a class="skip" href="#obsah">Přeskočit na obsah</a>
<header><div class="wrap nav">
  <a class="brand brand-mark" href="index.html" aria-label="Římskokatolická farnost Kraslice – úvod">{church_small()}</a>
  <nav aria-label="Hlavní menu"><ul id="menu">{items}<li>{SOC}</li></ul></nav>
  <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24"><path d="M4 8h16M4 16h16"/></svg></button>
</div></header>'''

def footer():
    return f'''<footer><div class="wrap">
  <div class="foot">
    <div>
      <a class="brand" href="index.html">{church_small()}<span><b>Římskokatolická</b><small>farnost Kraslice</small></span></a>
      <p class="foot-verse">„Já jsem světlo světa.“ <br><small style="font-family:var(--sans);font-style:normal;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#9AA6BC">Jan 8,12</small></p>
      {SOC}
    </div>
    <div><h4>Adresa</h4><p>Kpt. Jaroše 321/2<br>358 01 Kraslice</p></div>
    <div><h4>Farní kostel</h4><p>Nejsvětějšího Těla Kristova (Božího Těla)<br>Hradební 1821, 358 01 Kraslice</p></div>
    <div><h4>Údaje</h4><p>IČ: 45374872<br>Č. ú.: 860622379/0800</p><p style="margin-top:10px"><a href="kontakty.html">Kontakty →</a></p></div>
  </div>
  <div class="foot-bottom"><span>© Římskokatolická farnost Kraslice</span><span>Biskupství plzeňské</span></div>
</div></footer>'''

def page(slug, key, title, desc, body, line=True):
    line_svg = ('<div id="shapes" aria-hidden="true"></div>' if line else '')
    qr = '<script src="assets/js/qrcode.min.js"></script>' if 'id="qr' in body else ''
    html = f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#E3EFFA">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/Adorage.otf" as="font" type="font/otf" crossorigin>
<link rel="stylesheet" href="style.css">
</head>
<body data-page="{key}">
{line_svg}
{header()}
<main id="obsah">
{body}
</main>
{footer()}
{qr}<script src="main.js"></script>
</body>
</html>
'''
    (ROOT / slug).write_text(html, encoding="utf-8")
    print("✓", slug)

def end_contact(title="Máte otázku? Ozvěte se nám.", text="S důvěrou se na nás obraťte – osobně, telefonicky nebo e-mailem."):
    return f'''<section data-line="end" class="bg-cream"><div class="wrap end-box reveal">
  <span class="eyebrow">Kontakt</span>
  <h2>{title}</h2>
  <p class="lead">{text}</p>
  <div class="btns"><a class="btn" href="kontakty.html">Kontakty {ARROW}</a><a class="btn ghost" href="tel:+420720512641">+420 720 512 641</a></div>
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

# =====================================================================
# ÚVOD – maximálně jednoduchý, jako na původním webu
# =====================================================================
index_body = f'''<section class="hero home" data-line="hero">
  <div class="wrap home-inner">
    <h1 class="wordmark reveal d1"><span>Římskokatolická</span><small>farnost Kraslice</small></h1>
    <blockquote class="reveal d2">
      <p class="verse">„Já jsem světlo světa; kdo mě následuje, nebude chodit ve tmě, ale bude mít <em>světlo života.</em>“</p>
      <p class="verse-ref">— Ježíš, Jan 8,12</p>
    </blockquote>
    <div class="btns reveal d3"><a class="btn" href="o-nas.html">O nás {ARROW}</a></div>
  </div>
</section>'''

# Dětský tábor – cena (Kč)
TABOR_CENA = 5000
TABOR_CENA_TXT = f"{TABOR_CENA:,}".replace(",", " ")

# QR kód pro dar – stejný box je na stránce O nás i Kontakty
GIVE_BOX = '''<div class="give-box reveal d1">
    <h3>Dar přes QR kód</h3>
    <p class="muted" style="font-size:15px;margin:0 auto 18px">Vyberte částku a naskenujte kód v aplikaci své banky.</p>
    <div class="amounts" role="group" aria-label="Částka daru">
      <button type="button" data-am="200" aria-pressed="false">200 Kč</button>
      <button type="button" data-am="500" aria-pressed="true">500 Kč</button>
      <button type="button" data-am="1000" aria-pressed="false">1 000 Kč</button>
      <input id="own" inputmode="numeric" placeholder="jiná částka" aria-label="Jiná částka v Kč">
    </div>
    <div id="qr" aria-label="QR kód pro platbu"></div>
    <p class="acct">Číslo účtu farnosti · <span id="qr-amount">500 Kč</span><strong>860622379/0800</strong><button class="copy" type="button" data-copy="860622379/0800">Zkopírovat číslo účtu</button></p>
  </div>'''

# =====================================================================
# O NÁS
# =====================================================================
onas_body = f'''<section class="page-hero" data-line="hero"><div class="wrap">
  <span class="eyebrow">O nás</span>
  <h1>Život v naší farnosti</h1>
  <p class="lead">Jsme společenstvím křesťanů, kteří společně sdílejí víru v Boha, scházejí se k modlitbě a slavení eucharistie a snaží se vzájemně se podporovat v každodenním životě. Naše farní rodina zahrnuje nejen samotné město Kraslice, ale s láskou duchovně provázíme také věřící v okolních obcích – na Rotavě, Bublavě, v Šindelové a v dalších přilehlých místech našeho krásného, ale i zkoušeného pohraničního kraje.</p>
  <div class="btns"><a class="btn" href="aktuality.html">Aktuality {ARROW}</a></div>
</div></section>

<section data-line="right"><div class="wrap center reveal">
  <span class="eyebrow">Vítejte</span>
  <h2>Jsme společenstvím <em>otevřeným pro každého.</em></h2>
  <p class="lead">Rádi mezi sebou přivítáme ty, kteří víru a smysl života teprve hledají, stejně jako rodiny s dětmi, mládež i starší generaci. Všichni jste u nás upřímně vítáni.</p>
</div></section>

<section class="bg-mist" data-line="left"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Naše duchovní správa</span>
    <h2>S důvěrou se na nás obraťte</h2>
    <p>O naše duchovní potřeby a správu celého farního obvodu pečuje náš duchovní správce. S důvěrou a bez obav se na nás můžete obrátit v jakékoli životní situaci – ať už radostné, nebo v chvílích bolesti a hledání.</p>
    <div class="priest"><img src="assets/img/bystrik.jpg" alt="P. Bystrík Feranec" width="72" height="72"><div><small>Náš duchovní správce</small><b>P. Bystrík Feranec</b></div></div>
  </div>
  <div class="reveal d1">
    <h3>S čím vám rádi pomůžeme</h3>
    <ul class="services">
      <li><span><b>Svátosti:</b> příprava na křest (dětí i dospělých), svatbu v kostele, první svaté přijímání či biřmování.</span></li>
      <li><span><b>Duchovní opora:</b> svatá zpověď nebo osobní duchovní rozhovor.</span></li>
      <li><span><b>Návštěvy nemocných:</b> rádi navštívíme staré či nemocné farníky u nich doma s modlitbou a svátostmi.</span></li>
      <li><span><b>Těžké chvíle:</b> pomůžeme vám s křesťanským rozloučením a organizací pohřbu vašich blízkých.</span></li>
    </ul>
  </div>
</div></section>

<section data-line="right"><div class="wrap split">
  <div class="photo wide reveal"><img src="assets/img/onas-spolecne.jpg" alt="Interiér kostela" loading="lazy"></div>
  <div class="reveal d1">
    <span class="eyebrow">Společně tvoříme farnost</span>
    <h2>Farnost, to nejsme jen pan farář, ale <em>my všichni</em></h2>
    <p>Při správě a organizaci života ve farnosti pomáhají naši farníci sdružení v pastorační a ekonomické radě. Staráme se o praktické věci – od úklidu a květinové výzdoby našich kostelů přes službu lektorů a akolytů při liturgii až po organizaci farních setkání, koncertů a péči o farní budovy.</p>
    <p>Budeme upřímně vděční, pokud se budete chtít k našemu společnému úsilí jakýmkoli způsobem připojit – ať už modlitbou, nebo praktickou pomocí.</p>
  </div>
</div></section>

<section data-line="end"><div class="wrap give">
  <div class="reveal">
    <span class="eyebrow">Podpora našeho farního domova</span>
    <h2>Každý dar pomáhá</h2>
    <p>Chod farnosti, vytápění kostelů v zimních měsících a finančně velmi náročné opravy historických sakrálních památek v našem regionu můžeme zajišťovat výhradně díky vaší obětavosti a dobrovolným darům.</p>
    <p>Pokud máte možnost a chcete provoz farnosti a záchranu našeho duchovního dědictví podpořit, můžete tak učinit při nedělní sbírce, nebo zasláním finančního daru přímo na náš bankovní účet.</p>
    <p><b>Potvrzení o daru:</b> na požádání vám rádi vystavíme potvrzení o daru pro účely daňového přiznání.</p>
    <p class="muted" style="margin-top:22px;font-style:italic">Ze srdce vám děkujeme za každou vaši pomoc, štědrost a modlitbu. Kéž vám Pán Bůh vaši dobrotu oplatí.</p>
  </div>
  {GIVE_BOX}
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

# =====================================================================
# HISTORIE
# =====================================================================
CHURCHES = [
    ("rotava", "rotava.jpg", "Kostel sv. Petra a Pavla v Rotavě", "Vydupaný ze země dělnickou vytrvalostí", "1914–1925",
     "Zatímco jiné kostely stavěla bohatá šlechta, tento pseudorománský kostel (1914–1925) si postavili sami dělníci z místních železáren. Procházel nejtěžší zkouškou – stavěl se během první světové války, kdy byl kritický nedostatek materiálu i peněz. Přesto ho místní lidé s obrovskou láskou dokončili."),
    ("jindrichovice", "jindrichovice.jpg", "Kostel sv. Martina v Jindřichovicích", "Barokní oáza s příběhem záchrany", "gotika a baroko",
     "Tento půvabný kostel s výraznou žlutou siluetou v sobě spojuje gotické kořeny s barokní elegancí, kterou mu vtiskli hrabata z Nostitzu. Přestože ve druhé polovině 20. století málem podlehl zkáze, dnes opět hrdě svítí do okolí. Zastavte se u něj během toulek jindřichovickou krajinou a nasajte klid místa, které dokázalo přežít bouřlivé časy."),
    ("olovi", "olovi.jpg", "Kostel sv. Michaela archanděla v Oloví", "Novogotická dominanta nad údolím Svatavy", "počátek 20. století",
     "Tento majestátní novogotický chrám, postavený na samém počátku 20. století na místě staršího hornického kostelíka, shlíží na město z výšky jako tichý strážce. Přestože v minulých desetiletích utrpěl šrámy a na čas utichl, jeho štíhlá věž s nárožními opěráky stále tvoří nezaměnitelnou kulisu krajiny, kde se potkávají Krušné hory se Smrčinami. Ideální zastavení, až budete scházet z nedaleké rozhledny Cibulka a zatoužíte po kousku nostalgické historie."),
    ("bublava", "bublava.jpg", "Kostel sv. Jakuba Staršího na Bublavě", "Chrám, který stráží hřebeny hor", "1908",
     "Tento horský kostelík byl vysvěcen v roce 1908 a jeho architektura dokonale splývá s drsnou krušnohorskou přírodou. Pokud plánujete pěší túru nebo cyklovýlet po hřebenech, zastavte se u něj. Je to ideální místo pro ztišení a načerpání nové energie."),
    ("stribrna", "stribrna.jpg", "Kostel Nejsvětějšího Srdce Páně ve Stříbrné", "Moderní novogotická perla v srdci Silberbachu", "1910",
     "Tento působivý pseudogotický chrám z roku 1910, postavený kraslickým stavitelem Augustem Hochbergerem, se pyšní majestátní, 44 metrů vysokou věží. Svým elegantním stylem skvěle doplňuje atmosféru horského údolí a známého zimního střediska. Až se budete vracet z túry na nedaleký nejvyšší vrchol západních Krušných hor Špičák, zastavte se u něj a obdivujte stavbu, která vznikla z čisté lásky a odhodlání místních obyvatel."),
    ("sindelova", "sindelova.jpg", "Kostel sv. Jiljí v Šindelové", "Barokní perla, která odmítla zaniknout", "1755",
     "Nejstarší z našich venkovských kostelů (z roku 1755) dýchá čistým barokem. Po těžkých dekádách minulého století, kdy chátral, dnes zažívá své znovuzrození. Díky nadšení dobrovolníků a spolků má novou střechu a fasádu a znovu se stává centrem kultury a setkávání na venkově."),
]
rows = "".join(f'''<article class="church-row" id="{cid}">
    <div class="photo reveal"><img src="assets/img/{img}" alt="{name}" loading="lazy"></div>
    <div class="reveal d1"><span class="tag">{year}</span><h3>{name}</h3><q>{motto}</q><p>{text}</p></div>
  </article>''' for cid, img, name, motto, year, text in CHURCHES)

BULB = '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M24 44c0-6-8-10-8-20a16 16 0 0 1 32 0c0 10-8 14-8 20z"/><path d="M25 50h14M27 56h10"/><line x1="32" y1="2" x2="32" y2="-4"/><path d="M10 10l-4-4M54 10l4-4M4 26H-2M60 26h6"/></svg>'

historie_body = f'''<section class="page-hero" data-line="hero"><div class="wrap page-hero-grid">
  <div>
    <span class="eyebrow">Historie</span>
    <h1>Příběhy našich kostelů</h1>
    <p class="lead">Vítejte v kraji, kde strmé krušnohorské svahy ukrývají architektonické skvosty a strhující příběhy lidské víry, odhodlání i naděje. Naše kostely nejsou jen chladné zdi z kamene – jsou to místa plná dramatických osudů.</p>
    <p>Pojďte s námi sfouknout prach ze starých farních kronik a objevit historii, která vás překvapí!</p>
    <div class="btns"><a class="btn" href="aktuality.html">Aktuality {ARROW}</a><a class="btn ghost" href="kontakty.html">Adresa</a></div>
  </div>
  <div class="page-hero-img"><img src="assets/img/kraslice-kostel.jpg" alt="Děkanský kostel Nejsvětějšího Těla v Kraslicích"></div>
</div></section>

<section data-line="left"><div class="wrap split rev">
  <div class="reveal">
    <span class="eyebrow">Kraslice · 1893–1896</span>
    <h2>Děkanský kostel Nejsvětějšího Těla v Kraslicích</h2>
    <p class="lead"><em>Chrám, který povstal z hrozící katastrofy.</em></p>
    <p>Když dnes stojíte před kraslickým kostelem, vidíte majestátní, 63 metrů vysokou novorománskou baziliku, která působí, jako by tu stála odjakživa. Jenže na konci 19. století chybělo málo a Kraslice zůstaly úplně bez kostela.</p>
    <div class="facts">
      <div class="fact"><b>Kostel podepřený stromy</b><p>Původní starý kostel ze 17. století byl na konci 19. století v tak katastrofálním stavu, že se stal pro lidi nebezpečným. Když v roce 1885 odhalili obrovské trhliny ve stropě, úřady v něm okamžitě zakázaly bohoslužby. Aby se stavba nezřítila, musel být strop zevnitř podepřen mohutnými kmeny stromů.</p></div>
      <div class="fact"><b>Městská vzpoura proti slavnému architektovi</b><p>Slavný architekt pražské katedrály sv. Víta, Josef Mocker, tehdy navrhl, aby se starý kostel nezbořil, ale jen rozšířil. Vedení města to ale rázně odmítlo – Mockerův plán by totiž zablokoval a nebezpečně zúžil tehdejší hlavní silnici, která vedla šikmo kolem kostela.</p></div>
      <div class="fact"><b>Stavební rekord</b><p>Díky štědré podpoře patrona, hraběte Nostitze, a neústupnosti kraslických občanů se nakonec rozhodlo pro úplnou novostavbu. Současný kostel byl postaven v neuvěřitelném rekordu mezi lety 1893–1896.</p></div>
    </div>
  </div>
  <div class="photo tall reveal d1"><img src="assets/img/kraslice-kresba.jpg" alt="Kresba kostela v Kraslicích" loading="lazy"></div>
</div></section>

<section data-line="right" style="padding-top:0"><div class="wrap">
  <div class="know reveal">{BULB}<div><h3>Víte, že…?</h3><p>Uvnitř kostela se nachází opravdový král hudebních nástrojů. Jde o vzácné romantické varhany z roku 1895 z legendární krnovské dílny Rieger. Jejich mohutný zvuk dodnes provází nejen bohoslužby, ale i pravidelné koncerty, které lákají milovníky hudby z širokého okolí.</p></div></div>
</div></section>

<section class="bg-mist" data-line="left"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(20px,3vw,40px)">
    <span class="eyebrow">Horské klenoty</span>
    <h2>A zaniklá místa v okolí</h2>
    <p class="lead">Kraslická farnost historicky spravuje duchovní srdce celého okolního kraje. Každé z těchto míst vypráví svůj vlastní, hluboký příběh, který stojí za to prozkoumat během víkendového výletu.</p>
  </div>
  {rows}
</div></section>

<section data-line="right"><div class="wrap">
  <div class="know reveal">{BULB}<div><h3>Víte, že…?</h3><p>Naše farnost pamatuje i na místa, která musela ustoupit pohnutým dějinám 20. století. V Krásné Lípě (Schönlind) stával od roku 1813 zděný kostel sv. Josefa. Dnes nám tyto zaniklé osady a příběhy lidí, kteří odtud kdysi odcházeli za chlebem až do daleké Ameriky, připomínají už jen obnovené kříže a pietní místa skrytá v lesích.</p></div></div>
</div></section>

<section data-line="end"><div class="wrap split">
  <div class="photo wide reveal"><img src="assets/img/poutnici.jpg" alt="Kostel při západu slunce" loading="lazy"></div>
  <div class="reveal d1">
    <span class="eyebrow">Tip pro poutníky a turisty</span>
    <h2>Naše kostely pro veřejnost</h2>
    <p>Nejen během bohoslužeb, ale i při akcích, jako je „Noc kostelů“ nebo adventní koncerty. Chcete nahlédnout dovnitř mimo běžný čas? Ozvěte se nám.</p>
    <div class="btns"><a class="btn" href="kontakty.html">Kontaktujte nás {ARROW}</a></div>
  </div>
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

# =====================================================================
# KONTAKTY
# =====================================================================
kontakty_body = f'''<section class="page-hero" data-line="hero"><div class="wrap">
  <span class="eyebrow">Kontakty</span>
  <h1>Kontaktujte nás</h1>
  <p class="lead">Budeme rádi za každé vaše setkání s námi, ať už osobní, telefonické nebo e-mailové. S důvěrou se na nás obraťte.</p>
</div></section>

<section data-line="right" style="padding-top:clamp(20px,3vw,40px)"><div class="wrap contact-grid">
  <div class="cbox reveal">
    <div class="priest" style="margin:0;box-shadow:none;padding:0"><img src="assets/img/bystrik.jpg" alt="P. Bystrík Feranec" width="72" height="72"><div><small>Duchovní správce</small><b>P. Bystrík Feranec</b></div></div>
    <dl>
      <dt>E-mail</dt><dd><a href="mailto:feranec@bip.cz">feranec@bip.cz</a><br><a href="mailto:farnost.kraslice@bip.cz">farnost.kraslice@bip.cz</a></dd>
      <dt>Telefon</dt><dd><a href="tel:+420720512641">+420 720 512 641</a></dd>
      <dt>Úřední hodiny</dt><dd>pondělí – pátek, 8:30 – 16:00</dd>
      <dt>Adresa</dt><dd>Kpt. Jaroše 321/2, 358 01 Kraslice</dd>
      <dt>Farní kostel</dt><dd>Nejsvětějšího Těla Kristova (Božího Těla)<br>Hradební 1821, 358 01 Kraslice</dd>
      <dt>IČ · účet</dt><dd>45374872 · 860622379/0800</dd>
    </dl>
  </div>
  <div class="cbox reveal d1">
    <h3>Biskupství plzeňské</h3>
    <dl>
      <dt>E-mail</dt><dd><a href="mailto:bip@bip.cz">bip@bip.cz</a></dd>
      <dt>Statutární zástupci</dt><dd>Mons. Tomáš Holub, biskup plzeňský<br>P. Petr Hruška, generální vikář</dd>
      <dt>Adresa</dt><dd>náměstí Republiky 234/35, 301 00 Plzeň</dd>
      <dt>IČ · DIČ</dt><dd>45334439 · CZ45334439</dd>
    </dl>
  </div>
</div></section>

<section class="bg-cream" data-line="left"><div class="wrap give">
  <div class="reveal">
    <span class="eyebrow">Podpořte farnost</span>
    <h2>Každý dar pomáhá</h2>
    <p>Chod farnosti, vytápění kostelů v zimních měsících a opravy historických sakrálních památek můžeme zajišťovat díky vaší obětavosti a dobrovolným darům.</p>
    <p><b>Potvrzení o daru:</b> na požádání vám rádi vystavíme potvrzení o daru pro účely daňového přiznání.</p>
    <p class="muted" style="margin-top:22px;font-style:italic">Ze srdce vám děkujeme za každou vaši pomoc, štědrost a modlitbu.</p>
  </div>
  {GIVE_BOX}
</div></section>

<section data-line="end"><div class="wrap">
  <div class="center reveal"><span class="eyebrow">Najdete nás zde</span><h2>Kpt. Jaroše 321/2, Kraslice</h2></div>
  <div class="map reveal"><button class="map-load" type="button" data-src="{MAP}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/></svg>Zobrazit mapu<small>Načte se mapa od Googlu</small></button></div>
  <div class="center" style="margin-top:22px"><a class="btn ghost" href="https://www.google.com/maps/search/?api=1&amp;query=Kpt.+Jaro%C5%A1e+321%2F2,+358+01+Kraslice" target="_blank" rel="noopener">Otevřít v Google Mapách {ARROW}</a></div>
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

# =====================================================================
# DĚTSKÝ TÁBOR
# =====================================================================
DOCS = [("assets/docs/prihlaska-tabor-2027.pdf", "Přihláška"),
        ("assets/docs/posudek-o-zdravotni-zpusobilosti.pdf", "Posudek o zdravotní způsobilosti"),
        ("assets/docs/prohlaseni-zakonnych-zastupcu.pdf", "Prohlášení zákonných zástupců"),
        ("assets/docs/souhlas-foto.pdf", "Souhlas se zveřejněním fotografií")]
# dokumenty, které se vyplňují a posílají zvlášť (papírovou přihlášku nahrazuje online formulář)
docs = "".join(f'<a class="doc" href="{h}" target="_blank" rel="noopener"><i>PDF</i>{t}</a>' for h, t in DOCS[1:])
MAIL = '<a href="mailto:detskytaborslunicko@gmail.com">detskytaborslunicko@gmail.com</a>'
tabor_body = f'''<section class="page-hero" data-line="hero"><div class="wrap page-hero-grid">
  <div>
    <span class="eyebrow">Dětský tábor</span>
    <h1>Léto plné zážitků, dobrodružství a nových přátel</h1>
    <dl class="facts-strip">
      <div><dt>Termín</dt><dd>17. 7. – 24. 7. 2027</dd></div>
      <div><dt>Kapacita</dt><dd>50 míst</dd></div>
      <div><dt>Cena</dt><dd><a href="#platba">{TABOR_CENA_TXT} Kč</a><small>platba do 31. 5. 2027</small></dd></div>
    </dl>
    <p class="lead">Připravujeme další ročník našeho dětského tábora! Těšit se můžete na společně strávené dny plné her, zábavy, výletů, dobrodružství a nezapomenutelných zážitků.</p>
  </div>
  <div class="page-hero-img"><img src="assets/img/tabor.jpg" alt="Děti na táboře"></div>
</div></section>

<section data-line="left"><div class="wrap cards" style="grid-template-columns:1fr 1fr">
  <div class="card reveal">
    <div class="ico"><svg viewBox="0 0 24 24"><path d="M3 6h18v12H3zM3 7l9 6 9-6"/></svg></div>
    <h3>Přihlášky</h3>
    <p>Přihlášky na dětský tábor 2027 přijímáme od 1. listopadu 2026. Nejjednodušší je vyplnit online přihlášku přímo tady na webu.</p>
    <a class="more-link" href="#prihlaska">Vyplnit přihlášku online {ARROW}</a>
  </div>
  <div class="card reveal d1">
    <div class="ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6M12 17h.01"/></svg></div>
    <h3>Máte dotaz?</h3>
    <p>Pokud potřebujete více informací nebo se chcete na cokoliv zeptat, napište nám na {MAIL}. Každý dotaz rádi zodpovíme.</p>
    <p style="margin-top:10px;font-size:17px;color:var(--navy)">Těšíme se na společné léto! ☀️</p>
  </div>
</div></section>

<section class="bg-mist" data-line="right" id="prihlaska"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(30px,4vw,50px)">
    <span class="eyebrow">Online přihláška</span>
    <h2>Přihláška na tábor 2027</h2>
    <p class="lead">Termín 17.–24. 7. 2027 · Tábor Sluníčko. Pole označená hvězdičkou jsou povinná.</p>
  </div>
  <form class="prihlaska reveal" name="prihlaska-tabor" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/detsky-tabor.html?odeslano=1#prihlaska" novalidate>
    <input type="hidden" name="form-name" value="prihlaska-tabor">
    <p hidden><label>Nevyplňujte: <input name="bot-field"></label></p>
    <input type="hidden" name="subject" value="Přihláška na tábor 2027">

    <fieldset>
      <legend><span>1</span>Údaje o dítěti</legend>
      <div class="f-grid">
        <label class="f">Jméno a příjmení *<input name="dite_jmeno" required autocomplete="off"></label>
        <label class="f">Datum narození *<input name="dite_narozeni" type="date" required></label>
        <label class="f wide">Adresa trvalého pobytu *<input name="dite_adresa" required autocomplete="street-address"></label>
        <label class="f">Zdravotní pojišťovna *<input name="dite_pojistovna" required placeholder="např. VZP (111)"></label>
        <div class="f"><span>Plavec / neplavec *</span><div class="choice"><label><input type="radio" name="plavec" value="Plavec" required><span>Plavec</span></label><label><input type="radio" name="plavec" value="Neplavec"><span>Neplavec</span></label></div></div>
      </div>
    </fieldset>

    <fieldset>
      <legend><span>2</span>Zákonný zástupce a kontakty</legend>
      <div class="f-grid">
        <label class="f wide">Jméno a příjmení zákonného zástupce *<input name="zastupce_jmeno" required autocomplete="name"></label>
        <label class="f">Telefon *<input name="zastupce_telefon" type="tel" required autocomplete="tel"></label>
        <label class="f">E-mail *<input name="email" type="email" required autocomplete="email"></label>
        <label class="f">Další kontakt pro naléhavé situace *<input name="dalsi_kontakt" required placeholder="jméno a vztah k dítěti"></label>
        <label class="f">Telefon další kontaktní osoby *<input name="dalsi_telefon" type="tel" required></label>
      </div>
    </fieldset>

    <fieldset>
      <legend><span>3</span>Informace důležité pro pobyt</legend>
      <div class="f-grid">
        <label class="f wide">Alergie, stravovací omezení, zdravotní či pohybová omezení<textarea name="alergie" rows="2"></textarea></label>
        <label class="f wide">Pravidelně užívané léky, dávkování a další důležité informace pro zdravotníka<textarea name="leky" rows="2"></textarea></label>
        <label class="f wide">Další potřeby dítěte, případně přání ohledně společného ubytování<textarea name="potreby" rows="2"></textarea></label>
      </div>
    </fieldset>

    <fieldset>
      <legend><span>4</span>Prohlášení zákonného zástupce</legend>
      <label class="check"><input type="checkbox" name="prohlaseni" value="Ano" required><span>Přihlašuji uvedené dítě na Tábor Sluníčko pořádaný Římskokatolickou farností Kraslice. Potvrzuji správnost uvedených údajů a zavazuji se bez zbytečného odkladu oznámit jejich změny, zejména změny zdravotního stavu a kontaktních údajů. Beru na vědomí, že součástí programu mohou být přiměřené pohybové, výletní a duchovní aktivity odpovídající charakteru farního tábora. *</span></label>
      <label class="check"><input type="checkbox" name="osobni_udaje" value="Ano" required><span>Beru na vědomí, že pořadatel zpracovává údaje potřebné k organizaci tábora, komunikaci se zákonnými zástupci a zajištění bezpečnosti účastníků. Podrobné informace o zpracování osobních údajů mi budou poskytnuty pořadatelem. *</span></label>
      <div class="f" style="margin-top:14px"><span>Souhlas se zveřejněním fotografií a videí dítěte pro prezentaci tábora/farnosti *</span>
        <div class="choice"><label><input type="radio" name="foto_souhlas" value="Souhlasím" required><span>Souhlasím</span></label><label><input type="radio" name="foto_souhlas" value="Nesouhlasím"><span>Nesouhlasím</span></label></div>
        <small class="muted">Neudělení souhlasu nemá vliv na účast dítěte.</small></div>
    </fieldset>

    <div class="docs-notice">
      <p><b>Nezapomeňte na dokumenty.</b> Kromě online přihlášky je potřeba vyplnit, podepsat a poslat na {MAIL} také tyto dokumenty:</p>
      <div class="docs">{docs}</div>
    </div>

    <div class="f-submit">
      <button class="btn" type="submit">Odeslat přihlášku {ARROW}</button>
      <p class="form-note">Po odeslání přijde přihláška pořadatelům na {MAIL}.</p>
      <p class="form-ok" role="status" hidden>Děkujeme, přihláška byla odeslána! Brzy se vám ozveme. Nezapomeňte prosím poslat vyplněné dokumenty a uhradit platbu do 31. 5. 2027.</p>
      <p class="form-err" role="alert" hidden>Přihlášku se nepodařilo odeslat. Zkuste to prosím znovu, nebo ji pošlete e-mailem na {MAIL}.</p>
      <p class="form-invalid" role="alert" hidden>Vyplňte prosím všechna povinná pole označená hvězdičkou.</p>
    </div>
  </form>
</div></section>

<section data-line="end" id="platba"><div class="wrap give">
  <div class="reveal">
    <span class="eyebrow">Cena a platba</span>
    <h2>Cena tábora</h2>
    <div class="date-big">{TABOR_CENA_TXT} Kč</div>
    <p class="lead" style="margin-top:22px">Platbu prosím pošlete na bankovní účet farnosti <b>do 31. 5. 2027</b>.</p>
    <div class="cbox" style="margin-top:22px">
      <dl style="margin-top:0">
        <dt>Číslo účtu</dt><dd><b>860622379/0800</b> <button class="copy" type="button" data-copy="860622379/0800">Zkopírovat</button></dd>
        <dt>Částka</dt><dd>{TABOR_CENA_TXT} Kč</dd>
        <dt>Splatnost</dt><dd><b>do 31. 5. 2027</b></dd>
        <dt>Variabilní symbol</dt><dd>datum narození dítěte ve tvaru DDMMRRRR<br><span class="muted" style="font-size:15px">např. 15. 3. 2015 → 15032015</span></dd>
        <dt>Zpráva pro příjemce</dt><dd>Tábor 2027 a jméno dítěte</dd>
      </dl>
    </div>
  </div>
  <div class="give-box reveal d1">
    <h3>Platba přes QR kód</h3>
    <p class="muted" style="font-size:15px;margin:0 auto 16px">Vyplňte údaje o dítěti a naskenujte kód v aplikaci své banky.</p>
    <div class="amounts"><input id="tabor-jmeno" style="width:min(100%,280px)" placeholder="jméno a příjmení dítěte" aria-label="Jméno a příjmení dítěte" autocomplete="off">
      <input id="tabor-narozeni" style="width:min(100%,280px)" inputmode="numeric" placeholder="datum narození, např. 15. 3. 2015" aria-label="Datum narození dítěte" autocomplete="off"></div>
    <div id="qr-tabor" class="qr" aria-label="QR kód pro platbu tábora" data-amount="{TABOR_CENA}" data-due="20270531"></div>
    <p class="acct">Tábor 2027 · {TABOR_CENA_TXT} Kč · <span id="tabor-vs">VS: datum narození</span><strong>860622379/0800</strong></p>
  </div>
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

# =====================================================================
# AKTUALITY
# =====================================================================
aktuality_body = f'''<section class="page-hero" data-line="hero"><div class="wrap page-hero-grid">
  <div>
    <span class="eyebrow">Aktuality</span>
    <h1>Aktuality naší farnosti</h1>
    <p class="lead">Zde najdete nejnovější informace o dění v naší farnosti, pozvánky na bohoslužby, společná setkání, kulturní a duchovní akce i další důležité události.</p>
    <p>Sledujte, co se u nás chystá, a buďte součástí života našeho farního společenství. Těšíme se na společná setkání!</p>
  </div>
  <div class="page-hero-img"><img src="assets/img/aktuality.jpg" alt="Kostel při západu slunce"></div>
</div></section>

<section class="bg-mist" data-line="end"><div class="wrap">
  <div class="sec-head reveal"><div><span class="eyebrow">Nadcházející události</span><h2>Co se chystá</h2></div>
    <div class="btns" style="margin:0"><a class="btn ghost" href="{FB}" target="_blank" rel="noopener">Facebook</a><a class="btn ghost" href="{IG}" target="_blank" rel="noopener">Instagram</a></div></div>
  <div class="akce-list full" data-akce><p class="empty">Načítám akce…</p></div>
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

# =====================================================================
# POŘAD MĚSÍCE
# =====================================================================
porad_body = f'''<section class="page-hero" data-line="hero"><div class="wrap page-hero-grid">
  <div>
    <span class="eyebrow">Pořad měsíce</span>
    <h1>Buďte stále v obraze</h1>
    <p class="lead">Přinášíme vám aktuální přehled bohoslužeb a dalších událostí v naší farnosti. Najdete zde informace o termínech, časech a místech konání.</p>
    <p>Srdečně vás zveme ke společným setkáním a modlitbě.</p>
  </div>
  <div class="page-hero-img"><img src="assets/img/porad.jpg" alt="Oltář se svící a Biblí"></div>
</div></section>

<section data-line="end"><div class="wrap">
  <a class="porad-card reveal" href="{PORAD_PDF}" target="_blank" rel="noopener" data-porad>
    <span class="pdf">PDF</span>
    <span><small>Pořad měsíce</small><strong data-porad-nazev>{PORAD_NAZEV}</strong></span>
    <span class="btn">Otevřít {DOWN}</span>
  </a>
  <p class="center muted reveal" style="margin:28px auto 0">Další akce najdete v <a href="aktuality.html">Aktualitách</a>.</p>
</div>
  <div class="church-spot" aria-hidden="true"></div>
</section>'''

notfound_body = f'''<section class="page-hero" style="min-height:70vh"><div class="wrap center">
  <span class="eyebrow">Chyba 404</span><h1 style="margin:0 auto">Tato stránka neexistuje</h1>
  <div class="btns" style="justify-content:center"><a class="btn" href="index.html">Zpět na úvod {ARROW}</a></div>
</div></section>'''

D = "Římskokatolická farnost Kraslice – společenství věřících v Kraslicích a okolí: bohoslužby, aktuality, historie kostelů, dětský tábor a kontakty."
page("index.html", "uvod", "Římskokatolická farnost Kraslice", D, index_body, line=False)
page("o-nas.html", "onas", "O nás – Římskokatolická farnost Kraslice", "Život v naší farnosti: duchovní správa, svátosti, společenství a podpora farnosti.", onas_body)
page("historie.html", "historie", "Historie – Římskokatolická farnost Kraslice", "Příběhy kostelů na Kraslicku: Kraslice, Rotava, Jindřichovice, Oloví, Bublava, Stříbrná, Šindelová.", historie_body)
page("kontakty.html", "kontakty", "Kontakty – Římskokatolická farnost Kraslice", "Kontakt na farnost Kraslice a duchovního správce P. Bystríka Ferance.", kontakty_body)
page("detsky-tabor.html", "tabor", "Dětský tábor – Římskokatolická farnost Kraslice", "Dětský tábor 17.–24. 7. 2027, kapacita 50 míst: cena, platba, přihlášky a dokumenty ke stažení.", tabor_body)
page("aktuality.html", "aktuality", "Aktuality – Římskokatolická farnost Kraslice", "Nadcházející akce a události farnosti Kraslice.", aktuality_body)
page("porad-mesice.html", "porad", "Pořad měsíce – Římskokatolická farnost Kraslice", "Aktuální pořad bohoslužeb a farní ohlášky.", porad_body)
page("404.html", "", "Stránka nenalezena – farnost Kraslice", D, notfound_body, line=False)

# favicon
(ROOT / "assets/favicon.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}"><path fill="#F2D35C" fill-rule="evenodd" d="{CHURCH_D}{WINDOWS_D}"/></svg>', encoding="utf-8")
