#leia 2 numeros e ofereça um menu com
#1 soma, multiplicaçao, maior, novos numeros
#2 botao de sair
n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))
r = 0

while r != 5:

    if r == 4:
        n1 = float(input('Digite um numero:'))
        n2 = float(input('Digite outro numero:'))

    print('='*15)
    print('[1]Para somar.')
    print('[2]Para multiplicar.')
    print('[3]Para ver qual deles é o maior.')
    print('[4]Para reescrever os numeros.')
    print('[5]Pra sair do programa.')

    r = int(input('Oque você deseja: '))
    if r == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}')
    elif r == 2:
        print(f'O produto de {n1} e {n2} é {n1 * n2}')
    elif r == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2}')
print('='*15)