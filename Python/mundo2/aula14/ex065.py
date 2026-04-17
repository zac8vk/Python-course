print(f'{'='*7}Calculador de media.{'='*7}')
n1 = soma = count = 0
resp = 'S'
maior = 1
menor = int()
while resp not in 'N':
    n1 = int(input('Digite um numero: '))
    if count == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    soma += n1
    count += 1
    resp = str(input('[S/N] Deseja proseguir? ')).strip().upper()
print(f'{'='*20}')
print(f'Numeros digitados: {count}')
print(f'Soma: {soma}')
print(f'Media: {soma / count}')
print(f'O MAIOR numero foi {maior} e o MENOR foi {menor}')