num = []
par = []
impar = []
while True:
    n = int(input('Digite um numero: '))
    num.append(n)

    continuar = ''
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
        if continuar in 'SN':
            break

    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)

    if continuar in 'N':
        break
print(f'Lista completa: {num}')
print(f'Pares: {par}')
print(f'Impares: {impar}')