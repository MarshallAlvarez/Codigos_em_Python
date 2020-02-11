
carrosL = [ "HRV", "Golf"  , "Focus" , "Argo" ]   # Array / List
carrosM = [ [ "Modelo...." , "HRV"            ] , 
            [ "Fabricante" , "Honda"          ] , 
            [ "Ano......." , 2016             ] ]  # Matriz

print ( "\nCarro na posicao 1 da list: " + carrosL[ 1 ] + "\n\nCarros dentro da list:\n" )

carrosL[ 2 ] = "Fusion"

for i in carrosL : print ( i )

print ( "\nCarro na posicao 01 da matriz: " + carrosM[ 0 ][ 1 ] + '\n' )

carrosM[ 2 ][ 1 ] = 2019

carrosM.append( [ "Cor......." , "Prata" ] )

for i , j in carrosM :
    print ( i  + ": " + str ( j ) )

print ( '\n' )
