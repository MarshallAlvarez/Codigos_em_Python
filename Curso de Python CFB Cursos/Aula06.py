
curso = "Curso de Python "

print ( '\n' + curso[ 0 ] + '\n' + curso[ 0 : 5 ] )

print ( '\n' + curso.strip() + "\nTamanho : " + str( len( curso ) ) )

print ( '\n' + curso.lower().strip() + "\nTamanho : " + str( len( curso ) ) )
print ( '\n' + curso.upper().strip() + "\nTamanho : " + str( len( curso ) ) )

print ( '\n' + curso.replace( "Python" , "C++" ).strip() + "\nTamanho : " + str( len( curso ) ) )

a = curso.split( " " )

print ( "\nTamanho : " + str( len( curso ) ) ) 
print ( '\n' + a[ 0 ] + '\n' + a[ 1 ] + '\n' + a[ 2 ] ) 
