produtos = ('Blusa',30.55, 
            'Short',40.99, 
            'Saia', 55.99,
            'Calça',65.99, 
            'Vestido',78.50, 
            'Macacão',100.90)
print('LOJINHA DA GEOW')
print('-' * 40)
print('\033[1;36mLISTAGEM DE PRODUTOS:\033[m')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:>7}')
print('-' * 40)