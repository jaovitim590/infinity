"""Dado um dicionário de estudantes com suas respectivas notas, calcule a média de notas de todos os alunos. """

notas = {'Alice': 8, 'Bob': 7, 'Carlos': 6}
quantidade = 0
soma = 0

def cal_media():
    global quantidade
    global soma
    for chave, valor in notas.items():
        quantidade += 1
        soma += valor

cal_media()
media = soma / quantidade

print(media)
