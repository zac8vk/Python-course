velo = str(input('Em que velocidade seu carro estava? ')).split()
kmh = float(velo[0])
limite = 70
multa = (kmh - limite) * 7
acima = kmh - limite
if kmh > limite:
    print(f'Voce foi multado em US {multa:.1f} por andar {acima} km/h acima do limite de velocidade')
