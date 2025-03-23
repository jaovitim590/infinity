soma = 0

print("-- iremos somar todos os numeros que voce enviar!")
print("--! o programa para quando voce colocar um numero negativo !--")

def pedir_numeros():
    global soma
    while True:
        try:
            numero = float(input("digite um numero:"))
            if numero >= 0 :
                soma += numero
            else:
                break
        except ValueError:
            print("digite um numero valido!")

pedir_numeros()


print(f"a soma desses numero é : {soma}")