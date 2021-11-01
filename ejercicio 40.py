print("Ingresa tres números: ")
lista = []
for i in range(3):
    numero=int(input())
    lista.append(numero)
if len(lista) != len(set(lista)):  
    print("Tienes al menos dos números iguales") 
else:
    print("Todos los números que ingresaste son diferentes")

