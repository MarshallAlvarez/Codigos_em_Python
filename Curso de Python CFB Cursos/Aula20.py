
def soma( n1 , n2 , n3 , n4 ) : r = n1 + n2 + n3 + n4 ; print ( '\n' + str ( n1 ) + " + " + str ( n2 ) + " + " + str ( n3 ) + " + " + str ( n4 ) + " = " + str ( r ) )
def subt( n1 , n2 , n3 , n4 ) : r = n1 - n2 - n3 - n4 ; print ( '\n' + str ( n1 ) + " - " + str ( n2 ) + " - " + str ( n3 ) + " - " + str ( n4 ) + " = " + str ( r ) )
def mult( n1 , n2 , n3 , n4 ) : r = n1 * n2 * n3 * n4 ; print ( '\n' + str ( n1 ) + " * " + str ( n2 ) + " * " + str ( n3 ) + " * " + str ( n4 ) + " = " + str ( r ) )
def divi( n1 , n2 , n3 , n4 ) : r = n1 / n2 / n3 / n4 ; print ( '\n' + str ( n1 ) + " / " + str ( n2 ) + " / " + str ( n3 ) + " / " + str ( n4 ) + " = " + str ( r ) )
    
def textos( *txt ) :
    for t in txt : 
        print ( t )

def calculos() : soma( 5 , 7 , 3 , 2 ) ; subt( 12 , 8 , 1 , 20 ) ; mult( 1 , 2 , 0 , 0 ) ; divi( 10 , 5 , 10 , 5 )

calculos()

print ( '\n' )

textos( "CFB Cursos" , "Python" , "Canal" , "Curso" , "Computador" )

def somar( *num ) :
    r = 0
    for i in num :
        r += i
    print ( "\nSoma = " + str ( r ) )

somar( 5 , 2 , 3 , 5 , 20 , 15 , 0 , 1 , 37 )

def carros( c = "Golf" ) :
    print ( "\nModelo: " + c )

carros( "HRV" )
carros()

valores = [ 1 , 5 , 3 , 2 ]

def somatorio( num ) :
    r = 0
    for i in num :
        r += i
    print ( "\nSoma = " + str ( r ) )

somatorio( valores )

print ( '\n' )
