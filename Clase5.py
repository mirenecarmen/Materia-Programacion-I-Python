'''
4.5 Operadores Lógicos

operador     descripcion                                            uso
AND          devuelve True si ambos operandos son True             a and b
OR           devuelve True si alguno de los operandos es True      a or b
NOT          devuelve True si alguno de los operandos es False     not a
el operador not es un operador unario,es decir que solamente necesita un operando para
funcionar.
Podemos observar en este caso que solamente esta utilizando la variable A,no estamos utilizando el
el valor de B o una expresion del lado derecho.
En este caso,solamente es una expresin o el valor de A que es un tipo booleano.
y entonces el operador NOT simplemente lo que va a hacer es invertir el valor.
Si el valor de A es verdadero ,entonces al aplicarle el operador NOt se convierte en False.
Y si el valor de A es falso,al aplicarle el operador NOT,entonces se convierte en verdadero.
'''
#                             operadores logicos
#operadores AND y OR son binarios,porque necesitan los dos operandos para poder ejecutarse

#operador AND
a = True
b = True
resultado = a and b
print(resultado)

# operador OR
a = True
b = False
resultado = a or b
print(resultado)

a = True
b = False
resultado = a or b
print(resultado)

# operador NOT es un operador unario,porque necesita solo un operando para ejecutarse

a = False
b = False
resultado = not a
print(resultado)
