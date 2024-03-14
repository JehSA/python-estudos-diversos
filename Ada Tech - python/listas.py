notas = [9.7, 8, 4]

# Listas vazias
lista = []
lista2 = list()

lista3 = ['Jefferson', 4, 7.7, True]

lista_de_listas = [10, [1, 2, 3], lista3]


# Indexação de slices (fatiamento)
lista3 = ['Jefferson', 4, 7.7, True]
print(lista3[0], lista3[3])
print(lista3[-1])


# Slices
lista4 = [10, 20, 30, 40, 50, 60]
print(lista4[2:5])
print(lista4[1:6:2])

# Iterações com For
for elemento in lista4:
    print(elemento)


print('Quantidade de elementos da lista', len(lista4))

for i in range(len(lista4)):
    print(lista4[i])