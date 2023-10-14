from random import randint
computador = randint(0,5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Qual número eu pensei? ')) #jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você consegiu me vencer!')
else:
    print(f'GANHEI! Pensei no número {computador} e não {jogador}')