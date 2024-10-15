# Testes com Estrutura de repetição

# estrutura for
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
    print(n)


frase = "Luiz Otávio AMA Rosicléia!"
conta_letras = 0
for n in frase:
    print(n)
    if n != ' ':
        conta_letras += 1
print('A Frase tem',conta_letras, 'letras, sem espaços!')

# Estrutura While
contador = 5
while contador > 0:
    print(contador)
    contador = contador - 1

contador = 0
while contador < 5 :
    print(contador)
    contador = contador + 1

contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
      #break # se usar o break o else será ignorado e pulado
else:
      print("O loop while terminou!")



# No for o uso do else é OPCIONAL!!!!!
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")


for i in range(0, 10):
    print(i)
else:
    print('Todos os numeros foram listados!')



sagas_cinema = ['Senhor dos Anéis', 'Harry Potter', 'Star Wars', 'Jogos Vorazes']

for saga in sagas_cinema:
   print(saga)