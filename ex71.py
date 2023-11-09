print('=-=' * 10)
print('BANCO DA GEOW')
print('=-=' * 10)
valor = int(input('Qual é o valor que você quer sacar? R$'))
total = valor
ced = 50
totcedulas = 0

while True:
    if total >= ced:
        total -= ced
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f'Total de {totcedulas} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totcedulas = 0
        if total == 0:
         break
        
print('-' * 20)
print('Volte sempre ao BANCO DA GEOW!')
    

