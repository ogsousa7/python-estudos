entradas = ["10", "25", "abc", "0", "8", "3.5", "-2"]

resultados = []
erros = 0

for entrada in entradas:

    try:
        numero = int(entrada)

        resultado = 100 / numero

        resultados.append(resultado)

    except ValueError:
        print("O valor precisa ser um numero inteiro!")
        erros += 1

    except ZeroDivisionError:
        print("Impossivel divir por zero!")
        erros += 1

print(resultados)
print(erros)