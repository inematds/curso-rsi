# RSI v6.2 — Entenda e aplique ciclos de melhoria em IA

Curso gratuito em português, inglês e espanhol: 18 aulas, seis módulos, 54 cartões de revisão, glossário e projeto final. Baseado no projeto RSI e em pesquisa com fontes originais.

- Entrada: https://inematds.github.io/curso-rsi/
- Español: https://inematds.github.io/curso-rsi/es/
- English: https://inematds.github.io/curso-rsi/en/
- Área RSI: https://eventos.inema.pro/rsi/
- Aulas: https://inematds.github.io/curso-rsi/curso.html
- Pesquisa e limites: [docs/pesquisa.md](docs/pesquisa.md)
- Currículo: [context/curriculo.md](context/curriculo.md)
- Materiais: [materiais/](materiais/)

## Manutenção

`python3 scripts/montar.py` gera aulas, configuração, landing e curso a partir do conteúdo autoral em `scripts/conteudo.py` e do motor oficial local formato-curso-v6. O motor foi copiado sem alterações. As fontes HTML estão versionadas para edição e consulta independente.

O pedido foi formato v6.2. A versão local do motor inclui melhoria compatível de navegação por módulos da família v6. Não requer conta para ler; progresso fica no navegador. Exportação/importação está no menu.

As práticas não enviam mensagens nem executam ações externas. Personagens, políticas e números dos exercícios são fictícios. Nenhuma prática comprova RSI autônoma.

## Validação

Auditoria do formato e teste funcional com Playwright, mais revisão de leitor simulado. Evidências em `context/`. Teste com pessoas reais não realizado.

## Atualizar as versões traduzidas

Depois de montar PT, execute o tradutor oficial com `en es`:

```sh
python3 ~/.claude/skills/formato-curso-v6/scripts/traduzir-curso.py . en es
python3 scripts/finalizar-idiomas.py
python3 scripts/verificar-idiomas.py
```

Para remontar usando o cache revisado, acrescente `--so-montar` ao tradutor. As correções editoriais ficam em `i18n/en.json` e `i18n/es.json`; o glossário em `i18n/glossario.json`. EN/ES reaproveitam imagens/CSS e traduz somente o dicionário do motor. Progresso fica separado por idioma. Materiais de prática em `en/materiais/` e `es/materiais/`; relatório editorial de pesquisa permanece em português, indicado no link.

Curso, guia original e área de Eventos disponíveis em PT/EN/ES.

As aulas 4–6 aplicam LOOP-R: promoção, memória aprovada e reutilização sem repetir a mesma aprovação dentro do escopo. As aulas 17–18 incluem validade, suspensão e revogação no projeto final. Ficha adicional em `materiais/conhecimento-aprovado.txt`.
