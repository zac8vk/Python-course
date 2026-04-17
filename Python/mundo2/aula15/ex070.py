soma = conta = md1000 = 0
while True:
    print('-'*40)
    print(f'{'Loljinha':^40}')
    print('-'*40)

    prod = str(input('Nome do produto:'))
    preço = int(input('preço: R$'))
    soma += preço

    print('-'*40)
    
    if conta == 0 or menor > preço:
        menor = preço
    conta += 1
    if preço >= 1000:
        md1000 += 1 

    repetir = ' '
    while repetir not in 'SN':
        repetir = str(input('Deseja continuar[S/N]?')).strip().upper()
    if repetir == 'N':
        break
print(f'Total gasto: {soma}')
print(f'Produtos acima de mil: {md1000}')
print(f'Produto mais barato: {menor}')