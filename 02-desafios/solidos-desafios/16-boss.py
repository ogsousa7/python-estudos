from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_ARQUIVO = PASTA_ATUAL / "16-estoque.txt"
CAMINHO_RELATORIO = PASTA_ATUAL / "16-reposicao.txt"
CAMINHO_LOG = PASTA_ATUAL / "16-log.txt"

def ler_estoque():

    estoque = []

    erros = []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        next(arquivo, None) # consome a primeira linha, e o segundo parametro é oque ocorre caso ele estiver completamente vazio

        for linha in arquivo:
            produto = linha.strip().lower()

            if not produto:
                continue

            informacoes = produto.split(";")
            

            if len(informacoes) != 2:
                erros.append(f"Registro inválido: {produto} | Formato incorreto")
                continue

            nome = informacoes[0].strip()

            if not nome:
                erros.append(f"Registro inválido: {produto} | Nome vazio")
                continue

            try:
                quantidade = int(informacoes[1])

                if quantidade < 0:
                    erros.append(f"Registro inválido: {produto} | Quantidade negativa")
                    continue
            except ValueError:
                print("Quantidade invalida!")
                erros.append(f"Registro invalido: {produto} | Quantidade não numerica")

                continue

            dicionario = {
                "produto": nome,
                "quantidade": quantidade
            }

            estoque.append(dicionario)

    return estoque, erros

estoque, erros = ler_estoque()

def gerar_relatorio(estoque):

    produtos_baixo_estoque = []

    for produto in estoque:
        if produto["quantidade"] < 5:
            produtos_baixo_estoque.append(produto)

    with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATORIO DE REPOSIÇÃO\n\n\n")

        for produto in produtos_baixo_estoque:
            arquivo.write(f"{produto["produto"]}: {produto["quantidade"]} unidades\n")

        arquivo.write(f"\n\nTotal de produtos para reposição: {len(produtos_baixo_estoque)}")


def gerar_log(erros):
    with open(CAMINHO_LOG, "w", encoding="utf-8") as arquivo:
        arquivo.write("LOG DE PROCESSAMENTO\n\n")

        for erro in erros:
            arquivo.write(f"{erro}\n")

        arquivo.write(f"\nTotal de registros inválidos: {len(erros)}")

gerar_relatorio(estoque)
gerar_log(erros)