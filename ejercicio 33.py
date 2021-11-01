from math import sqrt
a=int(input("Ingresa el valor de la variable cuadraatica a="))
b=int(input("Ingresa el valor de la barieble b="))
c=int(input("Ingresa el valor independiente c="))
x1=0
x2=0
if ((b**2)-4*a*c)<0:
    print("Error, no ingresaste números complejos")
else:
    x1=(-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2=(-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("Tu solución es:")
    print("x1={:2f}".format(x1))
    print("x2={:.2f}".format(x2))