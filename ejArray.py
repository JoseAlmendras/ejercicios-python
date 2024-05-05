frutas = ["Pera","Manzana","Naranja","Plátano"] # Array frutas = lista de frutas
contador = 0

for fruta in frutas: #Recorre Frutas y asigna a fruta cada valor de la lista 
    if fruta == "Naranja":
        print("¡Encontrar la", fruta, "!")
        break

    contador += 1
    print("Interacion", contador)
    print(fruta)

print("Programa terminado.")

