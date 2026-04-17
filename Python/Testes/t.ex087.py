#exercicio 87 so que o usuario decide a quantidade de colunas e linhas da matriz

#variaveis
info = []
matriz = []

#matriz
print(f'{"-="*11}Gerador de matriz{"-="*12}')
coluna = int(input('Quantidade de colunas: '))
linha = int(input('Quantidade de linhas: '))
print(f'{"-="*30}')
for l in range(linha):
    for c in range(coluna):
        info.append(int(input('Digite um numero: ')))
    matriz.append(info[:])
    info.clear()
print(f'{"-="*30}')

#saida da matriz
for l in range(linha):
    for c in range(coluna):
        print(f'[ {matriz[l][c]:^3} ]', end= '')
    print('')