r = ''
while not r == 'n':
    s = str(input('Qual o sexo dessa pessoa? [M/F] ')).strip().lower()
    if s not in ['m', 'f']:
        print(f'Valor {s} não é uma opção valida, tente novamente')
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()