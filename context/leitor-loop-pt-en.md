# Leitura simulada — LOOP-R e aprovação reutilizável (PT/EN)

Data: 2026-09-25. Persona: gestora iniciante de 34 anos, com 15 minutos por sessão e familiaridade com chat de IA. Revisão textual de `curso.html`, `en/curso.html` e da edição em `scripts/conteudo.py`, aulas 4, 5, 6, 13, 17 e 18. Não é teste com participante humano. Não inclui espanhol nem verificação visual desta edição.

## Parecer

**PT aprovado: a distinção solicitada ficou concreta e utilizável. EN requer as correções de fidelidade e os complementos de tradução listados abaixo antes da aprovação.** JSON corretivo entregue em `/tmp/rsi-loop-en-fixes.json` (19 chaves PT→EN, inclusive HTML preservado). Não alterei código nem cache.

Como iniciante, agora entendo quatro decisões diferentes:

1. Avaliar uma candidata ainda não autoriza adotá-la.
2. Aprovar e promover registra qual regra ficou vigente, para quais usos e até quando.
3. Reutilizar essa regra válida no mesmo escopo dispensa pedir a mesma aprovação. Conferir fonte, escopo e validade não é pedir aprovação novamente.
4. Mudar a regra ou ampliar as ações exige decisão própria; enviar uma mensagem não está incluído numa autorização limitada a rascunhos.

O curso também explica que aprovação não é verdade absoluta, uma resposta isolada não implica regra geral, persistência precisa ser implementada e uma regra aprovada errada pode propagar o erro. Revogação retira a regra do uso sem apagar o histórico. A revisão de cada resposta, quando exigida pelo piloto, continua existindo e não se confunde com aprovar a mesma regra novamente.

## Avaliação por aula

| Aula | PT | EN antes da correção | Evidência de entendimento e ponto de atenção |
| --- | --- | --- | --- |
| 4 | 9.3 | 7.5 | Steps 1–2 mantêm referência e mudança isolada. Step 3 agora distingue candidata e regra vigente na figura. A prática registra versão, responsável e usos autorizados. EN ainda tem definição e complementar inteiros em PT; “makes the current version” é incompleto. |
| 5 | 9.4 | 9.1 | Papéis e critérios dos steps 1–2 continuam claros. Step 3 e figura mostram rascunho permitido versus envio não autorizado. Prática exige separar regra persistente de ação externa. Não encontrei bloqueio novo de sentido. |
| 6 | 9.6 | 8.0 | É a aula central: H1/P1, mudança para P2 e envio formam três situações distintas. Figura 1 separa teste de aprovação, figura 2 separa reuso de envio, figura 3 trata erro/revogação. EN traduz “Aprove pensando...” como “Use it...”, perdendo o foco na decisão de aprovar; gabarito troca envio por pedido. |
| 13 | 9.2 | 9.0 | Referência pequena, comparação e validação preservadas. A cola deixa explícito que aprovar regra não amplia o escopo. Perguntar por informação faltante à loja não é reabrir autorização de uso da regra. Não travaria na prática. |
| 17 | 9.3 | 8.2 | Custos, limites e reversão continuam compreensíveis; ficha adiciona conhecimento, escopo, validade e revogador. EN distorce retirada para “removed/removal” e condição de parada para “it stops you from...”, que parece uma prevenção automática. |
| 18 | 9.4 | 9.0 | A decisão final inclui conhecimento aceito e usos equivalentes, sem eliminar revisão pedagógica ou do piloto. Gabarito não trata dados fictícios como comprovação real. EN compreensível, mas melhorar “Decide what else...” e soma dos tempos para evitar leitura de custo incremental. |

### Práticas, promessa e pontos em que pararia

- **Aula 4:** faço as oito etapas no papel com o caso fornecido. Entendo promoção como adoção registrada. No EN, pararia no complementar em português. A promessa é cumprida em PT.
- **Aula 5:** preencho os três papéis e consigo indicar rascunho já autorizado e envio ainda não autorizado. A prática não depende de programação. Promessa cumprida em ambos.
- **Aula 6:** classifico A como reuso, B como suspensão/revisão e C como nova ação. Fonte, evidência, data, responsável, validade e revogação estão disponíveis. No EN, “the request requires its own authorization” me faria hesitar se pedir ao sistema já exige nova autorização; o correto é o **envio**. Promessa cumprida em PT, condicionada à correção em EN.
- **Aula 13:** consigo comparar rascunhos e só depois abrir validação. O bloqueio a aprovar cedo é sobre uma candidata ainda não avaliada, não sobre repetir aprovação já concedida. Promessa cumprida.
- **Aula 17:** consigo calcular 20 usos sem manutenção e explicar o saldo mensal de 30 minutos. Sei quem decide, quando parar e qual regra volta. EN precisa preservar a ação de **parar quando ocorrer erro**, em vez de prometer que o sistema impedirá o erro.
- **Aula 18:** consigo entregar relatório com decisão limitada, escopo, fonte e revogação, indicando que os resultados foram fornecidos. A revisão das respostas continua explícita, sem nova aprovação da regra a cada uso. Promessa cumprida.

Em uma sessão curta, pularia os complementares e legendas repetidas. Não pularia as figuras da aula 6 nem o gabarito do projeto final. As figuras textuais e rótulos, lidos isoladamente, comunicam a distinção pretendida; não fiz nova avaliação visual por captura nesta rodada.

## Correções EN entregues

Bloqueantes para esta edição:

- Traduzir a nova definição LOOP-R, incluindo `data-def` e glossário; traduzir complementar atualizado e título da fonte “guia do método”.
- `Validation confirms...` → `Validation checks...` para não pressupor resultado favorável; promoção torna a versão aprovada vigente.
- `H1 passed a test, but you haven’t received authorization yet.` → `H1 passed a test, but has not yet been authorized for use.`
- `Use it with the next uses in mind` → `Approve with future uses in mind`.
- `combined criteria` → `agreed criteria` (critérios combinados no sentido de acordados).
- `C: the request requires its own authorization.` → `C: sending requires its own authorization.`
- Em política P2, Marina revisa a referência; o sujeito não deve mudar para “you”.
- Aula 17: retirada → pickup; casos de reserva → held-out cases; parar se inventar informação/atingir teto, sem alegar prevenção automática.

Polimento incluído no mesmo JSON: título “Also decide what can be reused”, termos held-out, review times, soma explícita de 8 e 3 minutos, correção de “your answer” para “its answer” no retorno automático.

Nenhuma correção obrigatória de conteúdo PT foi identificada. Aprovação EN final depende de regenerar a partir das correções e conferir ausência dos vazamentos e erros listados. As notas são qualitativas de um leitor simulado, não medidas de aprendizagem humana.


## Fechamento após regeneração e rodada final

EN aulas 4 e 6 verificadas após as correções: definições e complemento traduzidos, promoção torna a versão aprovada vigente, cuidado ao aprovar preservado, critérios acordados e autorização específica de envio corretos. Notas finais simuladas: aula 4 **9.4/10**, aula 6 **9.5/10**. EN aula 5 teve o último resíduo `notes` corrigido para `grades`, com `contact families`; reavaliada em **9.4/10**. As três aulas estão aprovadas na revisão simulada. Evidência complementar em `context/leitor-es-1-6.md`, rodada final.
