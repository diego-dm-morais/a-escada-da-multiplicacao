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
6. As duas Declarações (Pão e Vinho) são frases curtas (uma linha, uma frase só, sem dois pontos separando trechos) de Santa Ceia, baseadas no capítulo do dia (tema do vídeo) — sem citar referência formal, só a frase pronta pra líder falar e congregação repetir. Devem ser confissão da própria Palavra de Deus em Cristo Jesus: tom alegre, cristocêntrico, declarando graça e amor (não pedido, não lamento). Sempre iniciar com "Participo desta ceia com meus irmãos e...", seguido de "como do corpo de Cristo" (Pão) ou "bebo do sangue de Cristo" (Vinho) — e a própria declaração de fé do tema do capítulo entra dentro dessa mesma oração, amarrada com "e" ou "porque", não como frase à parte. Exemplo: "Participo desta ceia com meus irmãos e como do corpo de Cristo, porque em Cristo sou multiplicado com alegria!"
7. Salvar em `content/outline/<mesmo-nome-do-arquivo-de-origem>.md` (criar pasta `content/outline/` se não existir, mesmo slug do arquivo de entrada).
8. Rodar a skill `/marca-texto` (`.claude/skills/marca-texto/SKILL.md`) nesse mesmo arquivo recém-salvo, pra destacar os trechos-chave antes de considerar a tarefa concluída.

## Requisitos

- Não precisa de script python — feito via leitura (Read) e escrita (Write) direta do markdown.
