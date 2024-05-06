listaDeTupla = ("Pc" , "Play 5", "Xbox", "Switch")

"""
hice un diccionario en el cual nos regimos en el orden gerarquico en este caso de plataformas de videojuegos 
como los que sus plataformas son tomadas como el orden mas alto en la gerarquia y de ahí colocar dentro de otro diccionario
el siguiente orden gerarquico que en este caso seria los juegos de respectiva plataforma su numero asignado para que lo reconosca
al pedirlo con el comando print y me de solo los datos que yo le pida tanto como todos sus dato o solo su plataforma o 
solo su nombre.

"""
_juegos = {
    listaDeTupla[0]:{ 
        "0":{"nombre":"Valorant",
             "valor":  12500,
        "dispositivo":listaDeTupla[0]},
        "1":{"nombre":"GTA 5",
             "valor": 55000,
        "dispositivo":listaDeTupla[0]},
        "2":{"nombre":"Fortnite",
             "valor": 35000,
        "dispositivo":listaDeTupla[0]}
        },

    listaDeTupla[3]:{
        "0":{"nombre":"Mario Kart",
             "valor": 45000,
        "dispositivo":listaDeTupla[3]},
        "1":{"nombre":"Super Metroid",
             "valor": 24500,
        "dispositivo":listaDeTupla[3]},
        "2":{"nombre":"Fifa 24",
             "valor": 75000,
        "dispositivo":listaDeTupla[3]},
        },
    listaDeTupla[2]:{
        "0":{"nombre":"Forza horizon 5",
             "valor": 44500,
             "dispositivo":listaDeTupla[2]},
        "1":{"nombre":"Gears 5",
             "valor": 30000,
             "dispositivo":listaDeTupla[2]},
        "2":{"nombre":"Starfield",
             "valor": 23500,
             "dispositivo":listaDeTupla[2]}
        },
    listaDeTupla[1]:{
        "0":{"nombre":"God of war Ragnarok",
             "valor": 34000,
             "dispositivo":listaDeTupla[1]},
        "1":{"nombre":"Gran turismo",
             "valor": 45000,
             "dispositivo":listaDeTupla[1]},
        "2":{"nombre":"The last of us",
             "valor": 46000,
             "dispositivo":listaDeTupla[1]}
    }

}
