'''

-- 6.0 Vamos a comenzar haciendo varios commit
-- 6.1 Ciclo While


contador = 0
while contador < 78:
    print('ejecutamos el ciclo while:',contador)
    contador += 10
else:
    print('fin del ciclo while.')

-- 6.2 Ejercicios con el ciclo while
--imprimir numeros del 0 al 5 en el ciclo while


maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1



minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

-- 6.3 Ciclo For, palabra break y continue


cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('fin del ciclo')

for letra in 'Alemania':
    if letra == 'a':
        print(f'letra escondida {letra}')
        break
else:
    print('fin del ciclo for')



for i in range(6):
    if i%2 ==0:
        print(f'valor:{i}')
'''
for i in range(6):
    if i%2 !=0:
        continue
    print(f'valor:{i}')