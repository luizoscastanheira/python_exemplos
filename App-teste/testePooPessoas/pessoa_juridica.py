## Testando herança em python

# PRIMEIRO - importar a classe pai
from pessoa import Pessoa

# SEGUNDO - criar a classe filha passando a classe Pai entre ()
class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, idade):
        super().__init__(nome, idade)
        self.CNPJ = CNPJ

    def getCNPJ(self):
        return self.CNPJ

    def setCNPJ(self, CNPJ):
        self.CNPJ = CNPJ