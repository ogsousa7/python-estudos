from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_GASTOS = PASTA_ATUAL / "17-checkpoint-gastos.txt"


def ler_gastos(caminho):

    erros = []
    gastos_validos = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        next(arquivo, None)

        for numero, linha in enumerate(arquivo, start=2):
            produto = linha.strip().lower()

            if not produto:
                continue

            informacoes = produto.split(";")
            # data, descricao, categoria, valor

            if len(informacoes) != 4:
                erros.append(f"Linha {numero}: Registro inválido: {produto} | Quantidade incorreta de campos")

                continue

            data = informacoes[0].strip()
            descricao = informacoes[1].strip()
            categoria = informacoes[2].strip().capitalize()

            if not data: 
                erros.append(f"Linha {numero}: Registro inválido: {produto} | Data vazia")
            
                continue

            if not descricao: 
                erros.append(f"Linha {numero}: Registro inválido: {produto} | Descrição vazia")
            
                continue

            if not categoria: 
                erros.append(f"Linha {numero}: Registro inválido: {produto} | Categoria vazia")

                continue
            
            try:
                valor = float(informacoes[3].replace(",", "."))

                if valor < 0:
                    erros.append(f"Linha {numero}: Registro inválido: {produto} | Valor negativo")
                    
                    continue

            except ValueError:
                erros.append(f"Linha {numero}: Registro inválido: {produto} | Valor não numerico")

                continue

            dicionario = {
                "data": data,
                "descrição": descricao,
                "categoria": categoria,
                "valor": valor
            }

            gastos_validos.append(dicionario)


    return gastos_validos, erros

gastos, erros = ler_gastos(CAMINHO_GASTOS)

print(gastos)
print(erros)