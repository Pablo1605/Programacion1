import random

def find_word(random_word,board,attempts,letter):
    if letter in random_word: #Aca en caso de que la letra sea correcta se intercambia el guion bajo por la letra ingresada y se manda el mensaje correspondiente
        print("Adivinaste una letra correctamente")
        for i in range(len(random_word)):
            if random_word[i] == letter:
                board[i] = letter
    else: #En caso de que la letra ingresada sea incorrecta se le resta un numero al intento y se manda el mensaje correspondiente
        attempts -= 1
        print(f"Letra incorrecta, te quedan {attempts} intentos")
    return attempts


words = ['programacion','python','computacion','java','tecnologia','utn','mendoza','argentina','pablo','laboratorio']
random_word = random.choice(words) #Aca se selecciona una palabra aleatoria de la lista de palabras
board = ["_" for _ in random_word]
attempts = 6

while attempts > 0:
    if all(letter in random_word for letter in board):
        break
    print(" ".join(board))
    letter = input("Ingresa una letra: ")
    letter = letter.lower()
    
    if len(letter) != 1 or not letter.isalpha(): #Validacion de datos
        print("Ingresa una sola letra y que sea valida")
        continue
    
    attempts = find_word(random_word,board,attempts,letter) #Aca se pasa a la funcion en donde se comprueba si la letra ingresada es correcta o no

if "_" not in board: 
    print(f"¡¡¡Felicidades!!! adivinaste la palabra '{random_word}'") #Mensaje por si el usuario encuentra la palabra
else:
    print(f"Mala suerte, no pudiste adivinar la palabra, la palabra era '{random_word}'") #Mensaje por si el usuario no encuentra la palabra