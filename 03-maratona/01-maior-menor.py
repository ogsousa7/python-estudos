qntd_valores = 5
valores = [12, 45, 7, 89, 23]

maior = valores[0]
menor = valores[0]
for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")