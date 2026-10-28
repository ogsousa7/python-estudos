produto = ("Teclado", 150.00, 8, "Perifericos")

nome, preco, estoque, categoria = produto

print(f"O produto {nome}, é R${preco}, tem {estoque} itens no estoque e é da categoria {categoria}.")

print(len(produto))

print("Teclado" in produto)