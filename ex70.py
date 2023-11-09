print('-=-' * 10)
print('LOJA BARATINHA DA GEOW')
print('-=-' * 10)
total = 0
mais = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Qual é o nome do produto? '))
    preço = int(input('Qual é o preço do produto? R$'))
    cont +=1
    total += preço
    
    if preço > 1000:
        mais += 1
    
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
        
    escolha = ' '
    while escolha not in 'SN':
        escolha =  str(input('Quer continuar? [S/N] ')).strip().upper() [0]
        
    if escolha == 'N':
         break
        
        
print(f'O total gasto na compra é de R${total:.2f}. {mais} produto custaram mais que R$1000,00. E o produto mais barato foi {barato} que custa {menor:.2f}.')
        