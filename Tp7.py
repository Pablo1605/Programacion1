'''Trabajo Práctico nro. 7'''

from operator import itemgetter
#Ejercicio 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [20,10,80,40,60,30,50,90,70]
bubble_sort(numbers)
print("Lista de números ordenada: ")
print(numbers)

#Ejercicio 2
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
words = ["Dado","Bordo","Casa","Elefante","Auto","Foca"]
selection_sort(words)
print("Lista de palabras ordenada alfabeticamente: ")
print(words)

#Ejercicio 3
def sort_books(books,camp):
    return sorted(books,key=itemgetter(camp))

books = [
    {"titulo": "El principito","autor": "Antonie de Saint-Exupery","año":1943},
    {"titulo": "Don Quijote","autor": "Miguel de Cervantes","año":1605},
    {"titulo": "Ficciones","autor": "Jorge Luis Borges","año":1944},
    {"titulo": "2001: A Space Odyssey","autor": "Arthur C. Clarke","año":1968}
]
books_arranged_by_year = sort_books(books,"año")
print("Libros ordenados por año de publicación: ")
for book in books_arranged_by_year:
    print(book)

#Ejercicio 4
def insertion_sort(list):
    for i in range(1, len(list)):
        clave = list[i]
        j = i - 1
        while j >= 0 and len(clave) < len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = clave

strings = ["uno","hola","mundo","America","Argentina"]
insertion_sort(strings)
print(strings)

#Ejercicio 5
def insertion_sort_descendant(list):
    for i in range(1, len(list)):
        clue = list[i]
        j = i - 1
        while j >= 0 and len(clue) > len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = clue

insertion_sort_descendant(strings)
print(strings)

#Ejercicio 6
def count_sort(list):
    count = {}
    
    for num in list:
        count[num] = count.get(num, 0) + 1
    
    ordered_list = []
    for num, freq in sorted(count.items()):
        ordered_list.extend([num] * freq)
    
    return ordered_list

integer = [5,1,4,8,2,9,3,7,6]
ordered_numbers = count_sort(integer)
print(ordered_numbers)

#Ejercicio 7
def sort_list_numbers_and_strings(list):
    num = [element for element in list if isinstance(element, (int, float))]
    strings = [element for element in list if isinstance(element, str)]

    num.sort()

    strings.sort()

    ordered_list = num + strings

    return ordered_list

list = [5, "manzana", 3.5, "pera", 2, "uva", "banana", 1, "kiwi"]
ordered_list = sort_list_numbers_and_strings(list)
print(ordered_list)

#Ejercicio 8
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

integer1 = [70,50,90,80,100,60]
ordered_numbers1 = merge_sort(integer1)
print(ordered_numbers1)