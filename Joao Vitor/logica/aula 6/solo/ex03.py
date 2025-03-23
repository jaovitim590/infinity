def verificar_numero(numero):
    if numero > 0:
        return "numero positivo!"
    elif numero < 0:
        return "numero negativo!"
    else:
        return None
    
print(verificar_numero(5))