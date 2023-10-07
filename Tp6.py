import random
'''Trabajo práctico nro.6'''

#Ejercicio 1
list_numbers = []
while True:
    num = int(input("Ingrese un número, ingrese 0 cuando desee dejar de ingresarlos: "))
    if num == 0:
        break
    list_numbers.append(num)
print(f"Lista de los números ingresados: {list_numbers}")

#Ejercicio 2
num_to_delete = int(input("Ingrese un número: "))
if num_to_delete in list_numbers:
    list_numbers.remove(num_to_delete)
    print(f"Se elimino el número {num_to_delete} de la lista")
    print(f"Lista de los números ingresados ahora: {list_numbers}")
else:
    print(f"El número {num_to_delete} no se pudo eliminar porque no está en la lista")

#Ejercicio 3
summation = sum(list_numbers)
print(f"La sumatoria de todos los números de la lista es: {summation}")

#Ejercicio 4
limit = int(input("Ingresa un número limite: "))
list_numbers2 = [num for num in list_numbers if num < limit]
for element in list_numbers2:
    print(element)

#Ejercicio 5
list_with_tumples = [(num,list_numbers.count(num)) for num in set(list_numbers)]
print(f"Lista con tuplas: {list_with_tumples}")

#Ejercicio 6
primary_names = []
high_school_names = []
while True:
    name = input("Ingrese el nombre de pila de los alumnos de nivel primario, ingrese 'x' para salir: ")
    if name == "x":
        break
    primary_names.append(name)

while True:
    name = input("Ingrese el nombre de pila de los alumnos de nivel secundario, ingrese 'x' para salir: ")
    if name == "x":
        break
    high_school_names.append(name)

total_names = set(primary_names + high_school_names)
repeated_names = set([name for name in primary_names if name in high_school_names])
unique_primary_names = set([name for name in primary_names if name not in high_school_names])

print(f"Nombre de todos los alumnos sin repeticiones: \n{total_names}")
print(f"Nombre repetidos: \n{repeated_names}")
print(f"Nombre del nivel primario que nos se repiten en los de nivel secundario: \n{unique_primary_names}")

#Ejercicio 7
ocurrences = {}
for _ in range(50):
    string = input("Ingrese un string, deje un espacio en blanco si ya no desea ingresar mas strings si no: ")
    if not string:
        break
    for character in string:
        if character in ocurrences:
            ocurrences[character] += 1
        else:
            ocurrences[character] = 1

for character, amount in ocurrences.items():
    print(f"{character}:{amount}")

#Ejercicio 8
goals = [
    [0, 2, 3, 1, 0, 0, 2, 1, 0, 2],
    [2, 0, 1, 3, 2, 1, 0, 0, 1, 1],
    [1, 3, 0, 2, 1, 2, 1, 3, 0, 0],
    [3, 1, 2, 0, 1, 0, 3, 2, 1, 1],
    [0, 2, 1, 1, 0, 1, 0, 1, 2, 2],
    [1, 0, 2, 0, 1, 0, 2, 1, 1, 0],
    [0, 3, 1, 3, 0, 2, 0, 2, 0, 1],
    [2, 1, 3, 2, 2, 1, 2, 0, 0, 1],
    [3, 0, 1, 2, 0, 1, 3, 2, 0, 0],
    [1, 0, 2, 1, 3, 0, 1, 1, 2, 0]
]

triumphs = [0] * 10
ties = [0] * 10
defeats = [0] * 10
goals_scored = [0] * 10
goals_received = [0] * 10
points = [0] * 10

for i in range(10):
    for j in range(10):
        if i != j:
            goals_scored[i] += goals[i][j]
            goals_received[i] += goals[j][i]
            if goals[i][j] > goals[j][i]:
                triumphs[i] += 1
            elif goals[i][j] == goals[j][i]:
                ties[i] += 1
            else:
                defeats[i] += 1

for i in range(10):
    points[i] = triumphs[i]*3 + ties[i]

for i in range(10):
    print(f"Equipo {i+1}: Triunfos={triumphs[i]}, Empates={ties[i]}, Derrotas={defeats[i]}, Diferencia de Goles={goals_scored[i]-goals_received[i]}, Puntos={points[i]}")

#Ejercicio 9
rows = 4
columns = 4
numbers = list(range(1, (rows*columns)//2 + 1))
cards = numbers + numbers
random.shuffle(cards)
board = [[0]*columns for _ in range(rows)]
for i in range(rows):
    for j in range(columns):
        board[i][j] = cards.pop()

# Print the current board
def print_board(board, selected):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) in selected or board[i][j] < 0:
                print(f'{board[i][j]:2}', end=' ')
            else:
                print('X ', end=' ')
        print()

# Check if the game is over
def game_over(board):
    for row in board:
        for card in row:
            if card > 0:
                return False
    return True

selected = []
attempts = 0

while not game_over(board):
    print_board(board, selected)

    # Get user selection
    row1 = int(input('Ingrese la fila de la primera carta: '))
    col1 = int(input('Ingrese la columna de la primera carta: '))

    row2 = int(input('Ingrese la fila de la segunda carta: '))
    col2 = int(input('Ingrese la columna de la segunda carta: '))

    if (row1, col1) == (row2, col2) or board[row1][col1] < 0 or board[row2][col2] < 0:
        print('Movimiento inválido. Inténtalo de nuevo.')
        continue

    # Reveal selected cards
    selected = [(row1, col1), (row2, col2)]
    print_board(board, selected)

    if board[row1][col1] == board[row2][col2]:
        print('Encontraste una pareja')
        board[row1][col1] = board[row2][col2] = -board[row1][col1]
    else:
        print('No son iguales. Intente de nuevo.')
        board[row1][col1] = board[row2][col2] = 0

    attempts += 1
    selected = []
print("¡Felicidades! Has encontrado todas las parejas.")

#Ejercicio 10
def get_main_diagonal(matrix):
    n = len(matrix)
    main_diagonal = [matrix[i][i] for i in range(n)]
    return main_diagonal

def get_reverse_diagonal(matrix):
    n = len(matrix)
    reverse_diagonal = [matrix[i][n-i-1] for i in range(n)]
    return reverse_diagonal

matrix = [1,2,3],[4,5,6],[7,8,9]

main_diagonal = get_main_diagonal(matrix)
reverse_digonal = get_reverse_diagonal(matrix)

print(f"Diagonal principal: {main_diagonal}")
print(f"Diagonal inversa: {reverse_digonal}")

#Ejercicio 11
foreign_exchange = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
badge = input("Ingrese el nombre de una divisa [Euro/Dollar/Yen]: ")

if badge in foreign_exchange:
    simbol = foreign_exchange[badge]
    print(f"El símbolo de {badge} es {simbol}")
else:
    print("La divisa no se encontro en el diccionario")
    
#Ejercicio 12
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
direction = input("Ingrese su dirección: ")
telefone = input("Ingrese su número de teléfono: ")

information = {'Nombre': name, 'Edad': age, 'Dirección': direction, 'Teléfono': telefone}

print(f"{information['Nombre']} tiene {information['Edad']} años, vive en {information['Dirección']} y su número de teléfono es {information['Teléfono']}.")

#Ejercicio 13
fruit_price = {'Pera': 55, 'Banana': 40, 'Manzana': 45, 'Naranja': 30, 'Melón': 50}

fruit = input("Ingrese el nombre de una fruta: ")
kilos = float(input("Ingrese la cantidad de kilos que desea comprar: "))

if fruit in fruit_price:
    total_price = fruit_price[fruit] * kilos
    print(f"El precio de {kilos} kilos de {fruit} es ${total_price}.")
else:
    print("Fruta no encontrada en el diccionario de precios.")