#seno cosseno e tangente
from math import cos, tan, sin, radians
angulo = float(input('Digite um angulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente{tangente:.2f}')
