# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Digite o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in name.lower()))
