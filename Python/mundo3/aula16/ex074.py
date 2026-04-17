from random import randint
n1 = ()
for c in range(5):
    n1 += ((randint(0, 10),))
menor = n1[0]
maior = n1[1]
for f in range(0, len(n1)):
    if n1[f] > maior:
        maior = n1[f]
    if menor > n1[f]:
        menor = n1[f]
print(n1)
#max e min ajudam a fazer maior e menor mas so funciona em tuplas
print(f'O maior numero foi {maior} enquanto que o menor foi {menor}.')
