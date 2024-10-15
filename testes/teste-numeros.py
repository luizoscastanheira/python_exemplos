# Importando Decimal para teste
from decimal import Decimal


# Meses
meses = ['janeiro', 'fevereiro', 'março', 'abril']
for mes in meses:
    print('mês de', mes)

print()
print()


#Notas dos alunos
nota1 = 10
nota2 = 6
nota3 = 9
nota4 = "7"
media = (nota1 + nota2 + nota3) / 3
if(media >= 7):
    print("Aprovado")
    print("Parabéns, continue assim!!!!!")
elif (media >=5) and (media <7):
    print("Recuperação")
else:
    print("Reprovado")

print()
print()

# Testando tipos de variáveis.
print(type(nota1))
print(type(nota4))

num_complexo = 1J *3j
print(type(num_complexo))

aprovado = True
print(type(aprovado))

reprovado = "Sim"
print(type(reprovado))

num_decimal = Decimal("0.1")
print(type(num_decimal))

# comparando o numero 1 com True temos true
s = 1
if s == True:
    print("true")
else:
    print("false")