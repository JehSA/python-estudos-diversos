# Métodos de lista

lista = [1, 3, 12, 8, 2]
print('lista antes', lista)

lista.append(3)
print('lista depois do append', lista)

lista.insert(2, 10)
print('lista depois do insert', lista)

lista2 = [1, 2, 2]

lista.extend(lista2)
print('lista depois do extend', lista)

lista.pop()
print('lista depois do pop', lista)
lista.pop(2)
print('lista depois do pop', lista)

lista.remove(3)
print('lista depois do remove', lista)

print('Quantidades de 3 na lista:', lista.count(3))
print('Quantidades de 2 na lista:', lista.count(2))

print('Indice do elemento:', lista.index(12))

# Organiza de forma crescente e decrescente
lista.sort()
print('Lista organizada - cerscente', lista)
lista.sort(reverse = True)
print('Lista organizada - decrescente', lista)


# Funções para lista
print(len(lista))
print(sum(lista))
print(min(lista))
print(max(lista))