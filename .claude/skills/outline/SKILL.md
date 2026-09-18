---
name: outline
description: Gera esboço de pregação de 10 minutos, dividido em 3 partes, com referências bíblicas, a partir de um arquivo markdown de transcrição (gerado pela skill youtube-to-md). Use quando usuário pedir /outline <arquivo.md> ou "esboço de pregação".
---

# outline

Gera esboço de pregação (10 min, 3 partes) a partir de um `.md` de transcrição.

## Uso

```
/outline <caminho/do/arquivo.md>
```

Exemplo:
```
/outline content/youtube/LIVE-21-Dias-de-Jejum-e-Oração-Pr-Wilson-Silva--Cap-02-Coragem-faz-parte-de-uma-Grande-Fé15-09.md
```

## Passos

1. Ler o arquivo `.md` informado (título + texto completo).
2. Extrair o título do vídeo (linha `# Título` do arquivo de origem).
3. Montar esboço com esta estrutura:

```markdown
# Esboço: <Título do vídeo>

## Introdução
(breve gancho/contexto, ~1-2 min)

## Parte 1 — <subtítulo>
(pontos principais, ~3 min)
- referência bíblica (ACF)

## Parte 2 — <subtítulo>
(pontos principais, ~3 min)
- referência bíblica (ACF)

## Parte 3 — <subtítulo>
(pontos principais, ~3 min)
- referência bíblica (ACF)

## Conclusão / Chamado à ação
(~1 min)

## Declaração — Pão
(frase curta, declarada em voz alta, congregação repete antes de comer o pão)

## Declaração — Vinho
(frase curta, declarada em voz alta, congregação repete antes de beber o vinho)
```

4. Todo versículo citado deve estar na versão Almeida Corrigida Fiel (ACF), conforme regra do CLAUDE.md do projeto.
5. Esboço deve caber em leitura/apresentação de ~10 minutos — direto, sem repetir o texto completo da transcrição, só os pontos-chave.
6. As duas Declarações (Pão e Vinho) são frases curtas (uma linha, uma frase só, sem dois pontos separando trechos) de Santa Ceia, baseadas no capítulo do dia — sem citar referência formal, só a frase pronta pra líder falar e congregação repetir. Devem ser confissão da própria Palavra de Deus em Cristo Jesus: tom alegre, cristocêntrico, declarando graça e amor (não pedido, não lamento).
   - **Não usar prefixo fixo.** A frase "Participo desta ceia com meus irmãos e..." está proibida — cada capítulo tem abertura própria.
   - A abertura nasce do contexto do capítulo: reler o `## Resumo` e o `## Texto completo` do arquivo de origem em `content/youtube/` e começar a declaração pela imagem/tema central daquele capítulo (ex.: a botija de azeite, o vento contrário, a coragem, a esperança ancorada), em primeira pessoa e no presente.
   - Cada capítulo deve ter abertura diferente da dos capítulos anteriores já salvos em `content/outline/` — conferir os arquivos existentes antes de escrever, pra não repetir fórmula.
   - Ambas (Pão e Vinho) devem amarrar o mesmo tema central do capítulo — não só o Pão. Vinho não pode ser genérico/repetição de outra live: extrair o tema central específico deste capítulo e aplicar nas duas declarações, cada uma com sua própria variação de frase.
   - Dentro da mesma frase, amarrar o elemento da ceia: "como do corpo de Cristo" (Pão) ou "bebo do sangue de Cristo" (Vinho), ligado por "e" ou "porque" — nunca como frase à parte.
   - Exemplos (formato, não fórmula a copiar):
     - Pão (Cap. Botija de azeite): "A botija que Deus enche não seca, e por isso como do corpo de Cristo sabendo que nEle o pouco vira multiplicação de graça!"
     - Vinho (Cap. Coragem): "O medo não manda mais em mim, porque bebo do sangue de Cristo e nEle já fui perdoado e feito corajoso!"
7. Salvar em `content/outline/<mesmo-nome-do-arquivo-de-origem>.md` (criar pasta `content/outline/` se não existir, mesmo slug do arquivo de entrada).
8. Rodar a skill `/marca-texto` (`.claude/skills/marca-texto/SKILL.md`) nesse mesmo arquivo recém-salvo, pra destacar os trechos-chave antes de considerar a tarefa concluída.

## Requisitos

- Não precisa de script python — feito via leitura (Read) e escrita (Write) direta do markdown.
