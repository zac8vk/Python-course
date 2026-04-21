gols = []
time = []
while True:
    jogador = {
        'nome': input('Nome: '),
        'partidas': int(input('Partidas jogadas: ')),
        'gols': [],
        'total': 0
    }
    for c in range(jogador['partidas']):
        jogador['gols'].append(int(input(f'\tQuantos gols ele fez na {c+1}a partida: ')))
        jogador['total'] += jogador['gols'][c]
    time.append(jogador.copy())
    
    continuar = ''
    while True:
        continuar = input('Deseja continuar[S/N]? ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERROR: Resposta tem de estar em S ou N.')
    if continuar in 'N':
        break

n = 0
print('=-'*30)
print(f'{'No':<3}{'Nome':<10}{'Gols':<20}{'Total':<5}')
for k, v in enumerate(time):
    gols_str = str(v['gols'])
    print(f'{k:<3}{v['nome']:<10}{gols_str:<20}{v['total']:<5}')

print('=-'*30)
while True:
    n = int(input('Deseja ver os dados de qual jogador(999 pra sair)? '))
    if n == 999:
        break
    elif n in range(len(time)):
        print(f'Jogador: {time[n]['nome']}')
        for c, g in enumerate(time[n]['gols']):
            print(f'\t{c+1}a partida: {g} gols')
    else:
            print(f'ERROR: jogador No {n} nao existe.')