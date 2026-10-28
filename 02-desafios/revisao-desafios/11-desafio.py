alunos = [
    ("Marina", 8.5),
    ("Carlos", 6.0),
    ("Ana", 9.5),
    ("Pedro", 7.0),
    ("Lucas", 8.0)
]

alunos_ordenados = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)

print(alunos_ordenados)

alunos_ordenados_nomes = sorted(alunos, key=lambda aluno: aluno[0])

print(alunos_ordenados_nomes)