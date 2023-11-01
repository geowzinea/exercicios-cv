from random import randint
computador = randint(0, 10)
print('Sou seu computador e vou tentar adivinhar um número de 0 a 10.')
print('Você consegue adivinhar qual número é?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual número eu pensei? '))
    palpites += 1
    if jogador == computador:
      acertou = True
    else:
       if jogador < computador:
          print('Mais... Tente mais uma vez.')
       elif jogador > computador:
          print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns! ')