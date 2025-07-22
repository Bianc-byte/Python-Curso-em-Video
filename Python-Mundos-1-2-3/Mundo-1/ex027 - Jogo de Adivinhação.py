#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
numero = random.randint(0,5)
n = int(input('Digite o número que eu pensei: '))
print('Processando...')
sleep(3) #de time eu importei sleep que é para depois da frase acima ele aguardar nesse caso 3 segundos antes de ir para a próxima mensagem
if n == numero:
    print('Você acertou!!')
else:
    print(f'Você errou! Eu pensei no número {numero}.')