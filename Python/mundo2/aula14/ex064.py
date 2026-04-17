print(f'{'-=-'*5}Digite 999 ou maior para encerrar o programa.{'-=-'*5}')
n1 = 0
soma = 0
ndigitados = 0 
while n1 != 999:
    n1 = int(input('Digite um numero: '))
    if n1 != 999:
        soma += n1
        ndigitados += 1
print(f'Numeros digitados: {ndigit