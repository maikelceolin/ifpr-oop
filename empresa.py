import funcionario as func

class Empresa():
    def __init__(self, codigo, nome, end, cnpj, cpf, func):
        self.__codigo = codigo
        self.__nome = nome
        self.__end = end
        self.__cnpj = cnpj
        self.__cpf = func.Funcionario.cpf
        self.__func = func

    def describe(self):
        print(f"\nCodigo: {self.__codigo}\nNome: {self.nome}\nEndereço:{self.__end}\nCPNJ:{self.__cnpj}\n")

    def showfunc(self):
        print(f"CPF:{self.__cpf}\nFuncionário:{self.__func}")

#contratar  

    #pedir dados
#associacao, agragação e heranç
#exibir lista de funcionarios


