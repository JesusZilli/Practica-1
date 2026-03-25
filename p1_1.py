AACTUAL = 2026

anioN = int(input("ingrese su año de nacimiento: "))
edad = 18
anioX = anioN + edad

if anioX < AACTUAL:
    print(f'cumpliste {edad} en el año {anioX}. ')
else:
    print(f'vas a cumplir {edad} en el año {anioX}. ')

edad = 21
anioX = anioN + edad
if anioX < AACTUAL:
    print(f'cumpliste {edad} en el año {anioX}. ')
else:
    print(f'vas a cumplir {edad} en el año {anioX}. ')

edad = 100
anioX = anioN + edad
if anioX < AACTUAL:
    print(f'cumpliste {edad} en el año {anioX}. ')
else:
    print(f'vas a cumplir {edad} en el año {anioX}. ')

