numeros = [40, 10, 30, 20]

ordenados = sorted(numeros)

print(ordenados)
print(numeros)

# da também em forma decrescente 

print(sorted(numeros, reverse=True))

# e oque é a "key"?

nomes = ["Elias", "Ana", "Matheus", "João"]

ordenados = sorted(nomes, key=len) # ordenou pela a quantidade de letras em ordem crescente

print(ordenados)

# e se quisermos ordenar uma lista de dicionarios?

produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900}
]

produtos_ordenados = sorted(
    produtos,
    key=lambda produto: produto["preco"]
)

print(produtos_ordenados)