'''Trabajo Practico nro. 8'''

#Ejercicio 1
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

num = int(input("Ingrese un número: "))
print(f"El número {num} tiene {contar_digitos(num)} digitos")

#Ejercicio 2
def es_potencia(n,b):
    if n == 1:
        return True
    elif n < b:
        return False
    else:
        return es_potencia(n / b,b)

n = int(input("Ingrese el valor de 'n': "))
b = int(input("Ingrese el valor de 'b': "))
print(f"¿{n} es potencia de {b}?: {es_potencia(n,b)}")

#Ejercicio 3
def encontrar_posiciones(a,b,start=0):
    index = a.find(b,start)
    if index == -1:
        return []
    else:
        return [index] + encontrar_posiciones(a,b,index + 1)

a = input("Ingrese una frase para 'a': ")
b = input("Ingrese una palabra para 'b' a encontrar en 'a': ")
posiciones = encontrar_posiciones(a,b)
print(posiciones)

#Ejercicio 4
def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n - 1)

#Ejercicio 5
def encontrar_mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximo = encontrar_mayor(lista[1:])
        return maximo if maximo > lista[0] else lista[0]

lista = [4,2,9,7,10,1,3,8,6,5]
mayor_num = encontrar_mayor(lista)
print(f"El mayor número de la lista es: {mayor_num}")

#Ejercicio 6
def replicar_lista(lista,n):
    if n == 1:
        return lista
    else:
        return [elemento for elemento in lista for _ in range(n)]

lista = [1,2,3]
n = 3
print(replicar_lista(lista,n))

#Ejercicio 7
def k(n,p):
    if n == 1:
        return p
    else:
        return n * p + k(n-1,p)

n = int(input("Ingrese el valor de 'n': "))
p = int(input("Ingrese el valor de 'p': "))
resultado = k(n,p)
print(f"El resultado de K({n},{p}) es: {resultado}")

#Ejercicio 8
def pascal(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n-1,k-1) + pascal(n-1,k)

n = int(input("Ingrese el valor de 'n': "))
k = int(input("Ingrese el valor de 'k': "))
resultado = pascal(n,k)
print(f"El valor en la fila {n} y la columna {k} es {resultado}")

#Ejercicio 9
def combinaciones(lista,k,prefijo=""):
    if k == 0:
        print(prefijo)
        return
    for caracter in lista:
        combinaciones(lista,k-1,prefijo + caracter)

caracteres = ['a','b','c','d']
k = 3
combinaciones(caracteres,k)

#Ejercicio 10
def medidas(n):
    if n == 0:
        return (841,1189)
    else:
        ancho_anterior,largo_anterior = medidas(n-1)
        nuevo_ancho = largo_anterior // 2
        nuevo_largo = ancho_anterior
        return (nuevo_ancho,nuevo_largo)

n = int(input("Ingrese un valor mayor que 0 para 'N': "))
ancho,largo = medidas(n)
print(f"Las medidas de la hoja son: {ancho} mm x {largo} mm")