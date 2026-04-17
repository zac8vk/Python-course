print('='*40)
while True:
    n = int(input('De qual numero você quer ver a tabuada? '))
    if n <= 0:
        break
    print(f'A tabuada de {n}:')
    for c in range(0, 11):
        print(f'{n} x {c} = {n*c}')
    print('='*40)
print('='*40)
print('Fim, obrigado por jogar')