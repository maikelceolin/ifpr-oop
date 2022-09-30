from empresa import Empresa, Administrador, Vendedor, Operario
from programa import Menu

Menu.titulo(None)

while True:
    op = Menu.principal(None)
    if op == "1":
        
        i = [1] # este i serve para controlar as linhas do excel, a cada laço, desce uma linha
        while True:
            cargo = Menu.cargo(None)
    
            if cargo == "1":
                i.append(1)
                vendedor = Vendedor()
                vendedor.contratar(i)
                

            elif cargo == "2":
                i.append(1)
                operario = Operario()
                operario.contratar(i)
                

            elif cargo == "3":
                i.append(1)
                adm = Administrador()
                adm.contratar(i)
                
            elif cargo == "0":
                break

            else:
                print("\n**** Opção inválida")

    elif op =="2":
        print("Voce ainda nao fez nada aqui\n")
        
    else:
        print("\n**** Opção inválida")
                




