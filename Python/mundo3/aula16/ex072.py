numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    # validacao do numero:
    while True:
        try:
            n2 = int(input('Digite um numero de 0 a 20: '))
            if 0 <= n2 <= 20:
                break
            print(f'{'ERRO':^25}')
        except ValueError:
            print('Error code 1: Digite apenas NUMEROS.')
    print(f'Você digitou o numero {numeros[n2]}.')

    #valida;ao do continuar
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if continuar not in 'SN':
            print(f'{'ERRO':^25}')
        else:
            break
        
    if continuar == 'N':
        break