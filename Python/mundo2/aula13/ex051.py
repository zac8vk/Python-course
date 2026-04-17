print('='*30)
print('     10 termos de uma PA')
print('='*30)
i = int(input('Digite o inicio: '))
r = int(input('Digite a razao: '))
f = i + (11 - 1) * r
for n in range(i, f, r):
    print(n, end=' > ')