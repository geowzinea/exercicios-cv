soma = 0 
cont = 0
for c in range (1, 7):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Voce informou {cont} números PARES e a soma foi de {soma}')
