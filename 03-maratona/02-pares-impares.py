qtd_n = int(input(""))

valores = []
for i in range(qtd_n):
    num = int(input(""))

    valores.append(num)

pares = 0 
impares = 0
soma_pares = 0

for valor in valores:
    if valor % 2 == 0:
        pares += 1

        soma_pares += valor
    else:
        impares += 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")
print(f"Soma dos pares: {soma_pares}")