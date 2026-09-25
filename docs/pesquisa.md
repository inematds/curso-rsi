# Pesquisa e análise editorial — RSI v6.2

Data de corte e consulta: 25/09/2026. Curso aberto em português. Os exemplos de trabalho são autorais e fictícios. Esta pesquisa combina documentos primários e análise metodológica; não reproduz as transcrições recebidas.

## 1. O que havia no projeto original

A pasta `../rsi/docs` continha três transcrições em alemão (`material-1.txt` a `material-3.txt`), a análise conceitual do usuário (`material-0-analise-do-usuario.md`) e pesquisas sobre conceitos/riscos e aplicações. O projeto também tinha imagens e estrutura de publicação em preparação. Não foi identificado código de um sistema RSI executável nesses materiais. Portanto, o novo projeto é um curso sobre o assunto, não a documentação de uma ferramenta operacional já implementada.

O material 1 combina infraestrutura DSec, notícias sobre pesquisa automatizada, robótica e modelos recentes. O material 2 discute avaliações de capacidade, supervisão, ritmo de desenvolvimento e propostas de governança. O material 3 aproxima pesquisa interna de laboratórios, otimização de operações computacionais, ambientes de treinamento e riscos de atalhos. Os textos misturam relato técnico, opinião e linguagem de divulgação.

A contribuição mais útil da análise do usuário é deslocar a atenção de “qual modelo é melhor” para “como um sistema propõe, mede e preserva melhorias”. Mantivemos essa linha no LOOP-R. “IA Cultivada” e “LOOP-R” são nomenclaturas conceituais do projeto; não as apresentamos como padrões reconhecidos universalmente.

## 2. Perguntas que orientaram a pesquisa

1. Qual componente muda: resposta, instrução, memória, ferramenta, código do agente ou parâmetros do modelo?
2. Como a mudança é avaliada e quem controla essa avaliação?
3. A melhoria transfere para tarefas reservadas ou só aumenta uma nota conhecida?
4. A nova versão também melhora a capacidade de descobrir melhorias futuras?
5. Qual parte do ciclo continua dependendo de julgamento humano, computação, dados ou infraestrutura?
6. Qual aplicação pode ser ensaiada com baixo custo, resultado observável e possibilidade de reversão?

Essas perguntas permitem ler projetos distintos sem transformar qualquer automação em RSI. A fronteira terminológica não é consensual. O curso usa “indício de recursão” quando existe um mecanismo de realimentação, sem inferir crescimento indefinido.

## 3. Mecanismos e diferenças fundamentais

### Revisão durante o uso

Self-Refine estuda geração, crítica e revisão iterativa usando um modelo, sem exigir treinamento adicional para o procedimento apresentado. Isso ajuda a distinguir melhorar a resposta atual de melhorar o processo que produzirá gerações de sistemas. [Madaan e colaboradores, 2023](https://arxiv.org/abs/2303.17651).

Reflexion usa feedback em linguagem e memória episódica para orientar tentativas posteriores sem atualizar os pesos. Uma memória de reflexão é um mecanismo concreto de adaptação durante a tarefa; não se deve descrevê-la automaticamente como um novo modelo treinado. [Shinn e colaboradores, 2023](https://arxiv.org/abs/2303.11366).

### Alteração do sistema que usa o modelo

A instrução, as ferramentas disponíveis e o procedimento de avaliação podem mudar sem modificar parâmetros. Essa camada é a mais acessível nos exercícios: alterar uma regra, manter referências e comparar resultados. Os exercícios são analogias operacionais, não reproduções dos estudos.

A DGM mantém variantes de agentes e propõe alterações em seu código. O artigo permite examinar a diferença entre busca exploratória e simples substituição pela candidata com maior nota. [Zhang e colaboradores](https://arxiv.org/abs/2505.22954). O curso reserva a adoção para uma decisão separada da exploração.

### Alteração de parâmetros e sinais de aprendizagem

Treinamento modifica valores internos a partir de dados e sinais de avaliação. No trabalho Self-Rewarding Language Models, o modelo participa da produção de recompensas durante um procedimento de treinamento iterativo. Isso é diferente de pedir uma crítica numa conversa. [Yuan e colaboradores, ICML 2024](https://arxiv.org/abs/2401.10020).

Um sistema pode combinar camadas, mas elas não são intercambiáveis. Se falta uma referência, melhorar a recuperação pode resolver. Se uma avaliação premia respostas inventadas, aumentar a quantidade de treinamento pode reforçar o erro. A escolha da intervenção depende do diagnóstico, não da aparência sofisticada da técnica.

### Prova, teste e incerteza

A máquina de Gödel é uma proposta teórica de autorreescrita condicionada à demonstração de benefício dentro de seu formalismo. Suas premissas não devem ser confundidas com uma ferramenta disponível para uso cotidiano. Testes empíricos oferecem evidência sob condições, sem a mesma garantia formal. [Schmidhuber, 2003](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html).

Na prática editorial deste curso, a cadeia de evidência é: hipótese escrita → candidata preservada → comparação → validação → decisão limitada. A conclusão pode ser negativa. “Não obtivemos ganho confiável” é informação útil, desde que o registro permita entender o teste.

## 4. Matriz das evidências consultadas

| Fonte primária | O que sustenta no curso | Limite preservado |
|---|---|---|
| [AlphaEvolve, Google DeepMind](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) | Busca de programas com verificação; melhoria local versus efeito no conjunto | Percentuais pertencem às condições e componentes divulgados |
| [DGM, artigo](https://arxiv.org/abs/2505.22954) | Alterações do agente e arquivo de variantes | Resultados em avaliações específicas, sem garantia geral |
| [DGM, relato dos autores](https://sakana.ai/dgm/) | Necessidade de conferir execução e proteger avaliação | A própria avaliação pode ser explorada |
| [AI Scientist, Sakana](https://sakana.ai/ai-scientist-first-publication/) | Automação de etapas e experiência com revisão de artigo | Oficina vinculada ao ICLR, não conferência principal |
| [DSec, DeepSeek](https://arxiv.org/abs/2609.22978) | Infraestrutura e preparação de ambientes | Escala de execução não é medida de descoberta científica |
| [Pesquisa interna, OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/) | Apoio de agentes à pesquisa sob direção humana | Relato e avaliação da própria organização |
| [Padrões para IA, OpenAI](https://openai.com/index/building-standards-next-phase-ai/) | Discussão de controle e RSI | Posição institucional; não é lei nem auditoria universal |
| [Horizonte de tarefas, METR](https://metr.org/notes/2026-01-22-time-horizon-limitations/) | Medidas dependem de domínio e incerteza | Tempo humano equivalente não é duração de autonomia |
| [Manipulação da recompensa, Anthropic](https://www.anthropic.com/research/reward-tampering) | Critério incompleto e alteração indevida do exame | Experiências controladas; não atribuir intenção humana |
| [Colapso com dados gerados](https://arxiv.org/abs/2305.17493) | Preservar origem e diversidade dos dados | Não concluir que todo dado sintético é prejudicial |
| [Modelos que se autorrecompensam](https://arxiv.org/abs/2401.10020) | Julgamento automático pode fazer parte do treinamento | Uma preferência automática não é uma verdade factual |
| [Epoch: necessidade de experimentos](https://epoch.ai/gradient-updates/the-software-intelligence-explosion-debate-needs-experiments) | Debate sobre retornos e gargalos permanece empírico | Texto de análise dos autores, não previsão garantida |
| [Reflexion](https://arxiv.org/abs/2303.11366) | Feedback verbal e memória sem atualizar pesos | Adaptação de tentativas não equivale à autonomia geral |
| [Self-Refine](https://arxiv.org/abs/2303.17651) | Revisão iterativa de respostas | Resultado da tarefa e melhoria do sistema são distintos |
| [Máquina de Gödel](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html) | Autorreescrita teoricamente condicionada a prova | Premissas formais não viram garantia prática automaticamente |

## 5. Por que o ciclo pode desacelerar

Um modelo conceitual útil separa capacidade de propor, capacidade de testar e capacidade de reconhecer uma melhoria. Aumentar apenas uma delas pode deslocar o gargalo. Uma fila maior de propostas não produz necessariamente mais conclusões válidas.

Há pelo menos seis restrições práticas: orçamento computacional, qualidade dos dados, tempo de execução, validade da avaliação, integração da mudança e supervisão. Uma ideia pode funcionar num teste pequeno e não conservar o ganho em outro contexto. Além disso, examinar muitas candidatas aumenta a oportunidade de selecionar uma que teve sorte nos casos conhecidos.

O debate sobre explosão de inteligência de software exige distinguir hipóteses de retornos crescentes e limitações físicas. O texto da Epoch argumenta pela necessidade de experimentos, sem resolver a questão por uma extrapolação única. [Anson Ho e Parker Whitfill, 2025](https://epoch.ai/gradient-updates/the-software-intelligence-explosion-debate-needs-experiments).

Não usamos uma série de “QI 100 → 120 → 150” como modelo quantitativo. Essa imagem das transcrições não fornece unidade operacional, função de ganho ou custo. Uma análise verificável precisa dizer qual capacidade foi medida, em qual tarefa e contra qual comparação.

## 6. Como aplicar sem prometer RSI autônoma

O curso propõe três aplicações: respostas apoiadas numa política, questões apoiadas num texto e extração de ações apoiada em notas. Todas permitem verificar referência e lacunas. A saída é um rascunho revisável, sem envio automático nem decisão externa.

Uma experiência começa com dois critérios obrigatórios: fidelidade à referência e ausência de fatos inventados. Critérios de preferência, como concisão, só entram depois. A comparação usa as mesmas tarefas e registra também o esforço humano. Não basta reduzir o tempo de geração se a conferência ficou mais trabalhosa.

Os casos de desenvolvimento ajudam a ajustar. Os casos reservados são preparados antes e usados posteriormente. Quando o avaliador revela seus erros à etapa de revisão repetidamente, aquela avaliação perde parte de sua independência. Uma futura rodada deve reconhecer isso e preparar novos casos.

Para ampliar o projeto, a ficha precisa virar um acordo operacional: dados permitidos, ações permitidas, limites de gasto, evidências exigidas, responsável final e reversão. A equipe técnica deverá implementar permissões reais. Escrever “não faça” num pedido não é uma barreira técnica.

## 7. Decisões sobre alegações do material recebido

| Alegação ou enquadramento | Decisão editorial |
|---|---|
| Toda melhoria de resposta é RSI | Corrigido: distinguir resposta, sistema e capacidade de melhoria |
| LOOP-R e IA Cultivada como nomes científicos universais | Identificados como organização conceitual do projeto |
| DSec comprova autonomia integral | Não adotado; infraestrutura é um componente |
| Artigo do AI Scientist aceito no ICLR | Qualificado como oficina ligada à conferência |
| Tempo de agentes equivale a progresso científico | Não adotado; atividade e contribuição são diferentes |
| Vazamentos e comparações entre modelos comerciais | Não usados como base do currículo |
| Alegação sobre solução do problema do milênio Navier–Stokes | Não verificada nesta pesquisa; omitida do curso |
| Previsões de superinteligência em datas exatas | Tratadas como cenários, sem calendário garantido |
| Ferramentas ou políticas tornam todo ensaio seguro | Não adotado; condições e implementação importam |

## 8. Método e limitações desta pesquisa

Busca iniciada pelo roteiro agent-reach. Exa não estava configurado no mcporter; foi usado o mecanismo web disponível. Consultamos documentos dos autores, organizações responsáveis e artigos no arXiv. O acesso à página da Nature falhou; usamos a versão dos autores sobre dados recursivos. A documentação DSPy devolveu conteúdo insuficiente e não foi usada para orientar passos de uso.

Não executamos nem reproduzimos os estudos DGM, AlphaEvolve ou DSec. Não medimos eficácia de modelos comerciais. Não houve teste com alunos humanos reais. A revisão de compreensão do curso é simulada, distinta da auditoria automática do HTML e do teste funcional do motor.

Os percentuais didáticos, os personagens e as políticas de exemplo são fictícios. Resultados reportados por laboratórios mantêm a atribuição aos autores. O curso deve ser atualizado se o estado das evidências mudar, sem trocar automaticamente a versão publicada apenas por novas manchetes.


## 9. LOOP-R e conhecimento aprovado — atualização de 25/09/2026

A pedido do usuário, o curso passou a aplicar explicitamente o projeto [LOOP-R](https://inematds.github.io/loop-r/guia/). Foram consultados o README, a visão de produto, a crítica de viabilidade e as instruções do runner no repositório local. Não executamos seus agentes nem reproduzimos o exemplo de negócio.

A adoção de uma candidata é diferente de reutilizar uma versão já aprovada. No fluxo com revisão humana, avaliação favorável e decisão registrada permitem a promoção. A versão vigente passa a orientar usos futuros dentro da autorização. Repetir a mesma tarefa não exige repetir a mesma aprovação. Nova candidata, ampliação de escopo, mudança relevante de referência ou falha exigem tratamento próprio.

O curso usa “conhecimento aprovado” para uma regra ou informação aceita com fonte, versão, evidência, responsável, escopo e validade. Não afirma que aprovação transforma uma alegação em verdade, altera os pesos do modelo ou cria memória persistente sem implementação. A ficha separa aprovação de resultado isolado de autorização de reutilização. Ações externas mantêm seus próprios limites de autorização.

A responsabilidade de aprovar inclui considerar os usos futuros e a propagação de erro. Suspensão e revogação interrompem o uso afetado, preservando histórico e possibilidade de reversão. O registro é um recurso de controle; não garante que um sistema real consiga detectar todo erro ou evitar toda regressão.

O conteúdo e as fichas de prática estão em PT/EN/ES. Esta análise editorial permanece em português, explicitado nas páginas traduzidas.
