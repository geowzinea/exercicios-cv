def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


    


#programa principal
num = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o númmero {num}')