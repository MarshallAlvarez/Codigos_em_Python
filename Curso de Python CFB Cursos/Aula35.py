
import datetime

data = datetime.datetime.now()

print( "\n\nHora atual: " + str( data ) )

print( "\nHoje é: " + str( data.day ) + '/' + str( data.month ) + '/' + str( data.year ) )

nasc = datetime.datetime( 2000 , 11 , 20 )

print( "\nEu nasci em: " + str( nasc )                + 
       "\nNuma.......: \"" + str( nasc.strftime( "%A" ) ) + '\"' )

"""
    "%a" -> Semana por sigla   em inglês
    "%A" -> Semana por extenso em inglês
    "%w" -> Semana por número:
        
        0 - Sunday
        1 - Monday
        2 - Tuesday
        3 - wednesday
        4 - Thursday
        5 - Friday
        6 - Saturday
    
    "%d" -> Dia do mês por número ( 1 - 31 )
    "%b" -> Mês abreviado em inglês
    "%B" -> Mês           em inglês
    "%m" -> Mês por número:
    
        0  - January
        1  - Febryary
        2  - March
        3  - April
        4  - May
        5  - June
        6  - July
        7  - August
        8  - September
        9  - October
        10 - November
        11 - December
    
    "%y" -> Ano com 2 dígitos , 00   - 99
    "%Y" -> Ano com 4 dígitos , 0000 - 9999
    "%H" -> Hora de 00 - 23 
    "%I" -> Hora de 00 - 12
    "%p" -> AM ou PM 
    "%M" -> Minutos
    "%S" -> Segundos
    "%f" -> Milissegundos
    "%j" -> Dia do ano , 001 - 366
    "%W" -> Número da semana do ano
"""
print( "\n\n" )


