venta=int(input("Ingresa el valor de tu venta:"))
IVA=int(venta*0.19)
if IVA>=150000:
    IVA=int(venta*0.05)
    total=int(venta+IVA)
    print("El IVA de tu producto es:",IVA,"y el valor total de tu compra es:",total)
else:
    total=int(venta+IVA)
    print("El IVA de tu producto es:",IVA,"y el valor total de tu producto es:",total)