# App Empresa, inicializacao classe Funcionario

from Classes.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, setor, salario, jornada):
        super().__init__(nome, cpf)
        self.__setor = setor
        self.__salario = salario
        self.__jornada = jornada

    # getters and setters
    def getSetor (self):
        return self.__setor
    
    def setSetor (self, setor):
        self.__setor = setor
    
    def getSalario (self):
        return self.__salario
    
    def setSalario (self, salario):
        self.__setor = salario
    
    def getJornada (self):
        return self.__jornada
    
    def setJornada (self, jornada):
        self.__setor = jornada

    # app methods
    def dadosFuncionario(self):
        print(f'Setor: ${self.dadosPessoa()}')
        print(f'Setor: ${self.getSetor()}')
        print(f'Salario: ${self.getSalario()}')
        print(f'Jornada: ${self.getJornada()}')
       
