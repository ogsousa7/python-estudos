produtos = (
    ("Teclado", 150.00, 8),
    ("Mouse", 80.00, 15),
    ("Monitor", 900.00, 3),
    ("Headset", 200.00, 0),
    ("Webcam", 120.00, 5)
)

estoque_igual_zero = 0
nova_lista = []
valor_total = 0

for produto in produtos:
    nome, preco, estoque = produto
    print(f"{nome} - R${preco} - {estoque}")
    if estoque == 0:
        estoque_igual_zero += 1

    if estoque < 6:
        nova_lista.append(nome)

    valor_total += preco * estoque

print(f"Produtos sem estoque: {estoque_igual_zero}")
print(f"Produtos com estoque menor que 6: {nova_lista}")
print(f"Valor total do estoque: R$ {valor_total}")