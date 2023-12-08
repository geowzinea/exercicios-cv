
time = list()
dados = dict()
partidas = []
while True:
    dados.clear()
    dados['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        gols = int(input(f'Quantos gols na partida {c + 1}? '))
        partidas.append(gols)
         
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end=' ')
print()
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}: ')
    else:
        print(f' --LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
            
        for i, g in enumerate(time[busca]["gols"]):
            print(f' No jogo {i + 1} fez {g} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')

        
