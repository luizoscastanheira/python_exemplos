# Arquivo para criação e tste de funções

# Uma Função simples, sem parametros e sem retorno
def msg_tela():
    print('Olá Mundo!')
# Executando a função
msg_tela()

# Uma Função com paramentros
def faz_soma(num1, num2):
    print(num1 + num2)
# Chamando a função
print(faz_soma(10, 30))


# Uma Função com paramentros e com retorno
def minha_funcao(param1, param2):
    return param1 + param2
# Chamando a função
resultado = minha_funcao(10, 20)
print(resultado)  # Saída: 30

# Funçao recebendo dados do usuário
# Definindo a função
def faz_mult(num1, num2):
    return num1 * num2

numero = int(input('Digite o numero 1: '))
numero = int(input('Digite o numero 2: '))

# Chamando a Função
# Primeira Forma - usando as variáveis já declaradas
resultado = faz_mult(numero, numero)
print(resultado)
# Segunda forma - usando input direto na chamada da funçao, um para cada parametro
resultado = faz_mult(int(input('Digite o numero 1: ')), int(input('Digite o numero 2: ')) )
print(resultado)

def escolha():
    dado_digitado = input('Digite alguma coisa, texto ou numero e etc: ')
    print('Você digitou o seguinte: ', dado_digitado)
    
# Chamando a função
escolha()