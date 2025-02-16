num =  int(input("digite um numero que deseja saber o fatorial dele: "))
conta = 1

while num > 1:
    conta *= num 
    num -= 1
print(conta)