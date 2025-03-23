print("-----calculando media-----")
cont = int(input("insira a quantidade notas que ira inserir: "))
soma = 0
for i in range(cont):
    num = float(input("insira a sua nota: "))
    soma += num

media = soma / cont

print(f"a media desses numero é : {media}")
print("-----FIM DO PROGRAMA-----")