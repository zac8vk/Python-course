from time import sleep
def contador(ini, fim, pas):
    print('-='*15)
    print(f'Contagem de {ini} ate {fim} de {pas} em {pas}.')
    
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    
    cont = ini
    if ini > fim:
        while cont >= fim:
            print(cont, end= ' ', flush= True)
            cont -= pas
            sleep(0.5)
    else:
        while cont <= fim:
            print(cont, end= ' ', flush= True)
            cont += pas
            sleep(0.5)
    print('fim')
contador(1, 10, 1)
contador(10, 0, 2)

print('-='*15)
print('Personalize a sua contagem:')
inicio = int(input('\tInicio: '))
fim = int(input('\tFim: '))
passo = int(input('\tPasso: '))

contador(inicio, fim, passo)
