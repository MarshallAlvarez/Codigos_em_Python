
curso = "Curso de Python"

res = "Python" in curso     ; print ( "\nRes esta dentro de curso ? " + str( res ) )
res = "Python" not in curso ; print ( "Res nao esta dentro de curso ? " + str( res ) )

texto = "Curso de Python" ; palavra = "python"

res = palavra in texto      ; print ( "\nRes esta dentro de texto ? " + str( res ) )
res = "Python" not in texto ; print ( "Res nao esta dentro de texto ? " + str( res ) )

res = palavra.upper() in texto.upper() ; print ( "\nRes esta dentro de texto ? " + str( res ) )
res = "Python" not in texto            ; print ( "Res nao esta dentro de texto ? " + str( res ) )

canal = "CFB Cursos"

res = curso + " do canal " + canal

print ( '\n' + res )

dia = 15
mes = "Janeiro"
ano = 2020
cidade = "Cachoeirinha"
data = "{} , {} de {} de {} \n\"{}\""

print ( '\n' + cidade + " , " + str( dia ) + " de " + str( mes ) + " de " + str( ano ) + "\n\"" + canal + "\"" )

print ( "\nOu com format\n\n" + data.format( cidade , dia , mes , ano , canal ) )

# \' \" \n \r \t \b