# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
pi = 3.14159

raio = float(input('Digite o raio do circulo a ser calculada a área: '))
area = pi * raio**2 # usando base ** expoente
area2 = pi * pow(raio,2) # usando função pow(base, expoente)
print(area)
print(area2)
