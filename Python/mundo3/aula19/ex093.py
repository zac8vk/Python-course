jogador = {
    'nome': input('Nome: '),
    'partidas': int(input('Quantas partidas jogadas? ')),
    'gols': [],
    'total': 0
}
num = 0
for c in range(jogador['partidas']):
    num = int(input(f'Quantos gols na partida {c+1}: '))
    jogador['total'] += num
    jogador['gols'].append(num)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]}.')
for p, g in enumerate(jogador['gols']):
    print(f"{f'    Na {p+1}a partida ele fez {g}'}")
print(f"Total de gols: {jogador['total']}")