
x     =  10
#num   = "Bruno"
num = -10 

# if num < 1 : raise Exception( "Valor nao permitido" )

if not type( num ) is int : 
    
    raise Exception( "Somente numeros permitidos" )

else :
 
    print( "\nNum: " + str( num ) )

    try              : print( "x..: " + str( x )                 )
        
    except NameError : print( "\nX nao definido"                 )
    except           : print( "\nErro desconhecido no programa!" )

    else             : print( "\nTudo certo"                     )

    finally          : print( "Fim do tratamento"                )  






