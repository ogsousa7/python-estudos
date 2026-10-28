# Lambda é uma funcao anonima e pequena kkakaka 

dobrar = lambda numero: numero * 2 # aqui o "numero" depois do lambda é o parametro e depois do ":" é oque vai acontecer na funcao 

print(dobrar(5))

# varios parametros também funcionam!

somar = lambda a, b: a + b

print(somar(10, 5))

# da para combinar em condições com operadores ternarios 

maioridade = lambda idade: "Maior" if idade >= 18 else "Menor"

print(maioridade(180))