from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#opçoes
print('Pedra Papel Tesoura')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

player = int(input('Faça sua escolha: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

#resultados.
if 0 < player > 2:
    print('Jogada invalida.')
else:
    print(f'O computador escolheu... {itens[computador]}.')
    print(f'O player escolheu... {itens[player]}.')

    if computador == 0: #pedra
        if player == 0: 
            print('E o resultado do jogo é...EMPATE!!')
        elif player == 1:
            print('E o vencedor foi... O PLAYER!!')
        elif player == 2:
            print('E o vencedor foi... O COMPUTADOR!!')
    elif computador == 1:
        if player == 0:
            print('E o vencedor foi... O COMPUTADOR!!')
        elif player == 1:
            print('E o resultado do jogo é... EMPATE!!')
        elif player == 2:
            print('E o vencedor foi... O PLAYER!!')
    elif computador == 2:
        if player == 0:
            print('E o vencedor foi... O PLAYER!!')
        elif player == 1:
            print('E o vencedor foi... O COMPUTADOR!!')
        elif player == 2:
            print('E o resultado do jogo é... EMPATE!!')
