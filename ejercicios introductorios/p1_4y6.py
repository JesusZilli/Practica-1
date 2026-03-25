# Crea un programa que dado un número N ingresado por el usuario, imprima los
# números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
# donde haga falta.

#  Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
# finalizar.

# Sentencias comentadas son parte del ejercicio 4

l = []
lMult5 = []
x = int(input('ingrese un numero: '))

for i in range(1,x+1):
    if i % 5 == 0:
    #    continue
        list.append(lMult5, i)
#    print(i)
    else:
        list.append(l, i)

print("Lista de multiplos de 5: ")
print(lMult5)
print()
print("lista de restantes: ")
print(l)