'''
--ejercicio 3 : calcular estacion del año
pedir al usuario que ingrese un mes del año ,el valor debe ser entre 1 y 12,luego le decimos en
que estacion del año esta.
Verano : 21/12 al 21/03 ,1,2,3
Otoño : 21/03 al 21/06 ,4,5,6
Invierno : 21/06 al 21/09 7,8,9
Primavera : 21/09 al 21/12 ,10,11,12

En el ejercicio usamos NONE:esto indica que la variable aun no tiene asignado un valor(Esta vacia)
Este NONE es equivalente al null en otros lenguajes como java.

#solicitar al usuario que ingrese un mes del año
mes = int(input('ingrese un mes del año: \n 1,2,3 corresponde a Verano \n 3,4,5 corresponde a Otoño \n 6,8,9 corresponde a Invierno \n 10,11,12 corresponde a Primavera'))

#inicializar la variable estacion como NONE
estacion = None

#verificar el valor ingresado y determinar la estacion
if 1 <= mes <= 12:
    if mes == 1 or mes == 2 or mes == 3:
        estacion = "Verano"
    elif mes == 4 or mes == 5 or mes == 6:
        estacion = "Otoño"
    elif mes == 7 or mes == 8 or mes == 9:
        estacion = "Invierno"
    elif mes == 10 or mes == 11 or mes == 12:
        estacion = "Primavera"
else:
    print("El mes ingresado no es válido. Por favor, ingrese un valor entre 1 y 12.")

# Mostrar el resultado
if estacion is not None:
    print(f"El mes {mes} corresponde a la estación: {estacion}")

--Ejercicio 4: Etapas de la vida
Se pide un programa que cuando el usuario ingrese su edad  le diga o imprima la etapa de su
vida en una breve oracion:
 0 a 10 : La infancia es increible y bella
 10 a 19 : Tienes muchos cambios,mucho que estudiar
 20 a 29 : Amor y comienza el trabajo


edad = int(input('ingrese su edad:'))
etapa = None

if 0 <= edad <= 10:
    etapa = 'La infancia es increible y bella'
elif 10 < edad <= 19:
    etapa ='Tienes muchos cambios,mucho que estudiar'
elif 20 <= edad <= 29:
    etapa = 'Amor y comienza el trabajo'
if etapa is not None:
    print(etapa)
else:
    print('usted esta muerto.')

--Ejercicio 5: Sistema de calificaciones
EL objetivo del programa será crear un sistema de calificaciones de la siguiente manera:
Le pedimos al usuario que ingrese un valor del 0 al 10.
Luego,si ingreso 9 o 10 ,imprimimos A
Entre 8 y menor de 9 imprimimos B
Entre 7 y menor que 8,imprimimos C
Entre 6 y menor que 7 imprimimos D
Entre 0 y menor que 6,imprimimos E
De lo contrario el valor ingresado el incorrecto.

'''
calificacion = int(input('digite una calificacion entre 0 u 10:'))
if 9 <= calificacion <=10:
    print('A')
elif 8<= calificacion<9:
    print('B')
elif 7<= calificacion<8:
    print('C')
elif 6<= calificacion<7:
    print('D')
elif 0<= calificacion <6:
    print('F')
else:
    print('el valor es incorrecto.')