soma_idd = 0
maior = 0
nomehomenvelho = ''
count = 0
for p in range(1,5):
    print(f'{'-'*5} {p}ª Pessoa. {'-'*5}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [H/M]: ').strip()
    soma_idd += idade
    if p == 1 and sexo in 'Hh':
        maior = idade
        nomehomenvelho = nome
    if sexo in 'Hh' and idade > maior:
        maior = idade
        nomehomenvelho = nome
    if sexo in 'Mm' and idade < 20:
        count += 1
print(f'A idade media do grupo foi: {soma_idd / 4}')
print(f'O homen mais velho foi o {nomehomenvelho} com seus {maior} anos.')
print(f'A quantidade de mulheres abaixo dos 20 anos foi: {count}')