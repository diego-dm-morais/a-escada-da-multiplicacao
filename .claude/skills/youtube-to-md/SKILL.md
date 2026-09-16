---
name: youtube-to-md
description: Converte um link do YouTube em arquivo Markdown com título, resumo, texto completo e conclusão. Use quando o usuário pedir para transformar um vídeo do YouTube em markdown, gerar transcrição em .md, ou usar /youtube-to-md.
---

# youtube-to-md

Converte vídeo do YouTube em Markdown.

## Passos

1. Rodar o script python na raiz do projeto:
   ```
   python youtube_to_md.py "<URL_DO_VIDEO>"
   ```
   Gera `content/youtube/<titulo-do-video>.md` com:
   - `# Título`
   - `## Resumo` (placeholder `_(preencher)_`)
   - `## Texto completo` (transcrição corrida, sem timestamp)
   - `## Conclusão` (placeholder `_(preencher)_`)

2. Ler o arquivo gerado.

3. Preencher `## Resumo` e `## Conclusão` com base no texto completo (Edit tool) — resumo objetivo do conteúdo, conclusão seguindo as regras abaixo.

## Regras da Conclusão

- Cristocêntrica: Cristo é o centro, ênfase na graça, amor e favor de Deus.
- Evangelho da graça: somos salvos pelo sacrifício de Jesus na cruz, acesso ao Pai só por Ele, consumado pela fé — não por mérito próprio.
- Tom: alegre, envolvente, claro, motivador — desperta desejo de contemplar mais a Deus e conhecê-Lo.
- Toda citação bíblica na versão ACF (regra do CLAUDE.md do projeto).

## Requisitos

- `pip install yt-dlp youtube-transcript-api` (já instalado neste projeto)
- Vídeo precisa ter transcrição/legenda disponível (pt, pt-BR ou en)

## Script

`youtube_to_md.py` na raiz do projeto.
