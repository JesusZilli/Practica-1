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

def keep_playing(x):
    """Devuelve boolean según si el usuario ingresa "s"/"S" = True o "n"/"N" = False
        luego según eso se decide si el programa itera la partida o no.
    """
    while x != "s" and x != "n" and x != "S" and x != "N":
        x = input(f'S/N: ')
    if x == "S" or x == "N":
        x = x.lower()
    match x:
        case "s":
            p = True
        case "n":
            p = False
    return p


def get_word(key):
    """Elige una palabra aleatoria según la categoría seleccionada desde el diccionario de listas y luego la elimina.
        Si no hay más palabras en la categoría, devuelve ".".
    """
    match key:
        case 1:
            cat = "Lenguajes de Programación"
        case 2:
            cat = "Estructuras de Datos"
        case 3:
            cat = "Generales de Programación"

    if len(categ[cat]) == 0:
        return "."

    w = random.sample(list(categ[cat]), 1)[0]
    categ[cat].remove(w)
    return w


categ = {
    "Lenguajes de Programación": ["python", "c", "java", "javascript", "html"],
    "Estructuras de Datos": ["variable", "string", "cadena", "lista", "arreglo"],
    "Generales de Programación": ["programa", "bucle", "archivo", "funcion"],
}

play = True
points = 0

print("¡Bienvenido al Ahorcado!")
print()

while play:
    guessed = []
    attempts = 6
    word = " "

    print(f'Elija una de las siguientes categorias, ingresando el número correspondiente:\n'
              f'1.Lenguajes de Programación\n'
              f'2.Estructuras de Datos\n'
              f'3.Generales de Programación\n'
              f''
              )
    while word == " ":
        # Elegir una palabra según la categoria que ingrese el usuario
        k = int(input())
        if 4 > k > 0:
            word = get_word(k)
            while word == ".":
                print(f"No hay más palabras de esa categoría. ")
                word = get_word(int(input(f'Intente nuevamente: ')))
        else:
            print(f'\nNo existe la categoría, intentelo de nuevo: ')

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el usuario ya adivinó la palabra completa, sumar puntos
        # Verificar si el usuario quiere seguir jugando
        if "_" not in progress:
            points += 6
            print("¡Ganaste!")
            play = keep_playing(input(f'Querés seguir jugando? S/N: '))
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        # Chequear si el string ingresado es válido y si está o no dentro de la palabra
        # Reducir el número de intentos y restar puntos cuando corresponda
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
                points -= 1
                attempts -= 1
                print("Esa letra no está en la palabra.")
        else:
            print("Entrada no válida.")

        print()

    else:
        points = 0
        print(f"¡Perdiste! La palabra era: {word}")
        play = keep_playing(input(f'Querés seguir jugando? S/N: '))

print()
print(f'Puntaje final: {points}.')