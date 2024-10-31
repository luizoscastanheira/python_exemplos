# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário 
# de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

# Variáveis auxiliares
peso_limite_sp = 50
peso_excessivo = 0
multa_sp = 4.00

# ler a variavel peso (peso de peixes)
peso = float(input('Digite o peso total de peixes pescados: '))
# Calculando o excesso
excesso = peso - peso_limite_sp
# Calculando multa
multa_a_pagar = excesso * multa_sp

# Imprima os dados do programa com as mensagens adequadas.
print('-' * 46 )
print('O tal de peixe pescado foi de', peso, 'kg.')
print('O excesso de pescado foi de ', excesso, 'kg.')
print('A multa a pagar pelo excesso de pescado é de: ', multa_a_pagar, 'reais.')
print('-' * 46 )