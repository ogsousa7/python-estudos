notas = [7, 8, 9, 6]

def calcular_media(numeros):
    soma = 0
    for nota in numeros:
        soma += nota

    media = soma / len(numeros)
    return media

print(calcular_media(notas))