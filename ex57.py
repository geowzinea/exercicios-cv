s = str(input('Digite seu sexo:[M/F] ')).strip().upper() [0]
while s not in 'MmFf':
    s = str(input('Dados inválidos. Por Favor, informe seu sexo: ')).strip().upper() [0]
print(f'Sexo {s} foi registrado com sucesso!')
