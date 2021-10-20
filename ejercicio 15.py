import math

punto1=input("Ingresa la primer coordenada de tu primer punto:")
punto2=input("Ingresa la segunda coordenada de tu segund punto:")

p1=punto1.split((","))
p2=punto2.split((","))

x1= eval(p1[0])
y1= eval(p1[1])
x2= eval(p2[0])
y2= eval(p2[1])

distacia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("La diatancia de tus puntos es: {:.2f}".format(distancia))