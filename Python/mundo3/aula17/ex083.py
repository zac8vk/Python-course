exp = str(input('Digite uma expressão: '))
pilha = []
for char in exp:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        elif len(pilha) == 0:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expresão esta valida.')
elif len(pilha) > 0:
    print('Sua expresao esta invalida.')