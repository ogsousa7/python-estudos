aluno = ["Elias", 16, "Python", 8.5, "Aprovado"]

def analisador_aluno(aluno):
    nome, idade, linguagem, nota, situacao = aluno

    return {
        "Nome": nome,
        "Idade": idade,
        "Linguagem": linguagem,
        "Nota": nota,
        "Situacao": situacao
    }

analisar = analisador_aluno(aluno)

print(analisar)