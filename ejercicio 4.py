def suma(n1,n2):
    suma=n1+n2
    return suma


def resta(n1,n2):
    resta=n1-n2
    return resta

def division(n1,n2):
    division=n1/n2
    return division

def modulo(n1,n2):
    modulo=n1%n2
    return modulo

nm1=int(input("ingresa el primer número:"))
nm2=int(input("Ingresa el ultimo número:"))

print(f"La suma de {nm1} y {nm2} es de=", suma(n1,n2))

print(f"La resta de {nm1} y {nm2} es de=", resta(n1,n2))
print(f"La division de {nm1} y {nm2} es de=", division(n1,n2))
print(f"La modulo de {nm1} y {nm2} es de=", modulo(n1,n2))
print("gracias por participar <3")


