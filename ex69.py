print('-=-' * 10)
print('CADASTRAMENTO DE PESSOAS')
print('-=-' * 10)
cont = 0
maiores = 0
menores = 0
homens = 0
while True:
    idade = int(input('Qual é a sua idade? '))
    if idade > 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o seu sexo? [F/M] ')).strip().upper() [0]
        if sexo == 'M':
            homens += 1
        elif sexo == 'F' and idade < 20:
            menores += 1 
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if continuar == 'N':
        break
    print('-' * 30)
print(f'Ao total temos {maiores} pessoas tem mais de 18 anos. {homens} homens foram cadastrados. E {menores} mulheres tem menos de 20 anos.')
    
    
    