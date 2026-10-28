produtos = [
    "teclado", "mouse", "teclado",
    "monitor", "mouse", "teclado"
]

produtos_dicionario = {}

for produto in produtos:
    if produto in produtos_dicionario:
        produtos_dicionario[produto] += 1
    else: 
        produtos_dicionario[produto] = 1   

print(f"existem {len(set(produtos))} categorias de produtos!")

print(f"o produto de maior quantidade é {max(produtos_dicionario,key=produtos_dicionario.get)}")

print(set(produtos))
