#leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex digite um número: 1834
#unidade: 4   dezena: 3  centena: 8  milhar: 1

number = int(input('Digite um número de 1 a 9999: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('Analisando o número {}'. format(number))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#podemos fazer dessa forma também:
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
