nome = 'Sidney'
altura = 1.84
peso = 76
imc = 76 / (1.84 ** 2) # IMC = peso / (altura x altura)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)