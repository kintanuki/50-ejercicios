sesion={"usuario":"carlos","contraseña":"1234"}

usuario=input("Ingresa el nombre de usuario:")
contraseña=input("Ingresa tu contraseña:")

if sesion.get("usuario")==usuario and sesion.get  ("contraseña")==contraseña:
    print("La sesión inicio correctamete")
else:
    print("Error al iniciar sesión...verifica el usuario o la contraseña")