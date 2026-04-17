pala = ('mercado',
        'futuro',
        'ampulheta')
for p in pala:
    print(f'\n{p}', end= ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')