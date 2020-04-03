
import json

"""
    carros_json = ' { "Marca" : "Honda" , "Modelo" : "HRV" , "Cor" : "Prata" } '

    carros = json.loads( carros_json )

    print( "\n\n" + str( carros ) + '\n' )

    print( carros[ "Marca"  ] )
    print( carros[ "Modelo" ] )
    print( carros[ "Cor"    ] ) 


    print( '\n' ) 
    for i in carros          : print( i )

    print( '\n' ) 
    for i in carros.values() : print( i )

    print( '\n' ) 
    for i in carros.items () : print( i )

    for i , j in carros.items() : 
        
        print( i + ' - ' + j )
"""
carros = {

    "Marca"  : "Honda" , 
    "Modelo" : "HRV"   , 
    "Cor"    : "Prata" 
} 

carros_json = json.dumps( carros )

print( "\n\n" + str( carros_json ) + '\n' )
