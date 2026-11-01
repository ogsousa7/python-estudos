from pathlib import Path
import math

PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_GASTOS = PASTA_ATUAL / "17-checkpoint-gastos.txt"


def ler_gastos(caminho):

    erros = []
    gastos_validos = []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            next(arquivo, None)

            for numero, linha in enumerate(arquivo, start=2):
                produto = linha.strip()

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

                    if not math.isfinite(valor):
                        erros.append(f"Linha {numero}: Registro inválido: {produto} | Valor não finito")

                        continue

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
    
    except FileNotFoundError:
        erros.append(f"Arquivo '{caminho}' não encontrado!")

        return gastos_validos, erros
    

gastos, erros = ler_gastos(CAMINHO_GASTOS)


def total_por_categoria(gastos):
    totais = {}

    for gasto in gastos:
        categoria = gasto["categoria"]
        valor = gasto["valor"]

        if categoria in totais:
            totais[categoria] += valor
        else:
            totais[categoria] = valor

    return totais

def resumo(gastos):
    if not gastos:
        return {
            "Total-gasto": 0,
            "Quantidade-de-gastos": 0,
            "Média-por-gasto": None,
            "Maior-gasto-individual": None,
            "Categoria-com-maior-gasto-acumulado": None
        }

    totais = total_por_categoria(gastos)

    total_gasto = sum(gasto["valor"] for gasto in gastos)
    quantidade = len(gastos)
    media = total_gasto / quantidade
    maior_gasto = max(gasto["valor"] for gasto in gastos)
    categoria_maior_total = max(totais, key=totais.get)

    return {
        "Total-gasto": total_gasto,
        "Quantidade-de-gastos": quantidade,
        "Média-por-gasto": media,
        "Maior-gasto-individual": maior_gasto,
        "Categoria-com-maior-gasto-acumulado": categoria_maior_total
    }

resumo1 = resumo(gastos)
print(resumo1)
print(resumo([]))