
import json

""" dictionary -> obj json """

carros_dictionary = {

    "Marca"  : "Honda" ,
    "Modelo" : "HRV"   ,
    "Cor"    : "Prata" 
}

""" lists e tuplas -> array json """

carros_list  = [ "Honda" , "Volkswagem" , "Ford" , "Fiat" , "Chevrolet" ]
carros_tupla = ( "Honda" , "Volkswagem" , "Ford" , "Fiat" , "Chevrolet" )

carros_j = json.dumps( carros_list       ) ; print( '\n' + str ( carros_j )        )
carros_j = json.dumps( carros_tupla      ) ; print( '\n' + str ( carros_j )        )
carros_j = json.dumps( carros_dictionary ) ; print( '\n' + str ( carros_j ) + '\n' )

carros_j = json.dumps( carros_dictionary , indent = 4 , separators = ( ": " , " = " ) , sort_keys =  True ) ; print( '\n' + str ( carros_j ) + '\n' )














