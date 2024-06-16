#tipos de datos String
a = "hola alumnos"
print(type(a))
#tipo flotante
a = 3.78
print(type(a))
#tipos de datos booleanos-TRUE o False
a = True
print(type(a))
#los tipos de datos a su vez son clases
#tipo de dato int
a = 3
print(type(a))
#3.3 Manejo de cadenas
miGrupoFavorito = ("The Beatles")
print(miGrupoFavorito)
#concatenacion varias cadenas
print("mi grupo favorito es: "+miGrupoFavorito)

#concatenacion dntro de la asignacion con operador +
miGrupoFavorito = "The Beatles"+"Peso Pluma"
print("mi grupo favorito es: "+miGrupoFavorito)

#3.4 Más temas de manejo de cadenas

miGrupoFavorito = "The Letter Black"
caracteristica = " The best Band"
print("mi grupo favorito es :",miGrupoFavorito,caracteristica)

num1 = "7"
num2 = "8"
print(int(num1) + int(num2))

#3.5 Tipos Booleanos (Bool)
miBooleano = True # true o False es la literal del booleano
print(miBooleano)
miBooleano = 1 > 4
print(miBooleano)

# uso de condicional
if miBooleano:
    print("el resultado el verdadero")
else:
    print("el resultado es falso")

#3.6 Procesar entrada del usuario (Función input)
#como ingresa los datos el usuario
#el codigo duro es aquel que le asigno yo los valores,ahora,vamos a ver cuando el usuario
#le ingresa las variables
#usamos la funcion input
# input regresa un dato de tipo string (o sea le ingreso cualquier tipo de dato y me regresará el dato en tipo str)
#Esto significa que cualquier valor que el usuario ingrese será tratado como una cadena,
# independientemente de si parece un número, un booleano, etc.
# resultado = input()
# print(resultado)

#resultado = input("digite un numero: ")
#print(resultado)

#3.7 Conversión de la entrada de datos (en la funcion input)

#numero1 = input("escribe el primer numero:  ")
#numero2 = input("escribe el segundo numero:  ")
#resultado = numero1 + numero2
#print("el resultado de la suma es: ",resultado)
#aqui,si ingreso los numeeros ,el resultado será una concatenacion,no una suma,porque esta
# simplemente concatenando los string

#lo que se debe hacer es  cambiar a tipo entero el string

# numero1 = int(input("escribe el primer numero:  "))
# numero2 = int(input("escribe el segundo numero:  "))
# resultado = numero1 + numero2
# print("el resultado de la suma es: ",resultado)

# 3.8 Actividad:
# Ejercicio 1: Califica tu día
# ¿Cómo estuvo tu día (1 al 10)?
# Mi día estuvo de: 10
# Hacer el código
# Debes hacerlo en PyCharm y también en el celular y en la terminal de Python...

# calificacion = int(input("como estuvo tu dia (del 1 al 10)?:"))
# print( calificacion)

# Ejercicio 2:
# Se solicita incluir la siguiente información acerca de un libro:
# título
# autor
# Debes imprimir la información en el siguiente formato:
# Proporciona el título:
# Proporciona el autor:
# <título> fue escrito por <autor>
# Preguntas de esta tarea
# ¿Cuál es el código del requerimiento solicitado?

titulo = input("proporciona el titulo:")
autor = input("proporciona el autor:")
print("el libro",titulo," fue escrito por",autor)

