import unicodedata

def remover_acentos(texto):
    # Normaliza o texto para decompor os caracteres acentuados
    nfkd = unicodedata.normalize('NFKD', texto)
    # Filtra e mantém apenas os caracteres que não são acentos
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])


idades = {
    'Joao': 30,
    'Maria': None,
    'Carlos': 25
}

def verificar_idade(nome):


    nome = remover_acentos(nome)
    if nome in idades :
        if idades[nome] is None:
            return "idade nao disponivel"
        else:
            return idades[nome]
        
    else: 
        return "pessoa nao encontrada"
    
print(verificar_idade("João"))
print(verificar_idade("Maria"))
print(verificar_idade("Carlinhos"))