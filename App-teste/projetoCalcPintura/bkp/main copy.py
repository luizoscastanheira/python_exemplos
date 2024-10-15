# App de Calculo de Volume para pintura de paredes

# Criando as Variáveis
altura:float = float(input('Qual a altura do cômodo? '))
largura:float = float(input('Qual a largura do cômodo? '))
profundidade:float = float(input('Qual a profundidade do cômodo? '))

# Fórmula básica para o calculo da área das paredes
area_paredes: float = 2 * (largura + profundidade) * altura
print('Área das parede é: ', area_paredes)

# Fórmula cara calcular aarea do teto
area_teto: float = largura * profundidade
print('A área do teto é: ', area_teto)

# Litragem de tinta - a divisão por 10 é uma estimativa de rendimento da tinta por 1 litro para 10 metros quadrados
print('A litragem de tinta necessária é: ',(area_paredes + area_teto) / 10)