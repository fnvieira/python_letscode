# ESTRUTURAS CONDICIONAIS
idade= 19

if idade >= 18:
    print ('voce é maior de idade!')
else:
    print('voce é menor de idade')

media = float (input('informe a media'))
if media >=7:
    print ('voce foi aprovado')
elif media >=5:
    print ('voce foi para recuperação')
else:
    print('voce foi reprovado')


    '''codigo para trazer media e presença'''

    media= 5
    presenca= 60

    if media >=7 and presenca>=70:
        print ('aprovado')
        print ('parabens')
    else:
        print('reprovado')