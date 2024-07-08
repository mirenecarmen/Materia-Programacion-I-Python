'''
--Ejercicio 5:Calcular el factorial de un numero mayor o igual a 0.


num = int(input("Ingrese un número: "))
if num >= 0:
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f'El factorial del número {num} es {factorial}')
else:
    print('El número es menor que cero')

--Ejercicio 7: ingresar N enteros,visualizar la suma de los numeros pares
de la lista,cuantos numeros pares existen y cual es el promedio de los
numeros impares.

n_elementos= int(input("ingrese la cantidad de numeros a ingresar:"))
suma_pares=0
conteo_pares=0
suma_impares=0
conteo_impares=0

for i in range(n_elementos):
    num=int(input(f"ingrese el numero {i+1}:"))
    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1
promedio_impares=suma_impares/conteo_impares if conteo_impares > 0 else 0
print(f"suma de los numeros pares :{suma_pares}")
print(f"cantidad de numeros pares:{conteo_pares}")
print(f"promedio de los numeros impares:{promedio_impares}")


--ejercicio 8: dadas las horas trabajadas de 5 personas y la tarifa de pago,calcular el
salario y la sumatoria de todos los salarios.

'''
i=0
suma=0
horas_trabajadas=[]
cant_personas=i+1
for i in range(5):
    horas=int(input(f'ingrese las horas trabajadas por cada persona {i+1}:'))
    horas_trabajadas.append(horas)
tarifa=float(input("ingrese la tarifa de pago por hora:"))
for i in range(5):
    horas=horas_trabajadas[i]
    salario=horas*tarifa
    suma += salario
    print(f'persona{i+1}:horas trabajadas ={horas},tarifa={tarifa},salario={salario:.2f}')
    print(f'sumatoria de todos los salarios:{suma:.2f}')