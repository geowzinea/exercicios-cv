valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
          [1]SOMAR
          [2] MULTIPLICAR
          [3] MAIOR
          [4] NOVO NÚMERO
          [5] SAIR DO PROGRAMA
          ''')
    
    opcao = int(input('Qual é a opção desejada? '))
    
    if opcao == 1:
        soma = valor1 + valor2
        print('-=-' * 15)
        print(f'A soma de {valor1} com {valor2} é igual a {soma}')
        print('-=-' * 15)
        
    elif opcao == 2:
        multi = valor1 * valor2
        print('-=-' * 15)
        print(f'A multiplicação de {valor1} e {valor2} é igual a {multi}')
        print('-=-' * 15)
        
    elif opcao == 3:
        if valor1 > valor2:
            print('-=-' * 15)
            print(f'O valor {valor1} é maior que o  valor {valor2} ')
            print('-=-' * 15) 
        else:
            print('-=-' * 15)
            print(f'O valor {valor2} é maior que o valor {valor1} ')
            print('-=-' * 15)
            
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        
    elif opcao ==5:
        print('Programa finalizado com sucesso!')
        
        
    else:
        print('OPÇÃO INVÁLIDA! DIGITE A OPÇÃO NOVAMENTE.')
        
print('Fim do programa. Volte sempre :)')
            
