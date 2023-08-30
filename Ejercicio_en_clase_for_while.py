'''Ejercicio en clase FOR-WHILE'''

#Ejercicio 1
n = 1
i = 0
corrimiento = int(input("Ingrese el corrimiento hacia la derecha que desee para la encriptación: "))

for i in range(5):
        mensaje = input(f"Ingrese el mensaje {i+1}: ")
        alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
        mensaje_encriptado = ''
        mensaje = mensaje.lower()

        for letra in mensaje:
            if letra.isalpha():
                indice = (alfabeto.index(letra) + corrimiento) % 27
                nueva_letra = alfabeto[indice]
                mensaje_encriptado += nueva_letra
            else:
                mensaje_encriptado += letra
            n = 0
        print(f"Mensaje encriptado {i+1}: {mensaje_encriptado}")

#Ejercicio 2
i = 1
total_digitos_pares = 0
total_digitos_impares = 0
while i != 0:
    num = int(input("Ingrese un numero entero positivo, cuando desee dejar de ingresar numeros inserte 0: "))

    if num == 0:
        i = 0
        break

    digitos_pares = 0
    digitos_impares = 0
    num_temp = num

    while num_temp > 0:
        digito = num_temp % 10
        if digito % 2 == 0:
            digitos_pares += 1
        else:
            digitos_impares += 1
        num_temp //= 10

    total_digitos_pares += digitos_pares
    total_digitos_impares += digitos_impares
    print(f"El numero {num} tiene {digitos_pares} digitos pares y {digitos_impares} digitos impares")
print(f"El total de digitos pares es de: {total_digitos_pares}")
print(f"El total de digitos impares es de: {total_digitos_impares}")