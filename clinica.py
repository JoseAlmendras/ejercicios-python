#Ejercicio Clinica a Python 3.9
# Entero = int => 12
# Cadena = string => "texto"
# decimal = float => 12,2
# boleano = boolean => true o false
# print( = print
# Leer = input
import os 
valorRaI = 8500
valorRm = 180000
valorRmF = ( valorRm - ( valorRm * 0.39 ))
valorRmI = ( valorRm - ( valorRm * 0.70 ))
valorEsF = 95500
valorEs = ( valorEsF * 100 / 61)
valorEsI = ( valorEs * 0.30 )
valorRaI = 8500
valorRa = ( 8500 * 100 / 30 )
valorRaF = ( valorRa - ( valorRa * 0.39 ))
opcion = 0 # segun opcion hacer // match case // if "anidado"
dr = ""
examen = ""
valor = 0
# leer nombre 
if os.name != 'nt':
    os.system("clear")
else:
    os.system('cls')

nombre = input(" Nombre del paciente: \n")
rut = input("Rut del paciente: \n")
diagnostico = input(" Diagnostico del paciente: \n")
if os.name != 'nt':
    os.system("clear")
else:
    os.system('cls')

# Comentarios Establece un Menú
print(" Examen a realizar")
# Opciones de menú
print("1).- Resonancia Magnetica. \n 2).- Escaner. \n 3).- Radiografia. \n 0).- Salir.")
# solicita que ingrese una opción 
opcion = input(" Ingrece una opcion \n")
# opcion 1.- Resonancia
if opcion == "1":
    # agrega lo de la opcion 1

    if os.name != 'nt':
        os.system("clear")
    else:
        os.system('cls')

    print(" Resonancia magnetica ")
    print(" 1).- Particular. \n 2).- Con fonasa. \n 3).- Con isapre. \n" )
    pago = input(" Ingrece opcion de pago. \n")
    # comparacion de pago
    if pago == "1":
        examen ="Resonancia magnetica - Particular"
        dr = "Manuel Turiso"
        valor = valorRm
    if pago == "2":
        examen = "Resonancia magnetica - fonasa"
        dr = "Jorge Patiño"
        valor = valorRmF
    if pago == "3":
        examen ="Resonancia magnetica - isapre"
        dr = "Luis Quiroga"
        valor = valorRmI

# opcion 2.- Escaner
if opcion == "2":
    if os.name != 'nt':
        os.system("clear")
    else:
        os.system('cls')

    print(" Escaner ")
    print("1).- Particular \n 2).- Con fonasa \n 3).- Con isapre \n")
    pago = int(input(" Ingrece opcion de pago. \n"))
    if pago == 1:
        examen = "Escaner - particular"
        dr = "Jorge Nitales"
        valor = valorEs 
    if pago == 2:
        examen = "Escaner - fonasa"
        dr = " Alma Marcela Goso"
        valor = valorEsF
    if pago == 3:
        examen = "Escaner _ isapre"
        dr = " Duke Melano"
        valor = valorEsI
if opcion == "3":
    print(" Radiografia")
    print("1).- Particular \n 2).- Fonasa \n 3).- Isapre \n")
    # ciclo true 
    pago = int(input(" Ingrece opcion de pago. \n"))
    # solicita pago 
    if pago == 1:
        examen = "Radiografia - Particular"
        dr = "Jorge Lardes"
        valor = valorRa
    if pago == 2:
        examen = "Radiografia - fonasa"
        dr = "Pedro Pascal"
        valor = valorRaF
    if pago == 3:      
        examen =" Radiografia - isapre"
        dr = "Josefa Ovalle" 
        valor = valorRaI
elif opcion == "0":
    print("Saliendo del Sistema")
    exit()

#limpiar pantalla 
if os.name != 'nt':
    os.system("clear")
else:
    os.system('cls')

print( "====================================")
print( "Clinica IGN")
print( "Rut clinica: 43.456.323-4")
print( "Calle Colon Nº143, Los Angeles, Biobio, Chile")
print( f"Nombre del doctor: {dr}")
print( "====================================")
print( "====================================")
print( "Datos Paciente")
print( "Nombre Paciente: " + nombre)
print( "Rut del Paciente: " + rut)
print( " Diagnostico del Paciente: " + diagnostico)
print( "Examen del Paciente: " + examen)
print( f"Valor del Examen: {valor}")
print( "====================================")
	


## valores logicos y comparaciones 
# distinto !=
# asignacion =
# comparacion ==
# comparacion exacta ===
# o || 
# y &&
# 
