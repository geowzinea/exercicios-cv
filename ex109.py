import moeda


#programa principal

vo = float(input('Digite o preço: R$ '))
print(f'O dobro de {moeda.moeda(vo)} é {moeda.dobro(vo, True)}')
print(f'A metade de {moeda.moeda(vo)} é {moeda.metade(vo, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(vo, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(vo, 13, True)}')