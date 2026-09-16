# mind-map — template visual "pôster aquarela"

Referência: imagem "A Escada da Multiplicação" (grid poster, não radial).

## Layout geral

CSS Grid fixo, 3 colunas x 3 linhas lógicas:

```
[card 1]      [card 2 topo-centro]   [card 3]
[card 4]      [BLOCO CENTRAL]        [card 5 / citação]
[card 6 lista degraus]  [ilustração+título] [card 7]
[nota canto inf-esq]    [rodapé full-width] [nota canto inf-dir]
```

- Fundo geral: branco/off-white.
- Sem setas curvas ligando tudo ao centro — só 2-3 setas soltas, curtas, tracejadas, saindo de card específico apontando pro bloco central (não de todos).

## Cards (blocos temáticos)

- Retângulo, cantos bem arredondados (radius grande, ~24px), **sem preenchimento** (fundo branco), borda colorida fina (2px) em cor pastel diferente por card: rosa, verde-água, azul, amarelo.
- Título do card: dentro de uma pílula/badge da mesma cor pastel (fundo sólido leve), texto bold caixa alta, fonte sans arredondada tipo "Fredoka" ou "Baloo 2".
- Corpo: bullet list simples, fonte sans limpa (ex. "Nunito"), texto cinza-escuro, sem itálico.
- Ícone pequeno de linha (line-art, 1 cor) ao lado do título quando fizer sentido (ex. livro aberto pra "Base Bíblica").
- Card de "personagem/definição" pode ter uma seta pequena desenhada à mão saindo dele em direção ao próximo card relacionado — não obrigatório.

## Citação-chave

- Sem card/borda — texto solto sobre fundo, fonte handwriting (ex. "Caveat" ou "Patrick Hand"), cor sólida (não pastel de fundo), tamanho maior que corpo normal.
- Referência bíblica embaixo, menor, sans, cor neutra. **Sempre ACF** (regra do projeto).
- Pode ter emoji temático pequeno do lado (coração, folha, etc.) — usar com moderação, 1 por citação.

## Bloco central (título + ilustração)

- Rabisco de "pincel aquarela" atrás (blob de cor pastel suave, baixa opacidade, formato orgânico) — simular com SVG path ou `border-radius` irregular + `filter: blur`.
- Título principal: 2 linhas — linha 1 sans bold caixa alta pequena (ex. "A ESCADA DA"), linha 2 gigante em fonte script/handwriting (ex. "Great Vibes" ou "Dancing Script") em cor de destaque.
- Ilustração temática abaixo do título: SVG line-art simples relacionado ao tema central do vídeo (não obrigatório ser sempre o mesmo objeto — adaptar ao conteúdo real de cada capítulo).
- Linha de subtítulo pequena, sans, caixa alta, letter-spacing largo, 2-3 linhas curtas resumindo a mensagem central.
- Segunda citação-chave (a "citação de impacto") pode ficar ancorada perto da ilustração, mesmo estilo handwriting da seção acima.

## Lista numerada ("os degraus" / passos)

- Coluna própria, com "chave"/colchete decorativo do lado (opcional, SVG simples) agrupando os itens.
- Cada item: número dentro de círculo colorido sólido (cor pastel), título curto bold ao lado, descrição menor embaixo em cinza.

## Rodapé

- Card full-width, borda fina colorida (verde-água), fundo branco, cantos arredondados.
- Título pequeno caixa alta ("PARA LEMBRAR SEMPRE").
- Frase de fechamento em aspas, centralizada, sans.
- Linha de palavras-chave separadas por `|`, caixa alta, letter-spacing.

## Notas de canto (decorativas)

- Texto handwriting, cor pastel, inclinado levemente (`transform: rotate(-3deg)`), sem card — solto no canto inferior esquerdo e direito.
- Esquerda: frase inspiracional curta ligada ao tema.
- Direita: call-to-action curto (ex. "Siga para o próximo capítulo").
- Emoji de coração pequeno opcional no fim de cada nota.

## Paleta

- Rosa pastel `#F7D9D9` / borda `#E8A5A5`
- Verde-água pastel `#D6ECE4` / borda `#8FC9B5`
- Azul pastel `#DDEAF6` / borda `#9DBFDD`
- Amarelo pastel `#FBF0D0` / borda `#E8CE7A`
- Texto corpo: `#3A3A3A`
- Fundo: `#FFFFFF` / `#FDFCFA`

## Fontes (Google Fonts)

- Handwriting/script: "Caveat" ou "Dancing Script" (citações, título grande).
- Sans títulos/badges: "Baloo 2" ou "Fredoka".
- Sans corpo: "Nunito".

## Diferença do layout anterior (radial)

Remover do fluxo atual:
- setas curvas conectando TODOS os cards ao centro
- cards preenchidos com cor sólida forte

Adicionar:
- grid fixo 3 colunas
- cards com borda fina, fundo branco, badge de título colorido
- bloco central com blob aquarela atrás do título
- notas de canto handwriting soltas
