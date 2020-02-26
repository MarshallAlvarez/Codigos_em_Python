
class Carro :     velMax = 0   ;    cor = ""      ;    ligado = False 
c1 = Carro() ; c1.velMax = 200 ; c1.cor = "Preto" ; c1.ligado = False

estado = "sim" if c1.ligado else "nao"

print ( "\nVel.max.: " + str ( c1.velMax ) +
        "\nCor.....: " +       c1.cor      +
        "\nLigado..: " +       estado      )
        


