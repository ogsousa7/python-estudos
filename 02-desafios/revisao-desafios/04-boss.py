def processar_pedido(precos, desconto=0, frete=10):
    subtotal = 0
    for preco in precos:
        subtotal += preco

    desconto2 = subtotal * desconto

    total_final = subtotal - desconto2 + frete

    return {
        "subtotal": subtotal,
        "desconto": desconto2,
        "frete": frete,
        "total_final": total_final
    }

produtos = [50, 80, 120]

resultado = processar_pedido(produtos, desconto=0.10, frete=15)

print(resultado)