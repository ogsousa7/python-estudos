qtd = int(input(""))

valores = []
for i in range(qtd):
    num = int(input(""))

    valores.append(num)

num_posicao = int(input(""))

index = -1
encontrado = False
for valor in valores:
    index += 1
    if num_posicao == valor:
        encontrado = True
        print(f"Numero encontrado na posição: {index}")
        break

if not encontrado:
    print("Numero não encontrado")