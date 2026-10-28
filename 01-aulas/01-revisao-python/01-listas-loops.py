valores  = [120, 85, 200, 45, 150, 90, 310, 100]

print(valores[0])
print(valores[2])
print(len(valores))


valores.append(250)
valores.sort()

print(valores)


valores = [120, 85, 200, 45]

for valor in valores:
    print(valor)


for valor in valores:
    if valor > 100:
        print(valor)


total = 0

for valor in valores:
    total += valor

print(total)


quantidade = 0

for valor in valores:
    if valor > 100: 
        quantidade += 1

print(quantidade)        