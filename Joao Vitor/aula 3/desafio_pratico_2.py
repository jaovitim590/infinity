from desafio_pratico import verificar_pares

i = 0 
conta = 0

while i <= 50:
    if verificar_pares(i) == "numero inpar":
        conta += i
    i += 1
print(conta)