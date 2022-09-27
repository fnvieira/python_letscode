'''media =float
nota1= float(input("insira a nota 1 :"))
nota2= float(input("insira nota 2 :"))
nota3= float(input("insira nota 3 :"))
nota4= float(input("insira nota 4 :"))
media = (nota1 +nota2 +nota3 +nota4)/4'''

soma = 0

for i in range (1,5):
    nota = float (input(f'insira a nota {i} :'))


    soma = soma + nota

if (soma/4)>=7:
    print ("Aluno Aprovado media final =",soma/4)

else:
    print ("Aluno Reprovado media final =",soma/4)