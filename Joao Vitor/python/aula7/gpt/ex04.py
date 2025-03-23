"""Dado um dicionário, escreva uma função que verifique se uma chave específica existe nele. Se existir,
 retorne o valor associado à chave; caso contrário, retorne "Chave não encontrada"."""

notas = {'Alice': 8, 'Bob': 7, 'Carlos': 6}
espec = "Carlos"

def verificar():
    if espec in notas:
        print("chave encontrada")
    else:
        print("chave nao encontrada")

verificar()