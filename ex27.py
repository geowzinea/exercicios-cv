n = str(input('Digite seu nome completo: '))
nome = n.split()
print(f'O seu primeiro nome é {nome[0]}')
print(f'O seu último nome é {nome[len(nome)-1]}')