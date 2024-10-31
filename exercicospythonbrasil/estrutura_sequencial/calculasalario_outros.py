# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# salário bruto. / quanto pagou ao INSS. / quanto pagou ao sindicato. / o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# Exemplo de porcentagem
# porcentagem = 10 
# valor = 200 
# resultado = (porcentagem / 100) * valor 
# print(resultado) # Saída: 20.0

# Exemplo de formatação
# porcentagem = 75 
# print(f"A porcentagem é {porcentagem}%") # Saída: A porcentagem é 75%

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
print('-' * 100)
valor_da_hora = float(input('Qual o valor da sua hora trabalhada? '))
horas_mes = float(input('Quantas horas você trabalha por mês? '))

# Calculando - Salário Bruto
salario_bruto = valor_da_hora * horas_mes
print('Seu salário bruto é de: R$',round(salario_bruto, 2),'por mês.')

# Calculando - INSS - 8%
desc_inss = (8 / 100) * salario_bruto
print('Você paga de INSS 8%, o que corresponde a R$', desc_inss)

# Calculando - IR - 11%
desc_ir = (11 / 100) * salario_bruto
print('Você paga de imposto de renda 11%, o que corresponde a R$', desc_ir)

# Calculando - Sindicato
desc_sindicato = (5 / 100) * salario_bruto
print('Você paga de Sindicaro 5%, o que corresponde a R$', desc_sindicato)

# Total de Descontos e slaário Liquido
print('-' * 60 )
desc_total = desc_inss + desc_ir + desc_sindicato
salario_liquido = salario_bruto - desc_total
print('-' * 60 )
print('Total de Descontos: R$', desc_total)
print('Salário Liquido: R$', salario_liquido)
print('-' * 60 )
print('-' * 100 )