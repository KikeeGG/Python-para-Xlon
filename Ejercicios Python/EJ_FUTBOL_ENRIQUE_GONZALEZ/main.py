#MAIN
#IMPORTAR FUNCIONES Y LIBRERIAS
import tabulate
import rich
from equipos import menu_equipos
from jugadores import menu_jugadores
from calendario import menu_calendario
from ranking import menu_resultados

#MENU PRINCIPAL
def menu_principal():
    equipos=[]
    jugadores=[]
    partidos=[]
    opcion = 0
    while opcion != 5:
        print("---- MENÚ PRINCIPAL ----")
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Calendarios de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")
        print("-------------------------")

        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            opcion=0

        if opcion == 1:
            equipos=menu_equipos(equipos)
        elif opcion == 2:
            jugadores=menu_jugadores(jugadores, equipos)
        elif opcion == 3:
            partidos=menu_calendario(partidos, equipos)
        elif opcion == 4:
            partidos=menu_resultados(partidos, equipos)
        elif opcion == 5:
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

#EJECUTAR PROGRAMA
if __name__ == "__main__":
    menu_principal()