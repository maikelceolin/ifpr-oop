from empresa import Empresa, Administrador, Vendedor, Operario
from programa import Menu

Menu.titulo(None)

while True:
    op = Menu.principal(None)
    if op == "1":
        while True:
            cargo = Menu.cargo(None)
    
            if cargo == "1":
                vendedor = Vendedor()
                vendedor.contratar()

            elif cargo == "2":
                operario = Operario()
                operario.contratar()

            elif cargo == "3":
                adm = Administrador()
                adm.contratar()
            
            elif cargo == "0":
                break

            else:
                print("\n**** Opção inválida")

    elif op =="2":
        print("Voce ainda nao fez nada aqui\n")
    else:
        print("\n**** Opção inválida")
                




