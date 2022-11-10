# App Empresa, inicializacao das classes de cargos Administrador, Operario e Vendedor

from Classes.funcionario import Funcionario


# --------------------------------------
# ADMINISTRADOR
# --------------------------------------

class Administrador(Funcionario):
    def __init__(self, nome, cpf, setor, salario, jornada, ajudaDeCusto):
        super().__init__(nome, cpf, setor, salario, jornada)
        self.__ajudaDeCusto = ajudaDeCusto

    # getters and setters
    def getAjudaCusto(self):
        return self.__ajudaDeCusto
        
    def setAjudaCusto(self, ajudaDeCusto):
        self.__ajudaDeCusto = ajudaDeCusto
    
    # app methods

    def dadosAdministrador(self):
        print(f'{self.dadosFuncionario()}')
        print(f'{self.getAjudaCusto()}')
        

# --------------------------------------
# OPERARIO
# --------------------------------------

class Operario(Funcionario):
    def __init__(self, nome, cpf, setor, salario, jornada, valorProducao, comissao):
        super().__init__(nome, cpf, setor, salario, jornada)
        self.__valorProducao = valorProducao
        self.__comissao = comissao

    # getters and setters
    def getvalorProducao(self):
        return self.__valorProducao
        
    def setvalorProducao(self, valorProducao):
        self.__valorProducao = valorProducao

    def getComissao(self):
        return self.__comissao
        
    def setComissao(self, comissao):
        self.__comissao = comissao
    
    # app methods


# --------------------------------------
# VENDEDOR
# --------------------------------------

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, setor, salario, jornada, valorVendas, comissao):
        super().__init__(nome, cpf, setor, salario, jornada)
        self.__valorVendas = valorVendas
        self.__comissao = comissao

    # getters and setters
    def getvalorVendas(self):
        return self.__valorVendas
        
    def setvalorVendas(self, valorVendas):
        self.__valorVendas = valorVendas

    def getComissao(self):
        return self.__comissao
        
    def setComissao(self, comissao):
        self.__comissao = comissao