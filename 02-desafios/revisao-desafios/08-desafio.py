produtos = {
    "teclado": 120,
    "mouse": 50,
    "monitor": 900,
    "headset": 180,
    "mousepad": 30
}

produtos_caros = {
    nome: produto - (produto * 0.10)
    for nome, produto in produtos.items()
    if produto >= 100
}

print(produtos_caros)