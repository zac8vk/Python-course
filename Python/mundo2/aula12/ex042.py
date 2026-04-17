s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s3 + s2 and s2 < s3 + s1 and s3 < s2 + s1:
    print('Estes segmentos PODEM formar um triangulo', end='')
    if s1 == s2 == s3:
        print(' EQUILATERO')
    elif s1 != s2 != s3 != s1:
        print(' ESCALENO')
    else:
        print(' ISOSCELES')
else:
    print('Esses segmentos NAO podem formar um triangulo.')
