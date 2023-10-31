'''BINGO!'''

import random

def generate_cardboard():
    cardboard = []
    while len(cardboard) < 25:
        num = int(input(f"Ingrese el {len(cardboard)+1}° número (1-75): "))
        if num < 1 or num > 75 or num in cardboard:
            print("Número inválido. Por favor ingrese un número único entre 1 y 75.")
        else:
            cardboard.append(num)
    return cardboard

def extract_ball():
    return random.randint(1, 75)

def print_cardboard(cardboard):
    for i in range(5):
        print(cardboard[i*5:i*5+5])

def check_line(cardboard):
    lines = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24],
            [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24],
            [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]
    for line in lines:
        if all(cardboard[i] == 'X' for i in line):
            return True
    return False

def play():
    print("¡Bienvenido al juego de Bingo!")
    cardboard = generate_cardboard()
    print_cardboard(cardboard)
    input("Presione Enter para comenzar el juego  ")
    complete_lines = False
    while not complete_lines:
        ball = extract_ball()
        print(f"\nBola extraída: {ball}")
        if ball in cardboard:
            cardboard[cardboard.index(ball)] = 'X'
            print_cardboard(cardboard)
            complete_lines = check_line(cardboard)
            if complete_lines:
                print("\n¡Felicidades! ¡Has completado una línea en tu cartón!")
        else:
            print("Este número no está en tu cartón.")
    return input("\n¿Quieres jugar de nuevo? (s/n): ").lower() == 's'

while play():
    pass