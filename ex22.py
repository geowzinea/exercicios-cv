nome = str(input('Digite seu nome completo: ').strip())
print(nome.upper())
print(nome.lower())
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome tem {len(primeiro_nome)} letras')
