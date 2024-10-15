# Trabalhando com Lista, tuplas e dicionários

# Lista e seus métodos
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


# Tuplas e seus métodos
times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco', 'Bangu')

print(type(times_rj)) # class=’tuple’
print(times_rj) 
print(len(times_rj))

print(times_rj[0])

# Descomente a linha abaixo e veja o erro ao tentar alterar a tupla
#times_rj[0] = 'Bangu'

# Comparação - Aviso use uma virgula se a tupla tiver só um item ou vira objeto string
objeto_string = ('tesoura')
objeto_tupla = ('tesoura',)

print(type(objeto_string)) # class 'str'
print(type(objeto_tupla)) # class 'tuple'


frutas = 'Uva Goiaba Banana Ameixa Abacaxi Maracujá'
frutas_lista = frutas.split(' ')
print(type(frutas_lista))
print(frutas_lista)


# Dicionários e seu métodos
dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}
print(dados_cliente)
print(dados_cliente['Nome'])

print('Nome:', dados_cliente['Nome'], 'Telefone:', dados_cliente['Telefone'])

# Adicionando mais uma par chave/valor
dados_cliente['Idade'] = 40
print(dados_cliente)

# Removendo item do dicionario com pop()
dados_cliente.pop('Telefone', None)
print(dados_cliente)

# Removendo intem do dicionário com del
del dados_cliente['Idade']
print(dados_cliente)


# Funções para coleções

numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']

print(min(numeros)) # 0
print(max(numeros)) # 20
print(min(nomes)) # Alex
print(max(nomes)) # Renata

print(sum(numeros))

print(len(numeros))
print(len(nomes))

professores = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
cliente = {
    'Nome': 'Fábio Garcia',
    'email' : 'fabio_garcia_9@outlook.com'
}

print(type(professores)) # list
print(type(estacoes)) # tuple
print(type(cliente))


for i in range(len(professores)):
    print(i)