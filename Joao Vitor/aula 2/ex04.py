"""- Menos que 16 -> Não pode votar
- Menor que 18 e Maior ou Igual a 16 -> Voto Facultativo
- Maior ou Igual a 18 e menor que 65 -> Voto Obrigatório
- Maior que 65 -> Voto Facultativo
"""

idade = int(input("me informe sua idade: "))

if idade < 16:
    print("voce nao pode votar!")
elif idade >= 18 and idade < 65:
    print("seu voto é obrigatorio!")
elif idade > 16 or idade > 65:
    print("seu voto é facultativo!")