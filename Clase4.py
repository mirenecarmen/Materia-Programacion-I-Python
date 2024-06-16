'''
#4.1 Operadores Aritméticos
# operador suma +
# este operador realiza la operacion suma y tambien se usa en concatenacion en los datos de tipo string

# operacion resta -,multiplicacion,division
operador resto o modulo %
 usamos la triple comilla simple para comentar texto multilinea
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
# print("el resultado de la suma es :", suma)
print(f'el resultado de la suma es :{suma}')
# incluir la variable en una cadena se denomina INTERPOLACION,la f al comienzo es de "format"
resta = operandoA - operandoB
print(f'la resta es:{resta}')

multip = operandoA * operandoB
print(f'el resultado de la multiplicacion es :{multip}')
division = operandoA / operandoB # una sola barra da los decimales
print(f'el resultado de la division es :{division}')

division = operandoA // operandoB
print(f'el resultado de la division es :{division}')

modulo = operandoA % operandoB
print(f' el resultado o resto es:{modulo}')

exponente = operandoA ** operandoB
print(f'el resultado del exponente es:{exponente}')

#4.2 Ejercicio: Rectángulo
'en el siguiente se solicita calcular el area y el perimetro de una rectangulo.
Para ello debemos de crear las siguientes variables:
alto(int)
ancho(int)
el usuario debe de proporcionar los valores de alto y ancho,despues se debe de imprimir
el resultado en el siguiente formato:
proporciona el alto del rectangulo:5
proporciona el ancho del rectangulo:3
area= 15
perimeto = 16
las formulas para calcular el area y el perimetro de un rectangulo son:
area = alto * ancho
perimetro = (alto + ancho) * 2

alto = int(input("proporciona  el alto del rectangulo:"))
ancho = int(input("proporciona el ancho del rectangulo"))
area = alto * ancho
perimetro = (alto * 2)+(ancho *2)
print(f'dado el alto',alto,'y el ancho',ancho,'el area del rectangulo es:',area,'y el perimetro del rectangulo es:',
perimetro)


4.3 Operadores de Asignación y comparación

miVar3 = 10
print(miVar3)

#operaciones con reasignacion (ejemplo:incremento con reasignacion)
miVar3 += 1
print(miVar3)
#otra manera (asi se reduce la sintaxis

miVar3 += 1
print(miVar3)
# de la mismamanera su puede restar

miVar3 -= 1
print(miVar3)

# con multiplicacion
miVariab = 4
miVariab *= 3
print(miVariab)

# con division

miVariab /= 2
print(miVariab)
'''
'''
Algunos operadores aritmeticos nos permiten realizar operaciones sobre cadenas de texto
operador             descripcion      ejemplo
+  concatenacion    'ho' + 'la'       ='hola'
* repeticion         'hello world'*3  = 'hello world,hello world,hello world'

los operadores de comparacion nos permiten saber si dos valores son iguales o distintos

'''
'''
d=4
b=6
resultado = d == b # comprobamos si son iguales
print(resultado)

d=4
b=4
resultado = d == b # comprobamos si son iguales
print(resultado)

d=4
b=4
resultado = 3 == 8 # comprobamos si son iguales con numeros,es lo mismo
print(resultado)

d=4
b=4
resultado = d != b # comprobamos si son diferentes
print(resultado)

d=4
b=9
resultado = d > b # comprobamos si es mayor que
print(resultado)

d=4
b=9
resultado = d < b # comprobamos si es menor que
print(resultado)

d=4
b=9
resultado = d >= b # comprobamos si es mayor o igual que
print(resultado) # da false

d=4
b=4
resultado = d >= b # comprobamos si es mayor o igual que
print(resultado) # da true

# 4.4 Ejercicio 1 y 2

ejercicio numero par o impar
1-solicitamos que el usuario ingrese su numer
2-este se asigna a una variable
3-utilizaremos la estructura ifelse
4-la formula : <num>%2 == 0 .Esta operacion nos dice si es un numero par
5-si es True imprimimos que es par
6-si es False imprimimos que es impar
'''
'''
num = int(input("ingrese un numero:"))
print(f'el residuo de la division es  {num % 2}')
if num % 2 == 0:
    print(f'el numero {num} es par')
else:
    print(f'el numero {num} es impar')
'''

# ejercicio:determinar si es mayor de edad
# 1-pedir un numero al usuario
# 2-almacenar el valor en una variable
# 3-usar la estructura ifelse
# 4-la formula es <nuM> >= 18
# 5-True:eres mayor de edad,imprimir
# 6-false:eres menor de edad,imprimir

nuM = int(input("ingrese su edad:"))
print(f'la edad ingresada es {nuM}')
if nuM >= 18:
    print(f'Usted es mayor de edad')
else:
    print(f'Usted es menor de edad')