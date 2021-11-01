suma = 0
print("Ingresa 10 números....")
for i in range(10):
    numero = int(input())
    suma = suma+numero
print("La suma de tus números es = {}\ny el promedio de tu números es = {:.2f}".format(suma, suma/10))