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
        
        #Insere dados na planilha iniciando da linha 2:
        tabela['A'+ str(i)] = self.nome # A1 - nome
        tabela['B'+ str(i)] = self.cpf # B1 - cpf
        tabela['C'+ str(i)] = self.setor # C1 - setor
        tabela['D'+ str(i)] = self.entrada # D1 - entrada
        tabela['E'+ str(i)] = self.saida # E1 - saida
        tabela['F'+ str(i)] = "Administrador" # F1 - Cargo
        tabela['G'+ str(i)] = self.salario # G1 - salario
        tabela['H'+ str(i)] = self.auxilio # H1 - auxilio
        tabela['I'+ str(i)] = None # I1 - vendas
        tabela['J'+ str(i)] = None # J1 - producao
        tabela['K'+ str(i)] = None # K1 - comissao
        tabela['L'+ str(i)] = self.salario + self.auxilio # L1 - remuneracao

class Vendedor(Funcionario):
    def __init__(self, cpf=None, nome=None, setor="Loja", salario=1500, entrada=None, saida=None, vendas=0, comissao=30):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.vendas = vendas
        self.comissao = comissao

    def valorVenda(self):
        remuneracao = self.salario + self.vendas*self.comissao
        print(f"Remuneração: {remuneracao}")

    def contratar(self, i):

        #abre planilha para edição
        planilha = load_workbook("./cadastro.xlsx")
        tabela = planilha.active

        print("Insira os dados do novo Vendedor:")
        
        self.nome = str(input("Nome: "))
        self.cpf = str(input("CPF: "))
        self.setor = str(input("Setor: "))
        self.entrada = str(input("Entrada: "))
        self.saida = str(input("Saída: "))
        self.auxilio = str(input("Valor do vale gasolina: "))
        
        #Insere dados na planilha iniciando da linha 2:
        tabela['A'+ str(i)] = self.nome # A1 - nome
        tabela['B'+ str(i)] = self.cpf # B1 - cpf
        tabela['C'+ str(i)] = self.setor # C1 - setor
        tabela['D'+ str(i)] = self.entrada # D1 - entrada
        tabela['E'+ str(i)] = self.saida # E1 - saida
        tabela['F'+ str(i)] = "Vendedor" # F1 - Cargo
        tabela['G'+ str(i)] = self.salario # G1 - salario
        tabela['H'+ str(i)] = None # H1 - auxilio
        tabela['I'+ str(i)] = self.vendas # I1 - vendas
        tabela['J'+ str(i)] = None # J1 - producao
        tabela['K'+ str(i)] = self.comissao # K1 - comissao
        tabela['L'+ str(i)] = self.salario + self.vendas*self.comissao # L1 - remuneracao

class Operario(Funcionario):
    def __init__(self, cpf=None, nome=None, setor="Fabrica", salario=2000, entrada=None, saida=None, producao=None, comissao=20):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.producao = producao
        self.comissao = comissao

    def folhaOperario(self):
        remuneracao = self.__salario + self.comissao
        print(f"Remuneração: {remuneracao}")

    def contratar(self,i):

        #abre planilha para edição
        planilha = load_workbook("./cadastro.xlsx")
        tabela = planilha.active

        print("Insira os dados do novo Operário:")

        self.nome = str(input("Nome: "))
        self.cpf = str(input("CPF: "))
        self.setor = str(input("Setor: "))
        self.entrada = str(input("Entrada: "))
        self.saida = str(input("Saída: "))
        self.auxilio = str(input("Valor do vale gasolina: "))
        
        #Insere dados na planilha iniciando da linha 2:
        tabela['A'+ str(i)] = self.nome # A1 - nome
        tabela['B'+ str(i)] = self.cpf # B1 - cpf
        tabela['C'+ str(i)] = self.setor # C1 - setor
        tabela['D'+ str(i)] = self.entrada # D1 - entrada
        tabela['E'+ str(i)] = self.saida # E1 - saida
        tabela['F'+ str(i)] = "Operario" # F1 - Cargo
        tabela['G'+ str(i)] = self.salario # G1 - salario
        tabela['H'+ str(i)] = None # H1 - auxilio
        tabela['I'+ str(i)] = None # I1 - vendas
        tabela['J'+ str(i)] = self.producao # J1 - producao
        tabela['K'+ str(i)] = self.comissao # K1 - comissao
        tabela['L'+ str(i)] = self.salario + self.producao*self.comissao # L1 - remuneracao


#definição dos FORNECEDORES:

class Fornecedor(p.Pessoa):
    def __init__(self, cpf, nome, credito, divida):
        p.Pessoa.__init__(cpf, nome)
        self.credito = credito
        self.divida = divida

    def obterSaldo(self):
        saldo = self.credito - self.divida
        return saldo