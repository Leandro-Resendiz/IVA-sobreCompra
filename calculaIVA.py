""" Programa que Calcule IVA de una compra, siendo el IVA el 16% sobre el valor total de una compra """

def calcularIVA (total):
    IVA = total * 0.16
    return IVA 

precioCompra = float(input("Ingresa el total de la compra: "))

IVA = calcularIVA(precioCompra)

print("El total de la compra sin IVA es de: $", precioCompra)
print("El total a pagar con IVA incluido es de: $", (precioCompra+IVA))
