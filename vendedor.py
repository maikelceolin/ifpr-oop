import funcionario

class Vendedor(funcionario.Funcionario):
    def __init__(self, cpf, nome, credito, divida, ajudaCusto, valorVenda, comissao):
        super().__init__(self, cpf, nome, credito, divida)
        self.valorVenda = valorVenda
        self.comissao = comissao

        
