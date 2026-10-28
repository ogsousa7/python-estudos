venda = {
    "produto": "Teclado",
    "preco": 150,
    "quantidade": 3
}

print(venda["produto"])
print(venda["preco"])

venda["quantidade"] = 5
venda["categoria"] = "Perifericos"

print(venda)

# ----------------------------------------------

categorias = ["teclado", "mouse", "teclado", "monitor", "mouse"]

categorias_unicas = set(categorias)

print(categorias_unicas)

