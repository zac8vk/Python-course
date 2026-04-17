print(f'{'='*20}')
s = cont = 0
while True:
    n = int(input('Digite um numero[999 para parar]:'))
    if n == 999:
        break
    s += n
    cont += 1
print(f'{'='*20}')
print(f'Você digitou {cont} numeros e a soma desses numeros foi {s}.')