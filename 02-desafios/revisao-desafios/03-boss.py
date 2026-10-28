numeros = [4, 9, 2, 7]

def analisador_numeros(numeros):
    maior = numeros[0]
    menor = numeros[0]
    soma = 0

    for numero in numeros:
        soma += numero
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    media = soma / len(numeros)

    return maior, menor, soma, media

print(analisador_numeros(numeros))