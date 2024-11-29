cliente = "João"
passo = 0
status = "Aguardando novo pedido"

def entregar():
    global passo # informa que a variável a ser usada é global
    passo += 1
    status = "Pedido entregue"
    print(f"Passo {passo}: {status} ao {cliente}!")

def preparar():
    global passo
    passo += 1
    status = "Preparando..."
    print

print(status)
preparar()
entregar()