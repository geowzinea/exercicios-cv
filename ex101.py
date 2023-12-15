def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    
    if idade < 16:
        return (f"Com {idade} anos: VOTO É NEGADO")
    elif 16 <= idade < 18 or idade > 70:
        return (f"Com {idade} anos: VOTO É OPCIONAL")
    else:
        return (f"Com {idade} anos: VOTO É OBRIGATÓRIO")
        

    

print('-=' * 20)
nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))



