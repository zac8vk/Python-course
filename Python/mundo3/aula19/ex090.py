#ler nome e media
alunos = []
nomed = {
    'nome': input('Nome: '),
    'media': int(input('Média: ')),
    'resultado': ""
    }

#adicionar reprovado(<7) ou aprovado(>7)
if nomed['media'] >= 7:
    nomed['resultado'] = '\033[92mAPROVADO\033[0m'
else:
    nomed['resultado'] = '\033[91mREPROVADO\033[0m'

#mostrar dados
print('='*25)
for k, v in nomed.items():
    print(f'{k}: {v}')