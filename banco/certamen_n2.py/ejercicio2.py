def calcular_imc(peso, altura):
    imc = peso /(altura * altura)
    return imc
def interpretar_imc(imc):
    if imc< 18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en mestros: "))
imc = calcular_imc(peso, altura)
interpretacion = interpretar_imc(imc)

print("Su imc es:", imc)
print("interpretacion del imc",interpretacion )
