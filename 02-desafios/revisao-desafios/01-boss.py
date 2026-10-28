valores = [120, 85, 200, 45, 150, 90, 310, 100]

valores2 = []
for valor in valores:
    if valor > 100:
        valores2.append(valor)

#print(sorted(valores2))

precos = [25, 50, 100, 200]

def calcular_total(precos):
    soma = 0
    for preco in precos:
        soma += preco
    return soma

def aplicar_desconto(total):
    if total >= 200:
        valor_final = total - (total * 0.15)
        return valor_final
    else:
        valor_final = total - (total * 0.05)
        return valor_final


soma = calcular_total(precos)
desconto = aplicar_desconto(soma)

print(soma)
print(desconto)