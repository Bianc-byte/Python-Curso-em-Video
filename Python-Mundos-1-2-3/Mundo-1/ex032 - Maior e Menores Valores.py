#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outro número: '))

print('O maior valor é: {:.0f}'.format(max(a,b,c)))
print('E o menor valor é: {:.0f}'.format(min(a,b,c)))

#mas também podemos fazer assim:
#verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('=' * 20)
print('Fazendo do outro jeito daria: ')
print('O menor valor digitado foi {:.0f}'.format(menor))
print('O maior valor digitado foi {:.0f}'.format(maior))
print('=' * 20)
print('Ambos os jeitos está correto!')