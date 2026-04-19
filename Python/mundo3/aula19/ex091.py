from random import randint
from time import sleep
from operator import itemgetter
ranking = dict()
count = 1

dados = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}
print('Resultados:')
for k, c in dados.items():
    print(f"{f'O {k} tirou {c} no dado.':>4}")
    sleep(1)

ranking = sorted(dados.items(), key= itemgetter(1), reverse = True)
print('Ranking:')
for k, c in ranking:
    print(f"{f'{count}o lugar: {k} com {c}.':>4}")
    sleep(1)
    count += 1