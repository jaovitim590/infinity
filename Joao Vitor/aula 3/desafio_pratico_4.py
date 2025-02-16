from desafio_pratico import verificar_pares


comeco = int(input("digite o comeco do intervalo: "))
fim = int(input("digite o fim do intervalo: "))



while comeco <= fim:
    if verificar_pares(comeco) == "numero par":
        print(comeco)

    comeco += 1

