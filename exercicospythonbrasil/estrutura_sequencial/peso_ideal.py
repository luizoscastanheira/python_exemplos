# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58

# Entrada da altura 
altura = float(input('Digite sua altura: '))

# Calcule o peso ideal
peso_ideal = (72.7 * altura) - 58
print('Baseado em sua altura o peso idela seria de: ', peso_ideal, 'kg.')
print('Arredondando:', round(peso_ideal, 2))