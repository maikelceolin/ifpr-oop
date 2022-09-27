
class Funcionario():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def show(self):
        print(f"\nCPF: {self.cpf}\n{self.nome}\n")
