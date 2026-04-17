print('Promo: Viagens acima de 200 km estao com 5% de desconto')
viagem = int(input('De quantos km foi sua viagem? '))
if viagem >= 200:
    print(f'O custo da sua viagem foi R$ {viagem * 0.45}\nParabens! voce ganhou 5% de desconto.')
else:
 print(f'O custo de sua viagem foi R${viagem * 0.50}')