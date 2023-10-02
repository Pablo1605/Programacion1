'''Trabajo práctico nro. 5'''

import math
#Ejercicio 1
def validate_dni(dni):
    if len(dni) == 7 or len(dni) == 8:
        return True
    else:
        return False

dni = input("Ingrese un número de DNI: ")
if validate_dni(dni):
    print("El número de DNI es valido")
else:
    print("El número de DNI es invalido")

#Ejercicio 2
def last_word_lenght(string):
    string = string.strip()
    word = string.split()
    if word:
        return len(word[-1])
    else:
        return 0

string = input("Ingrese el string:")
lenght = last_word_lenght(string)
print(f"La longitud de la última palabra del string ingresado es '{lenght}'")

#Ejercicio 3
def validate_dni(dni):
    return len(dni) in (7,8) and dni.isdigit()

def get_identifier(name,dni):
    names = name.split()
    first_name = names[0].capitalize()
    lastName = names[-1].capitalize()
    dni = str(dni)[:3]
    return f"{first_name}{len(lastName)}{dni}"

while True:
    name = input("Ingrese su nombre completo, cuando desee salir deje en blanco: ")
    if not name:
        break
    dni = input("Ingrese su número de DNI: ")
    dni = dni.strip()
    while not validate_dni(dni):
        print("El número de DNI debe tener 7 u 8 digitos")
        dni = input("Ingrese el número de DNI nuevamente: ")
        dni = dni.strip()
    identifier = get_identifier(name,dni)
    print(f"ID -> {identifier}\n")

#Ejercicio 4
def is_multiple(num1,num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if is_multiple(num1,num2):
    print("Uno de los números es multiplo del otro")
else:
    print("Ninguno de los números es multiplo del otro")

#Ejercicio 5
def medium_temperature(maximum_temperature,minimum_temperature):
    return (maximum_temperature + minimum_temperature) / 2

days = int(input("Ingrese el número de días: "))
for day in range(1,days + 1):
    maximum_temperature = float(input(f"Ingrese la temperatura máxima para el día {day}: "))
    minimum_temperature = float(input(f"Ingrese la temperatura mínima para el día {day}: "))
    average_temperature = medium_temperature(maximum_temperature,minimum_temperature)
    print(f"La temperatura media para el día {day} es: {average_temperature}")

#Ejercicio 6
def spaces(text):
    return ' '.join(text)

text = input("Ingrese un texto: ")
modified_text = spaces(text)
print(f"Texto original: {text}")
print(f"Texto con espacios: {modified_text}")

#Ejercicio 7
def find_max_min(list):
    maximum = max(list)
    minimum = min(list)
    return maximum,minimum

numbers = []
num_elements = int(input("Ingresa el número de elementos de la lista: "))
for i in range(num_elements):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numbers.append(num)
maximum, minimum = find_max_min(numbers)
print(f"El valor máximo es: {maximum}")
print(f"El valor minimo es: {minimum}")

#Ejercicio 8
def circumference_calculation(radio):
    area = math.pi * radio**2
    perimeter = 2 * math.pi * radio
    return area, perimeter

radio = float(input("Ingrese el radio de la circunferencia: "))
area, perimeter = circumference_calculation(radio)
print(f"El area de la circunferencia es: {area}")
print(f"El perimetro de la circunferencia es: {perimeter}")

#Ejercicio 9
def login(user,password,attempts):
    if user == "usuario1" and password == "asdasd":
        return True, attempts
    else:
        attempts += 1
        return False, attempts

attempts = 0
while attempts < 3:
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    acces, attempts = login(user,password,attempts)
    if acces:
        print("Los datos ingreasdos son correctos")
        break
    else:
        print("Alguno o todos los datos ingresados son incorrectos")

#Ejercicio 10
def add_discount(trolley,discount):
    final_price = 0
    for product, price in trolley.items():
        if product in discount:
            discount = discount[product]
            price_with_discount = price * (1 - discount / 100)
            final_price += price_with_discount
        else:
            final_price += price
        return final_price


trolley = {"producto1":10,"producto2":20,"producto3":30,"producto4":40}
discount = {"producto1":10,"producto1":15}
final_price = add_discount(trolley,discount)
print(f"El precio final es: {final_price}")

#Ejercicio 11
def function_to_list(function,list):
    return [function(element) for element in list]

def square(num):
    return num**2

numbers = [1,2,3,4,5,6]
result = function_to_list(square,numbers)
print(result)

#Ejercicio 12
def get_words_lenght(phrase):
    words = phrase.split()
    words_lenght = {word: len(word) for word in words}
    return words_lenght

phrase = input("Ingrese una frase: ")
result = get_words_lenght(phrase)
print(result)

#Ejercicio 13
def vector_module(x, y, z):
    module = math.sqrt(x**2 + y**2 + z**2)
    return module

x = float(input("Ingrese el valor del componente x del vector: "))
y = float(input("Ingrese el valor del componente y del vector: "))
z = float(input("Ingrese el valor del componente z del vector: "))
module = vector_module(x, y, z)
print(f"El modulo del vector es {module}")

#Ejercicio 14
def is_prime(num):
    if num < 2:
        false
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

num = int(input("Ingrese un número entero: "))
if is_prime(num):
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")

#Ejercicio 15
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

quantity_numbers = 0
while True:
    try:
        num = int(input("Ingresa un número entero, ingresa 0 cuando desees salir: "))
        if num == 0:
            break
        elif num < 0:
            print("No se puede calcular el factorial de un número negativo")
        else:
            print(f"El factorial de {num} es: ", factorial(num))
            quantity_numbers += 1
    except ValueError:
        print("Error: ingresa un número entero que sea valido")
print(f"Se leyeron un total de {quantity_numbers} números")

#Ejercicio 16
def calculate_frecuency(num,digit):
    frecuency = str(num).count(str(digit))
    return frecuency

try:
    num = int(input("Ingrese un número entero: "))
    digit = int(input("Ingrese un digito: "))
    frecuency = calculate_frecuency(num,digit)

    print(f"El digito {digit} tiene {frecuency} ocurrencias en el número {num}")
except:
    print("Error: ingresa un número entero que sea valido")

#Ejercicio 17
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_digits(num):
    return sum(int(digit) for digit in str(num))

def count_frecuency(num,digit):
    return str(num).count(str(digit))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

greater_prime = 0
while True:
    try:
        num = int(input("Ingresa un número primo, cuando desees salir ingresa un número que no sea primo: "))
        if num <= 1:
            print("Ingresa un número primo mayor que 1")
            continue
        if not prime(num):
            break
        if num > greater_prime:
            greater_prime = num
        sum = sum_digits(num)
        
        print(f"La suma de los digitos es {sum}")

        digit = int(input("Ingresa un digito: "))
        frecuency = count_frecuency(num,digit)
        print(f"El digito {digit} tiene {frecuency} ocurrencias en el número {num}")
    except ValueError:
        print("Error: ingresa un número entero que sea valido")
if greater_prime != 0:
    print(f"El factorial de el mayor número {greater_prime} es ", factorial(greater_prime))