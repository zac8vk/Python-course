from datetime import date
ano_nasc = int(input('Em que ano o(a) atleta nasceu? '))
ano = int(date.today().year)
idade = ano - ano_nasc
if idade <= 9:
    print(f'O(a) atleta tem {idade}.')
    print('Categoria: Mirim')
elif 15 > idade >= 10:
    print(f'O(a) atleta tem {idade}.')
    print('Categoria: Infantil')
elif 20 > idade >= 15:
    print(f'O(a) atleta tem {idade}.')
    print('Categoria: Junior')
elif 26 > idade >= 20:
    print(f'O(a) atleta tem {idade}.')
    print('Categoria: Senior')
elif idade > 25:
    print(f'O(a) atleta tem {idade}.')
    print('Categoria: Master')