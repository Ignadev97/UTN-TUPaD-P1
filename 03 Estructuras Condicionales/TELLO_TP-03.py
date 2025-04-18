import random 
from statics import mode, median, mean


# Trabajo práctico N°3 CONDICIONALES 
# Ejercicio 1 

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# Ejercicio 2

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejerciocio 3 

num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("Por favor ingresar un número par")

# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Es niño/a")
elif edad >= 12 and edad < 18:
    print("Es adolescente")
elif edad >= 18 and edad < 30:
    print("Es adulto/a joven")
else:
    print("Es adulto/a")

# Ejercicio 5

password = input("Ingrese su contraseña: ")

if len(password) < 8 or len(password) > 12:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else: 
    print("Ha ingresado una contraseña correcta")

# Ejercicio 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda :
    print('Hay sesgo positivo')
elif media < mediana and mediana < moda:
    print('Hay sesgo negativo')
else: 
    print('No hay sesgo')

# Ejercicio 7

palabraOFrase = input('Por favor ingresar una Palabra o Frase')

#Tuve que investigar esta funcionalidad para obtener la última letra
ultimaLetra = palabraOFrase[-1]

if ultimaLetra == 'a' or ultimaLetra == 'e' or ultimaLetra == 'i' or  ultimaLetra == 'o' or ultimaLetra == 'u':
    print(f'{palabraOFrase}!') 
else: 
    print(f'{palabraOFrase}')


# Ejercicio 8 
nombre = input('Por favor ingrese su nombre')

opcionIngresada = input('Ahora ingrese una de las opciones: 1 Para escribir su nombre en mayúscula 2 Para escribir su nombre en minúscula 3 Para escribir su nombre sólo con la primer letra mayúscula')

#Busqué cómo simplificar para no repetir opcionIngresada
if opcionIngresada not in ('1', '2', '3'): 
    print('Opción nó válida')

if opcionIngresada == '1':
    print(nombre.upper()) 
elif opcionIngresada == '2':
    print(nombre.lower())
else:
    print(nombre.title())

# Ejercicio 9

magnitud = float(input('Por favor ingrese la magnitud del terremoto'))

if magnitud < 0: 
    print('Error en el dato ingresado')

if magnitud < 3: 
    print('Muy leve (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('Leve (ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('Fuerte (puede causar daños en estructuras débiles)')
elif magnitud >= 6 and magnitud < 7:
    print('Muy fuerte (puede causar daños significativos)')
elif magnitud > 7:
    print('Extremo (puede causar graves daños a gran escala)')


# Ejercicio 10

hemisferio = input('Por favor ingrese el hemisferio en el que se encuentra (norte o sur)')
mes = input('Por favor ingrese el mes en el que se encuentra')
dia = float(input('Por favor ingrese dia de hoy'))

estacion = ''

if mes in ('enero' , 'febrero', 'marzo') or (mes == 'diciembre' and dia > 20) :

    if hemisferio == 'norte' :
        estacion = 'invierno'
    if hemisferio == 'sur' :
        estacion = 'verano'

elif mes in ('abril', 'mayo', 'junio') or (mes == 'marzo' and dia >= 20): 

    if hemisferio == 'norte' :
        estacion = 'primavera'
    if hemisferio == 'sur' :
        estacion = 'otoño'   

elif mes in ('julio', 'agosto', 'septiembre') or (mes == 'junio' and dia >= 20): 

    if hemisferio == 'norte' :
        estacion = 'verano'
    if hemisferio == 'sur' :
        estacion = 'invierno'   

elif mes in ('octubre', 'noviembre', 'diciembre') or (mes == 'septiembre' and dia >= 20): 

    if hemisferio == 'norte' :
        estacion = 'otoño'
    if hemisferio == 'sur' :
        estacion = 'primavera'   
    

print(f'used encuentra en {estacion}')