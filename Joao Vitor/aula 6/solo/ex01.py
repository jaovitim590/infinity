"""Crie uma lista de números inteiros. Filtre e crie uma nova lista apenas com os números maiores que 10."""

numeros = [1,10,54,457,17,97,24,73,2,7]
numeros_maior_que_10 = []

for i in numeros:
    if i > 10:
        numeros_maior_que_10.append(i)

print(numeros)
print(numeros_maior_que_10)