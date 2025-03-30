alunos = {}

def pedir_notas():
    while True:
        nome = input("Digite o nome do aluno: ")

        notas = []
        for i in range(3):
            nota = float(input(f"Digite a {i + 1}ª nota do aluno {nome}: "))
            notas.append(nota)

        alunos[nome] = {"nome" : nome, "notas" : notas}
        break

pedir_notas()

soma_notas = 0

for nome , info in alunos.items():
    soma_notas = sum(info['notas'])

media = soma_notas / 3

situa = None
if media < 6 :
    situa = "reprovado!"
else:
    situa = "aprovado!"

print(alunos)
print(f"a media do aluno é : {media:.2f}")
print(situa)