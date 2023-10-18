casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f'A prestação será de R${prestacao}')
if salario > minimo:
    print('\033[1;32mEmpréstimo CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')