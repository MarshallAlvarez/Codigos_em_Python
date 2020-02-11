
         # Chave / Key - Valor / Value

carro = { "Fabricante" : "Honda" ,
          "Modelo"     : "HRV"   ,
          "Ano"        : "2016"  ,
          "Cor"        : "Prata"
         }

print ( "\nImprimir tudo: " + str ( carro ) )

print ( "\nImprimir apenas 1 valor duma chave: " + str ( carro[ "Modelo" ] ) )

fab = carro[ "Fabricante"] # fab = carro.get( "Fabricante" )

print ( "\nImprimir 1 valor duma chave dentro numa variavel: " + fab )

carro[ "Cor" ] = "Preto"

print ( '\n' + carro[ "Cor" ] + '\n' )

for i in carro : print ( i + ": " + carro[ i ] )

# Chave: print ( i )          
# Valor: print ( carro[ x ] )
    
if "Modelo" in carro :
    
    print ( "\nSim , modelo eh uma chave\n" )
    
print ( "Tamanho do Dictionary: " + str ( len ( carro ) ) + '\n' )

carro[ "Cambio" ] = "Automatico"

for c , v in carro.items() :

    print ( c + ": " + v )

print ( "\nTamanho do Dictionary: " + str ( len ( carro ) ) )

carro.pop( "Cambio" ) # del carro[ "Cambio" ]

print ( "\nCambio removido do Dictionary\n\n" + str ( carro ) + "\n\nTamanho do Dictionary: " + str ( len ( carro ) ) )

carro.clear()

print ( "\nDictionary limpo" + str ( carro ) + "\n\nTamanho do Dictionary: " + str ( len ( carro ) ) )

carros = {
            "Carro1" : { "Fabricantes" : "Honda"      , "Modelo" : "HRV"   } ,
            "Carro2" : { "Fabricantes" : "Volkswagem" , "Modelo" : "Golf"  } ,
            "Carro3" : { "Fabricantes" : "Ford"       , "Modelo" : "Focus" } }

print ( "\nFabricante do carro 1: " + carros[ "Carro1" ][ "Fabricantes" ] + '\n' )

Carro4 = { "Fabricantes" : "Honda"      , "Modelo" : "HRV"   }
Carro5 = { "Fabricantes" : "Volkswagem" , "Modelo" : "Golf"  }
Carro6 = { "Fabricantes" : "Ford"       , "Modelo" : "Focus" }  

Carros = {
            "C1" : Carro4 ,
            "C2" : Carro5 ,
            "C3" : Carro6 , }

for i in Carros : print ( Carros[ i ] )

print ( '\n' )
