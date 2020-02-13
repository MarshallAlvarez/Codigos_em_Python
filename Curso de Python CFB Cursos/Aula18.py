
import random
import os 

cont_erros = 0
numero_sorteado = random.randrange( 0 , 100 )
i = int( input( "\nDigite 1 numero de 0 - 100: " ) )

while ( numero_sorteado != i ) :
    
    if ( numero_sorteado > i ) :

        print ( "\nO numero numero_sorteado eh maior que " + str ( i ) + '\n' )    
   
    elif ( numero_sorteado < i ) :

        print ( "\nO numero numero_sorteado eh menor que " + str ( i ) + '\n' )
        
    os.system( "pause" )
    os.system( "cls"   )
   
    cont_erros += 1
    
    i = int ( input( "\nDigite 1 numero de 0 - 100: " ) )

print ( "\nParabens voce acertou! , o numero era " + str ( numero_sorteado ) + " , levou apenas " + str ( cont_erros + 1 ) + " tentativas para advinhar\n" )


