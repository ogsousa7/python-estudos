notas = {
    "Elias": 8.5,
    "João": 5.0,
    "Maria": 9.0
}

notas_dobradas = {
    nome: nota * 2
    for nome, nota in notas.items()
}

print(notas_dobradas)

# Também da para filtrar apenas os aprovados!

aprovados = {
    nome: nota
    for nome, nota in notas.items()
    if nota >= 7
}

print(aprovados)