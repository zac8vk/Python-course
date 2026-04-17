nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Tirando {nota1} e {nota2} a media do aluno sera {media}.')
    print('PARABENS você foi APROVADO!')
elif media >= 5 and media <= 6.9:
    print(f'Tirando {nota1} e {nota2} a media do aluno sera {media}.')
    print('Você esta de recuperação.')
elif media < 5:
    print(f'Tirando {nota1} e {nota2} a media do aluno sera {media}.')
    print('Você foi REPROVADO.')
