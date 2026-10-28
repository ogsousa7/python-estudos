def analisador_numeros():
    return 40, 10, 25

maior, menor, media = analisador_numeros()

print(maior)
print(menor)
print(media)

# Também funciona com listas!

produto = ["teclado", 150, 10]

nome, preco, estoque = produto

print(nome)
print(preco)
print(estoque)

# E se eu nao precisar de uma informação?

nome, _, idade = ["Elias", "Sao Paulo", 16]

print(nome)
print(idade)