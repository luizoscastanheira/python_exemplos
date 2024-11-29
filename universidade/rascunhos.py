var_1 = 300
var_2 = 0
var_3 = 0
var_4 = 1.000


def funcao1():
    #global var_4
    var_4 = 500
    var_5 = 20
    print(f'A variavel local var_4 é {var_4} e a var_5 é {var_5}')
    print(f'Já a variável global var_1 é {var_1}')

funcao1()
print(var_4)

n_str = 'Rosicleia'

print(n_str)

contaLetras = 0
for letras in n_str:
    print(letras)
    contaLetras+=1

print('a palavra tem', contaLetras, ' letras.')

n_int = 10
n_float = 1.56
n_bool = True
n_str = 'Eu amo a Rosi'
n_lista = ['Luiz Otávio', 'Rosi', 'Guilherme']
n_tupla = ('Luiz Otávio', 'Rosi', 'Guilherme')
n_dicionario = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}
print(type(n_int))
print(type(n_float))
print(type(n_bool))
print(type(n_str))
print(type(n_lista))
print(type(n_tupla))
print(type(n_dicionario))

print(n_dicionario['Telefone'])

# Dicionário com nomes, telefones, idades e emails 
contatos = { 
    "Alice": { 
        "telefone": "1234-5678", 
        "idade": 30, 
        "email": "alice@example.com" 
    }, 
    "Bruno": { 
        "telefone": "2345-6789", 
        "idade": 25, 
        "email": "bruno@example.com" 
    }, 
    "Carlos": { 
        "telefone": "3456-7890", 
        "idade": 35, 
        "email": "carlos@example.com" 
    }, 
    "Diana": { 
        "telefone": "4567-8901", 
        "idade": 28, 
        "email": "diana@example.com" 
    }, 
    "Eduardo": { 
        "telefone": "5678-9012", 
        "idade": 40, 
        "email": "eduardo@example.com" 
    } 
} 
# Exibindo o dicionário print
print(contatos)

print(type(contatos))

