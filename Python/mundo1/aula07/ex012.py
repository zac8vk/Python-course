#mostre o pre;o de um produto
#mostre o pre;o com desconto de 5%
p = float(input('preço atual: '))
pd = p * 0.05
prd = p - pd
print(f'Preço atual: {p:.2f}\nPreço c/ desconto: {prd:.2f}\nDesconto: {pd:.2f}')