matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0
#criando a matriz
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um numero para [{l}, {c}]: '))
print('-='*30)

for l in range(3):
    for c in range(3):
       # soma dos valores pares
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

       # soma dos valores da terceira coluna
        if c == 2:
            soma += matriz[l][c]

       # maior da segunda linha 
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
       # saida da matriz
        print(f'[ {matriz[l][c]:^3} ]', end= '')
    print()

#saida dos valores(par, soma, maior)
print('-='*30)
print(f'A soma dos valores pares foi {par}.')
print(f'A soma dos valores da terceira coluna foi {soma}.')
print(f'O maior valor da segunda linha foi {maior}.')