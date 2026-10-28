import math

try: 
    raio = float(input("Digite o raio de um circulo: "))

    area = math.pi * math.pow(raio, 2)

    print(f"A area aredondada é {round(area)}")

except ValueError:
    print("Digite um numero!")    