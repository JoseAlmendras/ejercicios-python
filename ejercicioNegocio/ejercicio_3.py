num1 = float(input("Ingrese la primera nota  "))
num2 = float(input("Infrese la segunda nota  "))
num3 = float(input("Ingrese la tercera nota: "))
mayor = num1
if num2 >mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
print("El mayor numero ingresado es:", mayor)
