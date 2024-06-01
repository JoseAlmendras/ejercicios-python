num = int(input("Ingrese un numero entero positivo de hasta tres cifras: "))
if num <= 0 or num > 999:
    print("Error: El numero deve ser un entero positivo de hasta tres cifras.")
else:
    if num < 10:
        print("El numero tiene 1 cifra.")
    elif num < 100:
        print("El numero tiene 2 cifras.")
    else:
        print("El numero tiene 3 cifras.")
        