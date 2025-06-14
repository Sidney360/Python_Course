nome = input('Digite seu nome: ')
lenght_name = len(nome) 
if lenght_name <= 4:
    print('Seu nome é curto')
elif lenght_name >= 5 and lenght_name <= 6:
    print("Seu nome é normal")
else:
    print('Seu nome é muito grande')