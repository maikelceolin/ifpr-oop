import pessoa as p

#define a classe empresa
class Empresa():
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

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


#define a classe FUNCIONARIO importando a classe Pessoa da lib pessoa (pessoa.Pessoa)

class Funcionario(p.Pessoa):
    def __init__(self, cpf, nome, setor, salario, entrada, saida):
        p.Pessoa.__init__(cpf, nome)
        self.__setor = setor
        self.__salario = salario
        self.__entrada = entrada
        self.__saida = saida

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
    def __init__(self, cpf, nome, setor, salario, entrada, saida, ajudaCusto):
        Funcionario.__init__(cpf, nome, setor, salario, entrada, saida)
        self.ajudaCusto = ajudaCusto

    def folhaAdm(self):
        remuneracao = self.__salario + self.ajudaCusto
        print(f"Remuneração: {remuneracao}")


class Vendedor(Funcionario):
    def __init__(self, cpf, nome, setor, salario, entrada, saida, valorVendas):
        Funcionario.__init__(cpf, nome, setor, salario, entrada, saida)
        self.valorVendas = valorVendas

    def valorVenda(self):
        remuneracao = self.__salario + self.valorVendas
        print(f"Remuneração: {remuneracao}")


class Operario(Funcionario):
    def __init__(self, cpf, nome, setor, salario, entrada, saida, valorProducao, comissao):
        Funcionario.__init__(cpf, nome, setor, salario, entrada, saida)
        self.valorProducao = valorProducao
        self.comissao = comissao

    def folhaOperario(self):
        remuneracao = self.__salario + self.comissao
        print(f"Remuneração: {remuneracao}")




#definição dos FORNECEDORES:

class Fornecedor(p.Pessoa):
    def __init__(self, cpf, nome, credito, divida):
        p.Pessoa.__init__(cpf, nome)
        self.credito = credito
        self.divida = divida

    def obterSaldo(self):
        saldo = self.credito - self.divida
        return saldo