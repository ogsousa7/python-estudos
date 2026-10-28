def somar_precos(*precos):
    total = 0

    for preco in precos:
        total += preco

    return total

print(somar_precos(10,20))
print(somar_precos(10, 20, 30, 40))