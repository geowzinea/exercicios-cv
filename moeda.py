import locale 

def aumentar(vo=0, taxa = 0,formato=False):
    aumento = vo * taxa / 100
    nv = vo + aumento
    return nv if formato is False else moeda(nv)


def diminuir(vo=0, taxa = 0,formato=False):
    nv = vo * (vo - taxa) / 100
    return nv if formato is False else moeda(nv)

def dobro(vo=0, formato=False):
    nv = vo * 2
    return nv if not formato is False else moeda(nv) 

def metade(vo=0, formato=False):
    nv = vo / 2
    return nv if not formato else moeda(nv)

def moeda(valor=0):
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
    vf = locale.currency(valor, grouping=True)
    return vf