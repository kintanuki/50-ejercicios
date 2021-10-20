def energia (m,v):
    energia=1/2*m*v**2
    return energia

m=float(input("Ingresa la masa del objeto:"))
v=float(input("Ingresa la velocidad:"))

print(f"la energí en Jouls de tu objeto es:",energia (m,v),"J")