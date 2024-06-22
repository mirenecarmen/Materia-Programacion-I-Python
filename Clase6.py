'''
Sentencias de Control

--- 6.1 Sentencia If/Else


condicion = True
if condicion:
    print('condicion verdadera')
else:
    print('condicion falsa')

 esto nos dará de resultado: "condicion verdadera"
 si le damos un valor numerico y lo ejecutamos,por ejemplo :10
nos dice que la condicion es verdadera,pero ¿que condicion esta ejecutando si le estoy poniendo
un valor numerico?evalua su la variable esta vacia o tiene algun valor,como en este caso le
asignamos el valor 10,nos dice que la condicion es verdadadera,pero si le ponemos doble comilla
simple '' ,lo toma como vacio ( o sea condicion = '')
y da de resultado "condicion Falsa"


condicion = False         # 'Hola alumnos' da "condicion sin especificar , "True" da "condicion verdadera"
if condicion == True:
    print('condicion verdadera')
elif condicion == False:
    print('condicion falsa')
else:
    print('condicion sin especificar') #si no hay ningun valor espeficado,nos dirá "condicion si especificar"



Ejecución Debug(depurar) en if/else--nos va mostrando el codigo para reparar

Ahora veremos la ejecucion con el modo paso a paso de Python
--nos situamos en donde esta lalinea con variable y hacemos click para que aparezca el boton rojo
--ahi es donde se detendrá el ejecutador
-.hacemos click secundario en el boton rojo y seleccionamos "debug main o debug clase6"
--se abren dos pestañas,la consola y debug
--

condicion = 10         # 'Hola alumnos' da "condicion sin especificar , "True" da "condicion verdadera"
if condicion == True:
    print('condicion verdadera')
elif condicion == False:
    print('condicion falsa')
else:
    print('condicion sin especificar') #si no hay ningun valor espeficado,nos dirá "condicion si especificar"

--Commiteamos en Python

--Ejercicio: Conversión de número a texto


num = int(input('digite un nmero en el rango del 1 al 3:'))
numTexto = ''
if num == 1:
    numTexto = 'numero uno'
elif num == 2:
    numTexto = 'numero dos'
elif num == 3:
    numTexto = 'numero tres'
else:
    numTexto = 'Has ingresado un numero fuera de rango'
print(f'el numero ingresado es: {num} = {numTexto}')


--6.2 Ejercicio 1


a = float(input('digite el valor de a:'))
b = float(input('digite el valor de b:'))
c = float(input('digite el valor de c:'))
resultado = (a ** 3 * (b ** 2 - 2 * a * c))/(2 * b)
print(f'el resultado es:{resultado}')

-- 6.3 Sintaxis simplificada (Operador Ternario)


condicion = False
print('condicion verdadera') if condicion else print('condicion falsa')

--ejercicio 2:
Determinar la solucion logica de la siguiente operacion:
((3+5*8)<3 and ((-6/3 * 4) + 2 < 2)) or (a > b)


a = int(input('digite el valor de a:'))
b = int(input('digite el valor de b:'))
c = int(input('digite el valor de c:'))

result = ((3+5*8)<3 and ((-6/3 * 4) + 2 < 2)) or (a > b)
print(f'el resultado es: {result}')

--ejercicio 3 :
Intercambiar el valor de dos variables.
Por ejemplo:
 a = 10 ---> a= 5
 b = 5  --> b = 10

# valores iniciales
a = 10
b = 5
#usar una variable temporal para intercambiar los valores
t = a
a = b
b = t

print(f'a = {a}') # a=5
print(f'b = {b}') # a=5
'''

#  --ejercicio 4
# area y longitud de un circulo
# hacer un programa para ingresar el radio de un circulo y reporte su area y longitud de circunfere
# ncia.
# area = pi * (r ** 2)
# longitud = 2 * pi * r
# en este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de
# Pi:
# se escribe import math

import math
radio = float(input('ingrese el valor del radio.'))
#calcular el area del circulo
area = math.pi * (radio ** 2)
#calcular la longitud de la circunferencia
longitud = 2 * math.pi * radio

#imprimir los resultado
print(f'dado un radio de {radio},el valor del area del circulo es : {area} y su longitud es {longitud}')
