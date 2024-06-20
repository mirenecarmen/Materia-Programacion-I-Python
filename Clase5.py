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

                           operadores logicos
operadores AND y OR son binarios,porque necesitan los dos operandos para poder ejecutarse

operador AND
a = True
b = True
resultado = a and b
print(resultado)

 operador OR
a = True
b = False
resultado = a or b
print(resultado)

a = True
b = False
resultado = a or b
print(resultado)

 operador NOT es un operador unario,porque necesita solo un operando para ejecutarse

a = False
b = False
resultado = not a
print(resultado)


4.6 Ejercicio: Valor dentro de un rango

ejercicio :valor dentro de un rango
1-pedimos al usuario un valor numerico
2-verificar si el valor ingresado se encuentra dentro del rango del 0 al 5.
3-la formula es <num> >= 0 and <num> <= 5



valor = int(input("ingrese un numero entero:"))

if valor>= 0 and valor<=5 :
    print(f'el valor ingresado {valor} esta dentro del rango de 0 a 5.')
else:
    print(f'el valor ingresado {valor} no esta en el rango de 0 a 5.')

4.7 Operadores or
ejercicio operador OR
La pregunta es ,si un padre puede asistir al juego de su hijo
1-verificamos si tiene vacaciones
2-verificamos si tiene un dia libre
3-usar la estructura 'if else'con el operador OR
4-imprimir


vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print(f'puede asistir al juego')
else:
    print(f'tiene trabajo que hacer.')

operador not

vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print(f' tiene trabajo que hacer.')
else:
    print(f'puede asistir al juego')


4.8 Ejercicio: Rango entre 20 y 30 años
Sintaxis simplificada del operador And

ejercicio:
1-preguntar la
2-si la edad esta dentro de los  20 o 30 esta dentro del rango.
3-combinamos los operadores and y or para saber si el usuario esta dentro del
rango o no.


edad = int(input("digite su edad:"))
veinte = edad >= 20 and edad < 30 # se almacena en la variable "veinte"
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    print("estas dentro de del rango de los (20'0) a (30'0) años") # sin la barra invertida
else:
    print('No estas dentro de del rango de los (20\'0) a (30\'0) años') #con la barra invertida se usa comilla doble


edad = int(input("digite su edad:"))
veinte = edad >= 20 and edad < 30 # se almacena en la variable "veinte"
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte :
    print("estas dentro de del rango de los (20'0) años")
elif treinta:
    print("estas dentro de del rango de los (30'0) años")

else:
    print('No estas dentro de del rango de los (20\'0) a (30\'0) años')

 #If else ANIDADO (cuidado con la identacion)

edad = int(input("digite su edad:"))
veinte = edad >= 20 and edad < 30 # se almacena en la variable "veinte"
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print("estas dentro de del rango de los (20'0) años")
    elif treinta:
        print("estas dentro de del rango de los (30'0) años")
    else:
        print("no estas en el rango.")

else:
    print('No estas dentro de del rango de los (20\'0) a (30\'0) años')


#una forma mas reducida es:

edad = int(input("digite su edad:"))
veinte = edad >= 20 and edad < 30 # se almacena en la variable "veinte"
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
   print("estas dentro de del rango de los (20'0) años")
else:
    print('No estas dentro de del rango de los (20\'0) a (30\'0) años')


#sintaxis simplificada del AND
edad = int(input("digite su edad:"))
veinte = edad >= 20 and edad < 30 # se almacena en la variable "veinte"
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if (20 <= edad < 30) or (30 <= edad < 40):
   print("estas dentro de del rango de los (20'0) años")
else:
    print('No estas dentro de del rango de los (20\'0) a (30\'0) años')


--Ejercicio 1: Mayor de 2 números
solicitar al usuario dos valores,determinar cual es el mayor.
1-solicitar al usuario dos valores
numero1(int)
numero2(int)
2-se debe imprimir el mayor de los dos
(la salida debe ser identica a la siguiente).
digite el valor para el numero 1:
digite el valor para el numero 2:
El numero mayor es: <numeroMayor>



numero1 = int(input(f'digite el valor para el numero 1:'))
numero2 = int(input(f'digite el valor para el numero 2:'))
if numero1 > numero2:
    print(f'el numero {numero1} es mayor que {numero2} ')
else:
    print(f' el numero {numero1} no es mayor al {numero2}')


--Ejercicio General: Tienda de Libros
1-Mostrar: ingrese los siguientes datos del libro
2-digite el nombre del libro
3-digite el id del libro
4-digite el precio del libro
5-indicar si el envio es gratuito(True/False)
6-Mostrar:
Nombre:
ID:
Precio:
Envio gratuito?:
'''

print('Digite los siguientes datos del libro')
nombre = input('Digite el nombre del libro:')
id = int(input('digite el ID del libro: '))
precio = float(input('digite el precio del libro:'))
envioGratuito = input('indicar si el envio del libro es gratuito(True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto,debe escribir True/False'
print(f'''
        Nombre:{nombre}
        Id:{id}
        precio:{precio}
        envio gratuito : {envioGratuito}
''')
