def analisar_dados(*numeros, **opcoes):
    total = 0 
    maior = numeros[0]
    menor = numeros[0]
    for numero in numeros:
        total += numero
        if maior < numero:
            maior = numero
        if menor > numero:
            menor = numero

    media = total / len(numeros)

    resultado = {}

    if opcoes.get("soma", False):
        resultado["soma"] = total

    if opcoes.get("maior", False):
        resultado["maior"] = maior

    if opcoes.get("menor", False):
        resultado["menor"] = menor

    if opcoes.get("media", False):
        resultado["media"] = media

    return resultado

resultado = analisar_dados(
    10, 20, 30, 40,
    soma=True,
    maior=True,
    menor=True,
    media=True
)

print(resultado)