## Conversor de Moedas
#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere que US$1.00 = R$3.27
money = float(input('Quanto dinheiro você tem em sua carteira: R$'))
d = money / 3.27
print ('Com R${:.1f} da para comprar US${:.1f}'.format(money,d))

