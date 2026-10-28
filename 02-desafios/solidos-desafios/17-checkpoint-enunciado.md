# Checkpoint de Python (17): Controle de Gastos

**Objetivo:** ver se você transfere o que usou na Mini Loja para um problema diferente: ler dados "sujos" de um arquivo, validar, agregar e gerar um relatório. Não é prova, é diagnóstico.

**Pasta:** `python-estudos/02-desafios/`

| Arquivo | Caminho completo |
|---|---|
| Dados (já está na pasta) | `python-estudos/02-desafios/17-checkpoint-gastos.txt` |
| Desafio normal | `python-estudos/02-desafios/17-checkpoint-desafio.py` |
| Boss | `python-estudos/02-desafios/17-checkpoint-boss.py` |
| Saída gerada pelo boss | `python-estudos/02-desafios/17-checkpoint-relatorio.json` |

**Pré-requisito:** Aula 16 (arquivos de texto) concluída.

**Conceitos cobrados:** funções com `return`, listas de dicionários, loops + `continue`, strings (`strip`, `split`, `replace`, `title`/`lower`), conversão de tipos, `try/except`, leitura de arquivo com `with open`, agregação com dicionário, `sorted` com `key`, JSON e `pathlib`.

## O cenário

Você anota seus gastos num arquivo de texto, uma linha por gasto, separado por `;`:

```
data;descricao;categoria;valor
```

O arquivo `17-checkpoint-gastos.txt` foi escrito "na mão", então tem problema de propósito. Leia ele com atenção antes de codar. Salve em UTF-8.

## Regras do jogo

- Sem IA e sem copiar solução da internet. Pode olhar seus próprios arquivos antigos.
- Se consultar documentação, anote no topo do arquivo, num comentário, **o que** consultou. Isso não desconta nada, só me mostra onde está a lacuna.
- Não use o módulo `csv` ainda (ele vem na aula 18). Aqui é `split` mesmo.
- Funções de cálculo **retornam** valores e **não imprimem**. Quem imprime é uma única função `main()` (ou o bloco final do arquivo).

## Desafio normal — `17-checkpoint-desafio.py`

1. **`ler_gastos(caminho)`**
   Lê o arquivo e retorna **duas coisas**: a lista de gastos válidos (cada um um dicionário com `data`, `descricao`, `categoria`, `valor`) e a lista de erros.
   - Pula o cabeçalho.
   - Linha em branco é ignorada em silêncio (não é erro).
   - Linha com campo faltando, valor que não é número ou valor menor ou igual a zero **não derruba o programa**: vira um erro registrado com o **número da linha no arquivo** e o **motivo**.
   - Categoria normalizada: sem espaços sobrando e com capitalização padronizada (`" alimentação "` e `"Alimentação"` são a mesma categoria).
   - Valor com vírgula decimal (`12,50`) é aceito como `12.50`.

2. **`total_por_categoria(gastos)`** → dicionário `{categoria: total}`.

3. **`resumo(gastos)`** → um dicionário com: total geral, quantidade de gastos, média por gasto, o maior gasto (o dicionário inteiro dele) e a categoria que mais gastou.

4. **Arquivo inexistente:** se o caminho estiver errado, mensagem amigável, sem traceback.

5. **Imprima** o relatório: totais por categoria com 2 casas decimais, o resumo e os erros (linha + motivo).

**Pra você conferir:** com o arquivo fornecido, devem sair **7 gastos válidos, 3 erros e total geral de R$ 245.00**. Se não bater, o bug é seu pra caçar 😄

## Boss — `17-checkpoint-boss.py`

Pode partir do código do normal (importar ou copiar, sua escolha, mas justifique num comentário).

1. **Orçamento:** use este dicionário de limites mensais:
   ```python
   limites = {"Alimentação": 80, "Transporte": 20, "Educação": 100}
   ```
   Crie uma função que retorna, para cada categoria gasta, o status: `"dentro"`, `"estourou"` (com quanto passou) ou `"sem limite definido"`.

2. **Ranking:** categorias ordenadas do maior total pro menor, e os 3 maiores gastos individuais. A lista original de gastos **não pode** mudar de ordem.

3. **Relatório em JSON:** salve tudo (resumo, totais por categoria, ranking, orçamento e erros) em `17-checkpoint-relatorio.json`, **na mesma pasta do script**, não importa de onde você rode o programa.

4. **Casos extremos:** o programa precisa funcionar sem quebrar se o arquivo tiver só o cabeçalho, ou se **todas** as linhas forem inválidas. Teste criando um segundo arquivo pequeno. (Pense: o que acontece com a média e com o "maior gasto" nesse caso?)

5. **Perguntas pra responder em comentário no final do arquivo** (curto, com suas palavras):
   - a) Dentro do loop que lê as linhas, por que usar `continue` numa linha inválida e não `break` ou `return`? O que cada um faria ali?
   - b) Por que no item 2 do boss `sorted()` serve e `.sort()` seria um problema?
   - c) Se `ler_gastos` imprimisse os gastos em vez de retornar, o que ficaria impossível de fazer no resto do programa?

## Como entregar

Manda os dois `.py` aqui no chat (ou fala que salvou na pasta). Eu reviso separando **bug** de **melhoria opcional**. Se travar, me fala onde; a ajuda vem em degraus: onde está o problema → dica → exemplo menor → solução só se você pedir.
