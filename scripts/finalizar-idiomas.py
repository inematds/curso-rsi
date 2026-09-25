"""Run after the official translation tool. Repair course-specific paths and metadata."""
from pathlib import Path
from bs4 import BeautifulSoup
B=Path(__file__).resolve().parent.parent
origin='https://inematds.github.io/curso-rsi/'
for lang in ('pt','en'):
    folder=B if lang=='pt' else B/lang
    for name in ('curso.html','landing.html'):
        p=folder/name
        soup=BeautifulSoup(p.read_text(),'html.parser')
        canonical=soup.find('link',rel='canonical')
        if canonical is None:
            canonical=soup.new_tag('link',rel='canonical');soup.head.append(canonical)
        canonical['href']=origin+('en/' if lang=='en' else '')+('curso.html' if name=='curso.html' else '')
        nav=soup.select_one('nav.langs')
        if nav:nav['aria-label']='Language' if lang=='en' else 'Idioma'
        if lang=='en':
            for a in soup.select('a[href]'):
                if a['href']=='docs/pesquisa.md':
                    a['href']='../docs/pesquisa.md';a.string='Read the research and editorial decisions (Portuguese)'
                if a['href'] in ('https://inema.club','https://inema.club/'):a['href']='https://inema.club/en/'
            # The official tool translates description but leaves social metadata in PT.
            for key,selector in [('og:title','title'),('og:description','meta[name="description"]')]:
                target=soup.find('meta',property=key)
                source=soup.select_one(selector)
                if target and source:target['content']=source.get('content',source.get_text())
            for node in soup.find_all('meta',property='og:url'):node['content']=canonical['href']
        p.write_text(str(soup))
    # Full landing on /en/, with its own metadata and language selector; no branded placeholder redirect.
    (folder/'index.html').write_text((folder/'landing.html').read_text())
print('PT/EN entry pages, metadata, navigation and reference links finalized.')
