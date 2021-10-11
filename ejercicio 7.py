def area (n1):
    area=3.14*n1**2
    return area
def perimetro (n1):
    perimetro=2*3.14*n1
    return perimetro

n1=float(input("ingresa el radio de tu circulo para hallar el area, y el perimetro:"))

print("el área de tu circulo es de:", area(n1))
print("el perimetro de tu circulo es de:", perimetro(n1))