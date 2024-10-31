# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# Formula: C = 5 * ((F-32) / 9)

# Faça um Programa que peça a temperatura em graus Fahrenheit,
temp_fa = float(input('Digite a temparatura em graus Fahreinheit: '))

# transforme e mostre a temperatura em graus Celsius.
celsius = 5 * ((temp_fa - 32) / 9)

print('A temperatura convertida para Celsius é de ', celsius, ' Celsius.')