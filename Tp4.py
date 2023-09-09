'''Trabajo Practico nro. 4 Break - Continue'''

#Ejercicio 1
x = 1

while x < 30:
    if x == 15:
        break
    if (x == 4) or (x == 6) or (x == 10):
        print(f"Se saltó el valor {x} de x")
        x += 1
        continue
    print(x)
    x += 1
print(f"Se rompió la ejecución del bucle cuando x valía: {x}")

#Ejercicio 1
line = []
word = " "

while word != "":
    
    word = input("Ingrese una linea, cuando quiera dejar de agregar lineas deje en blanco: ")
    if not word:
        break
    word = word.upper()
    line.append(word)
    
print(line)

#Ejercicio 2
balance = 0
while True:
    operation = input("Ingrese que tipo de operación desea realizar,'D' para depositar y 'R' para retirar, deje en blanco para salir: ")
    if not operation:
        break
    operation = operation.upper()
    if operation == 'D':
        deposit_amount = int(input("Ingrese el monto a depositar: "))
        balance += deposit_amount
    elif operation == 'R':
        withdrawal_amount = int(input("Ingrese el monto a retirar: "))
        balance -= withdrawal_amount
    else:
        print("Operación inexistente")
print(f"Saldo: {balance}")

#Ejercicio 3
amount_prime = 0
while True:
    num = int(input("Ingrese un número, cuando desee dejar de ingresar números ingrese 0: "))
    if num == 0:
        break

    if num < 2:
        continue

    prime = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        amount_prime += 1
print(f"La cantidad total de números primos es de {amount_prime}")

#Ejercicio 4
first_year = int(input("Ingrese el primer año: "))
second_year = int(input("Ingrese el segundo año: "))

for year in range(first_year,second_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if year % 10 == 0:
            print(year)

#Ejercicio 5
for i in range(1,20+1):
    if i % 2 != 0:
        continue
    print(i)

#Ejercicio 6
list = [1,2,3,4,5,6,7,8,9,10]
num_to_search = 4

for num in list:
    num = int(input("Busque el número especifico: "))
    if num == num_to_search:
        print(f"Encontraste al número {num_to_search}")
        break

#Ejercicio 7
while True:
    print("Opción 1\nOpción 2\nOpción 3")
    option = input("Elija una opción[1/2/3]: ")
    if not option:
        break
    option = int(option)
    if option == 1:
        print("Usted eligió la opción 1")
    elif option == 2:
        print("Usted eligió la opción 2")
    elif option == 3:
        print("Usted eligió la opción 3")
    else:
        print("Opción inexistente")