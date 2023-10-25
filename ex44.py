print(f'{"LOJAS DA GEOW".center(40, "=")}')

preco = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
[1] À VISTA OU CHEQUE
[2] À VISTA NO CARTÃO
[3] 2x NO CARTÃO
[4] 3x OU MAIS NO CARTÃO''')

opcao = int(input('Qual é a sua forma de pagamento? '))


if opcao == 1:
    total = preco - (preco * 10 / 100)

elif opcao == 2:
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f} COM JUROS')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final')
