print("Ingrese dos números entre 0 y 5:")
num1=int(input())
num2=int(input())
if 0<num1<5 and 0<num2<5:
    print("{} y {} ----> Verdadero".format(num1,num2))
else:
    print("{} y {} ----> Falso".format(num1,num2))