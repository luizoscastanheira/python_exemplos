# App de Calculo de Volume para pintura de paredes

# importando classe
from calculadora import Calculadora
from comodo import Comodo

# instanciando um objeto calculadora
calc = Calculadora()

# Criando as Variáveis
altura:float = float(input('Qual a altura do cômodo? '))
largura:float = float(input('Qual a largura do cômodo? '))
profundidade:float = float(input('Qual a profundidade do cômodo? '))

# intanciando um objeto comodo
comodo = Comodo(largura, profundidade)
# melhorando e criando input ao intanciar o objeto
#comodo = Comodo(input('Qual a largura do cômodo? '), input('Qual a profundidade do cômodo? '))

# Fórmula básica para o calculo da área das paredes
#calc.area_paredes = 2 * (largura + profundidade) * altura

print('Área das parede é: ', calc.calcular_area_paredes(comodo.largura,comodo.profundidade,comodo.altura))

# Fórmula cara calcular aarea do teto
#calc.area_teto = largura * profundidade
print('A área do teto é: ', calc.calcular_area_teto(comodo.largura,comodo.profundidade))

# Litragem de tinta - a divisão por 10 é uma estimativa de rendimento da tinta por 1 litro para 10 metros quadrados
print('A litragem de tinta necessária é: ', calc.litragem_necessaria())