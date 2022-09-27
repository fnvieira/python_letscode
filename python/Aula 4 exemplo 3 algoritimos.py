'''Exemplo 3: Dados 3 valores A, B e C, verificar se eles podem ser os comprimentos dos lados de um triângulo, ​

se forem, verificar se compõem um triângulo equilátero,  isósceles ou escaleno. Informar se não compuserem ​

nenhum triângulo. ​

Análise: ​

Dados de Entrada – 3 lados de um suposto triângulo (A, B, C)​

Dados de Saída – mensagens: não compõem triângulo, triângulo equilátero, triângulo isósceles, triângulo escaleno.​

O que é Triângulo?​

    Resposta: figura geométrica fechada de três lados, em que cada um é menor que a soma dos outros dois.​

​

O que é um Triângulo Equilátero?​

    Resposta: é um Triângulo com três lados iguais.​

​

O que é um Triângulo Isósceles?​

    Resposta: é um Triângulo com dois lados iguais.​

​

O que é um Triângulo Escaleno?​

    Resposta: é um Triângulo com todos os lados diferentes.​
    
    Exemplo 3: Dados 3 valores A, B e C, verificar se eles podem ser os comprimentos dos lados de um triângulo, ​

se forem, verificar se compõem um triângulo equilátero,  isósceles ou escaleno. Informar se não compuserem ​

nenhum triângulo. ​

Análise: ​

Com esses dados, montamos a tabela decisão a seguir:​

​

É Triângulo? É Equilátero? É Isósceles? É Escaleno? Resultado​

        V          V         F          F Equilátero ​

        V          F         V          - Isósceles ​

        V          F         F          V Escaleno​

        F          -         -          - Não é Triângulo​


Passando essa tabela para expressões lógicas, temos:​

É Triângulo:   (A < B + C) E (B < A + C) E (C < A + B)​

É Equilátero: (A == B) E (B == C)​

É Isósceles:   (A == B) OU (A == C) OU (B == C)​

É Escaleno:   (A != B) E (B != C)  E (A != C) ​'''


a=int(input("inserir valor 1 :"))
b=int(input("inserir valor 2 :"))
c= int(input("inserir valor3 :"))


if  (a<b+c) and  (b<a+c) and (c<a+b)   :
    print  (" e um triangulo")

elif (a!=b)  and  (a!=c)  and  (b!=c)   :
    print("triangulo escaleno")

elif (a==b) or (a==c) or (b==c):
    print ("triangulo isoceles")


elif (a==b) and  (b==c) :
    print ("e um Triangulo Equilatero")

else:
    print("nao e um triangulo")