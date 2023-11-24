valores = []  

while True: 
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    resp = input('Deseja continuar? (S/N): ')
    if resp.upper() != 'S':
        break 
valores.sort()
des = sorted(valores, reverse=True)
print(f'Foram digitados os seguintes valores {valores}, totalizando {len(valores)} números digitados')
print(f'A lista em ordem decrescente fica: {des}')
if 5 in valores:
    print('O número 5 está na lista')
else: 
    print('O número 5 não está na lista')