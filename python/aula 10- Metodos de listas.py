# metodos de listas

lista = [1,3, 12,8, 2 ]

#append
print(lista)

lista.append (3)

print( 'depois do append',lista)

#insert para inserir elementos a lista

lista.insert(2,10)

print ('depois do insert', lista)

#extend para juntar 2 listas

lista2 = [1,2,3]

lista.extend(lista2)

print ('depois do extend', lista)

# pop usado para remover elemento

lista.pop()

print( 'lista após o pop',lista)

lista.pop(0)
print('lista após o pop',lista)

#remove diz o valor que quer remover

lista.remove(3)

print ('depois do remove',lista)

# count para contar o numero de elementos da lista

print('quantidade de 2 na lista =',lista.count(2))

# index te fala o indice de um elemento
print ('qual o indice o elemento 12 =',lista.index(12))

#sort serve para ordenar uma lista

lista.sort()

print(lista)
# para organizar de forma decrescente
lista.sort(reverse= True)

print (lista)

# funções para listas

# len = para saber quantos elementos há na lista

print(len(lista))

#sum = soma dos elementos

print(sum(lista))

#max = maximo

print('maior elementos da lista',max(lista))

#min = minimo

print ('menor elemento da lista', min(lista))
