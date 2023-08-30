'''Trabajo Pràctico nro. 2'''

#Ejercicio 1
años_pc = int(input("Ingrese el numero de años que tiene su computadora: "))

if (años_pc >= 0):
    if (años_pc <= 2):
        print("Su computador es nuevo")
    else:
        print("Su computador es viejo")

#Ejercicio 2
else:
    print("Error: el numero tiene que ser positivo")

#Ejercicio 3
nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")

if nombre1[0] == nombre2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#Ejercicio 4
candidato = input("Elija el candidato al que va a votar (A/B/C): ")

if (candidato == "A" or candidato == "a"):
    print("Usted a votado por el partido rojo")
elif (candidato == "B" or candidato == "b"):
    print("Usted a votado por el partido verde")
elif (candidato == "C" or candidato == "c"):
    print("Usted a votado por el partido azul")

#Ejercicio 5
letra = input("Ingrese una letra: ")

if (len(letra) == 1):
    if (letra == "A" or letra == "a") or (letra == "E" or letra == "e") or (letra == "I" or letra == "i") or (letra == "O" or letra == "o") or (letra == "U" or letra == "u"):
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar el dato")

#Ejercicio 6
año = int(input("Ingrese el año que desee saber si es bisiesto: "))

if (año % 4) == 0 or (año % 4) == 0 and (año % 100) != 0:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")

#Ejercicio 7
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 > num2:
    if num2 > num3:
        print(f"El menor es {num3}")
    else:
        print(f"El menor es {num2}")
elif num1 > num3:
    print(f"El menor es {num3}")
else:
    print(f"El menor es {num1}")

#Ejercicio 8
nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if (nombre_usuario == "Gwenevere") and (contrasena == "excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#Ejercicio 9
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo: ")
nombre = nombre.lower()
sexo = sexo.lower()
a_mujer = ['a','b','c','d','e','f','g','h','i','j','k','l']
a_hombre = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

if (sexo == "mujer"):
    if (nombre[0] in a_mujer):
        print("Mujer grupo A")
    else:
        print("Mujer grupo B")
else:
    if (sexo == "hombre"):
        if (nombre[0] in a_hombre):
            print("Hombre grupo A")
        else:
            print("Homber grupo B")

#Ejercicio 10
edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Usted puede entrar gratis")
elif (edad > 3 and edad < 19):
    print("Usted debe pagar $500")
elif edad > 18:
    print("Uste debe pagar $1000")

#Ejercicio 11
pregunta = input("¿Usted desea comprar una pizza vegetariana?[si/no]: ")
pregunta = pregunta.lower()
ingredientes_elegidos = ['mozarrela','tomate']

if pregunta.lower() == "si":
    tipo_pizza = "vegetariana"
    print("Ingredientes vegetarianos: \n1_Pimiento  \n2_tofu")
    ingrediente = int(input("Seleccione un ingrediente[1/2]: "))
    if ingrediente == 1:
        ingredientes_elegidos.append('pimiento')
    elif ingrediente == 2:
        ingredientes_elegidos.append('tofu')
    else:
        print("Opcion invalida")

elif pregunta.lower() == "no":
    tipo_pizza = "no vegetariana"
    print("Ingredientes no vegetarianos: \n1_Peperoni \n2_Jamón \n3_Salmón")
    ingrediente = int(input("Seleccione un ingrediente[1/2/3]: "))
    if ingrediente == 1:
        ingredientes_elegidos.append('peperoni')
    elif ingrediente == 2:
        ingredientes_elegidos.append('jamón')
    elif ingrediente == 3:
        ingredientes_elegidos.append('salmón')
    else:
        print("Opcion invalida")

print(f"Usted ha elegido una pizza {tipo_pizza} con los siguientes ingredientes:")
print(ingredientes_elegidos)

#Ejercicio 12
año_actual = int(input("Ingrese el año actual: "))
año_cualquiera = int(input("Ingrese un año cualquiera: "))

if año_actual < año_cualquiera:
    años_faltantes = año_cualquiera - año_actual
    print(f"Faltan {años_faltantes} años para el año {año_cualquiera}")
elif año_actual > año_cualquiera:
    años_pasados = año_actual - año_cualquiera
    print(f"El año {año_cualquiera} fue hace {años_pasados} años")

#Ejercicio 13
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if (num1 <= 0) or (num2 <= 0):
    print("No se pueden ingresar valores negativos o nulos")
else:
    if num1 > num2:
        mayor = num1
        menor = num2
        if (mayor % menor) == 0:
            print(f"El numero {mayor} es multiplo de {menor}")
        else:
            print(f"El numero {mayor} no es multiplo de {menor}")
    elif num2 > num1:
        mayor = num2
        menor = num1
        if (mayor % menor) == 0:
            print(f"El numero {mayor} es multiplo de {menor}")
        else:
            print(f"El numero {mayor} no es multiplo de {menor}")

#Ejercicio 14
print("Ingrese los coeficientes de la siguiente ecuacion de primer grado: ax + b = 0")
a = float(input("Ingrese el valor de 'a': "))
b = float(input("Ingrese el valor de 'b': "))

if a == 0:
    print("La ecuacion no tiene solucion")

x = -b / a
print(f"El resultado de la ecuacion es x = {x}")

#Ejercicio 15
pregunta = input("¿Desea calcular el area de un triangulo o la de un circulo?: ")

if (pregunta[0] == "T" or pregunta[0] == "t"):
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print(f"El area del triangulo es {area}")
elif (pregunta[0] == "C" or pregunta[0] == "c"):
    radio = int(input("Ingrese el radio: "))
    area = 3,1416 * radio**2
    print(f"El area del circulo es {area}")

#Ejercicio 16
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
opcion = int(input("1_a + b\n2_a * b\n3_a - b \n4_a / b\nIngrese la operacion que desee hacer con los valores ingresados de a y b [1/2/3/4]: "))

if opcion == 1:
    resultado = a + b
    print(f"El resultado es {resultado}")
elif opcion == 2:
    resultado = a * b
    print(f"El resultado es {resultado}")
elif opcion == 3:
    resultado = a - b
    print(f"El resultado es {resultado}")
elif opcion == 4:
    resultado = a / b
    print(f"El resultado es {resultado}")
else:
    print("Opcion invalida")

#Ejercicio 17
dia_semana = input("Ingrese un dia de la semana: ")
dia_semana = dia_semana.lower()

if dia_semana == "lunes":
    print("Comienza la semana!")
elif dia_semana == "viernes":
    print("El fin de semana esta cerca!")
elif (dia_semana == "sabado") or (dia_semana == "domingo"):
    print("Disfruta del fin de semana!")
else:
    print("Que tenga un hermoso dia!")

#Ejercicio 18
horas_trabajadas = int(input("Ingrese su cantidad de horas trabajadas en el mes: "))
salario_hora = int(input("Ingrese su salario por hora: "))

horas_extras = horas_trabajadas - 48
salario_total = (horas_trabajadas * salario_hora) + (horas_extras * salario_hora * 1.10)

print(f"Horas extras trabajadas: {horas_extras}")
print(f"Salario total: {salario_total}")

#Ejercicio 19
cantidad_lapices = int(input("Ingrese la cantidad de lapices: "))

costo_sin_descuento = cantidad_lapices * 60

if cantidad_lapices > 1000:
    descuento = costo_sin_descuento * 0.07
    costo_con_descuento = costo_sin_descuento - descuento
    print(f"Costo total con el descuento de 7%: {costo_con_descuento}")
else:
    print(f"Costo total sin descuento: {costo_sin_descuento}")

#Ejercicio 20
nota1 = int(input("Ingrese su primera nota: "))
nota2 = int(input("Ingrese su segunda nota: "))
nota3 = int(input("Ingrese su tercera nota: "))
nota4 = int(input("Ingrese su cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 6:
    print(f"Usted aprobo el curso con un promedio de {promedio}")
else:
    print(f"Usted reprobo el curso con un promedio de {promedio}")