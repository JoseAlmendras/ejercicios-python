numero_de_piezas = int(input("Ingrese la cantidad de piezas a procesar: "))
piezas_aptas = 0
for i in range(numero_de_piezas):
    longitud = float(input(f"Ingrese la longitud de la pieza {i + 1}: "))
    if 1.20 <= longitud <= 1.30:
        piezas_aptas += 1

print("La cantidad de piezas aptas en el lote es :", piezas_aptas)
