try: 
    numero = int(input ('Digite um número inteiro: '))
    if numero%2 == 0: 
        print('Este número é par')
    else:
        print('Este número é ímpar')
except ValueError as e: 
    print(f'você não digitou um número inteiro {e}')

