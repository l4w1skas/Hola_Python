```Determine si la contraseña cumple con los requisitos para iniciar sesión, para ello deberá determinar que tenga un tamaño mínimo de 8 caracteres
  y que sea igual a la que se tiene almacenada```

username = input('Username:')
password = input('Password:')
if username == 'admin':
    if len(password) >= 8:
        if password == 'admin123':
            print('Welcome', username)
        else:
            print('Wrong Password!')
    else:
        print('Password is too short')
else:
    print('Wrong Username')
