# Programa da Loja de Tintas
#
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print('-' * 50)
print('-------------- Loja de Tintas ------------')
print('Calculadora de tintas ____________________')
print()
print('-' * 50)
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
area_pintura = float(input('Favor informar em metros quadrados a área a ser pintada: '))
print(f'Ok, você nos informou {area_pintura} metros quadrados.')

# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
vol_lata = 18
cobertura_tinta = area_pintura / 3
print(f'Para cobrir {area_pintura} metros quadrados você precisa de {cobertura_tinta} litros de tinta (Cada 1 litro cobre 3 metros quadrados).')
print('-' * 50)

# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print('Nós vendemos latas de 18 litros com valor de R$ 80.00 cada lata')
qtd_lata = cobertura_tinta / vol_lata


print('Você precisará de:')
print(qtd_lata)


