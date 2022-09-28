class Pessoa():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.__nome = nome

    def mostraDados(self):
        return self.__nome