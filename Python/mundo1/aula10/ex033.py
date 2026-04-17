n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
n3 = float(input('Digite o terceiro numero:'))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f'O maior numero é {maior:.2f}')
print(f'O menor numero é {menor:.2f}')

#solu;ao usando if
#menor
# menor = n1
# if n1 < n2 and n3 < n2
#   menor = n2 
# if n2 < n3 and n1 < n3 
#   print(f'numero menor: {menor}')