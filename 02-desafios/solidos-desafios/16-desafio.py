from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_ARQUIVO = PASTA_ATUAL / "16-produtos.txt"

produtos = []

with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:

        produto = linha.strip().lower()

        if not produto:
            continue

        produtos.append(produto)

def contar_produtos(produtos):
    contagem = {}

    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

    return contagem

contagem = contar_produtos(produtos)

print(f"Produtos analisados: {len(produtos)}")
print(f"Produtos diferentes: {len(contagem)}")

maior_quantidade = max(contagem.values())
nome_maior = []

for nome, quantidade in contagem.items():
    print(f'{nome}: {quantidade}')

    if quantidade == maior_quantidade:
        nome_maior.append(nome)

print(f"Maior frequencia: {maior_quantidade}")
print(f"Produtos mais frequentes: {', '.join(nome_maior)}")