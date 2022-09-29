from empresa import Empresa, Administrador, Vendedor, Operario
from programa import Menu

Menu.titulo(None)

while True:
    op = Menu.principal(None)
    if op == "1":
        while True:
            cargo = Menu.cargo(None)
            if cargo == "0":
                break
            else:
                print("\n**** Opção inválida")

    elif op =="2":
        print("Voce ainda nao fez nada aqui\n")
    else:
        print("\n**** Opção inválida")
    




