def area(larg, comp):
    cont = larg * comp
    print(f'A área de um terreno {l} x {c} é de {cont} m²')
   
#Programa Principal 
print('CONTROLE DE TERRENOS')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))


area(l, c)