distancia=int(input("Ingrese la distancia que va a recorrer su vuelo:"))
dias=int(input("Ingrese cuantos días va a estar en su destino:"))

valor_precio=distancia*5000

if distancia==20:
    precio=100000
    print("Tu pasaje tendra un valor de $",precio)
        
if distancia!=20:
    print(f"Tu pasaje tendra un valor de ${valor_precio}")
    
 
if distancia>1000 and dias>7:
    descuento_precio=valor_precio*0.15
    print(f"Tu pasaje tendra un valor de ${descuento_precio}")
        