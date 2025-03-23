lista1 = [1, 5, 3, 9, 2]
lista2 = []

def encontrar_maior(lista):
    global maior
    if not lista:
        return None
    else:
        return max(lista)


print(encontrar_maior(lista1))
print(encontrar_maior(lista2))

    