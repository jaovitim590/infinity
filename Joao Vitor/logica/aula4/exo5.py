"""Faça um programa que peça varios numeros, e após cada numero pergunte se o usuário deseja continuar (ele deve responder 'S' para Sim e 'N' para Não), 
quando essa resposta for 'N' você deve parar a repetição e mostrar a média dos numeros digitados."""
media = 0
contagem = 0
soma = 0
def pedir_numeros():
    global contagem
    global soma
    while True:
        try:
            numero = float(input("digite um numero: "))
            contagem += 1
            soma += numero
            confirmar = input("se deseja parar digite N (tem que ser maisculo!): ")
            if confirmar == "N" or "n":

                break
        except ValueError:
            print("digite um valor valido!")

pedir_numeros()

if contagem > 0 :
    media = soma / contagem
    print(f"voce digitou {contagem} numeros!")
    print(f"a soma desses numeros é {soma}")
    print(f"a media dos numero é: {media}")
else:
    print("nenhum numero foi inserido!")

