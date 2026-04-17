print(f'{'-=-' * 5}Sequencia de fibonacci.{'-=-' * 5}')
n1 = 1
n2 = 1
count = int(input('Quantos termos você deseja ver? ')) - 3
print('0, 1, 1, ', end= '')
while count != 0:
    count -= 1
    f = n1 + n2
    print(f'{f}, ', end='')
    n1 = n2
    n2 = f
print('FIM.')