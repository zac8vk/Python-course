from random import randint
from time import sleep
print('Impar ou par.')
vitoria = 0
while True:
    n = int(input('Digite um numero:'))
    player = str(input('[I/P] Impar ou par? ')).strip().upper()
    c = int(randint(1, 10))
    total = n + c
    tipo = ('PAR' if total % 2 == 0 else 'IMPAR') 

    print(f'O computador jogou {c} e voce {n} totalizando {total} que é um numero {tipo}')
    sleep(0.5)
    print('Você... ')
    sleep(0.5)

    if player in 'I':
        if total % 2 == 0:
            print('\033[31mPerdeu\033[m')
            break
        else:
            print('\033[32mVenceu.\033[m')
            vitoria += 1
    elif player in 'P':
        if total % 2 == 0:
            print('\033[32mVenceu.\033[m')
            vitoria += 1
        else:
            print('\033[31mPerdeu\033[m')
            break
print(f'Você venceu {vitoria} vezes antes de perder.')