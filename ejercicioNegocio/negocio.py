import juegos
import os

os.system('cls')

dicJuego = juegos._juegos
""" 

el codigo extrae datos del diccionario creado en el archivo anterior, en este lo que hacemos es a traves de algoritmos extraer los
los datos que nesesitemos y que nos aparescan solo los que queramos en pantalla.

"""
#tipo = "Pc"

#dicPc = dicJuego[tipo]
for tipo in dicJuego:
    print(f"==== Juegos de {tipo} =====")
    for game in dicJuego[tipo].keys():
        print(f" Nombre: {dicJuego[tipo][game]["nombre"]} \n Valor: $ {dicJuego[tipo][game]["valor"]} \n---------------")
    print( "\t=*/*=")
print("***************\n ")
