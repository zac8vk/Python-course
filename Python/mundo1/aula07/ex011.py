#leia a largura e alturaa de uma parede
#calcule a area
#diga quantos litros de tinta usaria pra pintar
#1 litro = 2m²
c = float(input('Qual o comprimento da sua parede em metros?'))
l = float(input('Qual a largura da parede em metros?'))
a = c * l
t = a / 2
print(f'Dimensao da parede {c}x{l}\nArea da parede: {a:.02f}m²\nLitros de tinta necessarios: {t}')