def saudar(nome="programador"):
    print(f"Olá, {nome}!")

saudar()
saudar("Elias")

# ----------------

def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos.")

apresentar(idade=16, nome= "Elias")

# -----------------

def calcular_preco(preco, desconto=0):
    return preco - (preco * desconto)

print(calcular_preco(100))
print(calcular_preco(100, desconto=0.15))