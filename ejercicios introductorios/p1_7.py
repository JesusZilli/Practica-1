#  Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
# oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
# espacios. Las palabras cortas deben ser excluidas del resultado final.
import string

l = []
palabra = "x"
oracion = ""

while palabra != "0":
    palabra = input('ingrese una palabra (0 para terminar): ')
    if palabra == "0":
        continue

    list.append(l, palabra)

for word in l:
    if len(word) > 3:
        oracion += f'{word} '
oracion += "."

print(l)
print(oracion)
