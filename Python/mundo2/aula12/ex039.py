from datetime import date
nasc = int(input('Em que ano você nasceu?'))
ano = int(date.today().year)
saldo = ano - nasc
print(ano)
if saldo == 18:
    print(f'Pessoas nascidas em {nasc} tem {saldo} anos em {ano}.')
    print(f'Você tem de se alistar IMEDIATAMENTE.')
elif saldo < 18:
    print(f'Pessoas nascidas em {nasc} tem {saldo} anos em {ano}.')
    print(f'Faltam {18 - saldo} anos para você precisar se alistar.')
elif saldo > 18:
    print(f'Pessoas nascidas em {nasc} tem {saldo} anos em {ano}.')
    print(f'Você já DEVERIA TER SE ALISTADO!')
    print(f'Seu alistamento foi a {saldo - 18} anos em {ano - (saldo -18)}.')