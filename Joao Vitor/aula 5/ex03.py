maior_numero = None
menor_numero = None
soma = 0
cont = 0

def pedir_numeros():
    global maior_numero
    global menor_numero
    global soma
    global cont
    
    while True:
        try:
            numero = input("Digite um número (ou 's' para parar): ")

            if numero.lower() == 's':  
                break
            
            numero = float(numero)
            cont += 1
            
            if maior_numero is None or numero > maior_numero:
                maior_numero = numero
            if menor_numero is None or numero < menor_numero:
                menor_numero = numero
            
            soma += numero

        except ValueError:
            print("Digite um número válido ou 's' para parar.")


pedir_numeros()

if cont > 0:
    media = soma / cont
    print(f"Você inseriu {cont} números.")
    print(f"O menor número é: {menor_numero}")
    print(f"O maior número é: {maior_numero}")
    print(f"A soma dos números é: {soma}")
    print(f"A média dos números é: {media}")
else:
    print("Nenhum número válido foi inserido.")
