from geometria import Ponto, Reta
from poligono import Quadrilatero

p1 = Ponto(2,2)
p2 = Ponto(5,2)
p3 = Ponto(5,5)
p4 = Ponto(2,5)

quad = Quadrilatero(p1, p2, p3, p4)
quad.calcPerimetro()


