de_maior = masc = fem_menor = 0
while True:
    print('-'*40)
    print(f'{'CADASTRE UMA PESSOA':^40}')
    print('-'*40)

    idade = int(input('Idade: '))
    sexo = ' '
    repetir = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    print('-'*40)

    if idade >= 18:
        de_maior += 1
    if sexo in 'M':
        masc += 1
    if idade <= 20 and sexo == 'F':
        fem_menor += 1


    while repetir not in 'SN':
        repetir = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if repetir == 'N':
        break
print(f'Total de pessoas maiores de 18: {de_maior}')
print(f'Total de homens cadastrados: {masc}')
print(f'Total de mulheres com menos de 20 anos: {fem_menor}')