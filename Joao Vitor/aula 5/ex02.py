maior_numero = None


for i in range(5):
    num =  float(input("insira um numero: "))
    if maior_numero is None or num > maior_numero:
        maior_numero = num

print(f"o maior numero inserido foi: {maior_numero}")