from decimal import Decimal # Importando para aprimorar a precisão decimal no lugar de float


var_1 = 0
var_2 = 0
var_3 = 0

_nome = 'Luiz Otavio'
print(_nome)

print('Variaveis globais dentro do progr principal:')
print(var_1 + var_2 + var_3)


def funcao1():
    var_4 = 10
    var_5 = 20
    print('Variáveis detro da função 1')
    print(var_4 + var_5)

def funcao2():
    global var_1 
    var_1 = 5
    var_2 = 5
    print('Variáveis detro da função 2')
    print(var_1 + var_2)

funcao1()
funcao2()

print('Após a função 2 declarar var_1 como global ela sobrepoem a var_1 do escopo principal')
print(var_1)

# usado apos importação para uma precisão maior se necessário
var_decimal = Decimal('0.1')
print(type(var_decimal))
print(var_decimal)


# comparando
var_float = 0.1
var_dec = Decimal(0.1)

print("Numero em float", var_float)
print(type(var_float))
print("Numero em Decimal", var_dec)
print(type(var_dec))
