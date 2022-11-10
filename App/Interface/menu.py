from Classes.cargo import *
import os


class Menu():
    def __init__(self) -> None:
        pass

    
# --------------------------------------
# MENU PRINCIPAL
# --------------------------------------
    def mainMenu(self):
        os.system("tput setaf 3")
        print("""
            Selecione uma opcao abaixo:\n
            1. Cadastrar novo funcionario
            2. Relatorio de funcionarios

            0. Sair do sistema
        """)

        self.mainOption()

# --------------------------------------
# OPCAO MENU PRINCIPAL
# --------------------------------------

    def mainOption(self):
        op = input(str(""))

        while True:
            if (op == "1"):
                self.registerMenu()

            elif (op == "2"):
                self.reportMenu()

            elif (op == "0"):
                print('Goodbye! ')
                break

            else:
                os.system("tput setaf 1")
                print('\n\nPor favor, digite uma opcao valida\n\n')
                self.mainMenu()


# --------------------------------------
# MENU DE REGISTRO DE FUNCIONARIOS
# --------------------------------------

    def registerMenu(self):
        os.system("tput setaf 5")
        print("""
            Selecione o cargo do novo funcionario:\n
            1. Administrador
            2. Vendedor
            3. Operario

            0. Voltar ao Menu Principal
        """)

        self.registerOption()

# --------------------------------------
# OPCAO DE REGISTRO DE FUNCIONARIO
# --------------------------------------

    def registerOption(self):
        op = input(str(""))

        while True:
            if (op == "1"):
                self.setAdministrador()
                self.moreRegister()

            elif (op == "2"):
                self.setVendedor()
                self.moreRegister()

            elif (op == "3"):
                self.setOperario()
                self.moreRegister()

            elif (op == "0"):
                self.mainMenu()

            else:
                os.system("tput setaf 1")
                print('\n\nPor favor, digite uma opcao valida\n\n')

    # --------------------------------------
    # CADASTRAR MAIS FUNCIONARIOS
    # --------------------------------------


    def moreRegister(self):
        os.system("tput setaf 8")

        op = input(str('\nDeseja cadastrar mais algum funcionario (S/n)?'))

        if (op == "s" or op =="S"):
            self.registerMenu()

        elif (op == "n" or op =="N"):
            self.mainMenu()

        else:
            os.system("tput setaf 1")
            print('\n\nPor favor, digite uma opcao valida\n\n')
        

    # --------------------------------------
    # CADASTRAR ADMINISTRADOR
    # --------------------------------------


    def setAdministrador(self):

        nome = input(str('Nome: '))
        cpf = input(str('CPF: '))
        setor = input(str('Setor: '))
        salario = input(str('Salario: '))
        jornada = input(str('Jornada: '))
        ajudaDeCusto = input(str('Auxilio gasolina: '))

        return Administrador(nome, cpf, setor, salario, jornada, ajudaDeCusto)
        
    # --------------------------------------
    # CADASTRAR VENDEDOR
    # --------------------------------------


    def setVendedor(self):

        nome = input(str('Nome: '))
        cpf = input(str('CPF: '))
        setor = input(str('Setor: '))
        salario = input(str('Salario: '))
        jornada = input(str('Jornada: '))
        valorVendas = "0"
        comissao = input(str('% da comissao: '))

        return Vendedor(nome, cpf, setor, salario, jornada, valorVendas, comissao)
        
    # --------------------------------------
    # CADASTRAR OPERARIO
    # --------------------------------------
    
    def setOperario(self):

        nome = input(str('\nNome: '))
        cpf = input(str('CPF: '))
        setor = input(str('Setor: '))
        salario = input(str('Salario: '))
        jornada = input(str('Jornada: '))
        valorProducao = "0"
        comissao = input(str('% da comissao: '))

        return Operario(nome, cpf, setor, salario, jornada, valorProducao, comissao)
        


    








    


