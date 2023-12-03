dados = dict()
partidas = []
dados['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))



for c in range(0, tot):
    gols = int(input(f'Quantos gols na partida {c}? '))
    partidas.append(gols)
    
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
    
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {tot} partidas')

for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')