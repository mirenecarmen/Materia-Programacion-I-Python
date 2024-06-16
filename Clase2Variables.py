miVariable = 3
print("miVariable")

#como python trabaja con variables dinamicas,no hace falta escribir el tipo de dato

miVariable = "hola a todos los alumnos de la tecnicatura"
print(miVariable)

miVariable = 3.5
print(miVariable)
#PRINT() EN REALIDAD ES UNA FUNCION,SUN FUNCION ES IMPRIMIR
##Que sucede en la memoria RAM
##en nuestro espacio de memoria RAM hay casillas,cada una va a almacenar la informacion
#de nuestros programas(seria la informacion que estamos asignando a las variables),
# por ejemplo,hacemos tres asignaciones
x = 10
y = 2
z = x + y
print(z)
#cada una de estas es una posicion unica
#cada valor es una literal:una literal es un valor que podemos asignar a nuestras variables
#la literal 10 que es un valor numerico,la literal 2 se asigna a y,las dos estan en diferentes
#posiciones de memoria
#para saber la direccion de memoria donde estan es:
#podemos obtener  la direccion id en el espacio de memoria que ocupa cada variable
print(id(x))
# del valor del id usamos solo los 3 ultimos espacios 140734495902424,o sea 424
# se escribe literal x424
#ahora si volvemos a imprimir el id,no nos da el mismo valor,esto es porque la memoria
#cambia al compilar de nuevp,se borra y compila cada vez
print(id(y)) # la variable y esta en la casilla y = x912
print(id(z)) # la variable z esta en la casilla z= 232
#porque pasa esto?
#es porque cuando ejecutamos el programa:arranca,reserva memoria,termina y volvemos a
# a ejecutar(recordemos que la memoria es volatil),esto quiere decir que al terminar de
# ejecutar nuestro programa,se eliminan todas las variables y se vuelven a crear cada
# cada vez que ejecutamos
## a esto se lo conoce como REFERENCIA DE MEMORIA o simplemente MEMORIA