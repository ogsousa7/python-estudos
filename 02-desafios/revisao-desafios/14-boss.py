import operacoes

try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numeros: "))

    print(f"Soma: {operacoes.somar(n1, n2)}")
    print(f"Multiplicação: {operacoes.multiplicar(n1, n2)}")
    print(f"Potência: {operacoes.potencia(n1, n2)}")

except ValueError:
    print("Digite um numero inteiro!")
