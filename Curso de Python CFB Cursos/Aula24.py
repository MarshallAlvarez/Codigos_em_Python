
class Carro :

    numero = 0 ; cor = "" ; velMax = 0 ; ligado = False 

    def __init__( self , n , v , l , c ) :

        self.numero = n
        self.cor    = c
        self.velMax = v
        self.ligado = l
    
    def mostrar( self ) :

        self.ligado = "sim" if self.ligado else "nao"
    
        print ( "  \nCarro numero: " + str ( self.numero ) +
                "  \nVel.max.....: " + str ( self.velMax ) +
                " km\nCor.........: " +       self.cor      +
                "  \nLigado......: " +       self.ligado      )
                   
    def ligar(    self ) : self.ligado = True
    def desligar( self ) : self.ligado = False

    def andar( self ) :

        if ( self.ligado ) : print ( "Esta........: Andando"   )
        else               : print ( "Esta........: Desligado" )


c1 = Carro( 1 , 200 , False , "Preto"    ) ; c1.ligar() ; c1.mostrar() ; c1.andar()
c2 = Carro( 2 , 120 , False , "Branco"   ) ; c2.ligar() ; c2.mostrar() ; c2.andar() 
c3 = Carro( 3 , 350 , False , "Vermelho" ) ; c3.ligar() ; c3.mostrar() ; c3.andar()
