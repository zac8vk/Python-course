from random import randint
from time import sleep

computador = randint(1, 10)
print(f'{'='*8} Adivinhe o numero! {'='*8}')
print('O computador "pensou" em um numero de 1 a 10 e o seu trabalho?\nAcertar em que numero ele pensou com o minimo de tentativas que conseguir.')

count = 0
player = 0

erro = str('\033[31mERRO\033[m')
acerto = str('\033[32mACERTO!!!\033[m')
while player != computador:
    count += 1
    player = int(input('Digite um numero de 1 a 10: '))
    if player != computador:
        print(f'{'-'*5} {count}ª Tentativa: {erro}  {'-'*5}')
        sleep(0.5)
    else:
        print(f'{'-'*5} {count}ª Tentativa: {acerto}  {'-'*5}')

print('='*30)
print('Obrigado por jogar.')
print(f'Você acertou na {count}ª tentativa.')
print(f'O computador pensou no numero {computador}.')