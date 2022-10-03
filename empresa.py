
import pessoa as p

#define a classe empresa
class Empresa():
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj


#definição dos FORNECEDORES:

class Fornecedor(p.Pessoa):
    def __init__(self, cpf, nome, valorCredito, valorDivida):
        p.Pessoa.__init__(cpf, nome)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida

    def obterSaldo(self):
        saldo = self.valorCredito - self.valorDivida
        return saldo