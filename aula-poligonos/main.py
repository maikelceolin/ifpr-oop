
from geometria import Ponto, Reta
from poligono import Pentagono, Quadrilatero

while True:
    op = input('\nEscolha a forma geometrica:\n1.Reta\n2.Quadrado\n3.Pentagono\n')

    if (op == '1'):
        print('\nDigite 2 pontos ex.: x,y')

        i = input('p1: ')
        p1 = Ponto(i[0],i[2])

        i = input('p2: ')
        p2 = Ponto(i[0],i[2])

        reta = Reta(p1, p2)

        reta.mostraPonto()
        dist = reta.calcDistancia()
        print(f"\n\tDistancia da reta: {dist:.2f} cm\n")

    elif (op == '2'):
        print('\nDigite 4 pontos ex.: x,y')

        i = input('p1: ')
        p1 = Ponto(i[0],i[2])

        i = input('p2: ')
        p2 = Ponto(i[0],i[2])

        i = input('p3: ')
        p3 = Ponto(i[0],i[2])

        i = input('p4: ')
        p4 = Ponto(i[0],i[2])

        quad = Quadrilatero(p1, p2, p3, p4)

        quad.mostraPonto()
        quad.forma()
        quad.calcPerimetro()

    elif (op == '3'):
        i = input('p1: ')
        p1 = Ponto(i[0],i[2])

        i = input('p2: ')
        p2 = Ponto(i[0],i[2])

        i = input('p3: ')
        p3 = Ponto(i[0],i[2])

        i = input('p4: ')
        p4 = Ponto(i[0],i[2])

        i = input('p5: ')
        p5 = Ponto(i[0],i[2])

        pent = Pentagono(p1, p2, p3, p4, p5)

        pent.mostraPonto()
        print('\n\tForma: Pentagono')
        pent.calcPerimetro()

    else:
        print('Ops! Opcao invalida, por favor, digite uma das opcoes')

