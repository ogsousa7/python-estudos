numeros = [1, 2, 3, 4, 5]

dobrados = [numero * 2 for numero in numeros]

print(dobrados)

# E se eu quiser colocar uma condição?

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)