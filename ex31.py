distancia = float(input('Qual é a distância da viagem? '))
print(f'Você está prestar a fazer uma viagem de {distancia} Km')
if distancia >= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem será de {preco}')