salario = float(input('Qual é o seu salário? '))
if salario <= 1250:
    aumento = salario + (salario * 15/ 100)
else: 
    aumento = salario + (salario * 10 / 100)
print(f'O seu novo salário passa a ser de R${aumento}')