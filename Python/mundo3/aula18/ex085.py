junt = [[], []]
for p in range(0, 7):
    num = int(input(f'Digite o {p+1}o. Valor: '))
    if num % 2 == 0:
        junt[0].append(num)
    elif num % 2 != 0:
        junt[1].append(num)
print(f'Numeros pares: {sorted(junt[0])}')
print(f'Numeros impares: {sorted(junt[1])}')
