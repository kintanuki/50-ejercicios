print("Ingresa un rango de números: ")
n=int(input())
m=int(input())
if m>n:
    for i in range(n+1,m):
        print(i)
else:
    print("Tus números no son validos")