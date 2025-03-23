import unicodedata

def remover_acentos(texto):
    # Normaliza o texto para decompor os caracteres acentuados
    nfkd = unicodedata.normalize('NFKD', texto)
    # Filtra e mantém apenas os caracteres que não são acentos
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])

print("contador de vogais")
palavra  = input("insira a palavra: ")
vogais = 'aeiou'
contagem = 0
palavra = remover_acentos(palavra)

for letra in palavra:
    
    if letra.lower() in vogais:
        print(letra)
        contagem += 1

print(f"a palavra tem {contagem} vogais!")