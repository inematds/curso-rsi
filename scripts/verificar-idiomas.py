"""Verify bilingual structure, resources, review cards and translation coverage."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import importlib.util,json,re
B=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('translator',Path.home()/'.claude/skills/formato-curso-v6/scripts/traduzir-curso.py')
tr=importlib.util.module_from_spec(spec);spec.loader.exec_module(tr)
cache=json.loads((B/'i18n/en.json').read_text())
missing=[u for u in tr.unidades(str(B)) if u not in cache]
# Language selector itself is inserted after translation.
missing=[u for u in missing if not ('class="langs"' in u or u in ('PT','EN','Idioma'))]
assert not missing,missing[:4]
for locale in ('pt','en'):
 d=B if locale=='pt' else B/'en'
 for name in ('index.html','landing.html','curso.html'):
  p=d/name;s=BeautifulSoup(p.read_text(),'html.parser')
  assert s.html['lang']==('pt-BR' if locale=='pt' else 'en')
  assert {x['hreflang'] for x in s.select('link[rel="alternate"]')}=={'pt-BR','en'}
  assert s.select_one('link[rel="canonical"]')['href'].startswith('https://inematds.github.io/curso-rsi/'+('en/' if locale=='en' else ''))
  for t in s.select('[href],[src]'):
   url=urlsplit(t.get('href',t.get('src','')))
   if url.scheme or url.netloc or not url.path:continue
   dest=(d/unquote(url.path)).resolve()
   assert dest.exists(),(str(p),str(dest))
  if name=='curso.html':
   lessons=s.select('[data-aula].view');assert len(lessons)==18
   assert sum(len(json.loads(c.string)) for c in s.select('script[id^="cards-"]'))==54
   assert len(s.select('.practice'))==18
   assert s.select_one('meta[name="curso"]')['content']=='curso-rsi-v62'+('-en' if locale=='en' else '')
   for quiz in s.select('.quiz'):
    assert quiz.select_one(f'.opt[data-k="{quiz["data-answer"]}"]')
pt=(B/'assets/curso.js').read_text();en=(B/'en/assets/curso.js').read_text()
mp,_=tr.ler_L(pt);me,_=tr.ler_L(en)
assert pt[:mp.start(1)]+pt[mp.end(1):]==en[:me.start(1)]+en[me.end(1):], 'English engine changed beyond L dictionary'
assert (B/'index.html').read_bytes()==(B/'landing.html').read_bytes()
assert (B/'en/index.html').read_bytes()==(B/'en/landing.html').read_bytes()
assert not (B/'es').exists()
print('PASS: PT/EN, 18 lessons and 54 cards per language, all local assets/links, separate progress, full cache, unchanged engine logic; no ES course.')
