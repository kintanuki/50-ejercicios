sem={1:"Lunes",2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sábado",7:"Domingo"}
numero=int(input("Ingresa el número del día de la semana que quieres encontrar: "))
dia=sem.get(numero)
print("{} ---> {}".format(numero,dia))