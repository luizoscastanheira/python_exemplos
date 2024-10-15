## Testando herança em python

# PRIMEIRO - importar a classe pai
from pessoa import Pessoa

# SEGUNDO - criar a classe filha passando a classe Pai entre ()
class PessoaFisica(Pessoa):
   def __init__(self, CPF, nome, idade):
       super().__init__(nome, idade)
       self.CPF = CPF

   def getCPF(self):
       return self.CPF

   def setCPF(self, CPF):
       self.CPF = CPF