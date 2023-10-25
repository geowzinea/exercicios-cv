from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print('-=' * 11)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #compurador nogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif computador == 1:
        print( 'COMPUTADOR VENCE')
    elif computador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
