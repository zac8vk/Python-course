frase = str(input('Digite uma frase: ')).strip().lower()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letras in range(len(junto) -1, -1, -1):
    inverso += junto[letras]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo')
else:
    print('NAO temos um palindromo')