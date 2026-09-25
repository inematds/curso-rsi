---
name: "Curso RSI — formato v6.2"
description: "Leitura em papel e prática supervisionada."
colors:
  bg: "#F7F3EA"
  bg2: "#EFE8DA"
  panel: "#FFFFFF"
  panel2: "#F2ECE0"
  ink: "#221E18"
  ink-soft: "#3A342B"
  muted: "#5E5546"
  line: "#E2D9C8"
  line2: "#CFC3AC"
  accent: "#0E6B55"
  accent-ink: "#FFFFFF"
  accent-soft: "rgba(14,107,85,.10)"
  warm: "#8F520A"
  warm-soft: "rgba(191,122,24,.13)"
  bad: "#A83426"
  bad-soft: "rgba(168,52,38,.08)"
  hl: "rgba(240,186,70,.45)"
  chat-bg: "#FFFFFF"
  chat-me: "#E6F1EC"
  chat-ia: "#F3EFE7"
  escuro-bg: "#15141B"
  escuro-bg2: "#1B1A23"
  escuro-panel: "#1F1D28"
  escuro-panel2: "#282532"
  escuro-ink: "#EFEAE0"
  escuro-ink-soft: "#D6D1DC"
  escuro-muted: "#ABA4BA"
  escuro-line: "#2F2B3B"
  escuro-line2: "#3F3A51"
  escuro-accent: "#7CE0C6"
  escuro-accent-ink: "#10131A"
  escuro-accent-soft: "rgba(124,224,198,.12)"
  escuro-warm: "#F2B45C"
  escuro-warm-soft: "rgba(242,180,92,.12)"
  escuro-bad: "#F0918A"
  escuro-bad-soft: "rgba(240,145,138,.10)"
  escuro-hl: "rgba(242,180,92,.32)"
  escuro-chat-bg: "#1B1A23"
  escuro-chat-me: "#1F3A33"
  escuro-chat-ia: "#282532"
  sepia-bg: "#EFE3CB"
  sepia-bg2: "#E7D8BC"
  sepia-panel: "#F8F0DF"
  sepia-panel2: "#EBDDC1"
  sepia-ink: "#35281A"
  sepia-ink-soft: "#46372A"
  sepia-muted: "#63523B"
  sepia-line: "#D9C8A8"
  sepia-line2: "#C6B18C"
  sepia-accent: "#0D5F4C"
  sepia-accent-ink: "#FFFFFF"
  sepia-accent-soft: "rgba(13,95,76,.10)"
  sepia-warm: "#7E4A0C"
  sepia-warm-soft: "rgba(160,100,20,.13)"
  sepia-bad: "#9A3122"
  sepia-bad-soft: "rgba(154,49,34,.08)"
  sepia-hl: "rgba(214,150,40,.40)"
  sepia-chat-bg: "#FBF5E8"
  sepia-chat-me: "#E1EADF"
  sepia-chat-ia: "#EFE4CE"
typography:
  display:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(38px,7vw,64px)"
    fontWeight: 500
    lineHeight: 1.04
    letterSpacing: "-.02em"
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "18px"
    lineHeight: 1.7
  label:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 600
  code:
    fontFamily: "JetBrains Mono, Space Mono, ui-monospace, monospace"
    fontSize: "15px"
    lineHeight: 1.6
rounded:
  surface: "14px"
  field: "12px"
  practice: "18px"
  pill: "99px"
spacing:
  gap: "12px"
  gutter: "16px"
  step: "32px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
  button-secondary:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
---
# Design System: Curso RSI

## Overview

**Creative North Star: "Leitura e prática em papel"**

Sistema existente do formato solicitado v6.2, extraído de landing.html, curso.html e assets/aula.css. O motor oficial preservado inclui melhorias compatíveis da família v6, como módulos recolhíveis. Esta documentação registra a interface existente.

Papel quente, títulos Newsreader e interface Inter organizam uma leitura calma em coluna única. Cenas FLUX.2 Klein mostram situações de trabalho junto do texto; práticas e evidências recebem destaque.

A expressão descreve o contrato existente, sem propor outra identidade.

**Key Characteristics:**

- Papel padrão; escuro e sépia como preferências.
- Títulos serifados e corpo sem serifa.
- Uma coluna de leitura com prática próxima.

## Colors

### Primary

Verde em `accent` para ações, progresso, numeração e acertos; `accent-soft` para promessa e definição. No escuro, o verde fica claro. Os tokens sem prefixo representam papel; `escuro-` e `sepia-` documentam variantes dos mesmos nomes CSS.

### Secondary

`warm` destaca atenção e orientação. `bad` indica erro; versões suaves preservam a leitura. São funções semânticas, não decoração.

### Neutral

`bg` é o papel; `panel` e `panel2` distinguem superfícies. `ink`, `ink-soft` e `muted` ordenam texto e metadados. `line` e `line2` desenham contornos. `chat-me` e `chat-ia` separam interlocutores; `hl` marca a leitura.

## Typography

Newsreader com Georgia de reserva nos títulos; Inter no corpo e controles; JetBrains Mono em pedidos e código. A trilha usa título entre 36 e 60px, linha 1.05; aulas entre 32 e 48px, linha 1.08. Etapas variam de 26 a 32px, linha 1.15. Corpo padrão de 18px com tamanho ajustável; legendas de 15px e metadados de 14px. A folha tem exceções menores no selo PRO (12px) e sinal de glossário (13px); o comentário de intenção de legibilidade não equivale a auditoria concluída.

## Layout

Leitura em uma coluna com largura máxima de 40rem; trilha, landing e barra em 54rem. Respiro lateral de 16px. Etapas têm 32px superiores. Cartões de aula combinam miniatura de 96×72px e texto. Cenas ocupam a coluna em 16:9.

A barra reduz rótulos abaixo de 560px; comparações empilham abaixo de 600px; blocos de público da landing abaixo de 640px. Visuais largos podem ultrapassar a coluna a partir de 900px. Resultados da landing usam grade fluida. Módulos recolhíveis revelam suas aulas.

## Elevation & Depth

Diferenças de superfície, bordas finas e sombra discreta dependente do tema. A sombra oficial aparece em cartões de aula, resumos, prática e preferências; valores exatos no sidecar. Barra sticky com fundo parcialmente transparente e desfoque de 8px. Painel lateral sobre fundo escurecido.

## Shapes

Superfícies com cantos de 14px, campos e opções com 12px, prática com 18px. Botões em pílula, numeração circular. Promessas e avisos usam borda lateral e cantos direitos arredondados.

## Components

- **Ações:** principal verde, texto contrastante, altura mínima de 48px; secundário com superfície de painel e texto verde. Sem hover próprio no CSS desses dois; foco global de 3px, afastamento de 2px.
- **Navegação:** barra sticky com controles; botões de 40px com borda verde no hover. Painel lateral de até 420px.
- **Cartão de aula:** miniatura, número, título serifado, duração e progresso; hover realça borda.
- **Promessa e resumo:** superfície verde suave e síntese numerada antes das etapas.
- **Prática:** borda verde de 2px, objetivo, pedido copiável e checklist.
- **Quiz:** opções de ao menos 48px, estados correto/incorreto com símbolos e explicação.
- **Anotações:** textarea de superfície neutra e cantos de 12px na reflexão e edição de cartões.
- **Glossário:** definição inline; complementos e fontes em details.
- **Módulos:** details nativo com +/−, resumo e duração, aulas reveladas ao expandir.

Movimento de interface: bordas e sobreposição em 0.2s, painel em 0.25s, progresso em 0.4s. A preferência reduced-motion desativa animações, transições e rolagem suave. Snippets do sidecar demonstram apresentação, sem substituir o motor.

## Do's and Don'ts

### Do

- Preservar o motor oficial e seus tokens nos três temas.
- Usar cenas de trabalho com texto alternativo e explicações em HTML.
- Manter foco visível e respeitar redução de movimento.
- Reservar monoespaçada para pedidos e código.

### Don’t

- Não substituir o tema papel por nova identidade.
- Não transformar aulas em painel de múltiplas colunas.
- Não embutir texto essencial nas imagens.
- Não apresentar cenas ilustrativas como evidência de RSI autônoma.
