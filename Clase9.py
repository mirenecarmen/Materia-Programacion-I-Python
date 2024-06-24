'''
-- diseñar un programa que ingresado un año,nos devuelva por consola,si es un año bisiesto
o no,repetir la accion hasta que el usuario lo decida.



# Solicitar al usuario que ingrese un año
num = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(f"El año {num} es bisiesto.")
else:
    print(f"El año {num} no es bisiesto.")

while True:
    # Solicitar al usuario que ingrese un año
    num = int(input("Ingrese un año: "))

    # Verificar si el año es bisiesto
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print(f"El año {num} es bisiesto.")
    else:
        print(f"El año {num} no es bisiesto.")

    # Preguntar al usuario si desea verificar otro año
    opcion = input("¿Desea verificar otro año? (s/n): ").strip().lower()
    if opcion != 's':
        break

-- Ejercicio 1 :Calcular la suma de N primeros numeros

N = 8
i = 1
suma = 0

while i <= N:
    suma += i
    i += 1
print(f'la suma de los primeros {N} numeros es {suma} ')

-- ejercicio 3:leer 10 numeros e imprimir cuantos son positivos,negativos y cuantos 0.

#num = 0
i = 1
positivos = 0
negativos =0
ceros = 0

while i <= 10:
    num = int(input(f' ingresa el numero {i} :'))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

    i += 1
print(f'cantidad de numeros negativos:{negativos}')
print(f'cantidad de numeros positivos:{positivos}')
print(f'cantidad de numeros ceros:{ceros}')

-- Ejecicio 4 :suponga que tiene un conjunto de calificaciones de un grupo de 10 alumnos,Realizar
un algoritmo para calcular la calificacion promedio y la calificacion mas baja 
'''
contNotas = 1
sumaNotas = 0
notaMinima = float('inf')
while contNotas <= 10:
    notas = float(input(f'ingresa el valor de la nota {contNotas} es:'))
    sumaNotas += notas

    if notas < notaMinima:
        notaMinima = notas
    contNotas += 1
promedio = sumaNotas/10
print(f'el promedio de las 10 notas ingresadas es:{promedio}')
print(f'el valor de la nota minima es :{notaMinima}')

