import random
from rich import print
from funciones import *
#LISTADO MONSTRUOS, RATIOS COMPRENDIDOS ENTE 0.1 Y 1
monstruos=[
    {"nombre": "Conde-Mor", "ratio": 0.3},
    {"nombre": "Perro Demonio", "ratio": 0.1},
    {"nombre": "Cola-cuerno", "ratio": 0.2},
    {"nombre": "Rey Vampiro", "ratio": 0.4},
    {"nombre": "Evil Lamin Yamal", "ratio": 0.25},
    {"nombre": "Piramid Head", "ratio": 0.2},
    {"nombre": "Principe De Las Tinieblas", "ratio": 0.06}
]
#LISTADO DE OBJETOS, USAN UN MULTIPLICADOR
objetos=[
    {"nombre": "Estaca común", "multiplicador": 1.0},
    {"nombre": "Agua bendita", "multiplicador": 1.2},
    {"nombre": "Balas de plata", "multiplicador": 1.5},
    {"nombre": "Cetro de escarcha", "multiplicador": 1.7},
    {"nombre": "Necronomicón", "multiplicador": 2.0}
]
print("--- ¡Bienvenido a la [red]Caza del Monstruo![/red] ---")
#ELEGIR MONSTRUO
monstruo=elegir_monstruo(monstruos)
##VARIABLES
#INTENTOS
intentos=3
intento=1
capturado=False
#OBJETOS
objetos_disponibles=objetos
objeto=objetos[0]
#BUCLE MIENTRAS SE FALLA EL CAPTURAR
while intento <= intentos and not capturado and len(objetos_disponibles)>0:
    print(f"Intento {intento} de {intentos}")
    mostrar_objetos(objetos)
    #ELECCION OBJETO
    try:
        eleccion=int(input("Elige un objeto(1-5): "))
        if 1 <= eleccion <= len(objetos):
            objeto=objetos[eleccion -1]
        else:
            print("Número fuera de rango, se usará [magenta]Estaca Común[/magenta].")
            objeto=objetos[0]
    except ValueError:
        print("Entrada inválida, se usará [magenta]Estaca Común[/magenta].")
        objeto = objetos[0]
    #CÁLCULOS PORCENTAJE CAPTURA
    prob_captura=monstruo["ratio"] * objeto["multiplicador"]
    exito=random.random() < prob_captura

    print(f"Eliges usar [magenta]{objeto['nombre']}[/magenta]...")
    if exito:
        print(f"¡Has capturado a [green]{monstruo['nombre']}[/green]!")
        capturado=True
    else:
        print("El [green]monstruo[/green] escapó...")
    intento += 1
if not capturado:
    print(f"\nEl [green]{monstruo['nombre']}[/green] huyó sin dejar rastro...")
    print("¡Has perdido!")