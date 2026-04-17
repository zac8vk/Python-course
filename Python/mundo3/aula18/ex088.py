from time import sleep
from random import randint
re1 = []
refinal = []
tot = 0

print('-'*40)
print(f'MEGA SENA'.center(40))
print('-'*40)
jogos  = int(input('Deseja quantos bilhetes? '))
while True:

    count = 0
    while count <= 6:
        n = randint(1, 60)
        if n not in re1:
            re1.append(n)
            count += 1
        if count >= 6:
            break
    refinal.append(re1[:])
    re1.clear()

    tot +=1
    if tot >= jogos:
        break

print(f"Resultado dos {jogos} jogos".center(40, '-'))
for i, l in enumerate(refinal):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
