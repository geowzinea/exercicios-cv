peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('Você está com o PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está OBESO!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA!')
