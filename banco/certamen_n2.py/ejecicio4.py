
multiplos_de_3 = 0
multiplos_de_5 = 0

for i in range(10):
    numero = int(input("Ingresa un número entero: "))
    
    if numero % 3 == 0 and numero % 5 == 0:
        multiplos_de_3 += 1
        multiplos_de_5 += 1
    elif numero % 3 == 0:
        multiplos_de_3 += 1
    elif numero % 5 == 0:
        multiplos_de_5 += 1

print("Cantidad de múltiplos de 3:", multiplos_de_3)
print("Cantidad de múltiplos de 5:", multiplos_de_5)