primer_numero = float(input("ingrece el primer numero: "))
segundo_numero = float(input("ingrese el segundo numero: "))

if primer_numero > segundo_numero:
    suma = primer_numero + segundo_numero
    diferencia = primer_numero - segundo_numero
    print("la suma de los numeros es: ", suma)
    print("la diferencia entre los numeros es: ", diferencia)
else:
    producto = primer_numero * segundo_numero
    divicion = primer_numero / segundo_numero
    print("el producto de los numeros es: ", producto)
    print("la divicion de los numeros es: ", divicion)

