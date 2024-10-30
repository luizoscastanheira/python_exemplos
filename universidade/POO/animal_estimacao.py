class AnimalEstimacao():
    def __init__(self, nome, especie, dono):
        # Definindo atributos
        self.nome = nome
        self.especie = especie
        self.dono = dono
    # Definindo métodos
    def correr(self):
        print('{0} está correndo'.format(self.nome))
    
    def brincar(self):
        print('Estou brincando')

# Criando os objetos à partir das classes
peludo = AnimalEstimacao('Peludo', 'Cão', 'Alice')
fofinho = AnimalEstimacao('Fofinho', 'Gato', 'Rosi')

print('Meu nome é: ', peludo.nome)
print('Meu nome é: ', fofinho.nome)

peludo.correr()
fofinho.brincar()