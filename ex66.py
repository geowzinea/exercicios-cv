n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Foram digitados {cont} números e a soma deles é igual a {soma}')
