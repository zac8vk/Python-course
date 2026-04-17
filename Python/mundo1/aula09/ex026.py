frase = str(input('Digite uma frase:')).strip().upper()
print(f'Quantidade de letras R na sua frase: {frase.count('A')}')
print(f'Primeira aparição da letra R: {frase.find('A')}')
print(f'Ultima aparição da letra R: {frase.rfind('A')}')
