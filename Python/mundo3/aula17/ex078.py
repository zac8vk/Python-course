num = []
mai = 0
men = 0
for c in range(0, 5):
    num.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        elif men > num[c]:
            men = num[c]
print('='*30)
print(f'Você digitou os valores: {num}')
print(f'O maior valor foi {mai} nas posições', end=' ')
for c, v in enumerate(num):
    if v == mai:
        print(f'{c}...', end='')
print(f'\nO menor valor foi {men} nas posições', end= ' ')
for c, v in enumerate(num):
    if v == men:
        print(f'{c}...', end='')