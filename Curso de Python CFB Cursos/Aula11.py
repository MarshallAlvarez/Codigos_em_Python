
a = 10 ; b = 5 ; op = '+' ; res = 0

if   op == '+' : res = a + b 
elif op == '-' : res = a - b
elif op == '*' : res = a * b
elif op == '/' : res = a / b

else : print ( "Operador invalido" )

print ( '\n' , a , ' ' , op , ' ' , b ,  " = " , res ) 

clima = "sol" ; lugar = "" ; dinheiro = 500

if clima == "sol" and ( dinheiro >= 300 and dinheiro <= 500 ) : 
    lugar = "clube"

else : 
    lugar = "cinema" 

print ( "\nVou ao " + lugar ) 

if clima == "sol" or ( dinheiro >= 300 and dinheiro <= 500 ) : 
    lugar = "clube"

else : 
    lugar = "cinema" 

print ( "\nVou ao " + lugar ) 
