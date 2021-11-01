print("Ingresa tres números: ")
num1=int(input())
num2 = int(input())
num3 = int(input())

if num1<num2<num3:
    print("{},{},{} ----> Tu número está incrementando".format(num1,num2,num3))
elif num1>num2>num3:
    print("{},{},{} ----> Tu número está disminuyendo".format(num1, num2, num3))
else:
    print("{},{},{} ----> Tu número ni se incrementa ni se disminuye".format(num1, num2, num3))