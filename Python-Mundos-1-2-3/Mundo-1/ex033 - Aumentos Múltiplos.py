#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário: R$'))
aumento1 = salario * 10 / 100 #10% do salário (10% significa 10 partes de 100 ou seja 10% = 10 / 100 (0.10)
resultado1 = salario + aumento1
aumento2 = salario * 15 / 100
resultado2 = salario + aumento2

if salario >= 1250:
    print('O seu salário de R${:.0f} recebeu um aumento e agora está em R${:.0f}!'.format(salario,resultado1))
else:
    print('O seu salário de R${:.0f} recebeu um aumento e agora está em R${:.0f}!'.format(salario,resultado2))