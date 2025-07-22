#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Qual a distância da sua viagem: '))
r1 = distancia * 0.50
r2 = distancia * 0.45
if distancia <= 200:
    print('O preço que terá que pagar de passagem é: {:.2f} reais'.format(r1))
else:
    print('O preço que terá que pagar de passagem é: {:.2f} reais'.format(r2))
    