produtos = [
    {"nome": "Teclado", "preco": 150, "estoque": 8},
    {"nome": "Mouse", "preco": 80, "estoque": 15},
    {"nome": "Monitor", "preco": 900, "estoque": 3},
    {"nome": "Headset", "preco": 200, "estoque": 0},
    {"nome": "Webcam", "preco": 120, "estoque": 5},
    {"nome": "Mousepad", "preco": 30, "estoque": 20}
]

ordenados_preco = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)

ordenados_estoque = sorted(produtos, key=lambda produto: produto["estoque"])

nova_lista = []

for produto in produtos:
    if produto["estoque"] > 0:
        nova_lista.append(produto)

produtos_disponiveis = sorted(
    nova_lista,
    key=lambda produto: produto["preco"]
)

print(produtos_disponiveis)