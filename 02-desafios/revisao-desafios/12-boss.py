alunos = [
    {"nome": "Elias", "nota": 8.5},
    {"nome": "Marina", "nota": 9.5},
    {"nome": "João", "nota": 6.0},
    {"nome": "Ana", "nota": 7.5},
    {"nome": "Carlos", "nota": 5.5}
]

alunos_ordenados_notas = sorted(alunos, key= lambda aluno: aluno["nota"], reverse=True)

nova_lista = []

for aluno in alunos:
    if aluno["nota"] >= 7:
        nova_lista.append(aluno)

nova_lista_ordenada = sorted(nova_lista, key= lambda aluno: aluno["nome"])

media_alunos = 0

for aluno in alunos:
    media_alunos += aluno["nota"]

media_alunos = media_alunos / len(alunos)

print(f"Ranking melhores alunos: \n{alunos_ordenados_notas}")
print(f"Aprovados: \n{nova_lista_ordenada}")
print(f"Média geral: {media_alunos}")