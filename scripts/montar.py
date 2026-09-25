from pathlib import Path
from html import escape as e
import json, math, re, subprocess
from conteudo import AULAS, FONTES, CALMAS
B=Path(__file__).resolve().parent.parent
S=Path('/home/nmaldaner/.claude/skills/formato-curso-v6')
assert len(AULAS)==18
modulos=[('Fundamentos: reconhecer o que mudou','Distinguir RSI, revisão de respostas e alegações sem evidência.'),('Funcionamento: desenhar um ciclo','Objetivos, papéis, avaliação, memória e adoção de melhorias.'),('Pesquisa: ler os casos reais','AlphaEvolve, DGM e as peças da pesquisa automatizada.'),('Avaliação: conferir antes de confiar','Casos reservados, manipulação de medidas e dados gerados.'),('Aplicações: usar no trabalho','Atendimento, educação e síntese de documentos com referências.'),('Projeto final: decidir com evidências','Escolher implementação, planejar um piloto e relatar seus limites.')]
cfg=dict(id='curso-rsi-v62',titulo='RSI v6.2 — Entenda e aplique ciclos de melhoria em IA',titulo_html='Como uma IA pode <em>ajudar a melhorar outra?</em>',curso_curto='RSI v6.2',kicker='RSI v6.2 · 6 módulos · 18 aulas',lead='Entenda o autoaperfeiçoamento recursivo, examine estudos reais e monte um ciclo supervisionado de melhoria. Leitura curta, exemplos visíveis e uma prática por aula.',imagem_trilha='assets/img/trilha.webp',alt_trilha='Gestora e educador comparam documentos e resultados de uma experiência de melhoria numa mesa de trabalho.',rodape='RSI v6.2 · INEMA.CLUB · <a href="landing.html">sobre o curso</a>',landing='landing.html',glossario=True,modulos=[dict(titulo=f'Módulo {i+1} · {t}',resumo=r,aulas=list(range(i*3+1,i*3+4))) for i,(t,r) in enumerate(modulos)])
(B/'curso.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')

def visual(step,n,k):
 _,_,_,la,a,lb,b=step
 kind=(n+k)%3
 if n==1 and k==2: kind=1
 if kind==0:
  return f'<figure class="largo"><div class="lado"><div class="neutro"><span class="rot">{e(la)}</span><p>{e(a)}</p></div><div class="neutro"><span class="rot">{e(lb)}</span><p>{e(b)}</p></div></div><figcaption>Compare os dois registros. Exemplo didático.</figcaption></figure>'
 if kind==1:
  return '<figure class="largo"><div class="tela"><div class="tela-top"><i></i><i></i><i></i><span>Fichas de comparação · ilustração</span></div>'+''.join(f'<div class="tela-caso" data-rotulo="{e(l)}"><div class="tela-body"><p class="msg ia"><span class="quem">{e(l)}</span>{e(t)}</p></div><p class="tela-nota">Registro didático para comparar; não é execução de uma ferramenta.</p></div>' for l,t in [(la,a),(lb,b)])+'</div><figcaption>Toque nos dois rótulos para examinar os registros.</figcaption></figure>'
 return f'<figure class="largo"><div class="janela"><div class="tela-top"><i></i><i></i><i></i><span>Ficha de trabalho · exemplo</span></div><div class="janela-body"><div class="item doc"><span class="pin">1</span><span><b>{e(la)}</b><br>{e(a)}</span></div><div class="item doc"><span class="pin">2</span><span><b>{e(lb)}</b><br>{e(b)}</span></div></div></div><figcaption>Leia o primeiro registro e confira como o segundo se relaciona com ele.</figcaption></figure>'

tempos=[]
for n,a in enumerate(AULAS,1):
 words=len((' '.join(s[1]+' '+s[2].split('|')[1] for s in a['steps'])+' '+a['dor']+' '+a['promessa']).split())
 tempo=math.ceil(words/200+10+1);tempos.append(tempo)
 resumo=''.join('<li>'+e(r)+'</li>' for r in a['resumo'])
 alt=f'Profissionais examinam materiais de trabalho e comparam registros para a aula: {a["titulo"]}.'
 if n==13: alt='Gestora de papelaria compara dois cartões ao preparar um teste de respostas, diante de prateleiras de materiais.'
 s=f'''<section class="view" id="v-aula-{n}" data-aula="{n}" data-tempo="{tempo}min"><div class="aula">
<header class="a-hero"><p class="kicker">Aula {n} de 18</p><h1>{e(a['titulo'])}</h1>
<figure class="cena"><img src="assets/img/aula-{n}.webp" width="1280" height="720" alt="{e(alt)}"></figure>
<p class="promise">Você consegue {e(a['promessa'])}</p><p class="why">{e(a['dor'])}</p>
<div class="em1min"><p class="k">Em 1 minuto</p><ol>{resumo}</ol></div></header>'''
 for k,step in enumerate(a['steps'],1):
  title,body,ex,*_=step;prof,example=ex.split('|')
  term=f'<p><span class="gterm" data-def="{e(a["definicao"],quote=True)}">{e(a["termo"])}</span>: {e(a["definicao"])}</p>' if k==1 else ''
  s+=f'<section class="step" data-kind="fundamento"><h2><span class="n">{k}</span>{e(title)}</h2>{term}<p>{e(body)}</p><p data-ex="{prof}">{e(example)}</p>{visual(step,n,k)}'
  if k==3:
   q,correct,bad1,bad2=a['quiz'];opts=[(correct,True),(bad1,False),(bad2,False)]
   shift=n%3;opts=opts[shift:]+opts[:shift];answer='abc'[[v for _,v in opts].index(True)]
   s+=f'<div class="quiz" data-answer="{answer}"><p class="qk">Teste-se</p><p class="q">{e(q)}</p>'
   for key,(label,good) in zip('abc',opts):
    fb=('Correto. '+a['gabarito']) if good else ('Reveja a comparação: '+correct.lower())
    s+=f'<button class="opt" data-k="{key}" data-fb="{e(fb)}">{e(label)}</button>'
   s+=' <p class="qfb" aria-live="polite"></p></div>'
   s+=f'<div class="calma"><p><span class="k">Se travou aqui, é normal</span>{e(CALMAS[n])}</p></div>'
  s+='</section>'
 mode='prompt' if n in [13,14,15] else 'tarefa' if n in [4,5,6,10,12,16,17,18] else 'analise'
 reserved = ('<details class="mais"><summary>Etapa 2 · abrir a validação depois do desenvolvimento</summary><p>'+e(a['reservado'])+'</p><p>'+e(a['semchat'])+'</p></details>') if 'reservado' in a else ''
 checks=''.join(f'<li><label><input type="checkbox" data-ptask="{i}"><span>{e(c)}</span></label></li>' for i,c in enumerate(a['checks'],1))
 s+=f'''<section class="practice" data-mode="{mode}"><p class="pk">Pratique agora <span class="pcount">0/3</span></p><h3 class="ph">{e(a['pratica'])}</h3>
<p class="pgoal">Cerca de 10 minutos, no celular, computador ou papel. Pronto quando você consegue {e(a['promessa'])}</p>
<p class="psafe">Use materiais fictícios. Não envie dados pessoais nem mensagens reais. Se algo sair estranho, compare com a referência e registre a falha.</p>
<div class="pcodewrap"><button class="pcopy" type="button">copiar</button><pre class="pcode">{e(a['molde'])}</pre></div><ol class="psteps">{checks}</ol>{reserved}
<details class="gabarito"><summary>Conferir o resultado esperado</summary><p>{e(a['gabarito'])}</p></details><p class="pdone">Capacidade praticada: {e(a['promessa'])}</p></section>
<div class="fecho"><div class="cola"><p class="k">Cola da aula</p><h3>{e(a['pratica'])}</h3><ol>{''.join('<li><span>'+e(r)+'</span></li>' for r in a['resumo'])}</ol></div>
<div class="next-action"><p class="nak">Seu próximo passo</p><p class="na-win">Você já sabe {e(a['promessa'])}</p><p class="na-action">Guarde o resultado nas suas notas como “RSI · aula {n}”. Se pulou a prática, use o molde desta página.</p><p class="na-hook">{e('Na próxima aula: '+AULAS[n]['titulo']+'.' if n<18 else 'Seu próximo ciclo: escolha uma tarefa pequena e reaplique os critérios que você registrou.')}</p></div></div>
<details class="complementar"><summary>Material complementar<small>Aprofundamento e fontes. Fora do tempo da aula.</small></summary><section class="comp-sec"><h3>{e(a['extra'][0])}</h3><p>{e(a['extra'][1])}</p><h3>Fontes para conferir</h3><ul>{''.join('<li><a href="'+e(FONTES[f][1])+'" target="_blank" rel="noopener">'+e(FONTES[f][0])+'</a></li>' for f in a['fontes'])}</ul><p>Consulta: 25 de setembro de 2026. Exemplos profissionais e números de exercícios são fictícios.</p></section></details>
<nav class="lnav"><a href="#trilha">voltar à trilha</a><a class="next" href="{'#aula-'+str(n+1) if n<18 else '#trilha'}">{'próxima aula' if n<18 else 'rever a trilha'} →</a></nav><p class="aula-pe">Aula {n} · RSI v6.2 · INEMA.CLUB</p></div><script type="application/json" id="cards-{n}">{json.dumps([dict(front=f,back=b) for f,b in a['cartoes']],ensure_ascii=False)}</script></section>'''
 (B/f'aulas/aula-{n}.html').write_text(s+'\n')

lp=(S/'assets/landing-template.html').read_text()
replace={'[Nome do curso]':cfg['titulo'],'[1 frase: o que a pessoa sai fazendo]':'Entenda RSI, leia casos reais e monte um ciclo supervisionado de melhoria com avaliação e limites. Curso aberto e gratuito.','[Nome curto]':'RSI v6.2','[Categoria — ex.: IA no seu trabalho]':'Autoaperfeiçoamento recursivo · RSI v6.2','[Promessa em <em>poucas palavras</em>]':'Entenda a IA que <em>ajuda a melhorar a IA.</em>','[O que a pessoa sai fazendo, em 1–2 frases. Sem vídeo, no seu tempo.]':'Dos conceitos ao seu primeiro ciclo supervisionado. Compare evidências, reconheça limites e teste melhorias em atendimento, educação e documentos.','[N]':'18','[alt da trilha]':cfg['alt_trilha'],'[Resultado 1]':'Entender o mecanismo','[em uma linha, concreto]':'Distinguir revisão de respostas, melhoria do sistema e recursão.','[Resultado 2]':'Julgar as evidências','[Resultado 3]':'Fazer um piloto','[profissão-alvo 1]':'Você atua em gestão ou educação','[resultado]':'avaliar e melhorar rotinas com IA'}
for a,b in replace.items(): lp=lp.replace(a,b)
lp=lp.replace('[…]','Examinar casos reais e organizar uma comparação verificável.',1).replace('[…]','Registrar critérios, resultados, custos e decisão.',1)
lp=lp.replace('18 aulas de ~15 minutos · sem instalar nada · funciona no celular e no computador',f'18 aulas · 6 módulos · cerca de {sum(tempos)} minutos · gratuito · celular e computador')
lp=lp.replace('<h2>As aulas</h2>','<h2>Seis módulos, uma prática por aula</h2>')
lp=lp.replace('<div class="aulas">\n<!--AULAS-->','<div>\n<!--AULAS-->')
lp=lp.replace('começar pela aula 1 →','abrir a trilha →')
lp=lp.replace('</head>','<link rel="canonical" href="https://inematds.github.io/curso-rsi/">\n<meta property="og:image" content="https://inematds.github.io/curso-rsi/capa/capa.png">\n</head>')
lp=lp.replace('</main>','''<section class="l-sec"><h2>Pesquisa com fonte e contexto</h2><p>AlphaEvolve, Darwin Gödel Machine, AI Scientist, DSec e estudos de avaliação. Fontes originais junto de cada aula, consultadas em 25/09/2026.</p><p>Marina e Ícaro são personagens fictícios. As telas ilustram comparações; não apresentam resultados medidos de ferramentas.</p><p>As práticas ensinam melhoria supervisionada. Não prometem criar uma IA autônoma nem treinar um novo modelo.</p><p><a href="docs/pesquisa.md">Ler a pesquisa e as decisões editoriais</a> · <a href="materiais/ficha-experimento.txt" download>Baixar ficha de experimento</a> · <a href="materiais/casos-atendimento.csv" download>Baixar casos de treino</a> · <a href="materiais/conhecimento-aprovado.txt" download>Baixar ficha de conhecimento aprovado</a></p></section></main>''')
if (B/'context/portal.json').exists():
 meta=json.loads((B/'context/portal.json').read_text())
 lp=lp.replace('<!-- inema-backlink:v1 — o link da ficha (/cursos/<id>-<slug>/) entra no cadastro do portal (atualiza-portal) -->', '<!-- inema-backlink:v1 -->'+'<p><a href="'+e(meta['ficha'])+'">Ficha completa deste curso no INEMA.CLUB</a></p>')
(B/'landing.html').write_text(lp)
subprocess.run(['python3',str(S/'scripts/montar-curso.py'),str(B)],check=True)
(B/'index.html').write_text((B/'landing.html').read_text())
(B/'context/curriculo.md').write_text('# Currículo RSI v6.2\n\nPúblico proposto: gestores de pequenas empresas e educadores iniciantes. Conhecimento esperado: leitura, notas e uso básico de chat. Nenhuma programação.\n\nDescoberta perguntada; perfil assumido e comunicado durante a execução. Saída: planejar e avaliar um ciclo supervisionado.\n\nFormato solicitado v6.2; motor local da família v6 inclui refinamento compatível de módulos da v6.3. Não foi alterado.\n\n'+ '\n'.join(f'{i}. **{a["titulo"]}** ({tempos[i-1]} min). Promessa: {a["promessa"]} Tipo: fundamento/aplicação. Gancho: '+(AULAS[i]['titulo'] if i<18 else 'Repetir um piloto próprio.') for i,a in enumerate(AULAS,1)))
print('Conteúdo:',len(AULAS),'aulas;',sum(tempos),'minutos')

# Snapshot before language selectors and course-specific links are injected.
import importlib.util
spec=importlib.util.spec_from_file_location('tradutor_v6',S/'scripts/traduzir-curso.py')
tradutor=importlib.util.module_from_spec(spec);spec.loader.exec_module(tradutor)
(B/'i18n').mkdir(exist_ok=True)
(B/'i18n/unidades-pt.json').write_text(json.dumps(tradutor.unidades(str(B)),ensure_ascii=False,indent=1)+'\n')
