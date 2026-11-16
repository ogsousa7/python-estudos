qtd = int(input(""))

valores = []
for i in range(qtd):
    num = int(input(""))

    valores.append(num)

primeiro_maior = float("-inf") # -inf representa menos infinito. Assim, qualquer número real será maior que ele.
segundo_maior = float("-inf")

for valor in valores:
    if valor > primeiro_maior:
        segundo_maior = primeiro_maior
        primeiro_maior = valor
    elif valor > segundo_maior and valor != primeiro_maior:
        segundo_maior = valor

print(f"Segundo maior valor: {segundo_maior}")