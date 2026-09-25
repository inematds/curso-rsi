# Revisão simulada EN — aulas 1–6

Persona: gestora de 34 anos, iniciante em IA, usa celular no intervalo de 15 minutos. Revisão simulada por agente; não é teste humano real. Texto EN comparado com PT e cache `i18n/en.json`; capturas móveis `/tmp/rsi-en-lesson-1.png` e `/tmp/rsi-en-lesson-4.png` inspecionadas. Data: 2026-09-25.

## Resultado da primeira rodada (superado pela reavaliação final abaixo)

A primeira versão foi reprovada até corrigir os erros abaixo. O layout móvel se mantém legível, com hierarquia e controles identificáveis. A prática é fornecida integralmente em todas as seis aulas; o problema é fidelidade da tradução, não falta de material. Não se deve registrar aprovação >=9 antes de regenerar e conferir as correções.

## Aula 1 — nota 8/10

- Step 1: em cinco segundos, a ficha deixa claro “texto revisado versus processo revisado”. Não travaria; não pularia.
- Step 2: os rótulos “Unclear request / Verifiable request” comunicam pedido verificável. Travaria na ação: PT manda **contar** perguntas; EN manda **fazer** perguntas. Isso retira a medida de qualidade. Pularia apenas a legenda repetida de ilustração.
- Step 3: os rótulos “Control question / Evidence needed” comunicam conferir o que mudou. “A version you praise” atribui o elogio ao leitor, perdendo a ideia central de autoelogio da versão. Não pularia a explicação.
- Prática: autossuficiente, três situações e gabarito. Promessa alcançável após correções. Mudança que mais aumenta a nota: preservar a operação **count** do critério de comparação.

Correções exatas:

1. `Compare two instructions using the same three texts. Ask questions that can be answered using only each individual text.` → `Compare two instructions using the same three texts. Count the questions that can be answered using only each text.`
2. `A version you praise doesn’t prove improvement.` → `A version that praises itself does not prove improvement.`
3. `Three levels of affirmation` → `Three levels of claims`.
4. Padronizar `recursiveness` como `recursion` nos exemplos e na cola; manter `recursive improvement` quando adjetivo.

## Aula 2 — nota 8.8/10

- Step 1: figura “No reference / With reference” comunica que a resposta depende do texto fornecido. “your parameters” parece falar de parâmetros do aluno. Não pularia.
- Step 2: “Incomplete record / Useful record” comunica informação datada e verificável. Sem travamento; pularia a legenda repetida.
- Step 3: ficha “Small change / Deep change” distingue instrução de treinamento. A explicação não exige conhecimento técnico extra, mas troca Ícaro por “you” no meio do exemplo.
- Prática: plenamente autossuficiente, três casos e gabarito. Promessa cumprida após ajuste de sujeitos. Maior correção: explicitar parâmetros **do modelo**.

Correções exatas:

1. `That doesn’t mean your parameters were updated.` → `That does not mean the model’s parameters were updated.`
2. `Icaro wants the questions to cite the supporting excerpt. First, you change the instruction and measure; you don’t need to start by training a model.` → `Ícaro wants the questions to cite the supporting excerpt. He first changes the instruction and measures the result; he does not need to start by training a model.`
3. `A false note that gets retrieved can often spread the same error.` → `A false note retrieved repeatedly can spread the same error.`

## Aula 3 — nota 8/10

- Step 1: cartões “Broad statement / Concrete question” orientam procurar quais etapas foram automatizadas. A definição de evidence usa “Registration” e “your measurement”; isso distrai sobre quem mediu. Não pularia.
- Step 2: a ficha contrapõe quantidade e qualidade de exercícios corretamente. “your students” muda os alunos de Ícaro para os meus; pequena perda de clareza. Não pularia.
- Step 3: “Observed / Open” comunica resultado conhecido e alcance ainda desconhecido. “guaranteed calendar” é literal demais; penso em agenda em vez de previsão. Pularia o complementar no intervalo.
- Prática: caso completo e executável sem pesquisa externa. Gabarito ainda contém `Teste da Escola Aurora`, diferindo do título em inglês da prática. A promessa deve ser uma afirmação, não pergunta. Maior mudança: uniformizar título e definição de evidência.

Correções exatas:

1. `Can you fill in an evidence sheet for a claim about RSI?` → `You can fill in an evidence sheet for a claim about RSI.`
2. `Registration that allows you to verify a statement. It can be an experiment, your measurement, and its conditions.` → `A record that lets you verify a claim. It may include an experiment, its measurements, and its conditions.`
3. `A video can present good ideas, but your narration does not replace the document.` → `A video can present good ideas, but its narration does not replace the original document.`
4. `That doesn’t tell you how many are correct or help your students.` → `That does not tell you how many are correct or help his students.`
5. `It doesn’t become a guaranteed calendar.` → `It does not establish a guaranteed timeline.`
6. `Marina agrees to test a new routine. It doesn’t change the whole company because of a deadline prediction.` → `Marina agrees to test a new routine. She does not change the whole company because of a predicted deadline.`
7. `Title: Teste da Escola Aurora.` → `Title: Escola Aurora test.`
8. `a real source from the complement` → `a real source in the additional material`.

## Aula 4 — nota 7/10

- Step 1: ficha “No reference / With reference” mostra comparar com uma base. A figura é clara; sem travamento. Não pularia.
- Step 2: “Mixed changes / Isolated change” mostra mudar uma variável. Falta sujeito em “Keeps the text”, mas entendo pelo contexto. Não pularia.
- Step 3: “Essay / Validation” faz parecer uma redação escolar. O falso cognato reaparece na explicação e quiz. É bloqueante para entender ensaio versus validação. A orientação parece dizer que Marina inventou o prazo, em vez da candidata.
- Prática: oito etapas prontas para preencher, caso fechado, condição de parada e responsável. Gabarito perde o sujeito A e a afirmação de falha nos dois critérios. Maior mudança: substituir **essay** por **trial** e recuperar a medida do gabarito. Promessa prejudicada até isso ser corrigido.

Correções exatas:

1. `A candidate can pass in the essay and fail in validation.` → `A candidate can pass the trial and fail validation.`
2. Rótulo `Essay` → `Trial`.
3. `The candidate improved in the essay. What’s the next step?` → `The candidate improved in the trial. What is the next step?`
4. `Marina checks the new questions before saving the orientation. If she invents a deadline, the candidate doesn’t go into use.` → `Marina checks new questions before saving the guidance. If the candidate invents a deadline, it is not put into use.`
5. `Measure: the flaw against both criteria.` → `Measure: A fails both criteria.`
6. `Orientation A: respond politely.` → `Instruction A: respond politely.`
7. `Keeps the text, the number of questions, and the previous criteria.` → `He keeps the text, the number of questions, and the previous criteria unchanged.`

## Aula 5 — nota 7/10

- Step 1: “Proposal / Evaluation” comunica criar e conferir. Entradas e saídas suficientes; sem travamento. Não pularia.
- Step 2: “Fragile check / Useful check” distingue concordância de evidência. “hiding them in a note” perde a ideia de esconder divergência numa **nota numérica**. Não pularia.
- Step 3: ficha de permissões comunica limites, mas `Change notes` contradiz `change grades` do texto. Prática manda “Separate the authorization proposal”, em vez de separar proposta **da** autorização. Isto compromete a competência prometida.
- Prática: possui casos, três papéis e campos necessários. Pode ser feita sem software, mas exige corrigir a instrução ambígua. Maior mudança: separar explicitamente proposta de aprovação.

Correções exatas:

1. `For subjective results, record disagreements instead of hiding them in a note.` → `For subjective results, record disagreements instead of hiding them in a score.`
2. `It can’t change grades or communicate families.` → `It cannot change grades or contact families.`
3. `Change notes or send messages to people.` → `Change grades or send messages to people.`
4. `Separate the authorization proposal.` → `Separate the proposal from the authorization.`
5. `proposer, evaluator, final responsible` → `proposer, evaluator, final decision-maker`.
6. `Outside the test` → `Outside the trial` para harmonizar a nomenclatura de ensaio.

## Aula 6 — nota 8/10

- Step 1: cartões “Vague record / Useful record” mostram registrar a mudança, casos e resultado. “experience” alterna com “experiment”, podendo parecer relato pessoal. Não pularia.
- Step 2: ficha “Symptom / Proposed correction” mostra o erro e a menor correção. Sem travamento; pularia somente a legenda repetida.
- Step 3: “Current use / Attempts file” separa o que está aprovado do histórico. “to comply” perde o contexto de atender clientes. Não pularia.
- Prática: respostas A e B, referência, critérios e campos presentes. O gabarito “The failure is because it states an uninformed opening” é obscuro e omite que **A** falhou. Maior mudança: deixar explícito qual resposta falhou e por quê. Promessa alcançável após correção.

Correções exatas:

1. `Save experiences, including the ones that failed` → `Save experiments, including the ones that failed` (atualizar também a antecipação na aula 5).
2. `Marina keeps “current guidance” and “attempts.” The team checks only the first one to comply.` → `Marina keeps “current guidance” and “attempts.” The team consults only the first when serving customers.`
3. `The failure is because it states an uninformed opening.` → `A fails because it claims the store is open without supporting information.`
4. `Review after reserved cases.` → `Review after testing the held-out cases.`
5. `Closed and fictional case.` → `A complete fictional case.`

## Consistência transversal

- Usar `held-out cases` para `casos reservados`; `reserved cases` soa tradução literal, embora a definição no curso permita entender.
- Usar `trial` para `ensaio`, nunca `essay`; `experiment` para experiência controlada; `guidance` ou `instruction` para orientação, nunca `orientation` neste contexto.
- `Educational record to compare; it’s not execution of a tool.` é compreensível, mas naturalizar como `Illustrative comparison; this is not a live tool run.` melhora as figuras repetidas.
- `Escola Aurora`, `Ícaro` e `Marina` podem permanecer como nomes próprios; `Teste da` no gabarito não é nome próprio e precisa tradução.
- Capturas examinadas não mostram recorte horizontal ou sobreposição. Não inferir tamanho de fonte pela miniatura da captura longa; sua função aqui é verificar composição e apresentação dos passos.


## Reavaliação final após correções — 2026-09-25

Relidos os 18 steps, seis práticas, promessas e gabaritos de `en/curso.html` regenerado. Cache conferido contra as 30 correções sugeridas; variantes `test` e `held-out` adotadas pelo responsável são adequadas. Captura móvel da aula 4 regenerada inspecionada: a figura agora diz “Test / Validation” e preserva a composição sem sobreposições.

| Aula | Nota final simulada | Evidência da correção / capacidade de uso |
| --- | --- | --- |
| 1 | 9.3/10 | Figura manda **Count the questions**; autoelogio da versão recuperado. Os três steps permitem classificar A/B/C sem ajuda. |
| 2 | 9.4/10 | Parâmetros atribuídos ao modelo; exemplo de Ícaro conserva o sujeito. Os três casos distinguem contexto, memória e treinamento. |
| 3 | 9.3/10 | Evidência definida como registro; título da prática coincide com gabarito; promessa afirmativa e distinção previsão/resultado preservadas. |
| 4 | 9.2/10 | `Essay` removido dos steps, figura e quiz; gabarito registra **A fails both criteria**. Consigo preencher as oito etapas com o caso fornecido. |
| 5 | 9.4/10 | `score`, `grades`, contato com famílias e separação proposta/autorização corrigidos. A ficha permite distribuir os três papéis e limites. |
| 6 | 9.2/10 | Experimentos nomeados corretamente, atendimento aos clientes recuperado e falha da resposta A explícita. Consigo registrar e recuperar a versão anterior. |

**Aprovadas na revisão simulada.** Todos os travamentos de sentido apontados na primeira rodada foram resolvidos. As práticas são autossuficientes; não preciso instalar ferramentas nem procurar um caso externo. Pularia apenas legendas repetidas e material complementar durante o intervalo de 15 minutos. As promessas são cumpridas dentro do escopo dos exemplos fictícios, sem afirmar demonstração real de RSI.

Polimento residual, sem bloqueio de compreensão:

- Aula 4, prática: `Reserved case to check later` → `Held-out case to check later` (normalização escapou por ser singular e iniciar em maiúscula).
- Aula 6, apoio: `Copy the closed case from the practice into the notes.` → `Copy the complete case from the practice into your notes.`; gabarito: `Review after held-out cases.` → `Review after testing the held-out cases.`.
- Aula 1 ainda alterna `recursiveness` e `recursion`; ambos são compreensíveis, preferir o segundo.
- Glossário relido: definições relevantes às aulas 1–6 preservam sentido e links. Melhorar fluência geral de `Separate examples before the changes and used afterward to evaluate the candidate.` para `Examples set aside before making changes and used afterward to evaluate the candidate.`; em bottleneck, preferir `system’s overall performance` a `group’s overall performance`.

Essas notas são avaliações qualitativas de um leitor simulado, não resultados de participantes humanos nem medição de aprendizagem.
