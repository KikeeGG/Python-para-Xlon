import numpy as np
import damas_core

#FUNCION PARA PINTAR EL TABLERO DE FORMA LEGIBLE
def pintar_tablero(tablero):
    print("   0 1 2 3 4 5 6 7")
    print("  -----------------")
    for fila in range(8):
        linea = str(fila) + " | "
        for columna in range(8):
            valor = tablero[fila, columna]

            if valor == 0:
                simbolo = "."
            elif valor == 1:
                simbolo = "o"
            elif valor == 2:
                simbolo = "O"
            elif valor == 3:
                simbolo = "x"
            elif valor == 4:
                simbolo = "X"
            else:
                simbolo = "?"

            linea = linea + simbolo + " "
        print(linea)
    print("  -----------------\n")

#FUNCION DEL FUNCIONAMIENTO DEL PROGRAMA
def programaFinal():
    tablero = np.zeros((8, 8))
    damas_core.colocar_fichas(tablero)
    pintar_tablero(tablero)

    terminado = False
    while not terminado:
        print("Turno Jugador 1")
        damas_core.jugador1(tablero)
        pintar_tablero(tablero)

        if damas_core.verSiHaTerminado(tablero):
            terminado = True
        else:
            print("Turno Jugador 2")
            damas_core.jugador2(tablero)
            pintar_tablero(tablero)

            if damas_core.verSiHaTerminado(tablero):
                terminado = True
#LLAMAR A LA FUNCION PARA EJECUTAR EL PROGRAMA
programaFinal()