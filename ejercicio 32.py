año=int(input("Ingresa un años para saber si es bisiesto:"))

if año % 4 != 0: 
	print("El año que ingresaste no es bisiesto")
elif año % 4 == 0 and año % 100 != 0: 
	print("El año que ingresaste es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	print("El año que ingresaste no es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("El año que ingresaste es bisiesto")