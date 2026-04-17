numero = int(input('Digite um numero: '))
print(f'Digite 1 para converter em BINARIO.')
print(f'Digite 2 para converter em OCTAL.')
print(f'Digite 3 para converter em HEXADECIMAL.')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(f'{numero} em BINARIO é {bin(numero)[2:]}.')
elif escolha == 2:
    print(f'{numero} em OCTAL é {oct(numero)[2:]}.')
elif escolha == 3:
    print(f'{numero} em HEXADECIMAL é { hex(numero)[2:]}.')
else:
    print('Opção invalida.')