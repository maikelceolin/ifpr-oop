class Pessoa():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def info(self):
        print(f"Nome: {self.nome}  CPF:{self.cpf}")