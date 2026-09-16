# marca-texto

Lê um `.md` de `content/outline/` e destaca (marca-texto) só os pontos-chave de cada parte/tópico — direto no próprio arquivo.

## Uso

```
/marca-texto <caminho/do/arquivo.md>
```

Exemplo:
```
/marca-texto content/outline/LIVE-21-Dias-de-Jejum-e-Oração-Pr-Wilson-Silva-Cap-02-Coragem-faz-parte-de-uma-Grande-Fé1509.md
```

## Passos

1. Ler o arquivo `.md` informado por completo (Read tool).
2. Por seção (`## Introdução`, `## Parte 1`, `## Parte 2`, `## Parte 3`, `## Conclusão`, declarações), identificar a frase ou trecho mais importante — o que resume a ideia central daquela parte, o "gancho" que não pode ser perdido numa pregação de 10 min.
3. Marcar esse trecho com `***texto***` (negrito + itálico, markdown puro — funciona em qualquer app/viewer, sem depender de HTML embutido nem de highlight `==...==`, que também pode não renderizar em alguns apps mobile).
4. Regras de marcação:
   - No máximo 1-2 marcações por seção — só o essencial, nunca o parágrafo inteiro.
   - Marcar frase ou oração curta (não a referência bíblica inteira, não bullet inteiro se for longo) — o trecho precisa caber num relance de leitura.
   - Preferir a frase que carrega a virada teológica ou o chamado à ação da seção (ex.: a chave de leitura do texto bíblico, o princípio central, o convite prático).
   - Não marcar títulos (`##`), não marcar referência bíblica sozinha, não marcar as Declarações inteiras — só a cláusula central dentro delas, se fizer sentido.
5. Aplicar as marcações via Edit tool diretamente no arquivo original (mesmo arquivo, sem gerar cópia nem pasta nova).
6. Ao final, listar no chat cada trecho marcado, seção a seção, para o usuário conferir.

## Requisitos

- Não reescrever nem resumir o texto — só envolver o trecho escolhido em `***...***`, preservando o resto exatamente como está.
- Formato único (negrito + itálico) para todo trecho marcado — sem variação por categoria.
- Não precisa de script — feito via leitura (Read) e edição (Edit) direta do markdown.
