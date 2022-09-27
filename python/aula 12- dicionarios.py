# em busca de palavras 

#criando Dicionarios

dicionario = {}
dicionario = dict()

dicionario = { 'nome':'fernando','idade':26, 'altura':1.85 }
print(dicionario)
print(dicionario['idade'])

# adiocionando elementos em dicionario

dicionario ['programador']= True

print (dicionario)

dicionario ['altura']= 2
print (dicionario)

#interando sobre um dicionario

for chave in dicionario:
    print( chave, dicionario[chave])

#testando a existencia de uma chave

print('peso' in dicionario)
print ('altura' in dicionario)