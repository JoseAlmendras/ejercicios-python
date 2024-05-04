frutas = ["Pera","Manzana","Naranja","Plátano"]
contador = 0

for fruta in frutas:
    if fruta == "Naranja":
        print("¡Encontrar la", fruta, "!")
        break

    contador += 1
    print("Interacion", contador)
    print(fruta)

print("Programa terminado.")

