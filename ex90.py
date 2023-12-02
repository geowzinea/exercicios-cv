aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno ["média"] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7: 
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
    
for k, v in aluno.items():
    print(f'{k} é igual a {v}')