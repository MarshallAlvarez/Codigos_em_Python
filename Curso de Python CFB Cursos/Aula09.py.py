
carros = [ "HRV" , "Golf" , "Argo" , "Focus" ]

print( '\n' + str( carros ) )
print( '\n' + str( carros[ 0 ] ) )
print( '\n' + str( carros[ 0 : 5 ] ) )

print( carros[ -1 ] ) 

carros[ 3 ] = "Fusion" ; print( carros )

carros[ 3 ] = "Focus"

carros.append( "Fit" )
carros.append( "Fusion" )
carros.append( "Polo" )

print( "\nHa " + str( len( carros ) ) + " carros na lista\nSendo eles:\n\n" + str( carros ) )

carros.remove( "Fusion" ) ; print( "\nHa " + str( len( carros ) )  + " carros na lista\nSendo eles:\n" + str( carros ) )
carros.pop()              ; print( "\nHa " + str( len( carros ) )  + " carros na lista\nSendo eles:\n" + str( carros ) )
del carros[ 2 ]           ; print( "\nHa " + str( len( carros ) )  + " carros na lista\nSendo eles:\n" + str( carros ) )
#carros.clear()           ; print( "\nHa " + str( len( carros ) )  + " carros na lista\nSendo eles:\n" + str( carros ) )
carros2 = list( carros )  ; print( "\nHa " + str( len( carros2 ) ) + " carros na lista 2\nSendo eles:\n" + str( carros2 ) )

carros2 = [ "Fusca" , "147" , "Brasilia" , "Celta" ]

carros3 = carros + carros2 ; print( "\nHa " + str( len( carros3 ) ) + " carros na lista 3\nSendo eles:\n" + str( carros3 ) )
