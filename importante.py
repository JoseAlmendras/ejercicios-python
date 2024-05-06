# Aplicacion del Banco Usando 
# Python

#if 5 > 3:
 #   print('5 es Mayor a 3')

# Variables

x = 5
y = "Chanchito Feliz"
email = "franco.n.ovalle.m@gmail.com"
mi_var = "otro tipo de Variable"
camelCase = "tambien"
_oConGuion = "con guion antes"

MAY_CONST = "En mayusculas para declarar constantes idealmente"

# Definir multiples Variables 

a, b, c = "lala" , "lele", "lili"

# Concatenacion 

inicio = "Hola "
final = "Mundo"

#print(inicio + final)
print(f"{inicio} {final}")

#print(x, y)

# tipos de datos 

#string
palabra = "Palabra"
palabraV2 = 'Palabra V2'

# numeros 
entero = 34
float = 3.4 # numero con decimales
complejo = 1j # numeros Complejos 

# listas 
lista = [1,2,'hola',3,4]
# agregar a lista .append() al ultimo de la lista 
lista.append(5)

# Eliminar el ultimo elemeto de la lista 
lista.pop()

# Eliminar un elemento seleccionado 
lista.remove('hola') 

# Cambiar el orden de la lista al reves
lista.reverse()

# Ordenar lista 
lista.sort() # solo funciona cuando el tipo de datos es el mismo en la lista 

# Limpiar lista
#lista.clear()

# Copiar Lista 
listaV2 = lista.copy()

# Contar en lista 
contar_4 = listaV2.count(4)

# Contar todos los elementos en la lista 
contar_Todo = len(listaV2)

# acceder a elementos de un arreglo [lista]
# acceder al primer elemento
indice_0 = lista[0]

### tuplas (inmutables)
tupla_1 = ('hola', 'mundo','Chanchito') 
# a las tuplas se les puede aplicar el count y ademas el index 
# obtener el valor en la posicion 0 de la tupla 
tupla_1[0]
# buscar el indice de un elemento 
busca_mundo = tupla_1.index('mundo')
# para modificar una tupla se debe convertir en lista 
listaDeTupla = list(tupla_1)
# Ahora se puede modificar listaDeTupla 

### Rangos 
rango = range(6) # este va desde 0 a 6 

# Diccionarios 
diccionario = {
    "Nombre" : "Titi",
    "Raza" : "Gato",
    "Edad" : 5
}
# para acceder a los datos del diccionario 
# diccionario["Nombre"] ### asi obtendria el nombre 
# diccionario.get('nombre') ### de esta forma igual accederia al nombre 


# Cambiar valores del diccionario 
diccionario["Nombre"] = "Molly"

# calcular la longitud o cantidad de datos 
contar_datos_diccionario = len(diccionario)

# agregar valores al diccionario 
diccionario["Genero"] = "Hembra"

# eliminar una propiedad 
diccionario.pop('Genero')
diccionario.popitem() # elimina el ultimo valor agregado al diccionario
del diccionario['Nombre'] # elimina el valor seleccionado 

# generar copia de diccionario
copia_Dic = diccionario.copy()
copia_Dic_otro = dict(diccionario)

# Diccionario de un diccionario Forma 1 
Gatitos = {
    "Molly" : {
        "nombre" : "Molly",
        "edad" : 4
    },
    "Titi" : {
        "Nombre" : "Titi",
        "edad" : 3
    }
}

# Diccionario de un diccionario Forma 2
molly = {
        "nombre" : "Molly",
        "edad" : 4
    }
titi = {
        "Nombre" : "Titi",
        "edad" : 3
    }
GatitosV2 = {
    "Molly" : molly,
    "Titi" : titi
}

# Crear diccionario con dict 
perros = dict( nombre = "Bobby", edad = 5 , genero = "Macho" )

# limpiar diccionario 
diccionario.clear()

# booleano 
verdadero = True
falso = False

# Control de Flujo #### CONDICIONES
if  3 > 5:
    print("Correcto")
elif 2 == 3 : ### IMPORTANTE elif se puede encadenar todas las veces q sea necesario 
    print('No')
else : 
    print("Incorrecto")
# == , != , < , > , <= , >=  
# Operadores Logicos 
# | , &, and , or

# if corto
if 4 < 5 : print("un if en linea")
# ternarios 
print(" Cuando es correcto ") if 5 == 2 else print(" Cuando es Falso ")

# Input ##### IMPORTANTE ##### los datos ingresados son considerados String 
dato = input("Ingrese Dato: ")
print(dato)

lista_Juego = ['hola', 'mundo', 'chanchito Feliz']
if lista_Juego.count(dato) > 0:
    print('El dato Existe ', dato)
else:
    print('El dato No Existe ', dato)

# Convertir String en int 
primer_numero = input("Ingrese 1 Numero: ")
primerN = int(primer_numero)

# Validar dato 
# Validar Numero
primer_numero = input("Ingrese 1 Numero: ")
try:
    primerNumero = int(primer_numero)
except:
    print("Error el dato ingresado no es un numero")

# Validar Antes 
primer_numero = input("Ingrese 1 Numero: ")
try:
    primerNumero = int(primer_numero)
except:
    primer_numero = True
###### Valida error
if primer_numero :
    print("Error")
    exit()
else:
    print("ingresaste un numero")


# While y Do while
i = 0
while i < 5:
    print(i)
    i = i + 1 # Aumenta i en 1 
    i += 1 # Aumenta i en 1

# While con break 
j = 0 
while j < 5:
    print(j)
    if j == 3:
        break # detiene la ejecucion
    j += 1

#while con continue 
j = 0 
while j < 5:
    j += 1
    if j == 3:
        continue # Vuelve a validar al while 
    print(j)

# For loop 
listUsuarios = ['Chanchito Feliz', 'Felipe', 'Nicolas']
for usuario in listUsuarios:
    print(usuario)

# imprime cada caracter de este usuario 
user = 'Franco Ovalle'
for c in user:
    print(c)

listUsuariosV2 = ['Chanchito Feliz', 'Felipe', 'Nicolas']
for usuario in listUsuariosV2:
    if usuario == 'Nicolas':
        print(usuario) # imprime hasta Nicolas
        break

listUsuariosV3 = ['Chanchito Feliz', 'Felipe', 'Nicolas']
for usuario in listUsuariosV3:
    if usuario == 'Felipe':
        continue # se saltara a Felipe
    print(usuario)

for x in range(1,6): ### pasando valores al range(inicial , final) o range(inicial , final, aumento)
    print(x)

####### FOR CON ELSE ######

for x in range(1,60, 10): ### pasando valores al range(inicial , final) o range(inicial , final, aumento)
    print(x)
else:
    print('Hemos terminado') ### Esto se ejecuta cuando termina el for 

# for con for 
usuariosV5 = ['Chanchito Feliz', 'Felipe', 'Nicolas']
edades = [24,30,31]
for user in usuariosV5:
    for edad in edades:
        print(usuario, edad)
    else:
        print('fin edades')
else:
    print('fin usuarios')

# Switch o match


    


# Funciones 
def miFuncion():
    print('mi primera funcion!')

miFuncion()

## funciones con argumentos 
def funcion_2(dato):
    print(dato) # aqui se llaman argumentos

funcion_2("Franco") # aqui se llama parametro
#### IMPORTANTE siempre se debe pasar los parametros que solicita la funcion

def funcion_variable(*data):
    print('El dato recibido es:', data) # data actua como una tupla y para ver los datos 
    # se debe usar de forma data[0] por ejemplo para imprimir Chanchito
funcion_variable('Chanchito', 'feliz','lele')

# funcion nombre completo
def nombreCompleto( apellido , nombre ):
    print(nombre, apellido)
# selecciona el argumento por el nombre en la definicion de la funcion 
nombreCompleto(nombre='Franco',apellido='Ovalle')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre='Franco',apellido='Ovalle')

# valor por defecto en caso de venir vacio
def miFuncion2(argumento = 'chanchito'):
    print(argumento)
miFuncion2()

# funcion con lista 
def funcionLista(lista):
    for el in lista:
        print(el)
funcionLista(['Chanchito','Feliz'])

# Concatenar valores 
def Concatena(lista):
    i=''
    for el in lista:
        i = i + el + ' ' 
    return i

nombre = Concatena(['Franco','Ovalle'])
print(nombre)

### RECURSIVIDAD

def recursion(i):
    if( i < 1 ):
        return i
    print(i)
    recursion(i - 1)

recursion(4)

### OBJETOS 
# clase es como el plano de una casa nos indica las dimensiones el numero de piezas etc 
# instancias son el numero de casas construidas 

# clase ( primera letra en mayuscula )
class User:
    nombre = 'Franco'
    apellido = 'Ovalle'
    edad = 30

# instancia ( en minuscula )
usuario = User()
### acceder a propiedades de la clase User
print(usuario.nombre, usuario.edad)

################################################
################################################

class UserV2:
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido
    
usuarioV4 = UserV2('Franco','Ovalle')
usuarioV5 = UserV2('Nicolas','Mellado')

print(usuarioV4.name, usuarioV4.apellido, usuariosV5.name, usuariosV5.apellido)

################################################

### METODOS 
class UserV2:
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido

    def saludo(self): # generamos un metodo el cual solo salude 
        print('Hola Mi nombre es: ', self.name)


usuarioV4 = UserV2('Franco','Ovalle')
usuarioV5 = UserV2('Nicolas','Mellado')

usuarioV4.saludo() # llamamos al metodo 

print(usuarioV4.name, usuarioV4.apellido, usuarioV5.name, usuarioV5.apellido)

# cambiar Valores 
usuarioV5.name = "Chanchito"
del usuarioV5.name # eliminar nombre del usuario
del usuarioV5 # Eliminar usuario

#### HERENCIA
class Admin(UserV2):
    def superSaludo(self):
        print('Hola me llamo ', self.name, ' y soy el administrador')

admin = Admin('Franco','Administrador')
admin.saludo() # aun puedo acceder al metodo de UserV2 gracias a la herencia
admin.superSaludo()

##### MODULOS ####
# importar modulos.py
from ejercicioModulos.modulos import modulos as mode

print(mode.mascotas)
mode.saludo('Franco')

# importar y cambiar nombre
#import modulos as mode # importamos el modulo y le cambiamos el nombre por mode 

print(mode.mascotas)
mode.saludo('Franco')

#importar solo el saludo 
#from modulos import saludo

#saludo('Nicolas')

#print(perros)

