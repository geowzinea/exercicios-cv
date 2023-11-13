valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))
valor4 = int(input('Digite o quarto número: '))
cont = 0

valores = (valor1, valor2, valor3, valor4)
tres = valores.index(3)

print(f'Os valores digitados são: {valores}')

for valor in valores:
    if valor == 9:
        cont += 1

if cont > 0:
    print(f'O número 9 apareceu {cont} vezes')
else:
    print('O número 9 não apareceu na tupla')

print(f'O número 3 aparece primeiro na posição {tres}')

pares = [valor for valor in valores if valor % 2 == 0]
print(f'Os números pares digitados foram {pares}')