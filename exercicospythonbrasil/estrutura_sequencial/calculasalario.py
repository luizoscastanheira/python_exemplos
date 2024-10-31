# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
valor_hora = float(input('Qual o valor de sua hora trabalhada? '))
hora_trabalhada = float(input('Quantas horas você trabalha por dia? '))

# Calcule e mostre o total do seu salário no referido mês.
salario_total = valor_hora * hora_trabalhada

# Sem arredondar o resultado
print('Seu salário total é de', salario_total , ' reais por mês')
# Arredondando o resultado com o round(valor, casas Decimais)
print('Seu salário total é de', round(salario_total, 2), ' reais por mês')