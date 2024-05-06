import juegos
import os

os.system('cls')

dicJuego = juegos._juegos

#tipo = "Pc"

#dicPc = dicJuego[tipo]
for tipo in dicJuego:
    print(f"==== Juegos de {tipo} =====")
    for game in dicJuego[tipo].keys():
        print(f" Nombre: {dicJuego[tipo][game]["nombre"]} \n Valor: $ {dicJuego[tipo][game]["valor"]} \n---------------")
    print( "\t=*/*=")
print("***************\n ")
