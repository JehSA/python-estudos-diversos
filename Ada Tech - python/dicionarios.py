# Dicionarios vazios
dicionarioVazio1 = {}
dicionarioVazio2 = dict()

dicionario = {
    'nome': 'Jefferson',
    'idade': 26,
    'altura': 1.55
}

print(dicionario)
print(dicionario['idade'])

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 1.54
print(dicionario)

# Iterando no dicionario
for variavel in dicionario:
    print(variavel)

for chave in dicionario:
    print(chave, dicionario[chave])


print('peso' in dicionario)
print('altura' in dicionario)
