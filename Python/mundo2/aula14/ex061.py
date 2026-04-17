print(f'{'-=-'*5} Gerador de PA. {'-=-'*5}')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: ')) 
count = 0
while count != 10:
    count += 1
    print(f'{pt}, ', end='')
    pt += r
print('FIM.', end='')