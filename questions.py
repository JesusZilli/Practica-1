# El juego tiene un bug. Si el usuario ingresa más de una letra, un número o
# cualquier otro carácter inválido,
# el programa se comporta de manera inesperada. Modificalo para que en ese caso
# muestre el mensaje
# "Entrada no válida" y continúe el juego en la siguiente iteración.

# Modificá el juego para que al final de la partida se muestre el puntaje
# del jugador. El puntaje se calcula de la siguiente forma: cada letra
# incorrecta resta 1 punto, adivinar la palabra completa suma 6 puntos,
# y perder deja el puntaje en 0.

# Modificá el juego para que las palabras estén agrupadas por categoría.
# Al inicio de cada partida, mostrar las categorías disponibles y permitir
# que el usuario elija una. Ayuda: utilizá un diccionario donde las claves
# sean los nombres de las categorías y los valores sean listas de palabras.

# Modificá el juego para que, al jugar varias rondas seguidas, no se
# repita la misma palabra. Investigá la función random.sample() .

import random
import string

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

points = 0
word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        points += 6
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    if letter.isalpha() and len(letter) == 1:
        if letter.isupper():
            letter = letter.lower()
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            points += -1
            attempts -= 1
            print("Esa letra no está en la palabra.")
    else:
        print("Entrada no válida.")

    print()

else:
    points = 0
    print(f"¡Perdiste! La palabra era: {word}")

print()
print(f'Puntaje final: {points}.')