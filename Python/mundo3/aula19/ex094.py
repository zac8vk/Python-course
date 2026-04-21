pessoas = []
mulheres = []
acima = []
quant = 0
while True:
    dados = {'nome': input('Nome: '),}
    sexo = ''
    while True:
        dados['sexo'] = input('Sexo[M/F]: ').upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERROR: Resposta deve estar em M ou F')
    dados['idade'] = int(input('Idade: '))
    if dados['sexo'] in 'F':
        mulheres.append(dados['nome'])
    pessoas.append(dados.copy())
    quant += 1
    continuar = ''
    while True:
        continuar = input('Deseja continuar[S/N]? ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO: Resposta tem de estar em S ou N')
    if continuar in 'N':
        break
media = 0
for p in pessoas:
    media += p['idade']
media /= quant
for c, v in enumerate(pessoas):
    if pessoas[c]['idade'] > media:
        acima.append(pessoas[c])
print('='*30)
print(f'Total de pessoas {quant}.')
print(f'Media de idade foi {media}.')
print(f'As mulheres cadastradas foram', end=' ')
for c in mulheres:
    print(c, end= ', ')
if len(acima) != 0:
    print('\nPessoas acima da media de idade:')
    for c in acima:
        print(f'\t{c}')
