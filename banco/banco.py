import os 
import datetime
import getpass
# Declaracion de datos del banco 
datosBanco = {
    "nombre" : "Aquí te Cagamos",
    "Rut":"78.965.890-K",
    "Direccion":"Sgto Aldea N° 1432, Antuco, Chile"
}

def limpiar_pantalla():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

hora = ""
fecha_actual = ""

def obtenerFecha():
    global hora, fecha_actual 
    hora_actual = datetime.datetime.now()
    hora = hora_actual.strftime('%H:%M:%S')
    fecha_actual = hora_actual.strftime('%d-%m-%Y')

# diccionario Idiomas 
español = {
    "Bienvenida" : "Bienvenido al Sistema del Banco",
    "Opciones" : "Seleccione Opción",
    "menu" : "1.- Consulta Saldo.\n2.- Transferir Saldo.\n3.- Girar Saldo.\n0.- Salir del Sistema.",
    "errorOpc": "Opción Incorrecta.",
    "selectOpc":"Ingrese Opción\n",
    "selectIdioma":"Opcion en Español",
    "consultaSaldo":"====== Consulta de Saldo ======",
    "transferirSaldo":"====== Transferir Saldo ======",
    "girarSaldo":"====== Girar Saldo ======",
    "tranferirMensaje": "Ingrese el Monto a Transferir: \n",
    "girarMensaje":"¿Cual es el monto que desea Girar?\n",
    "noNumero":"El valor ingresado no es número",
    "mensajeSaldo":"Tu Saldo Disponible es: ",
    "presionaContinuar":"Presione la tecla Enter para continuar...",
    "sinSaldo":"No tienes saldo suficiente...",
    "rutTransfer":"Ingrese Rut de Destinatario\n",
    "nombreTransfer":"Ingrese Nombre Destinatario\n",
    "notificaBancoTranfer":"Solo se permiten Transferencias al mismo Banco 'Aqui te Cagamos'."

}
ingles = {
    "Bienvenida" : "Welcome to Bank System",
    "Opciones" : "Select One Choice",
    "menu" : "1.- Balance Inquiry.\n2.- Transfer Balance.\n3.- Take out Balance.\n0.- Get out of the System.",
    "errorOpc": "Incorrect Choice.",
    "selectOpc":"Insert Choice\n",
    "selectIdioma":"Choice in English",
    "consultaSaldo":"====== Balance Inquiry ======",
    "transferirSaldo":"====== Transfer Balance ======",
    "girarSaldo":"====== Take out Balance ======",
    "tranferirMensaje": "Enter the Amount to Transfer: \n",
    "girarMensaje":"What is the amount you want to withdraw?\n",
    "noNumero":"The value entered is not a number",
    "mensajeSaldo":"Your balance is: ",
    "presionaContinuar": "Press Enter key to continue...",
    "sinSaldo":"You don't have enough balance...",
    "rutTransfer":"Enter Recipient ID\n",
    "nombreTransfer":"Enter Recipient Name\n",
    "notificaBancoTranfer":"Only Transfers are allowed to the same Bank 'Aqui te Cagamos'."

    
}
flayte = {
    "Bienvenida" : "Bienvenio Chuchatumaere",
    "Opciones" : "Elige una wea",
    "menu" : "1.- Cuanto que'a.\n2.- Manda plata.\n3.- Saca plata.\n0.- Virar de la wea.",
    "errorOpc": "Pao ql' te equivocaste.",
    "selectOpc":"Pone Alguna wea\n",
    "selectIdioma":"Estamos en Flayte",
    "consultaSaldo":"====== Cuanto Que'a ======",
    "transferirSaldo":"====== Manda Plata ======",
    "girarSaldo":"====== Saca Plata ======",
    "tranferirMensaje": "Cuanta plata va a mandar: \n",
    "girarMensaje":"Cuanta plata va a sacar?\n",
    "noNumero":"La wea que pusiste no es numero, pao ql",
    "mensajeSaldo":"Te que'an: ",
    "presionaContinuar": "Apreta Enter pa seguir ...",
    "sinSaldo":"No te queda wn...",
    "rutTransfer":"A que Rut va a tranferir\n",
    "nombreTransfer":"Nombre del weas\n",
    "notificaBancoTranfer":"Solo podi mandar plata al mismo Banco 'Aqui te Cagamos'."
    
}

idiomas = {
    "Español": español,
    "Ingles":ingles,
    "Flayte" : flayte
}
usuarios = {
    "18536396-1" : {
        "Rut":"18536396-1",
        "clave":"123",
        "nombre":"Franco Ovalle",
        "direccion":"B. Ohiggins #681, Antuco, Chile" },
    "18800898-4" : {
        "Rut":"18800898-4",
        "clave":"123",
        "nombre":"Prissila Lopez",
        "direccion":"Sgto. Aldea #23, Antuco, Chile" },
    "16399612-k" : {
        "Rut":"16399612-k",
        "clave":"123",
        "nombre":"Jenifer Ovalle",
        "direccion":"Las Camelias #182, Antuco, Chile" }

}

# REGISTRA MOVIMIENTOS EN BANCO
movimientos ={
    
}


# monto Inicial 1000uf pasar a $ CLP
# uf 03/04 37115
uf = 37115
saldoI = 1000 * uf
saldoM = saldoI
valor = 0 
def inicio_Sistema():
     # mensaje de inicio
     print("Banco ",datosBanco["nombre"])
     print("Direccion ",datosBanco["Direccion"])
user = ''

def inicio(i):
    if(i <= 3):
        limpiar_pantalla()
        inicio_Sistema()
        global user
        usuario = input("Ingrese Usuario\n")
        clave = getpass.getpass("Clave: \n")
        
        #clave = input("Ingrese Clave\n")
       
        if usuario in usuarios and usuarios[usuario]["clave"] == clave:
            user = usuario
            obtenerFecha()
            movimientos["inicio"] = f"Inicio Sistema... {usuarios[usuario]['nombre']}, Fecha: {fecha_actual} , Hora: {hora}"
            sistema()
        else: 
            print('Error Login')
            inicio(i + 1)
        
    else:
        print('demasiados errores')
        exit()
     

def consulta_saldo(leng):
    global saldoM
    if (saldoM>100):
        saldoM = saldoM - 100
        return True
    else:
        print(idiomas[leng]["sinSaldo"])
        return False

def transferir_saldo(saldo,leng):
     global saldoM
     try:
        saldo = int(saldo)
        if(saldoM > saldo + 200):
            saldoM = saldoM - saldo - 200
            return True
        else:
            print(idiomas[leng]["sinSaldo"])
            return False
     except:
        print(idiomas[leng]["noNumero"])

def giro_saldo(saldo,leng):
     global saldoM

     try:
        saldo = int(saldo)
        if(saldoM > saldo + 300):
            saldoM = saldoM - saldo - 300
            return True
        else:
            print(idiomas[leng]["sinSaldo"])
            return False
     except:
        print(idiomas[leng]["noNumero"])

def opciones(leng):
    while True:
                    limpiar_pantalla()
                    print(idiomas[leng]["selectIdioma"])
                    print(idiomas[leng]["Opciones"])
                    print(idiomas[leng]["menu"])
                    opcV1 = input(idiomas[leng]["selectOpc"])
                    try:
                        opcV1 = int(opcV1)
                    except ValueError:
                        print(idiomas[leng]["errorOpc"])
                        continue
                    match opcV1:
                         
                        case 1: # Consulta Saldo
                            limpiar_pantalla()
                            print(idiomas[leng]["Bienvenida"])
                            print(idiomas[leng]["consultaSaldo"])
                            # Consulta Saldo - 100
                            try:
                                if(consulta_saldo(leng)):
                                    saldoP = f'{saldoM:,}'
                                    numero_con_puntos = saldoP.replace(',', 'X').replace('.', ',').replace('X', '.')  
                                    print(idiomas[leng]["mensajeSaldo"],numero_con_puntos)
                                    obtenerFecha()
                                    movimientos[f"Consulta Saldo - {fecha_actual} : {hora}"]=f" Usuario: {usuarios[user]["nombre"]},  Comisión Consulta: $ 100.- Fecha:{fecha_actual} , Hora:{hora}"
                                    input(idiomas[leng]["presionaContinuar"])
                                else:
                                    input(idiomas[leng]["presionaContinuar"])
                            except:
                                input(idiomas[leng]["presionaContinuar"])

                        case 2: # Transferir Saldo
                            limpiar_pantalla()
                            print(idiomas[leng]["Bienvenida"])
                            print(idiomas[leng]["transferirSaldo"])
                            # Transferir Saldo
                            saldoP = f'{saldoM:,}'
                            numero_con_puntos_a = saldoP.replace(',', 'X').replace('.', ',').replace('X', '.')  
                            print(idiomas[leng]["mensajeSaldo"],numero_con_puntos_a)
                            # Solicita Datos de transferencia
                            print(idiomas[leng]["notificaBancoTranfer"])
                            valor = input(idiomas[leng]["tranferirMensaje"])
                            if(transferir_saldo(valor,leng)):
                                intent = 0
                                while intent < 3:
                                    rutT = input(idiomas[leng]["rutTransfer"])
                                    nombre = input(idiomas[leng]["nombreTransfer"])
                                    if(rutT != "" and nombre != ""):
                                        saldoP = f'{saldoM:,}'
                                        numero_con_puntos = saldoP.replace(',', 'X').replace('.', ',').replace('X', '.')  
                                        print(idiomas[leng]["mensajeSaldo"],numero_con_puntos)
                                        input(idiomas[leng]["presionaContinuar"])
                                        obtenerFecha()
                                        movimientos[f"Transferencias de Saldo - {fecha_actual} : {hora}"]=f" Usuario: {usuarios[user]["nombre"]} \n\t\tSaldo Anterior: $ {numero_con_puntos_a}.- \n\t\tComisión Consulta: $ 200.- \n\t\tRut Destinatario: {rutT}. \n\t\tNombre Destinatario: {nombre}. \n\t\tSaldo Restante: $ {numero_con_puntos}.-  \n\t\tFecha:{fecha_actual} , Hora:{hora}"
                                    
                                        intent += 3
                                    else:
                                        intent += 1
                                        input(idiomas[leng]["presionaContinuar"])
                                
                            else:
                                input(idiomas[leng]["presionaContinuar"])
                        case 3: # Sacar Saldo
                            limpiar_pantalla()
                            print(idiomas[leng]["Bienvenida"])
                            print(idiomas[leng]["girarSaldo"])
                            saldoP = f'{saldoM:,}'
                            numero_con_puntos_a = saldoP.replace(',', 'X').replace('.', ',').replace('X', '.')  
                            print(idiomas[leng]["mensajeSaldo"],numero_con_puntos_a)
                            # girar Saldo
                            valor = input(idiomas[leng]["girarMensaje"]) 
                            try:
                                valor = int(valor)
                                if(giro_saldo(valor,leng)):
                                    valor_c = f'{valor:,}'
                                    saldoP = f'{saldoM:,}'
                                    numero_con_puntos = saldoP.replace(',', 'X').replace('.', ',').replace('X', '.')  
                                    valor_puntos = valor_c.replace(',', 'X').replace('.', ',').replace('X', '.')
                                    print(idiomas[leng]["mensajeSaldo"],numero_con_puntos)
                                    obtenerFecha()
                                    movimientos[f"Giro Saldo - {fecha_actual} : {hora}"]=f" Usuario: {usuarios[user]["nombre"]} \n\t\tSaldo Anterior: $ {numero_con_puntos_a}.- \n\t\tMonto Girado: $ {valor_puntos}.- \n\t\tComisión Giro: $ 300.- \n\t\tSaldo Restante: $ {numero_con_puntos}.- \n\t\tFecha:{fecha_actual} , Hora:{hora}"
                                    input(idiomas[leng]["presionaContinuar"])
                                else:
                                    input(idiomas[leng]["presionaContinuar"])
                            except:
                                input(idiomas[leng]["presionaContinuar"])
                           
                           

                        case 0: 
                            break

# funcion opc
def sistema():
    while True:
        limpiar_pantalla()
        inicio_Sistema()
        print("===== ***** =====")
        print("Selecciona Idioma | Select Lenguage | Elige ql")
        print("1.- Español.")
        print("2.- English.")
        print("3.- Flayte.")
        print("0.- Salir.")
        opc = input("Ingrese Opción | Insert your Choice | Cual queri? \n")
        try:
            opc = int(opc)
        except ValueError:
            print("Favor Ingresar Opción Correcta | Please insert correct Choice | Mete Bien el deo ql")
            continue
        match opc:
            case 1:
                ###### Seleccion Menú Español
                leng = "Español" 
                opciones(leng)

            case 2:
                ###### Seleccion Menú Ingles
                leng = "Ingles" 
                opciones(leng)
            case 3:
                ###### Seleccion Menú Flyte
                leng = "Flayte" 
                opciones(leng)
            case 0:
                limpiar_pantalla()
                obtenerFecha()
                saldoP = f'{saldoM:,}'
                numero_con_puntos = saldoP.replace(',', 'X').replace('.', ',').replace('X', '.')  
                movimientos["Saldo Final: "] = f"$ {numero_con_puntos}.-\n "
                movimientos["Salida"]=f"Salida del Sistema... {usuarios[user]["nombre"]}, Fecha:{fecha_actual} , Hora:{hora}"
                print("****************************************************")
                print("****************************************************\n")
                print("Sistema Banco : ***** Controles de Movimientos *****")
                for clave, valor in movimientos.items():
                    print(f"- {clave}: {valor}\n")
                print("\n****************************************************")
                print("****************************************************")
                print("Adios | Bye | Chao Feo Ql\n")
                exit()
    
# Ingreso al sistema 
inicio(1)

# Opcion cliente y monto dinamico
