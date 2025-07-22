#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date #importar o date em datetime para o computador puxar o ano que estamos
ano = int(input('Digite o ano desejado que quer analisar, ou coloque 0 se deseja o ano atual: '))
resultado = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
#o ano é bissexto se for divisível por 4 e não é divisível por 100, a menos que também seja divisível por 400
if ano == 0:
    ano = date.today().year #para selecionar a data de hoje e apenas o ano
if resultado:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))