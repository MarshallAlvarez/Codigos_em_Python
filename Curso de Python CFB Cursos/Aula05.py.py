
import random

num_i = 10
num_f = 5.2
num_c =  1j

x = num_i ; print ( "\nValor: " + str( x ) + " - Tipo: " + str( type( x ) ) )
x = num_f ; print ( "Valor: "   + str( x ) + " - Tipo: " + str( type( x ) ) )
x = num_c ; print ( "Valor: "   + str( x ) + " - Tipo: " + str( type( x ) ) )

x = float( num_i )     ; print ( "\nValor: " + str( x ) + " - Tipo: " + str( type( x ) ) )
x = complex( num_i )   ; print ( "Valor: "   + str( x ) + " - Tipo: " + str( type( x ) ) )

x = int( num_f )       ; print ( "\nValor: " + str( x ) + " - Tipo: " + str( type( x ) ) )
x = complex( num_f )   ; print ( "Valor: "   + str( x ) + " - Tipo: " + str( type( x ) ) )

num_r = random.randrange( 0 , 59 )

x = num_r

print ( "\nValor: "   + str( x ) + " - Tipo: " + str( type( x ) ) )

num_r = [   random.randrange( 0 , 59 ) ,
            random.randrange( 0 , 59 ) ,
            random.randrange( 0 , 59 ) ,
            random.randrange( 0 , 59 ) ,
            random.randrange( 0 , 59 ) ,
            random.randrange( 0 , 59 ) , ]

x = num_r

print ( "\nValor 1: " + str( num_r[ 0 ] ) )
print ( "Valor 2: "   + str( num_r[ 1 ] ) )
print ( "Valor 3: "   + str( num_r[ 2 ] ) )
print ( "Valor 4: "   + str( num_r[ 3 ] ) )
print ( "Valor 5: "   + str( num_r[ 4 ] ) )
print ( "Valor 6: "   + str( num_r[ 5 ] ) )

