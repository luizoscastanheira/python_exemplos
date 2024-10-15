# testando a cricação de Funções

# Teste 1 - com um parâmetro
def hello(meu_nome):
    print('Olá', meu_nome)

hello('Luiz')
hello('Rosi')

# Teste 2 - com 2 parametros
def hello(meu_nome, idade):
   print('Olá',meu_nome,'\nSua idade é:',idade)

hello('Luiz', 47)
hello('Rosi', 45)
hello('Guilherme', 24)

# funçao com paramentro e com retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)


def conta(a, b, c):
    if a == 'm':
        return b * c
    elif a == 's':
        return b + c
    else:
        print('Escolha s para Soma ou m para multiplicar')

resultado = conta('s', 10, 5)
print(resultado)



def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

valor_fatorial = fatorial(5)
print(valor_fatorial)


def converteMaiuscula(texto):
    texto_convertido = texto.upper()
    return texto_convertido

frase = 'Estou aprendendo funções na linguagem Python'
frase_convertida = converteMaiuscula(frase)
print(frase_convertida)
    



def verifica_numero(num):
    if num % 2 == 0:
        print("Esse número é par!")
    else:
        print("Esse número é ímpar")

numero = int(input("Digite um número: "))
verifica_numero(numero) # descomente para o numero ser solicitado



temperatura_celsius = int(input("Digite a temperatura em graus celsius: "))

def celsius_fahreinheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit

temperatura_fahrenheit = celsius_fahreinheit(temperatura_celsius)
print(temperatura_celsius,"°C equivalem a : ", temperatura_fahrenheit, "°F")



def soma(num_1, num_2):
    return num_1 + num_2

def subtrai(num_1,num_2):
    total = 0
    total = num_1 - num_2
    return total



numero_1 = 10
numero_2 = 5

soma_numeros = soma(numero_1, numero_2)
print(soma_numeros, ' é a Soma')

subtrai_numeros = subtrai(numero_1, numero_2)
print(subtrai_numeros, ' É a subtração')


idade = 17

if idade <= 12:
    print("criança")
elif idade > 12 and idade <= 17:
    print("adolescente")
elif idade >= 18 and idade <= 59:
    print("adulto")
else:
    print("idoso")

# Trabalhando com parâmetos nomeados

def calculo_imc(peso, altura):
    print(peso / altura ** 2)

calculo_imc(75, 1.68)
calculo_imc(peso=75, altura=1.68)
calculo_imc(altura=1.68, peso=75) # invertento os parametros nomeados




def calcula_desconto(preco, desconto):
    novo_preco = preco - ( preco * desconto )
    return novo_preco

preco = 50
desconto = 0.1

preco_com_desconto = calcula_desconto(preco, desconto)

print("O preço do produto é: ", preco)
print("O preço do produto com desconto é: ", preco_com_desconto )


def imprime_tamanho(texto):
    print(len(texto))

texto = "Eu sou programador Python"
imprime_tamanho(texto)



def imprime_min_max(lista_numeros):
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)
    print("O número máximo da lista é: " + str(maximo))
    print("O número mínimo da lista é: " + str(minimo))

numeros = [10, 15, 28, 4, 17, 26, 1, 3, 39]

imprime_min_max(numeros)



def retorna_soma(valores):
    soma = 0
    for valor in valores:
        soma = soma + valor
    return soma

numeros = [5, 10, 15, 25]
soma_numeros = retorna_soma(numeros)
print(soma_numeros)