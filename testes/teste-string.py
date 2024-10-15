

# testando uso de tipo string e seus métodos

nome = "Luiz Otávio da Silva Castanheira"
print(nome)
print(type(nome))

# id() fornece o endereço de memória de uma variável
print(id(nome))
print(len(nome))
nome = "Rosicléia"
print(id(nome))

# len() serve para dar o tamanho, a contagem de caracteres de uma string, incluindo espaços
print(len(nome))

#Descomenta abaixo e verá que dá erro
# nome[3] ='s'

# Comparando variaveis

nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 is nome_2:
    print('iguais')
else:
    print('diferentes')

if nome_1 == nome_2:
    print('iguais')
else:
    print('diferentes')

## Testando métodos de string

# Método find()
mensagem = 'Luiz Otávio ama Rosi'
print(mensagem.find('Rosi'))

# Método replace()
mensagem = 'Quero aprender Java! Na DevMedia tem salas de Java para aprender essa linguagem'
nova_mensagem = mensagem.replace('Java', 'Python')
print(nova_mensagem) # Quero aprender Python! Na DevMedia tem salas de Python para aprender essa linguagem

# Método split()
mensagem = 'Estou aprendendo Python na DevMedia'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem)) # type 'list'
print(nova_mensagem) # ['Estou', 'aprendendo', 'Python', 'na', 'DevMedia']
print(nova_mensagem[1:3])
print(nova_mensagem[0])

# Trabalhando com Lista, tuplas e dicionários

# Lista
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana
print(programadores)

programadores[1] = 'Carolina'
print(programadores)

programadores.append('Renato')
print(programadores)

programadores.insert(1, 'Rafael')
print(programadores) 

programadores.remove('Victor')
print(programadores)

programadores.pop(0)
print(programadores)

seu_nome = input("Qual é o seu nome? ")
print(seu_nome)