# 🐍 Python: estudos

Minha trilha de estudos em Python, preparando para **Análise e Engenharia de Dados**.
Cada pasta tem o código das aulas e os desafios que resolvi depois, sem IA e sem copiar solução.

## 📂 Estrutura

```text
python-estudos/
├── 01-aulas/
│   ├── 01-revisao-python/   # 01 a 15: listas, dicionários, funções, comprehensions,
│   │                        #          strings, tuplas, ordenação, lambda, try/except, módulos, venv
│   └── 02-python-solido/    # 16: leitura e escrita de arquivos
└── 02-desafios/
    ├── revisao-desafios/    # desafios das aulas 01 a 15 (normal e "boss", o nível mais difícil)
    └── solidos-desafios/    # desafios da aula 16 e o checkpoint 17
```

## 🎯 Destaque: checkpoint 17, controle de gastos

Um arquivo de gastos escrito "à mão", com problemas de propósito: linha vazia, linha sem o valor, valor
com vírgula, valor negativo ou que não é número e categoria escrita de jeitos diferentes. O programa lê, **limpa e valida** os dados, **agrega por categoria** e gera um **relatório em JSON**.
É a mesma rotina de um trabalho de dados: dado bruto → dado limpo → informação.

Enunciado: [`17-checkpoint-enunciado.md`](02-desafios/solidos-desafios/17-checkpoint-enunciado.md)

## ▶️ Como rodar

Com o Python 3 instalado, entre na pasta do arquivo e rode:

```bash
python nome-do-arquivo.py
```

## 🔗 Relacionado

- [Mini Loja](https://github.com/ogsousa7/mini-loja-python): projeto de estoque e vendas com relatórios, feito a partir destes estudos.
