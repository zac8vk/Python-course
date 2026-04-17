print('analisador de triangulos')
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta3 < (reta1 + reta2) and reta1 < (reta2 + reta3) and reta2 < (reta3 + reta1):
    print('Esses segmentos PODEM formar um triangulo')
else:
    print('Esses segmentos NAO podem formar um triangulo')