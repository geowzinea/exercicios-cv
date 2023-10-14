velo = int(input('Qual é a velocidade do carro? '))
if velo >= 80:
    print(f'MULTADO! Você excedeu  a velocidade permitida que é de 80Km')
    multa = (velo - 80) * 7
    print(f'Você deve pagar uma multa de R${multa}')
print('Tenha um bom dia! Dirija com segurança.')