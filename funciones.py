# Funciones en python 
# las funciones se inician con def
persona = {
    "Jose":{
    "nombre": "Jose",
    "apellido": "Almendras",
    "pais": "Chile",
    "correo":"josealemdras@gmail.com"
    },
    "Franco":{
    "nombre": "Franco",
    "apellido": "Ovalle",
    "pais": "Chile",
    "correo":"franco.n.ovalle@gmail.com"
    }
}

def datos(data):
    # Para obtener y mostrar solo el nombre
    #genera correo a las 10 Pm
    for nombre in data:
        contenido = "buenos noches "+ data[nombre]["nombre"] +" "+data[nombre]["apellido"]+ " este es un correo de recordatorio "
        print(f"enviar correo a {data[nombre]["correo"]}")
        print(contenido)

datos(persona)

# def datosV2(data):
#     # Para buscar y mostrar los datos (clave y valor)
#     for clave, valor in data.items():
#         print(f"{clave}: {valor}")

# datosV2(persona)
