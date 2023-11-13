from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

menor = min(num)
maior = max(num)
print(f'Os valores sorteados foram {num}')
print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')
