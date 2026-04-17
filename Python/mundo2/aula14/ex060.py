print(f'{'-=-' * 5}Fatorial{'-=-' * 5}')
n1= int(input('Digite um numero: '))
count = n1
f = 1
while count > 0:
    print(f'{count}', end= ' ')
    f *= count
    count -= 1
    if count > 0:
        print('x ', end= '')
    else:
        print(f'= {f}', end= '')