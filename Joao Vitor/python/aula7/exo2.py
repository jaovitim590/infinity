"""Faça um programa que peça 5 nomes e mostre todos os nomes digitados"""

nomes = []

for i in range(5):
    nome = input("digite um nome: ")
    nomes.append(nome)

print(nomes)