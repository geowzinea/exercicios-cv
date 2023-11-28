tudo = []
while True: 
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    tudo.append((nome, peso))
     
    resp = str(input('Deseja continuar? (S/N): '))
    if resp.upper() == 'N':
        break  
    
quantidade = len(tudo) 
pesados = [pessoa for pessoa in tudo if pessoa[1] >= 85]
leves = [pessoa for pessoa in tudo if pessoa[1] < 85]

if pesados:
    print('Os mais pesados são: ')
    for pessoa in pesados:
        print(f'{pessoa[0]} com peso igual ou superior {pessoa[1]} kg')
else:
        print('Não há pessoas com peso igual ou superior a 85 kg.')

if leves:
    print('Os mais pesados são: ')
    for pessoa in leves:
        print(f'{pessoa[0]} com peso igual ou menor a{pessoa[1]} kg')
else:
        print('Não há pessoas com peso igual ou menor a 85 kg.')

print(f'Ao todo foram cadastrada {quantidade} pessoas')