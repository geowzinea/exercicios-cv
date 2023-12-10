from time import sleep

def maior(*num):
    cont = maior = 0 
    print('Analisando os valores passadoss...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1 
    print(f'Foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}')
    print('-=' * 20)
    
#Programa Principal

maior(7, 3, 8, 5, 4, 9)
maior(5, 6, 3)
maior(1, 7 )
maior(9)
maior()