from datetime import date
count = 0
meno = 0
ano = date.today().year
for idd in range(1, 8):
    idde = int(input('Em que ano você nasceu?'))
    idade = ano - idde
    if idade >= 18:
        count += 1
    else:
        meno += 1
print(f'Dessas 7 pessoas {meno} ainda sao menores e {count} ja sao maiores de idade.')