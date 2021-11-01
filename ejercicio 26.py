print("iIngresa las 5 notas de estudiante para sacar su promedio")
n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())

notas=[n1*0.15,n2*0.20,n3*0.15,n4*0.30,n5*0.20]
promedio=sum(notas)
if promedio < 2.0:
    print("Lo siento ya no puede habilitar ")
    if promedio<=3.0:
        print("El estudiante reprobo, pero todavia tiene la opción de recuperar :D")
if 3.0>= promedio <4.5:
    print("Aprobaste :D")
else: 
    print("Felicidades,obtuviste un magnifico promedio :D")
    
    