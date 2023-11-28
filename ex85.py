valores = []

for cont in range(0, 7):
    valores.append(int(input('Digite um valor: ')))
 
impares = []
pares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
if impares:
    print(f'Os valores ímpares são: {impares}')
if pares:
    print(f'Os valores pares são: {pares}')

valores.sort()
print(f'Valores em ordem crescente: {valores}')
  