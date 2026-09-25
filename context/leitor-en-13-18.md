# Revisão simulada EN — aulas 13–18

Data: 2026-09-25. Persona: gestora de 47 anos, iniciante, celular, intervalo de 15 minutos. Revisão simulada por agente, **não teste humano real**. Comparação do HTML EN com PT e cache `i18n/en.json`; leitura dos três materiais EN. Captura móvel inspecionada: `/tmp/rsi-en-lesson-17.png` (390 px; página inteira). Figuras dos demais steps avaliadas pelo conteúdo e rótulos HTML, sem presumir inspeção visual dessas capturas.

## Aula 13 — atendimento

- Step 1: em cinco segundos, a ficha comunica referência conhecida versus pergunta sem resposta. Entendo que a política não contém trocas. Sem bloqueio; não pularia a distinção.
- Step 2: os dois rascunhos tornam evidente a promessa inventada. Sem bloqueio; pularia a segunda analogia profissional se estivesse com pressa.
- Step 3: a pergunta de retirada exige verificar o aviso. A figura diferencia pergunta e resposta apoiada. Sem bloqueio.
- Bloqueio real no teste: `refuses until it provides the time` muda o sentido de `recusa até informar o horário`. Correção: `The AI avoids making things up but refuses even to state the opening hours. What is the problem?`.
- Prática autossuficiente: sim, contém política, instruções A/B, desenvolvimento e validação separada, alternativa em papel. Contudo, `What is the time?` pede a hora atual, não horário de atendimento: corrigir para `What are the opening hours?`.
- Promessa cumprida após correção. Nota inicial 8; alvo após aplicação/verificação 9,5. Mudança prioritária: preservar o significado de horário de atendimento e da recusa no teste.

## Aula 14 — educação

- Step 1: texto e objetivo comunicam localizar informação explícita; sem bloqueio.
- Step 2: cartões diferenciam tonelagem inventada e dia apoiado. Entendo em cinco segundos. Sem bloqueio.
- Step 3: cobertura repetida versus três informações explica variedade. Sem bloqueio; pularia a analogia de treinamento profissional, não a comparação.
- Teste: `Increase the score by the way it’s done` é vago; corrigir distrator para `Raise the score for presentation alone.`.
- Aprofundamento: `unnecessary experiences` significa vivências; `unnecessary experiments` preserva o sentido metodológico.
- Prática independente de chat, com texto completo e saída esperada; cabe no intervalo. Promessa cumprida. Nota inicial 9; após correções 9,5. Mudança prioritária: tornar o distrator inequívoco.

## Aula 15 — documentos

- Step 1: anotação e extração explicitam duas pessoas e a lacuna; sem bloqueio.
- Step 2: prazo inventado versus lacuna preservada mostra por que não completar. Sem bloqueio.
- Step 3: critérios por campo permitem conferir pessoa, ação e prazo. Sem bloqueio. Pularia aprofundamento no intervalo.
- Bloqueio semântico na prática: `until Friday` sugere atividade contínua até sexta, enquanto `até sexta` aqui é prazo. Corrigir `Marina will review the inventory by Friday.` e `Marina’s deadline is Friday.` também no feedback.
- Prática autossuficiente, com nota original e quatro campos. A promessa fica comprometida enquanto o próprio prazo-modelo é ambíguo. Nota inicial 8,5; após correção 9,5. Mudança prioritária: `by`, não `until`.

## Aula 16 — implantação

- Step 1: ensaio manual e pergunta de repetição deixam claro o ponto de partida. Pergunta pouco natural: trocar `Frequent repetition makes it worth automating this part?` por `Does frequent repetition make this part worth automating?`.
- Step 2: exigência vaga versus verificável funciona sem jargão adicional. Sem bloqueio.
- Step 3: necessidade delimitada versus pesquisa evita prometer laboratório pronto. Sem bloqueio; pularia aprofundamento durante o intervalo.
- Prática autossuficiente: três casos já fornecem frequência, recursos e revisão; não preciso inventar dados para recomendar um nível. Promessa cumprida. Nota inicial 9; após ajuste 9,5. Mudança prioritária: naturalidade da pergunta decisória. Distratores do teste serão equalizados pelo agente principal.

## Aula 17 — piloto

- Step 1: 40 minutos / 2 por uso = 20 usos é claro e calculável. Sem bloqueio.
- Step 2: teto de três candidatas e regra de validação ficam legíveis na captura. Sem bloqueio. Pularia apenas a nota complementar.
- Step 3: `Mandatory stop` no cartão de parada é circular e omite o critério que falhou. Correção: `Failure to meet a mandatory criterion, excessive cost, or an attempt outside the scope.`.
- Prompt: `change` para troca de mercadoria e `Reservation` para conjunto reservado alteram a ação. Corrigir linha para `Development cases: opening hours, pickup, exchanges, delivery. Held-out cases: public holidays and Sundays.`. Padronizar horário como `9 a.m.–6 p.m.`.
- O alt EN da imagem desta aula cita erroneamente o projeto final da aula 18; PT está correto. Correção exata no JSON entregue. Preservar acento de Ícaro.
- Layout observado: ordem vertical clara, botões e checkbox visíveis, blocos do prompt contidos, figura contextual adequada. A imagem é decorativa/contextual; os diagramas textuais carregam o raciocínio.
- Prática autossuficiente e cálculo correto: 30 min/mês líquidos não recuperam 40 min de preparo no primeiro mês. Promessa cumprida após correções. Nota inicial 8; alvo 9,5. Mudança prioritária: corrigir critérios e grupos do prompt.

## Aula 18 — projeto final

- Step 1: referência e candidata mostram uma única mudança. Sem bloqueio.
- Step 2: registro completo versus captura escolhida explica evidência suficiente. Sem bloqueio.
- Step 3: limite usa `essay`, redação, para `ensaio`, teste. Corrigir `The test does not measure learning or general autonomy.`. Pularia aprofundamento no intervalo.
- Prompt: `swap` é inadequado para troca de mercadoria; corrigir `Development — exchanges:`. `time` vira `opening hours`, e `Reserved — holiday` vira `Held-out — public holiday`.
- Prática autossuficiente: resultados e tempos fornecidos permitem relatório em dez minutos sem depender de execução externa. A soma 8 versus 3 minutos está correta, e a ausência de custo e dados reais é explícita. Promessa cumprida após correções. Nota inicial 8,5; alvo 9,5. Mudança prioritária: termos do experimento sem mudança de sentido.

## Materiais e consistência

`en/materiais/ficha-experimento.txt`, `casos-atendimento.csv` e `resultados.csv` estão integralmente em inglês, sem vazamento PT. O CSV usa `Held-out`, `opening hours`, `exchange` corretamente; alinhar aulas a esse vocabulário evita a impressão de métodos diferentes. Material é autossuficiente, preserva dados fictícios, decisão humana e rollback. Arquivos mantêm nomes PT por compatibilidade de URLs; isso não é conteúdo didático não traduzido.

## Entrega e situação

Correções exatas por chave PT estão em `/tmp/rsi-en-fixes-3.json` (15 entradas); nenhuma alteração foi feita no cache nem no código por este revisor. As notas após correção são metas condicionais; esta rodada **não aprova publicação das aulas 13, 15, 17 e 18 sem aplicar e conferir as correções**. Restam também padronizações globais `reserved` → `held-out` coordenadas pelo agente principal.

## Segunda rodada — aprovação após correções

Conferência real do HTML EN remontado e do cache: as correções semânticas estão presentes nas aulas 13–18. A busca pelos dez fragmentos problemáticos (`refuses until`, `until Friday`, `Mandatory stop`, `Development — swap`, `Development: schedule`, `The essay`, `What is the time?`, `Icaro reserves`, `9h–18h`, `unnecessary experiences`) retornou zero ocorrências nessas seis aulas. O alt da aula 17 descreve agora o piloto correto. `not provided` e `held-out` alinham os textos aos materiais. A captura móvel atualizada da aula 17 foi inspecionada: o critério de parada e o prompt corrigidos continuam contidos e legíveis.

Notas finais de entendimento/aplicação: aula 13 **9,5**; aula 14 **9,5**; aula 15 **9,5**; aula 16 **9,5**; aula 17 **9,5**; aula 18 **9,5**. As seis aulas estão **aprovadas nesta revisão simulada**. As práticas fornecem os dados necessários e as promessas permanecem proporcionais ao que o aluno realmente faz.

Detalhe tipográfico residual comunicado ao agente principal: a substituição do horário deixou `p.m..` no prompt da aula 18; remover o ponto duplicado. Não muda o significado nem impede a prática. Não houve novo teste humano real.
