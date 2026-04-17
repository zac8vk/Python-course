#com os catetos de um triangulo retangulo ache a hipotenusa 
#h² = a² + b²
#catetos:
from math import hypot
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
c = hypot(oposto, adjacente)
print(f'A hipotenusa desse triangulo: {c:.2f}')