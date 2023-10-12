from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o cosseno de {cosseno}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a tangente de {tangente}')