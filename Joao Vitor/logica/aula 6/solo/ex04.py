res = 2

def definir_valor():
    global res
    if res == None:
        res = "valor definido"
        return res
    else: 
        return "valor ja definido!"
    
print(definir_valor())