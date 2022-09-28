import funcionario

class Administrador(funcionario.Funcionario):
    def __init__(self, cpf, nome, credito, divida, ajudaCusto):
        super().__init__(self, cpf, nome, credito, divida)
        self.ajudaCusto = ajudaCusto