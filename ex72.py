from num2words import num2words

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte' )

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    
    if 0 <= n <= 20:
        n2 = num2words(n, lang='pt-br')
        print(f'Ok, você digitou {n2}')
        break  
    else:
        print('Opção inválida. Por favor, digite um número entre 0 e 20.')
