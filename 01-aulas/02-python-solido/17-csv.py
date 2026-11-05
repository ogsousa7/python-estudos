import csv
from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_CSV = PASTA_ATUAL / "17-vendas.csv"

with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
    #leitor = csv.reader(arquivo)
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        valor = float(linha["valor"])

        print(f"Produto: {linha["produto"]} | Categoria: {linha["categoria"]} | Valor: R${valor}")