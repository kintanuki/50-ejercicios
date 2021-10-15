def area (n1,n2):
    area=(n1*n2)/2
    return area

def areairregular (l1,l2,l3,l4,l5,l6,h1,h2,h3,h4,h5,h6):
    areairregular=(l1*h1)/2 + (l2*h2)/2 + (l3*h3)/2 + (l4*h4)/2 + (l5*h5)/2 + (l6*h6)/2 
    return areairregular


opcion= (input( """De que tipo es tu hexagono?:
1-regular
2-irregular
"""))
if opcion=="1":
    n1=float(input("ingresa el perimetro para hallar el área del hexagono:"))
    n2=float(input("ingresa el apotema para hallar el área del hexagono:"))

    print("el área de tu hexagono es de:", area(n1,n2))

elif opcion=="2":
    l1=float(input("ingresa el lado de tu primer triángulo:"))
    l2=float(input("ingresa el lado de tu segundo triángulo:"))
    l3=float(input("ingresa el lado de tu tercer triángulo:"))
    l4=float(input("ingresa el lado de tu cuarto triángulo:"))
    l5=float(input("ingresa el lado de tu quinto triángulo:"))
    l6=float(input("ingresa el lado de tu sexto triángulo:"))
    h1=float(input("ingresa la altura de tu primer triándulo:"))
    h2=float(input("ingresa la altura de tu primer triándulo:"))
    h3=float(input("ingresa la altura de tu primer triándulo:"))
    h4=float(input("ingresa la altura de tu primer triándulo:"))
    h5=float(input("ingresa la altura de tu primer triándulo:"))
    h6=float(input("ingresa la altura de tu primer triándulo:"))

    print("el área de tu hexagono irregular es", areairregular (l1,l2,l3,l4,l5,l6,h1,h2,h3,h4,h5,h6))
