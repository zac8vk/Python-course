numero = float(input('Primeiro numero:'))
numero2 = float(input('Segundo numero:'))
if numero > numero2:
    print(f'{numero} é MAIOR que {numero2}.')
elif numero2 > numero:
    print(f'{numero2} é MAIOR que {numero}.')
elif numero2 == numero:
    print('Os numeros sao IGUAIS.')