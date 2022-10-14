from math import sqrt, pow
from geometria import Ponto, Reta


class Quadrilatero():
    def __init__(self, p1:Ponto, p2:Ponto, p3:Ponto, p4:Ponto):

        #Ponto1
        self.p1 = (f"({p1.x},{p1.y})")
        self.x1 = p1.x
        self.y1 = p1.y

        #Ponto2
        self.p2 = (f"({p2.x},{p2.y})")
        self.x2 = p2.x
        self.y2 = p2.y

        #Ponto3
        self.p3 = (f"({p3.x},{p3.y})")
        self.x3 = p3.x
        self.y3 = p3.y

        #Ponto4
        self.p4 = (f"({p4.x},{p4.y})")
        self.x4 = p4.x
        self.y4 = p4.y

    def mostraPonto(self):
        print(f"\n\tp1 = {self.p1}  p2 = {self.p2}\n\tp3 = {self.p3}  p4 = {self.p4}")

    def calcPerimetro(self):

        #definindo as retas do quadrilatero
        reta1 = Reta(Ponto(self.x1, self.y1), Ponto(self.x2, self.y2))
        reta2 = Reta(Ponto(self.x2, self.y2), Ponto(self.x3, self.y3))
        reta3 = Reta(Ponto(self.x3, self.y3), Ponto(self.x4, self.y4))
        reta4 = Reta(Ponto(self.x4, self.y4), Ponto(self.x1, self.y1))

        #chama método calcDistancia de cada reta
        s1 = reta1.calcDistancia()
        s2 = reta2.calcDistancia()
        s3 = reta3.calcDistancia()
        s4 = reta4.calcDistancia()

        #soma de todas as retas
        p = s1 + s2 + s3 + s4

        print(f"\tPerímetro: {p:.2f} cm\n")
    
    def forma(self):

        reta1 = Reta(Ponto(self.x1, self.y1), Ponto(self.x2, self.y2))
        reta2 = Reta(Ponto(self.x2, self.y2), Ponto(self.x3, self.y3))
        reta3 = Reta(Ponto(self.x3, self.y3), Ponto(self.x4, self.y4))
        reta4 = Reta(Ponto(self.x4, self.y4), Ponto(self.x1, self.y1))

        s1 = reta1.calcDistancia()
        s2 = reta2.calcDistancia()
        s3 = reta3.calcDistancia()
        s4 = reta4.calcDistancia()
         
        p = s1 + s2 + s3 + s4

        # calculo para identificar um retangulo:
        # estou calculando a diagonal principal e segundaria, se elas forem iguais,
        # trata-se de um retangulo. O teste de quadrado eh realizado antes.

        h1 = sqrt(pow(s1,2)+pow(s2,2)) #diagonal principal
        h2 = sqrt(pow(s3,2)+pow(s4,2)) #diagonal secundaria

        #se o 1/4 do perimetro for igual a algum lado, entao eh um quadrado
        if (s1 == p/4):
            print("\n\tForma: Quadrado\n")

        elif (h1 == h2):
            print("\n\tForma: Retangulo\n")
        
        #caso nao seja um quadrado ou retangulo, nao iremos definir o trapezio por enquanto
        else:
            print("\n\tForma: Quadrilátero indefinido\n")



class Pentagono:
    def __init__(self, p1:Ponto, p2:Ponto, p3:Ponto, p4:Ponto, p5:Ponto):

        #Ponto1
        self.p1 = (f"({p1.x},{p1.y})")
        self.x1 = p1.x
        self.y1 = p1.y

        #Ponto2
        self.p2 = (f"({p2.x},{p2.y})")
        self.x2 = p2.x
        self.y2 = p2.y

        #Ponto3
        self.p3 = (f"({p3.x},{p3.y})")
        self.x3 = p3.x
        self.y3 = p3.y

        #Ponto4
        self.p4 = (f"({p4.x},{p4.y})")
        self.x4 = p4.x
        self.y4 = p4.y

        #Ponto5
        self.p5 = (f"({p5.x},{p5.y})")
        self.x5 = p5.x
        self.y5 = p5.y

    def mostraPonto(self):
        print(f"\n\tp1 = {self.p1}  p2 = {self.p2}\n\tp3 = {self.p3}  p4 = {self.p4}\n\tp5 = {self.p5}")

    def calcPerimetro(self):

        #definindo as retas do quadrilatero
        reta1 = Reta(Ponto(self.x1, self.y1), Ponto(self.x2, self.y2))
        reta2 = Reta(Ponto(self.x2, self.y2), Ponto(self.x3, self.y3))
        reta3 = Reta(Ponto(self.x3, self.y3), Ponto(self.x4, self.y4))
        reta4 = Reta(Ponto(self.x4, self.y4), Ponto(self.x5, self.y5))
        reta5 = Reta(Ponto(self.x5, self.y5), Ponto(self.x1, self.y1))

        #chama método calcDistancia de cada reta
        s1 = reta1.calcDistancia()
        s2 = reta2.calcDistancia()
        s3 = reta3.calcDistancia()
        s4 = reta4.calcDistancia()
        s5 = reta5.calcDistancia()

        #soma de todas as retas
        p = s1 + s2 + s3 + s4 + s5

        print(f"\n\tPerímetro: {p:.2f} cm\n")

        




        


