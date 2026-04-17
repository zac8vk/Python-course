pessoas = list()
dados = list()
maior = menor = count = 0
while True:
    dados.append((input('Nome:')))
    dados.append(int(input('Peso:')))
    pessoas.append(dados[:])
    dados.clear()
    count += 1
    if count == 1:
        maior = menor = pessoas[0][1]
    else:
        if pessoas[-1][1] > maior:
            maior = pessoas[-1][1]
        elif pessoas[-1][1] < menor:
            menor = pessoas[-1][1]

    continuar = ' '
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(f'Pessoas cadastradas: {count}')
print(f'As mais pesadas tiveram {maior} kilos, peso de: ', end= ' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end= '')    
print(f'\nAs mais leves tiveram {menor} kilos, peso de: ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end= '')