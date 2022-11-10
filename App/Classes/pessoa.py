# App Empresa, inicializacao classe Pessoa

class Pessoa ():
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    # getters and setters
    def getNome(self):
        return self.__nome

    def setNome (self, nome):
        self.__nome = nome

    def getCpf(self):
        return self.__cpf

    def setCpf (self, cpf):
        self.__cpf = cpf
    
    # app methods
    def dadosPessoa(self):
        print(f'Nome: ${self.getNome()}')
        print(f'CPF: ${self.getCpf()}')
    


