## Pintando a parede
#leia a largura e altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m ao quadrado
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
área = a * l
t = área / 2
print('Para pintar essa parede será preciso {:.0f} litros de tinta.'.format(t))
