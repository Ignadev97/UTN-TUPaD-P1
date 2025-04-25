# Trabajo práctico N°4 ESTRUCTURAS REPETITIVAS
import random

# Ejercicio 1
for i in range(101): 
    print(i)

# Ejercicio 2

# Fue lo primero que se me ocurrio
# num = input('Por favor ingrese un número entero: ')
# print(f'su número tiene {len(num)} digitos')

num = input('Por favor ingrese un número entero: ')

digitos = 0
for digito in num:
    digitos += 1

print(f'su número tiene {digito} digitos')

# Ejercicio 3

num1 = int(input('Por favor ingrese un primer número: '))
num2 = int(input('Por favor ingrese un segundo número: '))

resultado = 0

if num1 < num2: 
    for i in range(num1 +1 , num2): 
        resultado = resultado + i
        print(resultado)
elif num2 < num1: 
    for i in range(num1 -1 , num2, -1): 
        resultado = resultado + i

print(f'La suma entre los números enteros comprendudos entre el primer número y el segundo es: {resultado}')

# Ejercicio 4

num = int(input('por favor ingrese un número: '))

resultado = 0

while num != 0:
    resultado = resultado + num
    num = int(input('por favor ingrese otro número: '))

print(f'resultado final: {resultado}')

# Ejercicio 5

numRan = random.randint(1,10)

numUser = int(input('Por favor ingrese un número para ver si acierta el número1: '))

c = 1

while numRan != numUser:
    c += 1
    numUser = int(input('Ese no es!, intente de nuevo: '))

print(f'Usted atinó al número! le tomó {c} intentos!!')

# Ejercicio 6

for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7

numUser = int(input('Por favor ingresar un número'))

if numUser > 0:
    resultado = 0
    for i in range(0, numUser +1):
        resultado= resultado + i
    print(f'el resultado de la suma de los números que comprenden desde 0 hasta {numUser}, es {resultado}')
else:
    print('El número debe ser positivoooooooooo')

# Ejercicio 8

numerosPares, numerosImpares, numerosPositivos, numerosNegativos = 0, 0, 0, 0

for i in range(100):
    numUser = int(input('Por favor ingrese un número: '))
    
    if numUser > 0:
        numerosPositivos += 1
    elif numUser < 0:
        numerosNegativos += 1

    if numUser % 2 == 0: 
        numerosPares += 1
    else:  
        numerosImpares += 1

print("Positivos:", numerosPositivos)
print("Negativos:", numerosNegativos)
print("Pares:", numerosPares)
print("Impares:", numerosImpares)
    
# Ejercicio 9

suma = 0
cantidad = 0  

for i in range(100):  
    num = int(input('ingrese un número: '))
    suma += num
    cantidad += 1

print(f'La media de los números que ingresó es {suma / cantidad}')

# Ejercicio 10

numUser = input("Ingrese un número: ")


numero_invertido = ""

# lo tuve que investigar
for i in range(len(numUser) - 1, -1, -1):
    numero_invertido += numUser[i]


print("número invertido:", numero_invertido)
