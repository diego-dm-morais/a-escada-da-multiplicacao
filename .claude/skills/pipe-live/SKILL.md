---
name: pipe-live
description: Pipeline completo — recebe link do YouTube e roda em sequência youtube-to-md, outline, marca-texto, mind-map, jornada-multiplicacao, e commit+push pra main (dispara publicação automática do site estático). Use quando usuário pedir /pipe-live <URL> ou "processa essa live completa".
---

# pipe-live

Roda o fluxo completo a partir de um link do YouTube, em ordem:

1. `youtube-to-md` — gera `content/youtube/<titulo>.md`
2. `outline` — gera `content/outline/<mesmo-nome>.md`
3. `marca-texto` — destaca trechos-chave nesse mesmo outline (já roda embutido dentro da skill `outline`, mas confira aqui se rodou)
4. `mind-map` — gera e publica `content/mind-map/html/<mesmo-nome>.html` e `content/mind-map/png/<mesmo-nome>.png`
5. `jornada-multiplicacao` — incorpora o capítulo novo no arquivo vivo `content/mind-map/html/jornada-para-multiplicao.html` e republica
6. `commit + push` — commita tudo e envia pra `main`, disparando o pipeline do GitHub Actions (`.github/workflows/pages.yml`) que publica o site estático em produção

## Uso

```
/pipe-live <URL_DO_VIDEO>
```

## Passos

1. Rodar a skill `youtube-to-md` com a URL informada.
   - Aguardar terminar (script + Resumo/Conclusão preenchidos).
   - Guardar o caminho do arquivo gerado: `content/youtube/<titulo-slug>.md`.
2. Rodar a skill `outline` passando esse mesmo arquivo como argumento.
   - Confere geração de `content/outline/<titulo-slug>.md`.
   - A skill `outline` já roda `marca-texto` nesse arquivo ao final — confere se os trechos-chave saíram marcados (`***texto***`); se não saíram, rodar `/marca-texto` manualmente nesse arquivo antes de seguir.
3. Rodar a skill `mind-map` passando o arquivo de `content/youtube/<titulo-slug>.md` (ou o outline, o que tiver o resumo mais estruturado) como argumento.
   - Confere geração e publicação de `content/mind-map/html/<titulo-slug>.html` e do `content/mind-map/png/<titulo-slug>.png` de alta resolução gerado junto (pronto pra WhatsApp).
4. Rodar a skill `jornada-multiplicacao` (sem argumento — ela varre `content/youtube/` sozinha) para incorporar esse capítulo novo no arquivo vivo `content/mind-map/html/jornada-para-multiplicao.html`.
   - Confere que o capítulo novo entrou no comentário de controle e que o artifact foi republicado.
5. Commitar e dar push pra `main`:
   - `git add -A`
   - `git commit -m "..."` (mensagem descrevendo o capítulo processado)
   - `git push`
   - Confirmar no output do push que foi pra `main` sem erro. Isso dispara o workflow `Deploy static site to GitHub Pages`, que republica https://diego-dm-morais.github.io/a-escada-da-multiplicacao/ automaticamente.
6. Ao final, reportar os caminhos/links gerados (youtube, outline já marcado, mind-map do capítulo, link do artifact da jornada atualizado) e confirmação do push/deploy.

## Regra

- Não pular etapa. Se uma etapa falhar (ex.: vídeo sem transcrição), parar e informar — não seguir para a próxima.
- Cada etapa segue as regras do seu próprio SKILL.md (inclusive versículos em ACF, conforme CLAUDE.md do projeto).
- Push só na etapa 5, depois de todas as etapas de conteúdo confirmadas — nunca commitar parcial.
