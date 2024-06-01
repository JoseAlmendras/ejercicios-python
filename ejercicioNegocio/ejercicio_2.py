nota1 = float(input("Ingrece la primera nota: "))
nota2 = float(input("Ingrece la segunda nota: "))
nota3 = float(input("Ingrece la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 4:
    print(" Aprobado")
else:
    print("Reprobado")
print (promedio)