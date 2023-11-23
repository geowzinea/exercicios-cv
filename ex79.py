valores = []  

while True: 
    valor = int(input('Digite um valor: '))
    
    if valor in valores:
        print(f'O número {valor} já está na lista.')
    else:
        valores.append(valor)
        print(f'O número {valor} foi adicionado à lista.')
    
    resp = input('Deseja continuar? (S/N): ')
    if resp.upper() != 'S':
        break 
valores.sort()
print('Valores na lista:', valores)
