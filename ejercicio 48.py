suma=0
n=int(input("Ingresa la cantidad de números que quieras digitar para calcularles su suma y promedio: "))
print("Ingresa los números....")
for i in range(n):
    numero=int(input())
    suma=suma+numero
print("La suma de los números = {}\nEl promedio de los números es = {:.2f}".format(suma,suma/n))