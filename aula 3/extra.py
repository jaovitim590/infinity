def ano_bissexto(ano):
    if ano % 400 == 0:
        return(f" {ano} é um ano bissexto!")
    elif ano % 4 == 0 and ano % 100 != 0:
        return(f"{ano} é um ano bissexto!")
    else:
        return(f"{ano} nao é um ano bissexto!")


num =  int(input("digite um ano: "))

print(ano_bissexto(num))

