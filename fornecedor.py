import pessoa as p

class Fornecedor(p.Pessoa):
    def __init__(self, cpf, nome, credito, divida):
        super().__init__(cpf, nome)
        self.credito = credito
        self.divida = divida

    def obterSaldo(self):
        saldo = self.credito - self.divida
        return saldo