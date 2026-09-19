# youtube-to-md

Projeto converte links do YouTube em arquivos Markdown.

## Regras

- Toda citação de versículo bíblico (resumo, conclusão, qualquer texto gerado) deve usar a versão Almeida Corrigida Fiel (ACF). Se o vídeo citar outra versão, ao referenciar o versículo no markdown gerado, usar o texto da ACF.
- Toda `## Conclusão` (markdown e frase de fechamento do mind-map) deve ser cristocêntrica: Cristo no centro, ênfase na graça, amor e favor de Deus — evangelho da graça (salvos pelo sacrifício de Jesus na cruz, acesso ao Pai por Ele, consumado pela fé, não por mérito). Tom alegre, envolvente, claro, motivador, que desperta desejo de contemplar mais a Deus e conhecê-Lo.
- Declarações de Santa Ceia (Pão e Vinho) nunca começam com prefixo fixo — a frase "Participo desta ceia com meus irmãos..." está proibida. Cada declaração abre pela imagem/tema central do capítulo (lido em `content/youtube/`) e amarra "como do corpo de Cristo" / "bebo do sangue de Cristo" dentro da mesma frase.
- Script principal: `youtube_to_md.py` (raiz). Roda com `python youtube_to_md.py "<URL>"`.
- Saída sempre em `content/youtube/<titulo-slug-do-video>.md`, nunca na raiz.
- Markdown gerado sempre nesta estrutura: `# Título`, `## Resumo`, `## Texto completo`, `## Conclusão`.
- Texto completo é transcrição corrida, sem timestamp.
- Script só gera esqueleto (placeholders `_(preencher)_` em Resumo/Conclusão) — sempre preencher os dois lendo o texto completo antes de considerar tarefa concluída.
- Skill local `/youtube-to-md` (`.claude/skills/youtube-to-md/SKILL.md`) encapsula esse fluxo — usar ela para qualquer pedido de "vídeo do YouTube para markdown".
- Skill local `/outline` (`.claude/skills/outline/SKILL.md`) gera esboço de pregação de 10min em 3 partes a partir de um `.md` já gerado, salvo em `content/outline/<mesmo-nome>.md`, e já roda `/marca-texto` no arquivo gerado ao final.
- Skill local `/mind-map` (`.claude/skills/mind-map/SKILL.md`) gera mapa mental visual (artifact HTML estilo aquarela) a partir de um `.md`, salvo em `content/mind-map/<mesmo-nome>.html`.
- Pastas de saída (`youtube/`, `outline/`, `mind-map/`, `whatsapp/`, `scratchpad/`) ficam todas dentro de `content/`.
- Skill local `/mensagem-whatsapp` (`.claude/skills/mensagem-whatsapp/SKILL.md`) gera a mensagem do dia pra colar no WhatsApp a partir de um `.md` de `content/youtube/`, salva em `content/whatsapp/<mesmo-nome>.md`. Link do site (`https://diego-dm-morais.github.io/a-escada-da-multiplicacao/`) é fixo em toda mensagem. Chamada ao final da pipeline `/pipe-live`.
- Skill local `/pipe-live` (`.claude/skills/pipe-live/SKILL.md`) roda a pipeline completa a partir de um link do YouTube: youtube-to-md → outline → mind-map, em ordem.
- Dependências: `yt-dlp`, `youtube-transcript-api` (pip).
- Skill local `/marca-texto` (`.claude/skills/marca-texto/SKILL.md`) lê um `.md` de `content/outline/` e destaca (`***texto***`, negrito+itálico) só os trechos-chave de cada parte/tópico, editando o arquivo original. Chamada automaticamente pela skill `/outline` ao final de cada geração.
