'''EJERCICIO RECURSIÓN'''

#Ejercicio 1
import random
def tiempo_en_salir():
    camino = random.randint(1,3)
    if camino == 1:
        return 3 + tiempo_en_salir()
    elif camino == 2:
        return 5 + tiempo_en_salir()
    else:
        return 7

#Ejercicio 2
'''Crear una función llamada f que lea un número n como entrada
y lo invierta, por ejemplo si el valor de n es 123 que la función
devuelva 321'''