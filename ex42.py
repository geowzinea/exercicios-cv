analisar = 'Analisador de Triângulos'
print('-=-' * 10)
print(analisar)
print('-=-' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r3 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')