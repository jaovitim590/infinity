"""Dado um dicionário, escreva uma função que remova todas as chaves que possuem um valor específico."""

notas = {'Alice': 8, 'Bob': 7, 'Carlos': 6}
val = 6

def remove():
    chave_vala = [chave for chave, valor in notas.items() if valor == val]

    for chave in chave_vala:
        notas.pop(chave)

remove()
print(notas)