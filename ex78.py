valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    
maior = max(valores)
menor = min(valores)

for pos, v in enumerate(valores):
    if v == maior:
     print(f'O maior valor é {maior} e está na posição {pos} ')
    if v == menor:
     print(f'O menor valor é {menor} e está na posição {pos}')
    