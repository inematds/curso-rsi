from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,re
b=Path(__file__).resolve().parent.parent
errors=[]
for name in ['index.html','landing.html','curso.html']:
 p=b/name;soup=BeautifulSoup(p.read_text(),'html.parser')
 for el in soup.select('[href],[src]'):
  url=el.get('href',el.get('src',''));parts=urlsplit(url)
  if parts.scheme or url.startswith('//'):continue
  dest=p.parent/unquote(parts.path) if parts.path else p
  if not dest.exists():errors.append(f'{name}: ausente {url}')
  if parts.fragment and dest.suffix=='.html':
   ids={e.get('id') for e in BeautifulSoup(dest.read_text(),'html.parser').select('[id]')}
   if parts.fragment not in ids and 'v-'+parts.fragment not in ids:errors.append(f'{name}: âncora ausente {url}')
 if re.search(r'\[(?:Nome|Resultado|alt da|Categoria)',p.read_text()):errors.append(f'{name}: marcador de template')
c=BeautifulSoup((b/'curso.html').read_text(),'html.parser')
assert len(c.select('.view[data-aula]'))==18
assert sum(len(json.loads(x.string)) for x in c.select('script[id^="cards-"]'))==54
assert len(c.select('.practice'))==18
assert (b/'index.html').read_bytes()==(b/'landing.html').read_bytes()
assert not errors,'\n'.join(errors)
print('OK: links e âncoras locais; 18 aulas; 18 práticas; 54 cartões; entradas consistentes.')
