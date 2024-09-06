```Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.```


dividend = float(input("Dividend: "))
divisor = float(input("Divisor: "))
if divisor == 0:
    print("The divisor can't be 0")
else:
    print(dividend/divisor)
