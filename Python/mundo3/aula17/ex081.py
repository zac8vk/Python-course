num = []
count = 0
while True:
    num.append(int(input('Digite um numero: ')))
    count += 1

    continuar = ' '
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print(f'Você digitou {count} numeros.')
num.sort(reverse = True)
print(f'Você digitou os seguintes numeros: {num}')
if 5 in num:
    print('O numero 5 esta presente na lista.')
else:
    print('O numero 5 nao esta presente na lista.')