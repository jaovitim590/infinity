def verificar_pares(num):
    if num % 2 == 0:
        return "numero par"
    else:
        return "numero inpar"
    
i = 0
conta = 0

while i <= 100:
    if verificar_pares(i) == "numero par":
        conta += i
    i += 1

