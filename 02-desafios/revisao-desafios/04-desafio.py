def calcular_preco_final(preco, desconto=0, frete=10):
    return preco - (preco * desconto) + frete

print(calcular_preco_final(100))
print(calcular_preco_final(100, desconto=0.20))
print(calcular_preco_final(100, desconto=0.20, frete=0))