import csv 
from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_CSV = PASTA_ATUAL / "17-vendas.csv"

with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    faturamento_total = 0
    faturamento_categoria = {}
    maior_faturamento = 0
    produto_maior = ""
    quantidade_produtos = 0

    print("=== RELATÓRIO DE VENDAS ===\n")

    for linha in leitor:
        quantidade = int(linha['quantidade'])
        valor_unitario = float(linha['valor_unitario'])
        categoria = linha['categoria']

        faturamento = quantidade * valor_unitario

        faturamento_total += faturamento

        if categoria in faturamento_categoria:
            faturamento_categoria[categoria] += faturamento
        else:
            faturamento_categoria[categoria] = faturamento

        if faturamento > maior_faturamento:
            maior_faturamento = faturamento
            produto_maior = linha['produto']

        quantidade_produtos += 1

        

    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print("Faturamento por categoria:")

    for categoria, faturamento in faturamento_categoria.items():
        print(f"{categoria}: R$ {faturamento:.2f}")
    
    print("\nProduto com maior faturamento:")
    print(f"{produto_maior} - R$ {maior_faturamento:.2f}\n")
    print(f"Quantidade de produtos: \n{quantidade_produtos}")
