# Calcuclando IMC

# Variáveis Globais
nome = ""
altura = 0. # O ponto logo após o zero indica que srá dados tipo float
peso = 0.
imc = 0. # resultado

def le_dados():
    global nome
    global altura
    global peso
    # Coletando informação usuário
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

def calcula_imc():
    global peso
    global altura
    # Calculando
    imc = peso / pow(altura, 2)
    return round (imc, 2)

def avalia_imc():
    imc = calcula_imc()
    if imc < 18.5:
        return "Abaixo do peso."
    elif imc >= 18.5 and imc <= 25:
        return "Peso normal."
    else:
        return "Com sobrepeso."
    
le_dados()
imc = calcula_imc()
msg = avalia_imc()
print(f'{nome} está {msg}')