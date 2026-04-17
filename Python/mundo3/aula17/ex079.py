num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in num:
        print('ERRO: Valor REPETIDO.')
    else:
        num.append(valor)
    
    continuar = ' '
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if continuar not in 'SN':
            print(f"{'ERRO':^23}")
        else:
            break
    if continuar in 'N':
        break
print(sorted(num))