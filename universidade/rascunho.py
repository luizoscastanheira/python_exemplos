
# convertendo tipos
a = float(22/5)
b = int(4.5)
c = int(3.9)
d = int(0xff563)
e = float(int(3.9))
f = int(float(3.9))
g = int(float(3))
h = round(3.9)
i = round(3)
j = int(round(3.9))
print(a,b,c,d,e,f,g,h,i,j)

# strings
a = 'Isso é uma String com aspas Simples'
b = "Isso é uma String com aspas Duplas"
c = """Isso é Uma String com aspas Triplas"""
print(a + "\n" + b + "\n" + c)

#Na linha abaixo é utilizado um comentário #coding: utf-8, que permite a acentuação.

#coding: utf-8
meu_nome = "Sintaxes Python"
meu_nick = 'Devmedia'
print ("Nome: %s, Nick: %s" % (meu_nome.upper(), meu_nick))
print ("Meu nome comeca com a letra ", meu_nome[0])
print ("Meu nome comeca com a letra ", meu_nome[0].lower())
print ("Meu primeiro nome é ", meu_nome[0:7])


# coding: utf-8
var1 = int(input("Digite um Número para var1"))
var2 = int(input("Digite um Número para var2"))
if var1 == 1:
  print("Número var1 igual a 1")
elif var1 == 2 or var2 == 3:
  print("var1 diferente de 1 ou var2 diferente de 2")
elif var1 >= 1000 or var2 <= -1000:
  print("var1 maior que 1000 ou var2 menor que -1000")
else:
  print("nenhuma das alternativas anteriores")


texto_longo = '''
 Primeira linha do "texto"
 Segunda linha do texto
 Terceira linha do texto
 '''

print(texto_longo)