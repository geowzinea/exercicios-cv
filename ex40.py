n1 = float(input('Sua primeira nota: '))

n2 = float(input('Sua segunda nota: '))

media = (n1 + n2) / 2

print(f'Tirando {n1:.2f} e {n2:.2f} sua média é {media:.2f}')

if 7> media >= 5:
 print('\033[1;33mO aluno está em RECUPERAÇÃO!\033[m')

elif media < 5:
 print('\033[1;31mO aluno está REPROVADO!\033[m')

else: 
 print('\033[1;32mO aluno está APROVADO!\033[m')

