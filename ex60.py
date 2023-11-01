n1 = int(input('Digite um número para saber seu fatorial: '))
f1 = 1
c1 = n1
while c1 > 1:
    f1 *= c1
    c1 -= 1
print(f'O fatorial de {n1}! é {f1}')