#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input('Digite o número da primeira reta: '))
n2 = float(input('Digite o número da segunda reta: '))
n3 = float(input('Digite o número da terceira reta: '))

#Para construir um triângulo, é necessário que a soma das medidas de quaisquer dois lados seja sempre maior que a medida do terceiro lado
soma1 = n1 + n2
soma2 = n1 + n3
soma3 = n2 + n3

if soma1 > n3 and soma2 > n2 and soma3 > n1:
# ou tbm poderia fazer:  if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Podem formar um triângulo')
else:
    print('Não podem formar+ um triângulo')
