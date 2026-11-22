# Web Římskokatolické farnosti Kraslice

Statický web bez databáze. Stránky vyrábí skript `tools/build.py` (společná hlavička, patička a logo).

## Administrace (farnostkraslice.cz/admin)
Decap CMS, přihlášení přes GitHub (stejně jako u Moery). Upravuje se v ní:
- **Aktuality** – akce (`content/akce.json`): název, datum, čas, místo, krátký popis a podrobnosti. Proběhlé akce se skryjí samy.
- **Pořad měsíce** – název a PDF s farními ohláškami (`content/porad.json`, PDF se nahrává do `uploads/`).
Uložení v administraci se zapíše do GitHubu a Netlify web během chvilky sám aktualizuje.
Nastavení je v `admin/config.yml`. **Před spuštěním je potřeba v něm doplnit přesný název GitHub repozitáře** (řádek `repo:`) a v Netlify zapnout přihlašování přes GitHub (OAuth), stejně jako u Moery.

## Spuštění na Netlify (jednorázově)
Repozitář: https://github.com/farnostkraslice/farnost-web (soukromý, účet `farnostkraslice`).
1. **Netlify účet:** app.netlify.com → Sign up → „Continue with GitHub“ účtem farnostkraslice.
2. **Web:** Add new site → Import an existing project → GitHub → `farnost-web`. Build command nechat prázdné, Publish directory `.` → Deploy.
3. **Přihláška na tábor:** Site configuration → Forms → Enable form detection, pak znovu nasadit (Deploys → Trigger deploy). Ve Forms → Form notifications → Add notification → Email → `detskytaborslunicko@gmail.com`, formulář `prihlaska-tabor`.
4. **Přihlášení do administrace:** na GitHubu (účet farnostkraslice) Settings → Developer settings → OAuth Apps → New OAuth App: Homepage URL `https://farnostkraslice.cz`, Authorization callback URL `https://api.netlify.com/auth/done`. Vzniklé Client ID a Client secret vložit v Netlify: Site configuration → Access & security → OAuth → Install provider → GitHub.
5. **Doména:** Domain management → Add a domain → `farnostkraslice.cz`. U registrátora domény změnit jen záznamy pro web (A / CNAME) podle Netlify, záznamy pro e-mail (MX) nechat. HTTPS zapne Netlify sám.
6. Starý WordPress hosting nechat ještě pár týdnů, stáhnout zálohu a pak zrušit.

## Jak upravit
- **Texty stránek:** uprav v `tools/build.py` a spusť `python3 tools/build.py`. HTML soubory needituj ručně, další sestavení by úpravu přepsalo.
- **Akce (Aktuality):** nejjednodušeji v administraci. Data jsou v `content/akce.json`.
- **Pořad měsíce:** nejjednodušeji v administraci. Data jsou v `content/porad.json`.
- **Cena tábora:** v `tools/build.py` proměnná `TABOR_CENA` (teď 5000). Platí se na účet farnosti 860622379/0800, QR kód na stránce tábora se podle ceny vytvoří sám. Variabilní symbol je datum narození dítěte (DDMMRRRR), rodič ho napíše do políčka u QR kódu. Termín platby se neuvádí.
- **Online přihláška na tábor:** formulář `prihlaska-tabor` na stránce Dětský tábor (texty v `tools/build.py`). Odesílá se přes **Netlify Forms**, funguje tedy až na Netlify (v náhledu na počítači skončí chybou). V Netlify je potřeba v Forms → Form notifications nastavit e-mail **detskytaborslunicko@gmail.com**. Platba je splatná do 31. 5. 2027 (je i v QR kódu).
- **Dokumenty k táboru:** `assets/docs/`, seznam je v `tools/build.py` (proměnná `DOCS`). Na webu se nabízí jen v upozornění uvnitř online přihlášky (posudek, prohlášení, souhlas s fotkami). Papírová přihláška se neodkazuje, nahrazuje ji online formulář.

## Vzhled
- Barvy z vizuálního stylu: kostelík #F8E9A4, text #182347, žlutá #F8DF5A, modrá #B3D3EF a #E3EFFA, šedomodrá #4E5D6B.
- Písma: Adorage (název „Římskokatolická“ a nadpisy, písmo z loga) a Raleway (text), uložená přímo na webu v `assets/fonts/`.
- Kostelík z loga je v `tools/build.py` (proměnné `CHURCH_D` a `WINDOWS_D`). Okna jsou průhledná.

## Interaktivní prvek
Na konci každé podstránky (sekce s `data-line="end"`) se díly kostelíka přikutálí z okrajů a složí do loga. Kód je v `main.js`.
Kostelík má vlastní vyhrazené místo (`.church-spot`), takže ho nic nepřekrývá. Adresa s `?kostel=hotovo` ukáže kostelík rovnou složený.
Po složení přiběhne zprava modrý farář z geometrických tvarů, otevřou se před ním dveře ve věži a vběhne dovnitř (třída `.farar` ve `style.css`, funkce `playPriest` v `main.js`). Když se vyjede nahoru a znovu dolů, zopakuje se to.

## Právní stránky
`ochrana-osobnich-udaju.html` a `cookies.html` (texty v `tools/build.py`, odkazy v patičce spolu s „© 2026 Římskokatolická farnost Kraslice. Všechna práva vyhrazena.“). Web nepoužívá sledovací cookies, proto nemá lištu se souhlasem. Doby uchování údajů z přihlášky jsou navržené – farnost by je měla potvrdit.

## Přesměrování ze starého webu
Soubor `_redirects` (čte ho Netlify) posílá staré adresy z WordPressu (např. `/o-nas/`, `/historie-2/`, `/event/…`, staré PDF ve `/wp-content/uploads/…`) na nové stránky. Na konci je „záchranná síť“: každá jiná adresa, která na novém webu neexistuje, vede na úvodní stránku (proto se stránka 404 prakticky nezobrazí). Začne fungovat po nasazení na Netlify. Přesměrování z `www.` a z `http://` na `https://` zařídí Netlify sám po přidání domény.

## Spuštění na počítači
Ve složce farnost-kraslice spusť `python3 -m http.server 8732 --directory web` a otevři http://localhost:8732
