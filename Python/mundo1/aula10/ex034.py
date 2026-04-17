salario = float(input('Qual é o seu salario? '))
if salario <= 1250.0:
    reajuste = (salario * 0.15) + salario
    print(f'Seu salario saiu de {salario} pra {reajuste}')
else:
    reajuste = (salario * 0.10) + salario
    print(f'Seu salario saiu de {salario} pra {reajuste}')