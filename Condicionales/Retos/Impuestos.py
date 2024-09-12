```Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.```

age = int(input('How old are you?'))
money = int(input('How much money do you earn?'))

if age > 16 and money >= 1000:
  print('You must pay your taxes!')
else:
  print('You must not pay anything')
