n1 = ()
for c in range(0, 4):
    n1 += (int(input('Digite um numero:')),)

print(f'\nO numero nove apareceu {n1.count(9)} vezes.')
if 3 in n1:
    print(f'O numero tres aparece primeiro na posiçao {n1.index(3) + 1}')
else:
    print('O numero 3 nao foi digitado.')
print(f'Numeros pares digitados:', end=' ')
for f in range(0, len(n1)):
    if n1[f] % 2 == 0:
        print(n1[f], end=' ')
