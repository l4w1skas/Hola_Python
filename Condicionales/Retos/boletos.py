```Escribe un programa que calcule el precio en la entrada de un cine dependiendo de la edad:
      El precio normal de la entrada es de 10 Euros.
      Si el cliente tiene una edad de 60 o más años, solo pagará 2 Euros.
      Si el cliente tiene una edad de 12 o menos años, solo pagará 4 Euros.```

edad = int(input("Introduce la edad del cliente: "))

if edad >= 60:
    print("2")
elif edad <= 12:
     print("4")
else:
    print("10")

print("tienes el descuento")
