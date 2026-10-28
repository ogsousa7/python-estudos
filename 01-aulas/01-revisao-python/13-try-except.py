# usando o try para tratar erros

'''try:
    idade = int(input("Digite sua idade: "))
    print(f"Sua idade é {idade}")
except ValueError:
    print("Voce precisa digitar um numero inteiro!")'''

# também da varios tratamentos

"""try:

    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo numero: "))

    resultado = a / b
    print(resultado)

except ValueError:

    print('Digite apenas numeros inteiros!')

except ZeroDivisionError:

    print("Não é possivel dividir por zero!")"""


# tem mais funcoes!

try: 
    numero = int(input("Digite um numero: "))
except ValueError:
    print("Digite um numero inteiro!")
else:
    print(f"Você digitou o numero {numero}")
finally:
    print("Programa finalizado.")