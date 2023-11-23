valores = []
for cont in range(0, 5):
    valor = (int(input('Digite um valor: ')))

    if len(valores) == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        for i in range (len(valores)):
            if valor <= valores[i]:
                valores.insert(i, valor)
                break
print(valores)
    
    