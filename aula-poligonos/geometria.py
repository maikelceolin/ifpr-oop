from math import sqrt, pow

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostraPonto(self):
        print(f"{self.x},{self.y}")


class Reta:
    #Usando o tipo de dado "Ponto" criado na classe Ponto
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
        print(f"\n\tp1 = {self.p1}\tp2 = {self.p2}")

    def calcDistancia(self):

        # O calculo da distancia eh o seguinte:

        # Admite os dois pontos como vertices de um triangulo retangulo, e traça o 3 ponto imaginario
        # a distância entre pontos é a hipotenusa do triangulo retangulo
        # caso os pontos encontrem-se na mesma abscissa x ou y, um dos lados o triangulo se anula, 
        # sobrando apenas a distancia de um dos lados na expressão
        # Assim, eh possivel calcular qualquer distancia no plano cartesiano

        #criando o vertice
        vertice = Ponto(self.x1, self.y2)

        #identificando a distancia em numero modular (sem sinal)
        distX = abs(float(vertice.x) - float(self.x2))
        distY = abs(float(vertice.y) - float(self.y1))

        #calculo de pitagoras, retornando h
        h = sqrt(pow(distX,2)+pow(distY,2))
        return h