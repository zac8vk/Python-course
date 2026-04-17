sala = float(input('Qual é o seu salario?'))
preço = float(input('Qual o valor que você deseja?'))
anos = float(input('Em quantos anos você vai parcelar?'))
if (sala * 0.3) < preço / (anos * 12):
    print('Me desculpe, mas você não pode pegar esse emprestimo.')
else:
    print('Empretismo... concedido!')