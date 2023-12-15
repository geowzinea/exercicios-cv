def fatorial(n, show=False):
    """
    -> Calcula fatorial de um número.
    :param n: O número a ser calculado.
    :param show: Valor lógico mostrar ou não a conta (opcional)
    :return: retorna o valor de fatorial de um número n
    
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x')
            
        f *= c
    return f


#programa principal
#print(fatorial(7, show=True))
help(fatorial)

