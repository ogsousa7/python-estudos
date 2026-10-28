def somar_numeros(*numeros):
    total = 0 

    for numero in numeros:
        total += numero

    return total

print(somar_numeros(10,20))
print(somar_numeros(5, 10, 15, 20))
print(somar_numeros(7))