def area(a, c):
    b = a * c
    print(f'A area do terreno de {a}x{c} é {b}m².')

print('Terreno')
print('='*25)
comp = float(input('Comprimento (m): '))
larg = float(input('Largura (m): '))
area(comp, larg)
