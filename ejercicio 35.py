numero={0:"cero",1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",10:"diez"}
num=int(input("Ingresa un número entre 0 y 10:"))
nom=numero.get(num)
print("{}--->{}".format(num,nom))