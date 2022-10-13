
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostraPonto(self):
        print(f"{self.x},{self.y}")




class Reta:
    def __init__(self, p1:Ponto, p2:Ponto):

        #Ponto1
        self.p1 = (f"({p1.x},{p1.y})")
        self.x1 = p1.x
        self.y1 = p1.y

        #Ponto2
        self.p2 = (f"({p2.x},{p2.y})")
        self.x2 = p2.x
        self.y2 = p2.y

    def mostraPonto(self):
        print(f"\np1 = {self.p1}\tp2 = {self.p2}")

    def calcDistancia(self):
        vertice = Ponto(self.x1, self.y2)

        distX = abs(vertice.x - self.x2)
        distY = abs(vertice.y - self.y1)

        h = sqrt(pow(distX,2)+pow(distY,2))
        print(f"\nDistância: {h:.2f} cm\n")
        return h