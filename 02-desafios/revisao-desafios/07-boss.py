precos = [25, 80, 150, 40, 200, 95, 300, 60]

precos_promocionais = [round(preco - (preco * 0.15), 2) for preco in precos if preco >= 80 if preco - (preco * 0.15) < 200]

print(precos_promocionais)