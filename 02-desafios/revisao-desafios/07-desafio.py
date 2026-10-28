notas = [4, 7, 9, 5, 10, 6, 8, 3]

notas_aprovadas = [min(nota + 1, 10) for nota in notas if nota >= 7]

print(notas_aprovadas)