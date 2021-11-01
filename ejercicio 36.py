cantidad=0
cond="si"
while cond=="si":
    numero = int(input("Ingresa un número menor a 100000: "))
    numero1 = numero
    if numero <= 100000:
        while numero != 0:
           residuo = numero % 10
           numero //= 10
           cantidad += 1
        print("{} tiene {} digitos".format(numero1, cantidad))
        break          
    else:
        print("El número no es permitido...¿quieres volver a intentarlo, si o no?: ")
        cond = input()  
