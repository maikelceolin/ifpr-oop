import pessoa as p

class Funcionario(p.Pessoa):
    def __init__(self, cpf, nome, credito, divida):
        super().__init__(cpf, nome, credito, divida)
        self.__setor = setor
        self.__salario = salario

    def mostraDados(self):
        return super().mostraDados()+" "+self.getSetor()

    def getSetor(self):
        return self.__setor