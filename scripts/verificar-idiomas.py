"""Verify bilingual structure, resources, review cards and translation coverage."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import importlib.util,json,re
B=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('translator',Path.home()/'.claude/skills/formato-curso-v6/scripts/traduzir-curso.py')
tr=importlib.util.module_from_spec(spec);spec.loader.exec_module(tr)
source=json.loads((B/'i18n/unidades-pt.json').read_text())
for language in ('en','es'):
    cache=json.loads((B/f'i18n/{language}.json').read_text())
    missing=[u for u in source if u not in cache]
    assert not missing,(language,missing[:4])
for locale in ('pt','en','es'):
 d=B if locale=='pt' else B/locale
 for name in ('index.html','landing.html','curso.html'):
  p=d/name;s=BeautifulSoup(p.read_text(),'html.parser')
  assert s.html['lang']==('pt-BR' if locale=='pt' else locale)
  assert {x['hreflang'] for x in s.select('link[rel="alternate"]')}=={'pt-BR','en','es'}
  assert s.select_one('link[rel="canonical"]')['href'].startswith('https://inematds.github.io/curso-rsi/'+(locale+'/' if locale!='pt' else ''))
  for t in s.select('[href],[src]'):
   url=urlsplit(t.get('href',t.get('src','')))
   if url.scheme or url.netloc or not url.path:continue
   dest=(d/unquote(url.path)).resolve()
   assert dest.exists(),(str(p),str(dest))
  if name=='curso.html':
   lessons=s.select('[data-aula].view');assert len(lessons)==18
   assert sum(len(json.loads(c.string)) for c in s.select('script[id^="cards-"]'))==54
   assert len(s.select('.practice'))==18
   assert s.select_one('meta[name="curso"]')['content']=='curso-rsi-v62'+('-'+locale if locale!='pt' else '')
   for quiz in s.select('.quiz'):
    assert quiz.select_one(f'.opt[data-k="{quiz["data-answer"]}"]')
pt=(B/'assets/curso.js').read_text()
mp,_=tr.ler_L(pt)
for lang in ('en','es'):
    js=(B/lang/'assets/curso.js').read_text();m,_=tr.ler_L(js)
    assert pt[:mp.start(1)]+pt[mp.end(1):]==js[:m.start(1)]+js[m.end(1):], 'Translated engine changed beyond L dictionary'
for lang in ('','en','es'):
    assert (B/lang/'index.html').read_bytes()==(B/lang/'landing.html').read_bytes()
    assert (B/lang/'materiais/conhecimento-aprovado.txt').exists()
print('PASS: PT/EN/ES, 18 lessons and 54 cards each, local assets/links, separate progress, full translation caches, unchanged engine logic, approved knowledge worksheets.')
