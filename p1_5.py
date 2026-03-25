# Escribe un programa que simule una caja registradora: el usuario ingresa precios de
# productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
# acumulado. Nota: utilizá la sentencia break cuando haga falta.

x = int
tot = 0

while x != 0:
    x = int(input('ingrese un numero (ingrese 0 para terminar): '))
    if x == 0:
        break

    tot += x

print()
print(f'total: {tot}')