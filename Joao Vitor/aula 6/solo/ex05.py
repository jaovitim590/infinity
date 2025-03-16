lista = [1, None, 3, None, 5]
lista_nova = []


def substituir_none(lista):
    global lista_nova
    for i in lista:
        if i is None:
            lista_nova.append("valor ausente")
        else:
            lista_nova.append(i)

substituir_none(lista)

print(lista)
print(lista_nova)