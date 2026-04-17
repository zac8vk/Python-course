s = 0
cont = 0
for i in range(1,7):
    n = int(input(f'Digite o {i}° numero: '))
    if n % 2 == 0:
        cont += 1
        s += n
print(f'A soma dos {cont} numeros pares que voce digitou foi {s}.')