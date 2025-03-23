"""Faça um programa que peça 6 numeros e armazene-os em uma lista. Ao final, mostre a soma entre os numeros."""

numeros = []

for i in range(6):
    num =  float(input(f"digite o {i+1} numero: "))
    numeros.append(num)

print(numeros)
print(f"a soma dos numero é: {sum(numeros)}")   
