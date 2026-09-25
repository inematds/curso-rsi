# Revisão final independente de interface — RSI v6.2

## 1. Veredito

Aprovado no escopo visual inspecionado, sem problema material que bloqueie leitura ou acesso ao curso. A aprovação é da composição e do HTML; não substitui os testes funcionais feitos pela implementação. Nenhum arquivo de interface foi alterado nesta revisão.

## 2. Fidelidade ao contrato

As 12 capturas mostram papel, escuro e sépia com Newsreader nos títulos e Inter na interface, coluna central de leitura, cenas editoriais e ações destacadas. A landing apresenta promessa, acesso gratuito, 18 aulas e seis módulos. O curso mantém leitura confortável, controles compactos e promessa por aula. O HTML referencia assets/aula.css e assets/curso.js, conforme o contrato do motor oficial; não foi realizada comparação binária com a distribuição original nesta revisão.

O currículo identifica gestores e educadores iniciantes como hipótese editorial. As cenas de estudo e trabalho são coerentes com esse público e o material é marcado como fictício. Não há razão para redesenhar fontes, callouts ou cabeçalhos em resposta ao gosto genérico do detector. O briefing fixo prevalece sobre essas sugestões.

## 3. Problemas materiais com gravidade

Nenhum problema alto ou médio observado nas capturas. Títulos e parágrafos quebram dentro da largura, botões permanecem visíveis, imagens preservam proporção e a leitura da aula 13 mantém hierarquia nos três temas. A captura da etapa 3 mostra quiz, exemplo comparativo e orientação de recuperação sem sobreposição.

Observação baixa resolvida: conferido no HTML regenerado o texto alternativo da aula 13: “Gestora de papelaria compara dois cartões ao preparar um teste de respostas, diante de prateleiras de materiais.” A descrição agora corresponde à cena no singular. Não foi necessária nova captura, pois somente o atributo alt mudou.

## 4. Evidências verificadas e limites

Inspecionadas individualmente as 12 imagens landing/curso × 390/1440 × papel/escuro/sépia, além de aula-13-step-3.png. Lidos PRODUCT.md, context/curriculo.md, craft-floor.md, context/detector.json, links da landing e HTML da aula 13.

A prática da aula 13 fornece referência fictícia, instruções A/B, perguntas de desenvolvimento, botão de copiar e alternativa de execução em papel. O quiz tem alternativas reais, feedback e aria-live. A landing usa details/summary para módulos e links explícitos para as aulas; não são cards sem destino.

As capturas de curso exibem a aula 13, não a trilha inteira. Portanto acesso aos seis módulos foi examinado estruturalmente no HTML, sem teste de clique independente. Não abri navegador, conforme escopo. Não medi contraste calculado, foco por teclado, persistência, clipboard, zoom, leitores de tela nem estados de erro; não declaro conformidade WCAG integral. Também não certifico toda a altura das páginas a partir de capturas do primeiro viewport. A ausência de overflow se refere às regiões efetivamente vistas.

## 5. Disposição final de achados

| Achado | Quantidade | Disposição | Motivo |
|---|---:|---|---|
| overused-font | 2 | Aceito pelo contrato | Inter foi solicitado junto de Newsreader; há contraste claro entre interface e títulos. |
| flat-type-hierarchy | 1 | Não confirmado visualmente | Hero, corpo e metadados apresentam escala e peso claramente diferentes nas seis capturas da landing. |
| dark-glow | 2 | Aceito no escopo do motor | Nenhum halo prejudicial à leitura observado; manter motor oficial solicitado. |
| side-tab | 36 | Aceito pelo contrato | Callouts pertencem ao template; não se sobrepõem nem substituem instruções textuais. |
| border-accent-on-rounded | 18 | Aceito pelo contrato | Tratamento recorrente do template, sem defeito funcional observado. |
| Texto alternativo genérico da aula 13 | 1 | Resolvido, conferido no HTML | Descrição específica da gestora com cartões diante de prateleiras; nenhuma mudança visual. |
| Overflow/sobreposição em capturas | 0 observado | Aprovado no recorte | Conteúdo contido em 390 e 1440 px nos três temas inspecionados. |
| Interação e acessibilidade completa | Não reexecutadas | Fora desta revisão independente | Revisão limitada a capturas e HTML, sem navegador. |
