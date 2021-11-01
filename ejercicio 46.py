print("Ingresa dos números, uno de esos números debede ser mayor que el otro")
n=int(input())
m=int(input())
sum=0
if m>n:
    for i in range(n+1,m):
        sum=i+sum      
    print(f"La suma de los números: {sum}")
else:
    print("Error")
