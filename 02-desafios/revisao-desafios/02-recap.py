frequencias = {
    "teclado": 3,
    "mouse": 2,
    "monitor": 1
}

produto_mais_frequente = None
maior_frequencia = 0

for produto, quantidade in frequencias.items():
    if quantidade > maior_frequencia:
        produto_mais_frequente = produto
        maior_frequencia = quantidade

#print(produto_mais_frequente)
#print(maior_frequencia)


produtos = [
    "mouse",
    "teclado",
    "mouse",
    "monitor",
    "teclado",
    "mouse",
    "headset",
    "teclado"
]

produtos_dicionario = {}

for produto in produtos:
    if produto in produtos_dicionario:
        produtos_dicionario[produto] += 1
    else: 
        produtos_dicionario[produto] = 1   

produtos2 = []

for produto, quantidade in produtos_dicionario.items():
    if quantidade >= 2:
        produtos2.append(produto)

print(produtos2)