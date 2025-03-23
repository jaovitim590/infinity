import random

print("-- bem vindo ao jogo do adivinha! --")

print("--esse jogo ira escolher um numero entre 1 a 100--")

numero = random.randint(1, 100)

def obter_tentativa():
    while True:
        try:
            tentativa = int(input("faça seu chute: "))
            return tentativa
        except ValueError:
            print("por favor , digite um numero valido!")

tentativa = obter_tentativa()

while tentativa != numero:
    if tentativa < numero:
        print("mais alto!")
    else:
        print("mais baixo!")
    tentativa = obter_tentativa()

print("Parabens, você acertou!")