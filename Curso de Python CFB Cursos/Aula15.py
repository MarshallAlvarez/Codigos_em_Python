
# l_carros = [ "HRV" , "Golf" , "Argo" ]

t_carros = ( "HRV" , "Golf" , "Argo" )

l_carros = list ( t_carros )

l_carros[ 2 ] = "Focus"

t_carros = tuple ( l_carros )

for i in t_carros : 
    print ( i )

"""
    Erro: t_carros[ 2 ] = "Focus"

    print ( '\n' + t_carros[ 0 ] + '\n' )
    
    for i in l_carros : 
        print ( i )
"""

print ( '\n' )
