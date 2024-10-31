# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# Solicitando a altura
altura = float(input('Digite sua altura: '))

# Calculando - Homem
peso_ideal_homem = (72.7 * altura) - 58

# Calculando - Mulher
peso_ideal_mulher = (62.1 * altura) - 44.7

# Exibindo
print('Baseado em sua altura temos o seguinte peso ideal:')
print('Homem', peso_ideal_homem, 'kg.', 'Arredondando:', round(peso_ideal_homem, 2))
print('Mulher', peso_ideal_mulher, 'kg.', 'Arredondando:', round(peso_ideal_mulher, 2))
