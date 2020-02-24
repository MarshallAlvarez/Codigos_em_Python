
soma = lambda a , b      : a + b 
mult = lambda a , b , c  : ( a + b ) * c 

print ( '\n' + str ( soma( 1 , 1     )   ) )  
print (        str ( mult( 2 , 2 , 2 )   ) )
print ( ( lambda a , b : a + b ) ( 3 , 2 ) )

r = lambda x , func : x + func( x )

res = r( 2 , lambda x : x * x ) ; print ( res )
res = r( 2 , lambda x : x + 3 ) ; print ( res )
