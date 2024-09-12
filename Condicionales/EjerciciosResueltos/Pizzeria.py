```La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación:
  
      Ingredientes vegetarianos: Pimiento y tofu.
      Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

  Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes 
  disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
  por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.```

print('\tBienvenido a Bella Napoli \nTenemos opciones vegetarianas y no vegetarians ¿Qué opción prefiere?')
flavor = input('Seleccione el tipo de Pizza de su preferencia (Vegetariana o No Vegetariana):')

if flavor.lower() == 'vegetariana':
    print('Puedes escoger uno de los siguientes ingredientes \nPimiento \nTofu')
    ingredient =  input('Seleccione el ingrediente de su preferencia:')
    if ingredient.lower() == 'pimiento':
        print('Su orden es una pizza de queso Mozzarella y ', ingredient.lower())
    elif ingredient.lower() == 'tofu':
        print('La opción más sana del menú')
    else:
        print('Aun no logramos que la pizza sepa bien con eso!')
elif flavor.lower() == 'no vegetariana':
    print('Puedes escoger uno de los siguientes ingredientes \nPeperoni \nJamón \nSalmón')
    ingredient =  input('Seleccione el ingrediente de su preferencia:')
    if ingredient.lower() == 'peperoni':
        print('La pizza de ', ingredient.lower(),' es una excelente opción')
    elif ingredient.lower() == 'jamon':
        print('El jamón serrano va muy bien con el queso')
    elif ingredient.lower() == 'salmon':
        print('Una elección extravagante')
    else:
        print('Lo sentimos, eso no está disponible')
else: 
    print('Te recomendamos probar la pizza de peperoni')
