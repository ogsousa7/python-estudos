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

print(produtos_dicionario)        