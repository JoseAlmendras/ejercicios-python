import modulos
from camelcase import CamelCase

c = CamelCase()

s = 'esta oracion necesita camelcase'
print(c.hump(s))

print(modulos.mascotas)
modulos.saludo('Franco')