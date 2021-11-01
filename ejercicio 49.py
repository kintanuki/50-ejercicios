n = int(input("Ingresa la cantidad de números que quiera ingresar: "))
par = 0
sumpar = 0
impar = 0
sumimpar = 0
for i in range(n):
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        par = par+1
        sumpar = sumpar+numero
    else:
        impar = impar+1
        sumimpar = sumimpar+numero

print("La el promedio de tus números pares es de = ", sumpar/par)
print("La el promedio de tus números impares es de = ", sumimpar/impar)