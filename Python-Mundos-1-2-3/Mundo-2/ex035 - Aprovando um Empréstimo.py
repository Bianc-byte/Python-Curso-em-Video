#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

import time #aqui eu vou usar o import time mas é opcional

valor_casa = (float(input('Qual o valor da sua casa: ')))
salario = (float(input('Qual o seu salário: ')))
anos = (int(input('Em quantos anos você irá pagar: ')))
meses = anos * 12 #converter os anos para meses depois calcular a prestacao e o limite
prestacao = valor_casa / meses
limite = salario * 0.30


print(f'Prestação mensal: R$ {prestacao:.2f}')
print(f'30% do seu salário é: R$ {limite:.2f}')

print('Analisando seu pedido de empréstimo de acordo com os seus dados...')
time.sleep(2) #utilizei aqui o import apenas para aguardar uns segundos antes de mostrar o resultado
if prestacao <= limite:
    print('Parabéns!! Seu empréstimo foi aprovado!!')
else:
    print('Infelizmente o seu empréstimo foi negado.')