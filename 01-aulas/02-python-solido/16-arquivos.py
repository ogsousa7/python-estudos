"""with open("16-compras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        item = linha.strip()
        if item == "":
            continue
        print(item.title())"""


with open("16-compras.txt", "r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, start=1):
        print(numero, repr(linha))