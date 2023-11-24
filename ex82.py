valores = []  
valorespares = []
valoresimpares = []

while True: 
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    
    resp = str(input('Deseja continuar? (S/N): '))
    if resp.upper() == 'N':
        break  

    if valor % 2 == 0:
        valorespares.append(valor)
    else:
         valoresimpares.append(valor)
         
    
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares são: {valorespares}')
print(f'Os valores ímpares são: {valoresimpares}')
    

