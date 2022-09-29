
class Menu():
    def __init__(self) -> None:
        pass

    def titulo(self):
        print("\nBEM-VINDO AO SISTEMA EMPMASTER\n")

    def principal(self):
        print("-"*50)
        print("\nDigite o número da opção desejada: ")
        print("\n1. Contratar")
        print("2. Exibir lista de funcionarios\n")
        opcao = str(input())
        return opcao

    def cargo(self):
        print("-"*50)
        print("\nSelecione o cargo do novo funcionário:")
        print("\n1.Vendedor")
        print("2.Operário")
        print("3.Administrador\n")
        print("0. Voltar ao menu anterior\n")
        opcao = str(input())
        return opcao