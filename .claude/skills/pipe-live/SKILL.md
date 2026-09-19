---
name: pipe-live
description: Pipeline completo — recebe link do YouTube e roda em sequência youtube-to-md, outline, marca-texto, mind-map, jornada-multiplicacao, atualização do index.html, mensagem-whatsapp e commit+push pra main (dispara publicação automática do site estático). Use quando usuário pedir /pipe-live <URL> ou "processa essa live completa".
---

# pipe-live

Roda o fluxo completo a partir de um link do YouTube, em ordem:

1. `youtube-to-md` — gera `content/youtube/<titulo>.md`
2. `outline` — gera `content/outline/<mesmo-nome>.md`
3. `marca-texto` — destaca trechos-chave nesse mesmo outline (já roda embutido dentro da skill `outline`, mas confira aqui se rodou)
4. `mind-map` — gera e publica `content/mind-map/html/<mesmo-nome>.html` e `content/mind-map/png/<mesmo-nome>.png`
5. `jornada-multiplicacao` — incorpora o capítulo novo no arquivo vivo `content/mind-map/html/jornada-para-multiplicao.html` e republica
6. `index.html` — adiciona o link do novo capítulo em `C:\Users\Administrator\workspace\luke-lab\youtube-to-md\index.html`
7. `mensagem-whatsapp` — gera a mensagem do dia em `content/whatsapp/<mesmo-nome>.md` e imprime pronta pra colar
8. `commit + push` — commita tudo e envia pra `main`, disparando o pipeline do GitHub Actions (`.github/workflows/pages.yml`) que publica o site estático em produção

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
5. Atualizar `index.html` (raiz do projeto), mantendo o template atual (hero com `assets/stairway-sunrise.png`, cartões `.map-link.chapter` dentro de `<ol class="chapters">`) — não trocar por layout simples de lista:
   - Adicionar um novo `<li><a class="map-link chapter" href="content/mind-map/html/<titulo-slug-url-encoded>.html">...</a></li>` dentro de `<ol class="chapters">`, ao final, seguindo exatamente a mesma estrutura interna dos `<li>` existentes: `.thumbnail` (SVG com `<image href="assets/design-reference.png" width="1143" height="1052"/>` e `viewBox="54 Y 165 91"`), `.number` com o próximo número sequencial, `.copy` com `<h2>Cap. N — <Título></h2>` e um `<p>` de uma frase-gancho, e `.access`.
   - Para o `viewBox` do `.thumbnail`, incrementar o `Y` em ~106–107 em relação ao último capítulo (padrão observado: 475, 581, 688 — cada novo capítulo soma ~106/107 ao Y anterior), fatiando uma faixa nova de `assets/design-reference.png` sem repetir a de outro capítulo.
   - Não remover, reordenar nem reescrever os `<li>` existentes — só inserir o novo ao final, na ordem cronológica dos capítulos.
6. Rodar a skill `mensagem-whatsapp` (`.claude/skills/mensagem-whatsapp/SKILL.md`) passando o arquivo de `content/youtube/<titulo-slug>.md`.
   - Confere geração de `content/whatsapp/<titulo-slug>.md`.
   - A mensagem precisa sair com o link do YouTube deste capítulo e os dois links fixos (Instagram e site) — e com frase de motivação nova, diferente das mensagens já salvas em `content/whatsapp/`.
7. Commitar e dar push pra `main`:
   - `git add -A`
   - `git commit -m "..."` (mensagem descrevendo o capítulo processado)
   - `git push`
   - Confirmar no output do push que foi pra `main` sem erro. Isso dispara o workflow `Deploy static site to GitHub Pages`, que republica https://diego-dm-morais.github.io/a-escada-da-multiplicacao/ automaticamente.
8. Ao final, reportar os caminhos/links gerados (youtube, outline já marcado, mind-map do capítulo, link do artifact da jornada atualizado, entrada nova no index.html) e confirmação do push/deploy — e imprimir a mensagem de WhatsApp inteira num bloco de código, pronta pra copiar e colar.

## Regra

- Não pular etapa. Se uma etapa falhar (ex.: vídeo sem transcrição), parar e informar — não seguir para a próxima.
- Cada etapa segue as regras do seu próprio SKILL.md (inclusive versículos em ACF, conforme CLAUDE.md do projeto).
- Push só na etapa 7, depois de todas as etapas de conteúdo confirmadas (inclusive a mensagem de WhatsApp) — nunca commitar parcial.
