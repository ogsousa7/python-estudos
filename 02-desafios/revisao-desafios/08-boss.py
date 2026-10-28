estoque = {
    "teclado": 12,
    "mouse": 4,
    "monitor": 0,
    "headset": 7,
    "mousepad": 2,
    "webcam": 10
}

estoque_alerta = {
    nome: quantidade * 2
    for nome, quantidade in estoque.items()
    if quantidade > 0 
    if quantidade < 8 
}

print(estoque_alerta)