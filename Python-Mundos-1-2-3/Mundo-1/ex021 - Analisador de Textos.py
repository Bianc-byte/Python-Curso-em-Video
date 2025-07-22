frase = 'Meu nome é Pikachu'
print(frase.replace('Pikachu', 'Bombado'))

#leia o nome completo de uma pessoa e mostre
#o nome com todas as letras maiúsculas
# o nome com tds minúsculas
#quantas letras tem ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

name = str(input('Digite seu nome completo: ')).strip()

print('Seu nome: {}'.format(name))
print('Com letras maiúsculas: {}'.format(name.upper()))
print('Com letras minúsculas: {}'.format(name.lower()))
print('Ele possui: {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem: {} letras'.format(name.find(' ')))
