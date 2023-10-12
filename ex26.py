frase = str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece {frase.count("A")} em {frase}')
print(f'A letra A aparece pela primeira vez em {frase.find("A")} em {frase}')
print(f'A letra A aparece pela última vez em {frase.rfind("A")} em {frase}')

