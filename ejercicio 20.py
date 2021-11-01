numero = int(input("Ingresa un número para hallarle la inversa: "))
num= 0
while numero > 0:
    residuo= numero % 10
    num = (num * 10) + residuo
    numero //= 10
print('El inverso de tu número ingresado es: ', num)