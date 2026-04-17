print(f'{'-=-'*5} Gerador de PA. {'-=-'*5}')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: ')) 
count1 = 0
c = 1
while c != 0: 
    while count != 11:
        count += 1
        print(f'{pt}, ', end='')
        pt += r
    print('PAUSA.', end='')
    c = int(input("\nDeseja mostrar mais quantos algarismos? "))
    count -= c
print('FIM.')