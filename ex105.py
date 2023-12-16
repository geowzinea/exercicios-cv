def notas(*n, sit=False):
    """
    -> Análisa notas e situação de alunos 
    :param n: uma ou mais nota de alunos(aceita muitas)
    :param sit: valor opcional,indicando se deve ou não mostrar a situação.
    :return: dicionário com várias informações e situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7.0:
            r['situação'] = 'Aprovado'
        elif 5 <= r['media']:
            r['situação'] = 'Recuperação'
        else:
            r['sitação'] = 'Reprovado'
    
    return r
        

#
resp = notas(10, 8.8, 6.8, 7.1, 7.5, 3.8, sit=True)
print(resp)
help(notas)