intei = int(input('Digite um numero:'))
count = 0
for d in range(1, intei+1):
    if intei % d == 0:
        count += 1
        print('\033[34m', end= ' ')
    else:
        print('\033[33m', end= ' ')
    print(d, end = ' ')
print(f'\n\033[mO numero {intei} foi divisivel {count} vezes.')
if count == 2:
    print('E por isso ele PODE ser considerado um numero primo.')
elif count != 2:
    print('E por isso ele NAO pode ser considerado um numero primo.')