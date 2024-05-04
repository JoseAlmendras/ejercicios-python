# Definir valor de pi (aproximación)
pi= 3.14159

# Solicitar el diametro y la altura al usuario
diametro = float(input("Introduce el diametro del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

#Calcula el radio (r = diametro / 2)
radio = diametro / 2

#Calcular el volumen (v = pi * r^2 * altura)
volumen = pi * radio**2 * altura

#Imprimir el resultado
print("El volumen del cilindro es:", volumen, "unidades cúbicas.")