#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))
if n % 2 == 0: #o operador % calcula o resto da divisão e quando fazemos n % 2 estamos vendo se sobrra algo ao dividir n por 2 e se o resto for 0 significa que o número divide exatamente por 2 e é par, caso contrário é impar
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar!'.format(n))
    