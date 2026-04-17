#leia o nome completo
nome = input('Qual e seu nome completo?')
#mostre maiusculo e minusculo
maiu = nome.upper()
minu = nome.lower()
#quantos carecteres tem o nome completo e so o primeiro nome separado
primeiro = nome.split()
completo = ''.join(primeiro)
quantidadeC = len(completo)
quantidadeP = len(primeiro)
print (f"""Nome: {nome}\nMaiusculo: {maiu}\nMinusculo: {minu}
Quantidade de letras primeiro nome: {quantidadeP}
Quantidade nome completo: {quantidadeC}""")
