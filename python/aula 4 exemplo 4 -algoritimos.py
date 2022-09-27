'''Exemplo 4: Desenvolva um algoritmo que calcule o valor total de um pacote turístico, de acordo com a tabela a seguir, sendo dados o número de pessoas e a quantidade de dias:​

Quant. Pessoas          Valor Pacote R$​

        1 à 4          150/pessoa/dia​

        5 à 8          110/pessoa/dia​

  acima de 8            90/pessoa/dia​'''

pessoa=int(input("qtd de pessoas :"))
dia=int(input("qtd dias : "))
valor=int
if pessoa>8:
    valor=pessoa  *  90  *   dia
    print ("valor total a ser pago e R$ :{}".format(valor))
    print ("reserva para total de dias de :{}".format(dia))
    print ("reserva para total de pessoas :{}"  .format(pessoa))

elif pessoa>=5:
    valor=pessoa*110*dia
    print ("valor total a ser pago e R$ :{}".format(valor))
    print ("reserva para total de dias de :{}".format(dia))
    print ("reserva para total de pessoas :{}"  .format(pessoa))


else:
    valor= pessoa*150*dia
    print ("valor total a ser pago e R$ :{}".format(valor))
    print ("reserva para total de dias de :{}".format(dia))
    print ("reserva para total de pessoas :{}"  .format(pessoa))