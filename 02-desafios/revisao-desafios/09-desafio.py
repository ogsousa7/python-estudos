nomes = "  elias, MARIA, joÃO,   ana  "

nomes_limpos = nomes.split(",")

nomes_limpos = [nome.strip().title() for nome in nomes_limpos]

print(nomes_limpos)