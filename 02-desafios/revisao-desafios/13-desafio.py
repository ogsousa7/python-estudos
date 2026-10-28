try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))

    resultado = n1 / n2

    print(resultado)
except ValueError:
    print("Digite um numero inteiro!")

except ZeroDivisionError:
    print("Não da para dividir por zero!")