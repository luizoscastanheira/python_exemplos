# Arquvi principal

# importando as classes
from pessoa import Pessoa
from pessoa_juridica import PessoaJuridica

# Instanciando a classe pessoa
p1 = Pessoa('Luiz', 47)
print(p1.getNome(), '', p1.getIdade())

p1.setNome('Rosi')
p1.setIdade(45)

print(p1.getNome(), '', p1.getIdade())

# Testando a herança
# Instanciando a classe pesosa juridica
pj = PessoaJuridica('123123312123123', 'Luiz', 47)

print(pj.getCNPJ(), '', pj.getNome(), '', pj.getIdade())



