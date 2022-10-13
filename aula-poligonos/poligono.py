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
        print(f"\np1 = {self.p1}\np2 = {self.p2}\np3 = {self.p2}\np4 = {self.p2}")

    def calcPerimetro(self):
        reta1 = Reta(Ponto(self.x1, self.y1), Ponto(self.x2, self.y2))
        reta2 = Reta(Ponto(self.x2, self.y2), Ponto(self.x3, self.y3))
        reta3 = Reta(Ponto(self.x3, self.y3), Ponto(self.x4, self.y4))
        reta4 = Reta(Ponto(self.x4, self.y4), Ponto(self.x1, self.y1))

        
        s1 = reta1.calcDistancia()
        s2 = reta2.calcDistancia()
        s3 = reta3.calcDistancia()
        s4 = reta4.calcDistancia()

        #soma de todas as retas
        p = s1 + s2 + s3 + s4

        print(f"\nPerímetro: {p:.2f} cm\n")
    
    def formato(self):
        if (s1 == p/4):
            print("Quadrado")

        elif (reta1 == reta3 and reta1 != reta2):
            print("Retangulo")
        
        else:
            print("Quadrilátero indefinido")

        
        




        


