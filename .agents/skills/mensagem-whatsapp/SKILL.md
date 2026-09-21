---
name: mensagem-whatsapp
description: Gera a mensagem de WhatsApp do dia para convidar a família/célula a acompanhar o capítulo da série — saudação, frase de motivação em Cristo ligada ao capítulo, links (YouTube, Instagram, site) e convite final. Use quando o usuário pedir /mensagem-whatsapp <arquivo.md> ou "mensagem do dia para o WhatsApp".
---

# mensagem-whatsapp

Gera a mensagem pronta para colar no WhatsApp, a partir de um `.md` já gerado em `content/youtube/`.

A mensagem é sempre enviada **no dia** da live — o texto fala do capítulo de hoje, no presente.

## Uso

```
/mensagem-whatsapp <caminho/do/arquivo.md> [--saudacao "Boa tarde"]
```

Exemplo:

```
/mensagem-whatsapp content/youtube/LIVE-21-Dias-de-Jejum-e-Oração-Pr-Wilson-Silva-Cap-6-1909.md
```

## Passos

1. Ler o `.md` informado: título, `## Resumo`, `## Conclusão` e, se precisar de imagem/tema central, o `## Texto completo`.
2. Extrair:
   - **Número do capítulo** (do título, ex.: "Cap. 6" → `6`).
   - **Tema central** do capítulo (do Resumo — ex.: "andar como corpo aumenta a sua fé").
   - **Link do YouTube** — o campo `- **URL:**` do topo do arquivo.
3. Montar a mensagem seguindo o template abaixo.
4. Salvar em `content/whatsapp/<mesmo-nome-do-arquivo-de-origem>.md` (criar a pasta `content/whatsapp/` se não existir).
5. Imprimir a mensagem inteira no chat, dentro de um bloco de código, pronta para o usuário copiar e colar no WhatsApp.

## Template

```
<Saudação>, família! 🙏❤️

Mais um dia do nosso jejum! Hoje estamos no capítulo <N>.

<Frase de motivação em Cristo, ligada ao tema do capítulo — 2 a 3 linhas.>

📖 Link do capítulo <N>:
<URL do YouTube>

Meio dia estaremos com o Pr Isaías no instagram
<URL do Instagram>

🧠 Mapa mental geral de todos os capítulos, que desenvolvi para facilitar o acompanhamento e a revisão:
https://diego-dm-morais.github.io/a-escada-da-multiplicacao/

<Convite final: motiva, chama para participar e deseja um lindo dia.> 🙏🔥
```

## Regras

- **Tom obrigatório:** alegria, comunhão e amor em Cristo. Mensagem de família, não de aviso institucional.
- **Cristocêntrica:** a motivação aponta para o que Cristo já fez — graça, favor e amor de Deus — nunca para esforço ou mérito de quem lê.
- **Frase de motivação muda a cada capítulo:** nasce do tema central daquele dia (ler o Resumo antes de escrever). Nunca reaproveitar a frase de um capítulo anterior — conferir os arquivos já salvos em `content/whatsapp/` antes de escrever.
- **Convite final também muda a cada capítulo**, mas sempre com as três coisas: convite para participar, motivação e desejo de um lindo dia.
- **Links:**
  - YouTube: o do capítulo do dia, lido do próprio `.md`.
  - Instagram: `https://www.instagram.com/prisaiasnog/` — **fixo, sempre esse, em toda mensagem**.
  - Site (mapa mental geral): `https://diego-dm-morais.github.io/a-escada-da-multiplicacao/` — **fixo, sempre esse, em toda mensagem**.
- **Saudação:** `Bom dia` por padrão (a live é de manhã); só muda se o usuário passar `--saudacao`.
- Emojis com moderação, como no template — abertura (🙏❤️), links (📖, 🧠) e fechamento (🙏🔥).
- Se citar versículo, usar Almeida Corrigida Fiel (ACF), conforme regra do AGENTS.md do projeto.
- Mensagem curta o bastante para ler de relance no celular — sem parágrafo longo, sem repetir o resumo inteiro do capítulo.

## Requisitos

- Não precisa de script — feito via leitura (Read) e escrita (Write) direta do markdown.
