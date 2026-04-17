from random import randrange
n1 = randrange(0, 5)
chute = int(input('Digite um numero inteiro de 0 a 5: '))
if chute == n1:
    print('Parabens! Voce acertou!')
else:
    print('Infelizmente, voce errou')