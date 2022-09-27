#funções 

#len usada para saber quantos elementos há na lista
'''algumas das funções 
print() imprimi uma mensagem 
input() retorna um dado
len() 
max()'''

#função inicial como criar sua propria função com (def )

def saudacao():
    print('Seja bem Vindo')
    print ('olá um prazer fazer esse curso')

saudacao()
saudacao()
saudacao()

#função com parametro
def saudacao(nome, curso):
    print(f'Seja bem Vindo,{nome}')
    print (f'olá um prazer fazer do curso de :{curso}')

saudacao('Fernando','python')
saudacao('Amanda','javascript')

#função com parametro default

def saudacao(nome, curso='Python'):
    print(f'Seja bem Vindo,{nome}')
    print (f'olá um prazer fazer do curso de :{curso}')

saudacao('Fernando')
saudacao('Amanda')

#função com retorno

def soma (num1, num2):
    return  num1 + num2

resultado = soma(5,7)
print ('o resultado da soma é =',resultado)

def calculadora(num1, num2, operacao='+' ):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-' :
        return num1 - num2

resultado = calculadora(10, 20)

print (resultado)




