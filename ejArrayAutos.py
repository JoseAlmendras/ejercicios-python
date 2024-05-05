autos = ["kia", "hyundai", "chevrolet", "fiat", "dodge", "toyota", "lamborghini"]
# solicita al usuario ingrese la marca a buscar y luego imprimela 

#para solicitar datos se utiliza el input
print(autos)
respuesta = input("Ingrese una marca\n")

for auto in autos:
    if respuesta == auto:
        print(f"el resultado es: {auto}")

