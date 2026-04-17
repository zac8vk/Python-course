# imc = peso dividido por altura ao quadrado
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura ** 2)
print(f'Seu imc é {imc:.2f}.', end='')
if imc <= 18.5:
    print(' Você está abaixo do peso.')
elif imc <= 25:
    print(' Você esta no peso IDEAL!.')
elif imc <= 30:
    print(' Você esta com sobrepeso.')
elif imc <= 40:
    print(' Você esta OBESO!')
elif imc > 40:
    print(' Você foi diagnosticado com OBESIDADE MORBIDA!')
