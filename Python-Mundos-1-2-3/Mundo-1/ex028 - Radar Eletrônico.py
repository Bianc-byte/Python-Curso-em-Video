#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))
multa = velocidade - 80
resultado = multa * 7
if velocidade > 80:
    print('Você ultrapassou a velocidade permitida então será multado.')
    print('E o valor da multa será de {} reais.'.format(resultado))
else:
    print('Você está na velocidade permitida então não será multado.')
print('Tenha um ótimo dia e dirija com segurança!')

