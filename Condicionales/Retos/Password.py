```Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas 
y minúsculas.```

contraseña = int(input("escribe una contraseña"))
contraseña1 = int(input("repita la contraseña"))
if contraseña == contraseña1:
    print("contraseña correcta")

else: 
    print("contraseña incorrecta")
