import pessoa as p

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
    def __init__(self, cpf=None, nome=None, setor=None, salario=None, entrada=None, saida=None, ajudaCusto=None):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.ajudaCusto = ajudaCusto

    def folhaAdm(self):
        remuneracao = self.__salario + self.ajudaCusto
        print(f"Remuneração: {remuneracao}")

    def contratar(self):
        print("Insira os dados do novo Administrador:")

        cpf = str(input("CPF: "))
        self.cpf = cpf

        nome = str(input("Nome: "))
        self.nome = nome

        setor = str(input("Setor: "))
        self.setor = setor

        entrada = str(input("Entrada: "))
        self.entrada = entrada

        saida = str(input("Saída: "))
        self.saida = saida

        ajudaCusto = str(input("Valor do vale gasolina: "))
        self.ajudaCusto = ajudaCusto

class Vendedor(Funcionario):
    def __init__(self, cpf=None, nome=None, setor="Loja", salario=None, entrada=None, saida=None, valorVendas=0, comissao=30):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.valorVendas = valorVendas
        self.comissao = comissao

    def valorVenda(self):
        remuneracao = self.salario + self.valorVendas*comissao
        print(f"Remuneração: {remuneracao}")

    def contratar(self):
        print("Insira os dados do novo Vendedor:")
        
        cpf = str(input("CPF: "))
        self.cpf = cpf

        nome = str(input("Nome: "))
        self.nome = nome

        setor = str(input("Setor: "))
        self.setor = setor

        entrada = str(input("Entrada: "))
        self.entrada = entrada

        saida = str(input("Saída: "))
        self.saida = saida

class Operario(Funcionario):
    def __init__(self, cpf=None, nome=None, setor="Fabrica", salario=2000, entrada=None, saida=None, valorProducao=None, comissao=20):
        super().__init__(cpf, nome, setor, salario, entrada, saida)
        self.valorProducao = valorProducao
        self.comissao = comissao

    def folhaOperario(self):
        remuneracao = self.__salario + self.comissao
        print(f"Remuneração: {remuneracao}")

    def contratar(self):
        print("Insira os dados do novo Operário:")

        cpf = str(input("CPF: "))
        self.cpf = cpf

        nome = str(input("Nome: "))
        self.nome = nome

        setor = str(input("Setor: "))
        self.setor = setor

        entrada = str(input("Entrada: "))
        self.entrada = entrada

        saida = str(input("Saída: "))
        self.saida = saida



#definição dos FORNECEDORES:

class Fornecedor(p.Pessoa):
    def __init__(self, cpf, nome, credito, divida):
        p.Pessoa.__init__(cpf, nome)
        self.credito = credito
        self.divida = divida

    def obterSaldo(self):
        saldo = self.credito - self.divida
        return saldo