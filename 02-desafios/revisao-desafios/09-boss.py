frase = "  Python é incrível e Python é poderoso  "

frase_final = frase.strip().lower().split()

frase = [palavra for palavra in frase_final if len(palavra) > 4]

frase_final = "-".join(frase)

print(frase)
print(frase_final)