times = (
    'Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
    'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
    'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
    'São Paulo', 'Fluminense', 'Sport Recife',
    'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
    'Atlético-GO'
)
ord_alf = sorted(times)

print(f'Top 5: {times[:5]}')
print(f'Ultimos colocados: {times[-4:]}')
print(ord_alf)
print(f'A chapecoense esta na posição: {times.index('Chapecoense')+1}')