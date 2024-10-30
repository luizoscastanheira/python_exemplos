# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.
# Formula: F = (C * (9/5)) + 32 --- 
# o 9/5 equivale a 1.8 se quiser usar na formula

# Faça um Programa que peça a temperatura em graus Celsius,
temp_celsius = float(input('Digite a Temperatura em Graus Celsius: '))

# transforme e mostre em graus Fahrenheit.
temp_fa = (temp_celsius * (1.8)) + 32
print('A temperatura digitada em Celsis equivale a ', temp_fa, 'graus Fahreinht.')