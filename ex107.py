import moeda 

#programa principal

vo = float(input('Digite o preço: R$ '))
print(f'O dobro de {vo} é {moeda.dobro(vo)}')
print(f'A metade de {vo} é {moeda.metade(vo)}')
print(f'Aumentando 10%, temos {moeda.aumentar(vo)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(vo)}')