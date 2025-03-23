palavra = "paralelepipedo"

cont = {}

for i in palavra:
    if i in cont:
        cont[i] += 1
    else:
        cont[i] = 1

print(cont)