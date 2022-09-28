import funcionario
class Empresa():
    __func = []
    def __init__( self, codigo, nome, endereco, cnpj): 
        self.__codigo = codigo
        self.__nome = nome
        while True:
            print("1. Contratar")
            print("2. Exibir lista de funcionarios")
            op=int( input() )
   
            if op==1:
                self.contratar()
            elif op==2:
                self.exibir()
            else:
                print("Opçao invalida")
    def contratar(self):
        cpf = input("cpf: ")
        nome = input("Nome: ")
        setor = input("Setor: ")
        salario = input("Salario: ")
        self.__func.append( funcionario.Funcionario(cpf, nome, setor, salario) )
 
    def exibir(self):
        for fun in self.__func:
            print(fun.mostraDados())


    def mostraDados(self):
        print(str(self.__codigo)+" "+self.__nome)