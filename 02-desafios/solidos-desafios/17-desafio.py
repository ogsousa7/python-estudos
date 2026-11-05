import csv
from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_VENDAS = PASTA_ATUAL / "17-vendas.csv"

with open(CAMINHO_VENDAS, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    faturamento_total = 0

    print("=== RELATÓRIO DE VENDAS ===\n")

    for linha in leitor:
        quantidade = int(linha["quantidade"])
        valor_unitario = float(linha["valor_unitario"])

        faturamento = quantidade * valor_unitario
        faturamento_total += faturamento

        print(f"Produto: {linha["produto"]} | Faturamento: R$ {faturamento:.2f}")

    print(f"\nFaturamento total da empresa: R$ {faturamento_total:.2f}")