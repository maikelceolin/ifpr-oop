class Pessoa():
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    def info(self):
        print(f"Nome: {self.__nome}  CPF:{self.__cpf}")