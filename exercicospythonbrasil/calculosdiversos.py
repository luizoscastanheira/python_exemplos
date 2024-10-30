# Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre: 
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.

# Faça um Programa que peça 2 números inteiros e um número real
num_inteiro1 = int(input('Digite um número inteiro (sem casa decimal): '))
num_inteiro2 = int(input('Digite outro número inteiro: '))
num_float = float(input('Agora digite um numero real (com casa decimal): '))

# Calcule e exiba o produto do dobro do primeiro com metade do segundo .
resultado = (num_inteiro1 * 2) * (num_inteiro2 / 2)
print('Calcule e exiba o produto do dobro do primeiro com metade do segundo:')
print(resultado)

# Calcule a soma do triplo do primeiro com o terceiro.
resultado = (num_inteiro1 * 3) + num_float
print('Calcule a soma do triplo do primeiro com o terceiro.')
print(resultado)

# Calcule o terceiro elevado ao cubo.
resultado = num_float ** 3
print('Calcule o terceiro elevado ao cubo')
print(resultado)
