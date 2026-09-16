# jornada-multiplicacao

Mantém **um único arquivo vivo** — `content/mind-map/html/jornada-para-multiplicao.html` — com o passo a passo da vida cristã até a Grande Fé e a Multiplicação. Cada novo capítulo da série (novo `.md` em `content/youtube/`) enriquece esse mesmo arquivo; nunca cria um arquivo novo.

## Uso

```
/jornada-multiplicacao
```

Sem argumento: varre `content/youtube/` inteira e atualiza o arquivo com qualquer capítulo ainda não incorporado.

## Estrutura fixa (não mudar)

O arquivo tem 9 passos fixos, nessa ordem — é o modelo da jornada cristã até a multiplicação. Capítulos novos **enriquecem** um ou mais desses passos (texto, "Como fazer", e a tag do capítulo-fonte); eles nunca reordenam, removem ou criam um 10º passo, a menos que o usuário peça explicitamente:

1. Coragem para agir
2. Conhecer a Deus
3. Buscar a Cristo
4. Ter intimidade
5. Confiar
6. Ter esperança (esperar)
7. Declarar a palavra já entregue
8. Grande Fé
9. Multiplicação

## Passos

1. Ler `content/mind-map/html/jornada-para-multiplicao.html` (se não existir, avisar e não inventar do zero — pedir para rodar a skill `mind-map`/pipeline primeiro).
2. No topo do `<body>`, manter um comentário HTML `<!-- capítulos processados: <arquivo1>.md, <arquivo2>.md, ... -->` (criar se não existir). Esse comentário é a lista de controle — nunca reprocessar um capítulo já listado.
3. Listar todos os `.md` em `content/youtube/` (`ls content/youtube/*.md`).
4. Para cada arquivo ainda **não** listado no comentário de controle:
   a. Ler o `.md` (Resumo + Texto completo).
   b. Identificar a qual(is) dos 9 passos fixos o conteúdo desse capítulo mais se conecta (um capítulo pode reforçar mais de um passo).
   c. Editar o(s) `.step` correspondente(s):
      - Se o passo ainda não tem `<p class="how">`, escrever um "Como fazer" prático baseado no capítulo.
      - Se já tem, só enriquecer/ajustar o texto se o capítulo trouxer algo relevante novo — não duplicar conteúdo já coberto.
      - Adicionar/atualizar uma tag pequena de fonte no passo, ex.: `<span class="src">Cap. 3</span>` (mesma classe `.src` reaproveitada em todos os passos — criar o CSS uma única vez se ainda não existir).
   d. Acrescentar o nome do arquivo ao comentário de controle do passo 2.
5. Toda citação bíblica no arquivo (blockquote ou `.ref`) deve estar em ACF (Almeida Corrigida Fiel), conforme regra do CLAUDE.md do projeto.
6. Manter o `<div class="closing-card">` sempre cristocêntrico: Cristo no centro, graça, evangelho da graça, tom alegre e motivador — ajustar a citação/fechamento só se um capítulo novo trouxer um versículo-chave melhor para representar a jornada como um todo.
7. Depois de editar, publicar de novo com a ferramenta Artifact (`action: publish`, mesmo `url` da publicação anterior — está registrado num comentário `<!-- artifact-url: ... -->` logo abaixo do comentário de capítulos processados; se não houver url registrada ainda, publicar sem `url` e gravar a nova url nesse comentário).
8. Atualizar também o PNG de alta resolução:
   ```
   node scripts/html-to-png.mjs "content/mind-map/html/jornada-para-multiplicao.html" "content/mind-map/png/jornada-para-multiplicao.png"
   ```
9. Reportar ao usuário: quais capítulos foram incorporados, em quais passos, o link do artifact e o caminho do `.png` atualizado.

## Regras

- Nunca reescrever passos inteiros do zero — só enriquecer com o que o capítulo novo realmente acrescenta.
- **Arquivo único, sempre substituído, nunca duplicado.** Só existem estes dois arquivos, sempre com esse nome exato, sempre sobrescritos in-place a cada rodada — nunca `-v2`, `-novo`, `-atualizado`, data no nome, ou qualquer outro sufixo/cópia:
  - `content/mind-map/html/jornada-para-multiplicao.html`
  - `content/mind-map/png/jornada-para-multiplicao.png`
  Antes de reportar concluído, checar que não existe nenhum outro arquivo parecido nessas duas pastas (`ls content/mind-map/html/ content/mind-map/png/`) — se existir, é sinal de erro anterior; apagar a duplicata e manter só o arquivo canônico.
- Não pular a checagem do comentário de controle — evita reprocessar e duplicar conteúdo.
- Layout/CSS do arquivo são o template já validado — não redesenhar do zero a cada rodada, só ajustar o necessário para caber texto novo.
