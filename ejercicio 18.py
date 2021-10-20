segundos=int(input("Ingresa la cantidad de segundos:"))
horas=segundos//3600
sobrante1=segundos%3600
minutos=sobrante1//60
sobrante2=sobrante1%60

print(horas,"horas, ",minutos,"minutos, ",sobrante2,"segundos sofrantes.")