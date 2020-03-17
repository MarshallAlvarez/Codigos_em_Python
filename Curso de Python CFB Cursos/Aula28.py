
import os 

carros = []

class Carro :
    
    nome   = ""
    pot    = 0
    velMax = 0
    ligado = False

    def __init__( self , nome , pot ) :

        self.nome   = nome 
        self.pot    = pot
        self.velMax = int( pot ) * 2 
        self.ligado = False  

    def ligar   ( self ) : self.ligado = True
    def desligar( self ) : self.ligado = False

    def info( self ) :

        print(   "Nome....: " +      self.nome                      +
               "\nPotencia: " + str( self.pot                     ) +
               "\nVel max.: " + str( self.velMax                  ) +
               "\nLigado..: " + ( "Sim" if self.ligado else "Nao" ) +
               "\n\n-----------------\n\n"                        )

def Menu() :

    print( "\n------------------\n" +
           "\n1.Criar carro."       +
           "\n2.Dados carro."       + 
           "\n3.Excluir carro."     + 
           "\n4.Ligar carro."       +
           "\n5.Desligar carro."    + 
           "\n6.Listar carro."      +
           "\n7.Sair."              + 
           "\n\n------------------" +    
           "\n\nCarros no array: "  + str( len( carros ) ) + 
           "\n\n------------------\n" )

    opcao = input( "Opcao escolhida: " )
    
    os.system("cls")

    return opcao

    
def NovoCarro() :

    n = input( "\n\n-------------------\n\nNome....: " )
    p = input( "\n-------------------\n\nPotencia: " )
    
    print( "\n-------------------\n" )

    car = Carro( n , p ) ; carros.append( car ) ; os.system("pause") ; os.system("cls")

def informacoes() :
                
    n = input( "\n\n-----------------\n\nID do carro: " )

    print( "\n-----------------\n" )

    try    : carros[ int( n ) ].info() 
    except : print ( "Carro nao listado.\n\n-----------------\n\n" )

    os.system("pause") ; os.system("cls")

def excluirCarro() :
                
    n = input( "\n\n-----------------\n\nID do carro: " )

    print( "\n-----------------\n" )

    try    : del carros[ int( n ) ] 
    except : print ( "Carro nao listado.\n\n-----------------\n\n" )

    os.system("pause") ; os.system("cls")

def ligarCarro() :

    n = input( "\n\n-----------------\n\nID do carro: " )

    print( "\n-----------------\n" ) 

    try    : carros[ int( n ) ].ligar() ; print( "Carro ligado.     \n\n-----------------\n\n" )
    except :                              print( "Carro nao listado.\n\n-----------------\n\n" )

    os.system("pause") ; os.system("cls")

def desligarCarro() :

    n = input( "\n\n-----------------\n\nID do carro: " )

    print( "\n-----------------\n" ) 

    try    : carros[ int( n ) ].desligar() ; print( "Carro desligado.  \n\n-----------------\n\n" )
    except :                                 print( "Carro nao listado.\n\n-----------------\n\n" )

    os.system("pause") ; os.system("cls")

def listarCarros() :

    p = 0

    for c in carros :

        print( str( p ) + " - " + c.nome ) ; p += 1

    os.system("pause") ; os.system("cls")

ret = Menu()

while ret < "7" :

    if   ret == "1" : NovoCarro    () 
    elif ret == "2" : informacoes  ()   
    elif ret == "3" : excluirCarro ()
    elif ret == "4" : ligarCarro   ()
    elif ret == "5" : desligarCarro() 
    elif ret == "6" : listarCarros ()
    
    ret = Menu()

os.system( "cls" ) 

print( "\n\n----------------------" +
       "\n\nVoce saiu do programa." + 
       "\n\n----------------------\n\n" )
