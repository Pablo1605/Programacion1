'''Trabajo práctico nro. 3'''

#Ejercicio 1
word = input("Ingrese la palabra que desee repetir 10 veces: ")

for i in range(10):
    print(word)

#Ejercicio 2
age = int(input("Ingrese su edad: "))
e = 0
for i in range(age):
    if (e+1) == 1:
        print(f"Usted ha cumplido {e+1} año")
    else:
        print(f"Usted ha cumplido {e+1} años")
    e = e + 1

#Ejercicio 3
num = int(input("Ingrese un numero entero positivo: "))
n = 1
number = ''

print(f"Numeros impares desde 1 hasta {num}:")
for i in range(num):
    if (n) % 2 != 0:
        str(n)
        number = number +  f'{n}, '
    n = n + 1

print(number)

#Ejercicio 4
num = int(input("Ingrese un numero entero positivo: "))
number = ''

print(f"Cuenta atras desde {num} hasta 0:")
for num in range(num,-1,-1):
    str(num)
    number = number +  f'{num}, '

print(number)

#Ejercicio 5
amount_invested = float(input("Ingrese la cantidad a invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
num_years = int(input("Ingrese el numero de años: "))

annual_interest = annual_interest / 100

for i in range(1,num_years + 1):
    capital_obteined = amount_invested * (1 + annual_interest)
    print(f"Año {i}: Capital obtenido = {capital_obteined}")
    amount_invested = capital_obteined

#Ejercicio 6
num = int(input("Ingrese un numero entero positivo: "))
n = '*'

for i in range(num):
    print(n)
    n = n + '*'

#Ejercicio 7
for i in range(1,11):
    print(f"Tabla del {i}")
    for f in range(1,11):
        print(f," x ",i," = ",f*i)

#Ejercicio 8
num = int(input("Ingrese un numero entero positivo: "))
string = ""

for i in range(num):
    if (i % 2) != 0:
        string = str(i) + " " + string
        print(string)

#Ejercicio 9
correct_password = input("Ingrese la contraseña que desee: ")
i = True

while i == True:
    password = input("Introduzca la contraseña correcta: ")
    if password == correct_password:
        print("Contraseña correcta")
        i = False

#Ejercicio 10
num = int(input("Ingrese un numero entero: "))

if num <= 1:
    prime = False
else:
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break

if prime == True:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo") 

#Ejercicio 11
word = input("Introduzca una palabra: ")

for letter in reversed(word):
    print(letter)

#Ejercicio 12
phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
letter = letter
counter = 0

for character in phrase:
    if character.lower() == letter.lower():
        counter += 1

print(f"La letra {letter} aparece {counter} veces en la frase que ingreso")

#Ejercicio 13
exit = True
while exit==True:
    word = input("Ingrese una palabra,cuando desee salir ingrese 'salir': ")
    if word.lower() == "salir":
        exit = False
    else:
        for i in range(4):
            print(word)

#Ejercicio 14
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
pair = ""
odd = ""
i = 0

if num1 > num2:
    start = num2
    end = num1
elif num2 > num1:
    start = num1
    end = num2

for i in range(start,end+1):
    if i % 2 == 0:
        pair = pair + str(i) + " "

for i in range(start,end+1):
    if i % 2 != 0:
        odd = odd + str(i) + " "

print(f"Numeros pares: {pair}\nNumeros impares: {odd}")

#Ejercicio 15
num = int(input("Ingrese un numero entero mayor que 0: "))
divisor = ""

if num > 0:
    for i in range(1,num+1):
        if num %  i == 0:
            divisor = divisor + str(i) + " "
    print(f"Los divisores de {num} son: {divisor}")
else:
    print("Error: El numero tiene que ser mayor que 0")

#Ejercicio 16
amount = int(input("¿Cuantos numeros se van a introducir?: "))
negative_counter = 0

for i in range(amount):
    num = float(input(f"Ingrese el numero {i+1}: "))
    if num < 0:
        negative_counter += 1

print(f"Se introdujeron {negative_counter} numeros negativos")

#Ejercicio 17
phrase = input("Ingrese una frase: ")
v = ""
vocals = ['a','e','i','o','u']
vocals_in_phrase = []

for letter in phrase:
    if letter.lower() in vocals and letter.lower() not in vocals_in_phrase:
        vocals_in_phrase.append(letter.lower())

if vocals_in_phrase:
    for vocal in vocals_in_phrase:
        v = v + str(vocal) + " "
    print(f"Vocales en la frase: {vocals_in_phrase}")
else:
    print("No se encontraron vocales en la frase")

#Ejercicio 18
a = 0
b = 1

for i in range(10):
    print(a,end=" ")
    a,b = b,a+b

#Ejercicio 19
goal = float(input("Ingrese la cantidad que desee ahorrar: "))
total_saved = 0

while goal <= 0:
    print("El objetivo tiene que ser positivo")
    goal = float(input("Ingrese la cantidad que desee ahorrar: "))

while total_saved < goal:
    mount = float(input("Ingrese un monto a ahorrar: "))
    total_saved += mount

print(f"Se alcanzo el objetivo de ahorro de {goal}$ con un total ahorrado de {total_saved}")

#Ejercicio 20
num = 1
counter = 0
while num != 0:
    num = float(input("Ingrese un numero, cuando desee dejar de ingresar numeros ingrese 0: "))
    counter = counter + num

print(f"La suma de todos los numeros es de {counter}")

#Ejercicio 21
num = 1
bigger = 0
while num != 0:
    num = float(input("Ingrese un numero, cuando desee dejar de ingresar numeros ingrese 0: "))
    if num > bigger:
        bigger = num

print(f"El mayor numero ingresado fue: {bigger}")

#Ejercicio 22
num = 0
pair_counter = 0
while num != -1:
    num = int(input("Ingrese un numero entero positivo, ingrese -1 para salir: "))

    if num != -1:
        if num % 2 == 0:
            pair_counter += 1
    
        digit_sum = sum(int(digit) for digit in str(num))
        print(f"La suma de los digitos de {num} da {digit_sum}")

print(f"El usuario introdujo {pair_counter} numeros pares")

#Ejercicio 23
purchase_amount = []
amount = 1
while amount != 0:
    amount = float(input("Ingrese el monto de la compra, ingrese 0 para salir: "))
    if amount != 0:
        purchase_amount.append(amount)
total = sum(purchase_amount)

print(f"El total de las compras es de {total}")

#Ejercicio 24
purchase_amount = []
amount = 1
while amount != 0:
    amount = float(input("Ingrese el monto de la compra, ingrese 0 para salir: "))
    
    if amount < 0:
        print("No se pueden ingresar montos negativos. Vuelva a intentarlo")
    if amount > 0:
        purchase_amount.append(amount)
total = sum(purchase_amount)

if total > 1000:
    discount = total * 0.10
    total -= discount

print(f"El total de las compras es de {total}")

#Ejercicio 25
num = int(input("Ingrese un numero entero positivo: "))
multiplication = 1
i = 1

for i in range(num):
    i = i+1
    multiplication *= i

print(f"La multiplicacion de todos los numeros del 1 hasta el {num} da {multiplication}")