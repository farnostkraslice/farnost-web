# Web Římskokatolické farnosti Kraslice (farnostkraslice.cz)

Statický web bez build kroku na hostingu Netlify. Zdroj je v soukromém GitHub repozitáři `farnostkraslice/farnost-web` (větev `main`), účet GitHub `farnostkraslice` (na tomto počítači vedle `moera-cz`, přepnout `gh auth switch --user farnostkraslice`). Majitelka komunikuje česky a není programátorka: vysvětlovat jednoduše a česky.

## Struktura
- Stránky (`index.html`, `o-nas.html`, `historie.html`, `kontakty.html`, `detsky-tabor.html`, `aktuality.html`, `porad-mesice.html`, `404.html`) **generuje `tools/build.py`**. Texty měň tam a spusť `python3 tools/build.py`. HTML needituj ručně.
- `style.css`, `main.js`: společný styl a skripty.
- `content/akce.json`, `content/porad.json`: data z administrace (Decap CMS na `/admin`, konfigurace `admin/config.yml`). `main.js` je načítá za běhu.
- `_redirects`: přesměrování starých WordPress adres, na konci catch-all `/* → /`. Pracovní soubory schované 404.
- Online přihláška na tábor: Netlify Forms `prihlaska-tabor`, upozornění na detskytaborslunicko@gmail.com.

## Vzhled a pravidla od majitelky
- Logo = kostelík (`CHURCH_D`, `WINDOWS_D` v build.py), barva #F8E9A4, okna průhledná. V záhlaví jen kostelík bez textu a bez podkladu.
- Písma: Adorage (nadpisy a název „Římskokatolická“, písmo z loga), Raleway (text).
- Světlá varianta barev (ne výrazná žluto-modrá). Záhlaví nahoře průhledné, po scrollu bílé.
- Úvodní stránka maximálně jednoduchá (původní fotka, název, verš, tlačítko O nás). Menu ve stejném pořadí jako na starém webu.
- Interaktivní prvek: na konci podstránek se díly kostelíka přikutálí a složí (`.church-spot`), pak zprava přiběhne modrý geometrický farář a vběhne do dveří ve věži. Během stránky se nic nekutálí.
- Ikony sítí v záhlaví plné, bez koleček. Formuláře malé a minimalistické.
- Tábor: 17.–24. 7. 2027, kapacita 50, cena 5 000 Kč (`TABOR_CENA`), splatnost 31. 5. 2027, VS = datum narození dítěte (DDMMRRRR).
