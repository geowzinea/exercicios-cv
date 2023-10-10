k = float(input('Digite quantos kms você percorreu com o carro: '))
d = float(input('Digite por quantos dias você alugou o carro: '))
km = k * 0.15
di = d * 60
total = km + di 
print(f'O preço a ser pago é de R${total}')