def ficha(jog='sem nome', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input("Digite o nome do jogador: "))
g = str(input("Digite a quantidade de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g=0
if not n.strip() == ' ':
    ficha(gol=g)
else:
    ficha(n, g)