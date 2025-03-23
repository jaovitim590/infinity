"""Dado um dicionário d = {"a": 1, "b": 2, "c": 3}, escreva uma função que inverta as chaves e os valores, retornando {1: 'a', 2: 'b', 3: 'c'}"""

d = {"a": 1, 
     "b": 2, 
     "c": 3}

invertido = {}

def inverter():
    for chave, valor in d.items():
        invertido[valor] = chave

inverter()
print(invertido)