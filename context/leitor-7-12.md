# Revisão de leitor simulado — aulas 7–12

Data: 25/09/2026. Persona simulada: educador de 58 anos, usa e-mail e chat, não programa, lê no celular num intervalo de 15 minutos. **Não houve participante humano real nem medição de tempo de aprendizagem.** Notas são julgamento editorial simulado, não resultados de pesquisa com usuários.

Método: leitura integral dos seis HTML e inspeção por `view_image` das 24 capturas correspondentes (abertura no celular e steps 1–3 de cada aula). Seguida a referência `TESTE-HUMANO.md` do formato-curso-v6. A seção factual abaixo verifica delimitação e rastreabilidade interna; não afirma nova consulta aos endereços externos. Nenhuma aula foi editada nesta rodada.

## Observação visual transversal

A letra, o contraste e a largura parecem adequados ao celular. A abertura usa ilustração acolhedora, mas genérica: olhar somente a imagem não ensina o conceito específico. Nos steps predominam fichas textuais; o entendimento em cinco segundos vem dos rótulos e frases, não de representação visual da relação. Seria particularmente útil desenhar os tempos da aula 7 e a separação dos conjuntos da aula 10.

Em várias capturas de steps, o cabeçalho aparece sobre título ou trecho de parágrafo, às vezes no meio da imagem. **Não é possível distinguir por imagem se é sobreposição real ou efeito da captura de elemento com cabeçalho fixo.** Conferir no viewport durante rolagem e navegação por âncora; se real, ajustar deslocamento das âncoras/cabeçalho. Não declarar corrigido com base somente nesses recortes.

## Aula 7 — AlphaEvolve

| Step | Ideia em 5 segundos e acerto | Trava simulada | O que pularia |
|---|---|---|---|
| 1 | “Rápido só vale se continuar correto.” Acerto pelo par objetivo incompleto/completo. | “Variantes de programas” não informa se eu precisarei programar. A analogia ajuda, mas chega depois. | A enumeração técnica de componentes do AlphaEvolve. |
| 2 | “23% numa peça dá apenas 1% no conjunto.” Acerto na distinção, sem saber a conta do caso real. | “Aceleração” e “redução de tempo” podem parecer a mesma operação percentual. Não tentaria deduzir o 1% a partir do 23%. | Nenhum dos dois registros; são curtos e essenciais. |
| 3 | “Conte também o tempo para conferir.” Acerto, desde que abra a segunda aba. | “Transfira a lógica” é abstrato, embora o exemplo esclareça. | O aviso repetido de que a ficha não executa ferramenta. |

Prática: executável no papel; obtenho 27 minutos, 3 minutos poupados e 10%. Uma calculadora ajuda, e o gabarito permite conferir. Promessa: cumprida para distinguir ganho local e total; explicar o caso real ainda pede uma frase sobre a operação otimizada. Nota: **9/10**. Mudança prioritária: acrescentar a conta `3 ÷ 30 × 100 = 10%` e uma faixa visual 24 + 6 → 24 + 3. Trava adicional a resolver: dizer “Você aplicará o raciocínio no papel; não precisa programar”.

Rigor: números reais estão atribuídos à DeepMind; a conta de 50%/10% está explicitamente marcada como analogia fictícia. Boa separação. Preservar a distinção entre velocidade da operação e redução do tempo total; não dizer que a primeira equivale a 23% de redução de tempo. O link é primário, mas a exatidão do trecho externo precisa estar coberta pela auditoria de fontes do curso.

## Aula 8 — Darwin Gödel Machine

| Step | Ideia em 5 segundos e acerto | Trava simulada | O que pularia |
|---|---|---|---|
| 1 | “Muda a organização do agente, não todo o modelo.” Acerto parcial; a figura continua técnica. | “Parâmetros” e “código que organiza o agente”: não sei visualizar a diferença. | A discussão sobre treinar todos os parâmetros. |
| 2 | “Guardar uma ideia não é aprová-la.” Acerto com os dois rótulos. | “Candidata” pode significar resposta, instrução ou programa; a analogia troca agentes por respostas. | O aviso repetido nas fichas. |
| 3 | “Dizer aprovado não basta.” Acerto. | “Resultados preservados” ainda não mostra o que guardar concretamente. | Parte do texto abstrato sobre alcance das tarefas, se estiver com pressa. |

Prática: consigo rejeitar B para uso e guardar A/C para comparar. **Não consigo propor um teste que reprove A por demora sem limite de tempo, nem C sem uma referência completa que torne desnecessária a pergunta.** Promessa parcialmente cumprida: diversidade fica clara, objeto alterado menos. Nota: **8/10**. Mudança prioritária: fornecer um caso-base com resposta esperada e tempo aceitável, mais exemplos de falha: A ultrapassa o tempo; B inventa; C pede um dado já fornecido. Resolver demais travas: explicar parâmetros como valores aprendidos no treinamento; definir candidata como versão do agente; indicar guardar entrada, saída e critério aplicado.

Rigor: boa distinção entre alteração do agente e retreinamento do modelo. Separação explícita entre evidência empírica e prova geral é útil. A analogia com respostas deve ser apresentada como analogia de preservar alternativas, para não levar o leitor a achar que a DGM só reescreve mensagens. Artigo e página dos autores são rastreáveis; sem verificação externa nova nesta revisão.

## Aula 9 — Pesquisa automatizada

| Step | Ideia em 5 segundos e acerto | Trava simulada | O que pularia |
|---|---|---|---|
| 1 | “Automatizar uma experiência não comprova toda a ciência.” Acerto parcial: a aba inicial não mostra a limitação até tocar. | “ICLR” e “oficina” não situam claramente a hierarquia de evento para leigo. | A sigla, preservando a ressalva sobre conferência principal. |
| 2 | “Ter bancada pronta não é ter experimento útil.” Acerto, boa analogia. | “Infraestrutura” e “tarefas de agentes em escala” continuam amplos: qual é o produto concreto? | A sigla DSec se não houver exemplo de entrada/saída. |
| 3 | “Muita atividade não significa contribuição.” Acerto. | A terceira iniciativa prometida não ganha nome neste step; o texto fala genericamente de relatos. | A pergunta sobre quem define objetivos se não vier ligada ao terceiro caso. |

Prática: **não é autossuficiente em dez minutos**. Exige abrir fontes científicas externas para preencher quatro campos de três iniciativas. A terceira muda de “pesquisa com agentes” no comando para “uso interno de agentes” no gabarito. Promessa parcialmente cumprida: distingo funções, não comparo três iniciativas suficientemente identificadas. Nota: **7/10**. Mudança prioritária: incluir três fichas em português com nome, função, entradas, avaliador e limite; nomear a terceira como relato de uso interno de agentes pela OpenAI, vinculado à fonte correspondente. Fazer a prática usar essas fichas e deixar a leitura externa complementar. Resolver termos: “oficina científica vinculada ao evento, diferente da conferência principal”; exemplo de infraestrutura como ambiente de execução com recursos e registros.

Rigor: a aceitação na oficina está cuidadosamente delimitada; não é vendida como validação universal. A declaração da OpenAI é corretamente atribuída à organização e à data, sem alegar inspeção de todos os laboratórios. **DSec e os dois textos de setembro de 2026 exigem confirmação documental na auditoria principal**: o HTML contém links, mas um link/data de consulta não prova sozinho que o conteúdo sustenta a afirmação. Não marcar estes relatos como falsos nem como verificados nesta revisão. Separar explicitamente “relato organizacional” de “avaliação independente”.

## Aula 10 — Avaliação com casos reservados

| Step | Ideia em 5 segundos e acerto | Trava simulada | O que pularia |
|---|---|---|---|
| 1 | “Teste também perguntas sem resposta disponível.” Acerto. | Falta a referência fictícia de horários para eu criar critérios de verdade. | Nada nos dois casos, são familiares. |
| 2 | “Alguns textos ficam fora das revisões.” Acerto. | Guardar onde? Se uso a mesma conversa do chat, o modelo já viu os casos? Preciso de uma instrução operacional. | A segunda menção abstrata à troca de casos, se não mostrar como registrá-la. |
| 3 | “Não inventar é obrigatório; ser curto é preferência.” Acerto ao alternar fichas. | “Registre por caso” pede formato que não está mostrado. | Advertência final repetida sobre generalização, após compreendê-la. |

Prática: consigo separar quatro e dois no papel. Preparar seis textos do zero toma o intervalo inteiro; escolher perguntas de loja é mais viável, mas falta documento-base. Promessa parcialmente cumprida porque preparo casos sem necessariamente saber executá-los/registrá-los. Nota: **8/10**. Mudança prioritária: dar um horário fictício e seis perguntas prontas, com uma linha preenchida de avaliação. Resolver demais travas: guardar os dois casos em nota separada, não colá-los durante os ajustes, e abrir comparação final somente após congelar a orientação; informar que voltar a ajustar exige novos casos reservados.

Rigor: excelente delimitação da amostra de seis como didática e do uso repetido dos casos. O complemento METR define uma medida diferente; não deve parecer ser a fonte direta de toda a metodologia de separação. Identificar a metodologia como roteiro didático autoral e METR como exemplo de cautela na interpretação de métricas.

## Aula 11 — Atalhos na avaliação

| Step | Ideia em 5 segundos e acerto | Trava simulada | O que pularia |
|---|---|---|---|
| 1 | “Curto não pode perder a informação necessária.” Acerto. | “Manipulação da recompensa” parece intenção humana; definição e complemento ajudam a desfazer. | O termo técnico depois de entender o exemplo. |
| 2 | “Conferido precisa de prova.” Acerto, mas depende da segunda aba. | A ficha cita a segunda frase sem exibir texto; ainda não posso fazer a conferência ali. | O aviso de simulação já visto muitas vezes. |
| 3 | “Se a regra muda, compare tudo novamente.” Acerto. | “Preserve critérios fora do alcance” soa como configuração técnica, mas a prática pode ser manual. | Nada no exemplo, corresponde à avaliação escolar. |

Prática: executável agora; associo A a questões distintas, B a conteúdo obrigatório e C a trecho verificável. Promessa cumprida. Nota: **9/10**. Mudança prioritária: mostrar duas frases de referência e uma resposta conferida, tornando a evidência inspecionável no próprio step. Resolver demais travas com “No seu ensaio, basta guardar o gabarito numa nota separada e conferir pessoalmente; o termo descreve o comportamento, não uma intenção humana”.

Rigor: o texto não antropomorfiza como conclusão científica; delimita experimentos controlados e relatos. A afirmação “quem é avaliado não controla o gabarito” funciona como recomendação para o ensaio, sem prometer que resolve todo o problema. Duas fontes primárias identificadas, sem consulta externa nova nesta rodada.

## Aula 12 — Dados gerados

| Step | Ideia em 5 segundos e acerto | Trava simulada | O que pularia |
|---|---|---|---|
| 1 | “Dez perguntas iguais não cobrem dez ideias.” Acerto ao alternar fichas. | “Cobertura” ganha sentido no exemplo, mas fica menos claro antes de abrir a segunda aba. | O aviso repetido de ilustração. |
| 2 | “Conferir com a fonte original, não com a resposta anterior.” Acerto pela analogia. | “Respostas novas aprendem” pode sugerir que usar chat já retreina seu modelo. Treino recursivo e reciclagem de material são diferentes. | A expressão técnica treino recursivo, se não houver explicação curta. |
| 3 | “A IA sugere problemas e eu confiro.” Acerto. | “Confira uma amostra humana” é ambíguo: pessoas como amostra ou exemplos revisados por pessoa? | Nada da decisão conferida, é útil ao professor. |

Prática: possível, mas exige inventar texto e cinco perguntas antes de auditar. Se eu escrever cinco boas perguntas diferentes, pode não existir a repetição que sou orientado a substituir. Promessa parcialmente cumprida porque não há conjunto garantido para corrigir. Nota: **8/10**. Mudança prioritária: fornecer texto curto e cinco perguntas, incluindo uma repetida e uma sem resposta no texto; pedir que o leitor marque origem/ideia/resposta e corrija uma delas. Resolver demais travas: “Peça a uma pessoa que confira uma parte dos exemplos” e “No estudo, novos modelos são treinados com dados gerados; aqui fazemos apenas uma analogia com revisar materiais”.

Rigor: boa ressalva de que dado sintético não provoca necessariamente colapso; boa separação das duas linhas de pesquisa. A alegação específica de preferência por textos longos merece referência direta ao estudo que a demonstra, pois os dois links listados não identificam de forma evidente esse resultado. O quiz diz “corrigir a referência” mesmo que o erro possa estar nos exemplos e a referência correta: mudar para “Conferir a referência e corrigir os exemplos”. Isso evita ensinar a modificar a fonte para acomodar saídas erradas.

## Prioridades para a próxima rodada

1. Aula 9: comparação autossuficiente e terceiro caso nomeado; manter pendência factual explícita até a auditoria documental.
2. Aula 8: caso-base e critérios observáveis para testar A/B/C.
3. Aulas 10 e 12: fornecer material fictício pronto para a primeira prática; autoria livre fica opcional.
4. Aula 12: ajustar frase ambígua sobre amostra humana, analogia com treino e resposta do quiz.
5. Todas: conferir cabeçalho no viewport real; não usar recortes como prova de bug sem reproduzi-lo.

Notas inferiores a 9 precisam ajuste conforme a skill. As propostas acima não foram implementadas nem reavaliadas nesta rodada. Não converter estas notas em comprovação de aprendizagem humana.

## Reavaliação final após correções

Releitura dos HTML reconstruídos das aulas 8, 9, 10 e 12 em 25/09/2026. Esta seção substitui o veredito de pendência didática da primeira rodada; o histórico acima fica preservado. Continua sendo avaliação simulada, sem teste com pessoas. Não houve nova auditoria externa de fontes nesta etapa.

| Aula | Evidência conferida no HTML atualizado | Nota final | Veredito |
|---|---|---|---|
| 7 | Sem mudança necessária para o bloqueio de prática; conta e resultado já eram executáveis. | 9/10 | Aprovada na revisão simulada. |
| 8 | Referência de horário, pergunta comum e difícil, resultados A/B/C e gabarito permitem observar fidelidade e utilidade. C já tem falha concreta no caso comum; B inventa abertura. | 9/10 | Bloqueio da prática resolvido; consigo comparar e escolher uma candidata para validação. |
| 9 | Três fichas em português, terceiro caso nomeado como relato interno da OpenAI, campos comparáveis e leitura externa opcional. Gabarito distingue evidência e limite de cada iniciativa. | 9/10 | Bloqueio de autossuficiência resolvido; consigo fazer a comparação sem sair da aula. |
| 10 | Documento fictício e seis perguntas prontas; divisão 1–4/5–6 explícita; respostas esperadas e instrução de não enviar casos reservados à revisão. A prática declara que prepara a avaliação. | 9/10 | Bloqueio de preparação resolvido; consigo separar casos e escrever critérios no papel. |
| 11 | Prática já executável com os três atalhos e respectivas proteções. | 9/10 | Aprovada na revisão simulada. |
| 12 | Texto-base, cinco perguntas, repetição e informação ausente observáveis; gabarito aceita reduzir o conjunto a três ideias distintas. Quiz agora manda conferir/corrigir exemplos sem presumir erro da fonte. | 9/10 | Bloqueio da prática e problema do quiz resolvidos; consigo auditar o conjunto e justificar a seleção. |

O coordenador confirmou que a barra sobreposta era artefato do recorte e que o viewport normal está correto. Portanto, a observação visual da primeira rodada não permanece como defeito do produto; esta conclusão de viewport é atribuída à verificação do coordenador, não a uma nova execução minha.

**Veredito final:** as seis aulas atingem 9/10 nesta revisão de leitor simulado. As principais dificuldades que impediam executar as práticas foram resolvidas. Sugestões de polimento verbal da primeira rodada não foram todas implementadas; ficam como melhorias opcionais, sem nova rodada de detalhes. A verificação documental das fontes continua pertencendo à auditoria factual geral do curso, sem ser substituída por estas notas de legibilidade e uso.
