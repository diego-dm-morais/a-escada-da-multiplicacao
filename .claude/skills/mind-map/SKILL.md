---
name: mind-map
description: Gera um mapa mental visual (imagem, estilo aquarela/hand-drawn elegante) resumindo um capítulo a partir de um arquivo .md de transcrição/outline, e exporta em PNG de alta resolução pronto pra WhatsApp. Use quando usuário pedir /mind-map <arquivo.md> ou "mapa mental" de um vídeo/capítulo.
---

# mind-map

Gera mapa mental visual e elegante (estilo aquarela, hand-drawn, referência: cards com bordas arredondadas coloridas ao redor de um título central com ilustração) resumindo o conteúdo de um `.md` (transcrição gerada por `/youtube-to-md` ou esboço de `/outline`).

## Uso

```
/mind-map <caminho/do/arquivo.md>
```

Exemplo:
```
/mind-map content/youtube/LIVE-21-Dias-de-Jejum-e-Oração-Pr-Wilson-Silva-CAP-1-A-Multiplicação-do-Azeite-1409.md
```

## Template obrigatório

`template.html` (nesta pasta) é o layout canônico. Todo mind-map gerado deve ser **fiel** a ele: mesmo `<style>` (CSS, cores, fontes, classes `.card`, `.c1`..`.c6`, `.quote`, `footer`), mesma estrutura de divs, mesma organização visual. **Não inventar novo layout, cores ou classes.** Só o conteúdo (texto, emojis, referências) muda por vídeo.

## Passos

1. Ler `template.html` e usar como base — copiar o `<style>` e a estrutura de divs sem alteração.
2. Ler o arquivo `.md` informado (título + texto completo/resumo).
3. Extrair 5-7 blocos temáticos do conteúdo (ex.: "O que é", "Base bíblica", "Personagens", "Princípios/passos", "Aplicações práticas") — adaptar ao conteúdo real, preenchendo os placeholders `{{...}}` do template.
4. Preencher no template:
   - kicker (série/capítulo), título, subtítulo (pregador · data · referência principal), emoji central
   - cards (repetir `.card c1`..`.c6`, ciclando as classes se houver mais de 6 blocos)
   - `.quote` com citação-chave em ACF
   - `footer .closing` cristocêntrico (Cristo no centro, graça, evangelho da graça) e `.keywords`
   - referências bíblicas sempre em Almeida Corrigida Fiel (ACF), regra do CLAUDE.md do projeto
5. Carregar a skill `artifact-design` antes de publicar o HTML (fundamentos de design de artifact).
6. Publicar com a ferramenta Artifact (`action: publish`), favicon temático (emoji), título = nome do capítulo.
7. Salvar cópia do HTML final em `content/mind-map/html/<mesmo-nome-do-arquivo-de-origem>.html` (criar pasta `content/mind-map/html/` se não existir).
8. Converter esse HTML em PNG de resolução máxima, pronto pra enviar no WhatsApp:
   ```
   node scripts/html-to-png.mjs "content/mind-map/html/<mesmo-nome-do-arquivo-de-origem>.html" "content/mind-map/png/<mesmo-nome-do-arquivo-de-origem>.png"
   ```
   Gera `content/mind-map/png/<mesmo-nome-do-arquivo-de-origem>.png` (criar pasta `content/mind-map/png/` se não existir; screenshot full-page, `deviceScaleFactor: 3`, nítido em qualquer tela).
   - Requer `playwright` instalado (`npm install playwright` na raiz do projeto) e o browser baixado (`npx playwright install chromium`) — rodar uma vez se o comando falhar com "Executable doesn't exist".
9. Reportar ao usuário o caminho do `.png` gerado, além do link do artifact.

## Requisitos

- A saída visual em si é HTML/CSS (sem modelo de imagem raster nas tools) — o PNG final é gerado via screenshot desse HTML com Playwright (`scripts/html-to-png.mjs`), não desenhado do zero.
- Layout deve ser responsivo e legível tanto no artifact quanto no PNG exportado — nada pode ficar cortado no full-page screenshot.
