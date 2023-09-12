'''Trabajo Practico 1 parte 2'''

#Ejercicio 1
base = float(input("Ingrese el valor de la base del rectangulo: "))
altura = float(input("Ingrese el valor de la altura del rectangulo: "))

area = base * altura
perimetro = (base*2) + (altura*2)

print(f"El area del rectangulo es: {area},\nEl perimetro del rectangulo es: {perimetro}")

#Ejercicio 2
cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

hipotenusa = ((cateto1)**2 + (cateto2)**2)**(1/2)
print(f"La hipotenusa del triangulo es: {hipotenusa}")

#Ejercicio 3
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de los dos numeros es: {suma},\nLa resta de los dos numeros es: {resta},\nLa multiplicacion de los dos numeros es: {multiplicacion},\nLa division de los dos numeros es: {division}")

#Ejercicio 4
f = float(input("Ingrese los grados fahrenheit que desee convertir a grados celsius: "))

c = (f - 32)*5/9

print(f"{f} grados fahrenheit equivalen a {c} grados celsius")

#Ejercicio 5
#a)El problema es que la variable "nombre" no esta definida, que no esta encerrada en una cadena "f" y que el nombre de la variable esta en mayuscula que es valido pero es una mala practica
#Lo solucionaria de la siguiente manera:
nombre = input("Ingrese su nombre: ")
a = input(f"{nombre} ¿Cual es tu cancion favorita?: ")

#b)El problema es que la entrada de datos input es de tipo string y no de un tipo de dato numerico (int o float)
#Lo solucionaria de la siguiente manera:
precio = float(input("Precio: "))
total = precio + (precio*0.1)

#C)El problema es que el texto del parentesis no esta dentro de comillas y que la variable edad no esta encerrada en una cadena "f"
#Lo solucionaria de la siguiente manera:
edad = int(input("Edad: "))
print(f"Tu edad es {edad}")

#d)El problema es que se esta usando una asignacion en lugar de una comparacion
#Lo solucionaria de la siguiente manera:
edad = int(input("Edad: "))
print("Veamos si tu edad es 18...", edad == 18) 

#Ejercicio 6
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

media = (num1 + num2 + num3) / 3

print(f"La media de los tres numeros es {media}")

#Ejercicio 7
minutos_ingresados = int(input("Ingrese la cantidad cantidad de minutos: "))

horas = minutos_ingresados // 60
minutos = minutos_ingresados % 60

print(f"{minutos_ingresados} minutos corresponden a {horas} horas y {minutos} minutos")

#Ejercicio 8
sueldo_base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese las ganancias de la primera venta: "))
venta2 = float(input("Ingrese las ganancias de la segunda venta: "))
venta3 = float(input("Ingrese las ganancias de la tercera venta: "))

comision = (venta1 + venta2 + venta3) * 0.10
total = sueldo_base + comision

print(f"El monto por concepto de comisiones es {comision}")
print(f"El monto total a recibir en el mes es {total}")

#Ejercicio 9
total_compra = float(input("Ingrese el total de la compra: "))

descuento = total_compra * 0.15
total_pagar = total_compra - descuento

print(f"El total a pagar es con el descuento {total_pagar}")

#Ejercicio 10
parcial1 = float(input("Ingrese la calificacion del primer parcial: "))
parcial2 = float(input("Ingrese la calificacion del segundo parcial: "))
parcial3 = float(input("Ingrese la calificacion del tercer parcial: "))

examen_final = float(input("Ingrese la calificacion del examen final: "))

trabajo_final = float(input("Ingrese la calificacion del trabajo final: "))

promedio_parciales = (parcial1+parcial2+parcial3) / 3

calificacion_final = (promedio_parciales*0.55) + (examen_final*0.30) + (trabajo_final*0.15)
print(f"La clificacion final en la materia de algoritmos es {calificacion_final}")

#Ejercicio 11
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

distancia = abs(num1 - num2)

print(f"La distancia entre {num1} y {num2} es de {distancia}")

#Ejercicio 12
num = float(input("Ingrese el numero del que desee saber su raiz cuadrada y cubica: "))

raiz_cuadrada = num ** 0.5
raiz_cubica = num ** (1/3)

print(f"La raiz cuadrada de {num} es {raiz_cuadrada}\nLa raiz cubica de {num} es {raiz_cubica}")

#Ejercicio 13
num = int(input("Introduce un numero de dos cifras que desees invertir: "))
unidad = num % 10
decena = num // 10
numero_invertido = unidad * 10 + decena
print(f"El numero invertido es {numero_invertido}")

#Ejercicio 14
a = float(input("Ingrese el numero de la variable'a': "))
b = float(input("Ingrese el numero de la variable 'b': "))

aux = a
a = b
b = aux

print(f"Los numeros ahora intercambiados serian:\nNumero de la variable 'a': {a}\nNumero de la variable 'b': {b}")

#Ejercicio 15
hh = int(input("Ingrese la hora de partida (HH): "))
mm = int(input("Ingrese los minutos de partida (MM): "))
ss = int(input("Ingrese los segundos de partida (SS): "))
t = int(input("Ingrese el tiempo de viaje hasta llegar a otra ciudad B en segundos (T): "))

tiempo_total = hh * 3600 + mm * 60 + ss + t
hora_llegada = tiempo_total // 3600

print(f"La hora de llegada a la ciudad B es de {hora_llegada}hs")

#Ejercicio 16
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

inicial_nombre = nombre[0]
inicial_apellido1 = apellido1[0]
inicial_apellido2 = apellido2[0]

print("Las iniciales de tu nombre y tus dos apellidos son: ",inicial_nombre,inicial_apellido1,inicial_apellido2)

#Ejercicio 17
usuario = input("Ingrese su nombre: ")

print(f"Ahora estas en la matrix, {usuario}")

#Ejercicio 18
costo_cena = float(input("Ingrese el costo de la cena en el restaurante: "))

servicio = costo_cena * 0.062
propina = costo_cena * 0.10
monto_total = costo_cena + servicio + propina

print(f"El monto total a pagar es de ${monto_total}")

#Ejercicio 19
dd = int(input("Ingrese su dia de nacimiento: "))
mm = int(input("Ingrese su mes de nacimiento: "))
aaaa = int(input("Ingrese su año de nacimiento: "))

print(f"Su fecha de nacimiento es: {dd}/{mm}/{aaaa}")

#Ejercicio 20
ddmmaaaa = int(input("Ingrese su dia de nacimiento en formato DDMMAA: "))

print(f"SU fecha de nacimiento es: {ddmmaaaa}")

#Ejercicio 21
km_por_litro = float(input("Ingrese cuantos km puede recorrer su moto con 1 litro de combustible: "))
capacidad_tanque = float(input("Ingrese la capacidad del tanque en litros: "))
km_totales = float(input("Ingrese cuantos km recorreran en total: "))

km_por_tanque = km_por_litro * capacidad_tanque
tanques_necesarios = km_totales / km_por_tanque
tanques_necesarios = round(tanques_necesarios + 0.5)

print("Se necesitaran ",tanques_necesarios," tanques de combustible para el viaje")