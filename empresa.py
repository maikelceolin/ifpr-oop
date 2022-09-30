import pessoa as p
from openpyxl import load_workbook

#define a classe empresa
class Empresa():
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
 
    def exibir(self):
        for fun in self.__func:
            print(fun.mostraDados())


    def mostraDados(self):
        print(str(self.__codigo)+" "+self.__nome)


#define a classe FUNCIONARIO importando a classe Pessoa da lib pessoa (pessoa.Pessoa)

class Funcionario(p.Pessoa):
    def __init__(self, cpf, nome, setor, salario, entrada, saida):
        super().__init__(cpf, nome)
        self.setor = setor
        self.salario = salario
        self.entrada = entrada
        self.saida = saida
        
    def mostraDados(self):
        return super().mostraDados()+" "+self.getSetor()

    def setor(self):
        return self.__setor

    def mostraSalario():
        print(f"Salario: {self.__salario}")

    def mostraHorario():
        print(f"\nEntrada: {self.__entrada}\nSaída: {self.__saida}")


#definição dos CARGOS DA EMPRESA herdando a classe Funcionario:


class Administrador(Funcionario):
    def __init__(self, cpf=None, nome=None, setor=None, salario=5000, entrada=None, saida=None, auxilio=None):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.auxilio = auxilio

    def folhaAdm(self):
        remuneracao = self.salario + self.auxilio
        print(f"Remuneração: {remuneracao}")

    def contratar(self, i):

        j = str(len(i))
        #abre planilha para edição
        planilha = load_workbook("./cadastro.xlsx")
        tabela = planilha.active

        print("Insira os dados do novo Administrador:")

        self.nome = str(input("Nome: "))
        self.cpf = str(input("CPF: "))
        self.setor = str(input("Setor: "))
        self.entrada = str(input("Entrada: "))
        self.saida = str(input("Saída: "))
        self.auxilio = str(input("Valor do vale gasolina: "))
        remuneracao = self.salario + self.auxilio
        
        #Insere dados na planilha iniciando da linha 2:
        tabela['A'+ j].value = self.nome # A1 - nome
        tabela['B'+ j].value = self.cpf # B1 - cpf
        tabela['C'+ j].value = self.setor # C1 - setor
        tabela['D'+ j].value = self.entrada # D1 - entrada
        tabela['E'+ j].value = self.saida # E1 - saida
        tabela['F'+ j].value = "Administrador" # F1 - Cargo
        tabela['G'+ j].value = str(self.salario) # G1 - salario
        tabela['H'+ j].value = str(self.auxilio) # H1 - auxilio
        tabela['I'+ j].value = None # I1 - vendas
        tabela['J'+ j].value = None # J1 - producao
        tabela['K'+ j].value = None # K1 - comissao
        tabela['L'+ j].value = str(remuneracao) # L1 - remuneracao

        planilha.save("./cadastro.xlsx")

class Vendedor(Funcionario):
    def __init__(self, cpf=None, nome=None, setor="Loja", salario=None, entrada=None, saida=None, vendas=0, comissao=30):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.vendas = vendas
        self.comissao = comissao

    def valorVenda(self):
        remuneracao = self.salario + self.vendas*self.comissao
        print(f"Remuneração: {remuneracao}")

    def contratar(self, i):

        j = str(len(i))

        #abre planilha para edição
        planilha = load_workbook("./cadastro.xlsx")
        tabela = planilha.active

        print("Insira os dados do novo Vendedor:")
        
        self.nome = str(input("Nome: "))
        self.cpf = str(input("CPF: "))
        self.setor = str(input("Setor: "))
        self.entrada = str(input("Entrada: "))
        self.saida = str(input("Saída: "))
        self.salario = str(input("Salario combinado: "))
        self.vendas = ""
        self.comissao = ""
        
        #Insere dados na planilha iniciando da linha 2:
        tabela['A'+ j].value = self.nome # A1 - nome
        tabela['B'+ j].value = self.cpf # B1 - cpf
        tabela['C'+ j].value = self.setor # C1 - setor
        tabela['D'+ j].value = self.entrada # D1 - entrada
        tabela['E'+ j].value = self.saida # E1 - saida
        tabela['F'+ j].value = "Vendedor" # F1 - Cargo
        tabela['G'+ j].value = self.salario # G1 - salario
        tabela['H'+ j].value = "" # H1 - auxilio
        tabela['I'+ j].value = self.vendas # I1 - vendas
        tabela['J'+ j].value = "" # J1 - producao
        tabela['K'+ j].value = self.comissao # K1 - comissao

        planilha.save("./cadastro.xlsx")

class Operario(Funcionario):
    def __init__(self, cpf=None, nome=None, setor="Fabrica", salario=2000, entrada=None, saida=None, producao=None, comissao=20):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.producao = producao
        self.comissao = comissao

    def folhaOperario(self):
        remuneracao = self.__salario + self.comissao
        print(f"Remuneração: {remuneracao}")

    def contratar(self,i):

        j = str(len(i))

        #abre planilha para edição
        planilha = load_workbook("./cadastro.xlsx")
        tabela = planilha.active

        print("Insira os dados do novo Operário:")

        self.nome = str(input("Nome: "))
        self.cpf = str(input("CPF: "))
        self.setor = str(input("Setor: "))
        self.entrada = str(input("Entrada: "))
        self.saida = str(input("Saída: "))
        remuneracao = self.salario + self.producao*self.comissao

        #Insere dados na planilha iniciando da linha 2:
        tabela['A'+ j].value = self.nome # A1 - nome
        tabela['B'+ j].value = self.cpf # B1 - cpf
        tabela['C'+ j].value = self.setor # C1 - setor
        tabela['D'+ j].value = self.entrada # D1 - entrada
        tabela['E'+ j].value = self.saida # E1 - saida
        tabela['F'+ j].value = "Operario" # F1 - Cargo
        tabela['G'+ j].value = str(self.salario) # G1 - salario
        tabela['H'+ j].value = None # H1 - auxilio
        tabela['I'+ j].value = None # I1 - vendas
        tabela['J'+ j].value = str(self.producao) # J1 - producao
        tabela['K'+ j].value = str(self.comissao) # K1 - comissao
        tabela['L'+ j].value = str(remuneracao) # L1 - remuneracao

        planilha.save("./cadastro.xlsx")


#definição dos FORNECEDORES:

class Fornecedor(p.Pessoa):
    def __init__(self, cpf, nome, credito, divida):
        p.Pessoa.__init__(cpf, nome)
        self.credito = credito
        self.divida = divida

    def obterSaldo(self):
        saldo = self.credito - self.divida
        return saldo