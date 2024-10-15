dados_cliente = [
    {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul',  'Telefone': '982503645'},
    {'Nome': 'Luiz', 'Endereco': 'Rua Henrique Marinho', 'Telefone': '981839564'}
]

print(dados_cliente)
print(dados_cliente[1])
print(dados_cliente[1]['Nome'])

print(type(dados_cliente))
print(type(dados_cliente[1]))
print(type(dados_cliente[1]['Nome']))


idiomas = ['francês', 'italiano', 'inglês', 'japonês']

for idioma in idiomas:
    print(idioma)


# Abaixo ao declarar o tipo de variável criamos uma type hint
# A tipagem continua dinâmica
numero_1: float = 5.1
nome: str = 'luiz'

print(type(numero_1))
print(type(nome))