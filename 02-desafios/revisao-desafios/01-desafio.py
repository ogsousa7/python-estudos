valores = [120, 85, 200, 45, 150, 90, 310, 100]

print(sum(valores))

print((sum(valores) / (len(valores))))

print(max(valores))
print(min(valores))

quantidade = 0
for valor in valores:
    if valor > 100:
        quantidade += 1