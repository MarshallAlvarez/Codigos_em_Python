
import os

os.system ( 'cls' )

carros1 = [ "HRV" , "Golf" , "Argo" , "Onix" ] ; tam = len ( carros1 )
carros2 = [                                  ] ; i = 0 

print ( '\n' )

while i < 10 : 
    print ( i ) ; i += 1

    if i >= 5 :
        i = 0  
        print ( '\n' )  
        break

while i < tam :
    print ( carros1[ i ] ) ; i+= 1

veiculo = input( "\nDigite quantas vezes quiser o nome de um novo carro\nDigite -1 para parar\n\nNome do carro: " )

while veiculo != "-1" :
    carros2.append( veiculo )
    veiculo = input( "Nome do carro: " )

os.system ( 'cls' )

i = 0

for i in carros2 : print( i )

print( "\nFim dos loops\n" )