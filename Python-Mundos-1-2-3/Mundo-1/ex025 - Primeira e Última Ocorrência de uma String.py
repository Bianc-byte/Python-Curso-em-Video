#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper()
print('A sua frase aparece a letra A: {} vezes'.format(frase.count('A')))
print('A primeira vez que a letra A apareceu foi na posição: {}'.format(frase.find('A')+1)) #acrescentar o +1 pq sem ele vai começar por 0
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #o rfind vai verificar do final pro começo quando aparece primeiro a letra colocando o r na frente de find 
