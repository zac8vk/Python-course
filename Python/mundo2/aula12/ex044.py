preçon = float(input('Preço das compras: '))
print('Bem vindo(a)!!')
print('Formas de pagamento.')

#formas de pagamento
print('Digite [1] para pagamentos a vista em dinheiro ou cheque.')
print('Digite [2] para pagamentos a vista no cartão.')
print('Digite [3] para pagamentos de 2x no cartão.')

#resposta
print('Digite [4] para 3x ou mais no cartão')
forma = int(input('Qual vai ser a forma de pagamento? '))
if forma == 1:
    saldo = preçon - (preçon * 0.10)
    print(f'O(s) produtos que sairiam por {preçon} sairam por {saldo} no final.')
elif forma == 2:
    saldo = preçon (preçon * 0.05)
    print(f'Os produtos que sairiam por {preçon} sairam por {saldo} no final.')
elif forma == 3:
    print(f'O preço final foi {preçon}.')
elif forma == 4:
    saldo = preçon + (preçon * 0.20)
    parcelas = int(input('Qual vai ser o numero de parcelas?'))
    print(f'O(s) produtos que sairiam por {preçon} sairam {saldo} no final.')
else:
    print('Opçao invalida.')
