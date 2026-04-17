lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(3):
    for i in range(3):
        lista[c][i] = int(input(f'Digite um numero para [{c}, {i}]:'))
for c in range(3):
    for l in range(3):
        print(f'[{lista[c][l]}]', end= '')
    print()
