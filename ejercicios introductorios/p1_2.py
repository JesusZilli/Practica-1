
# Escribe un programa que solicite al usuario una cantidad de segundos y muestre
# cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
# hora, 1 minuto y 1 segundo.

seg = int(input("ingrese una cantidad de segundos: "))
horas = int(seg / 60 / 60)
minutos = int(seg / 60 % 60)
segundos = int(seg - ((horas * 3600) + (minutos * 60)))

print(f'{seg} segundos son {horas} hora/s, {minutos} minuto/s y {segundos} segundo/s.')

