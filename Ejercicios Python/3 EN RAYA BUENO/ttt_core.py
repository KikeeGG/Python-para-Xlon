import numpy as np
import random

#CREAR TABLERO CON NUMPY
def crear_tablero():
    return np.zeros((3,3), dtype=int) #DTYPE=INT ES PORQUE DA ERROR SI INTENTAS SELECCIONAR CIERTAS CORDENADAS
#PINTAR TABLERO
def pintar_tablero(tablero):#SACADO DE IA, SE ME DA MAL PINTAR TABLEROS
    print("\n   0   1   2")
    fichas = {0:" ",1:"X",2:"O"} #JUGADOR 1 REPRESENTADO POR "X" Y CPU O JUGADOR 2 REPRESENTADO POR "O"
    fila = 0
    while fila<3:
        print(str(fila)+"  "+fichas[tablero[fila,0]]+" | "+fichas[tablero[fila,1]]+" | "+fichas[tablero[fila,2]])
        if fila < 2:
            print("  ---+---+---")
        fila = fila + 1
    print()

#LEER VICTORIA
def hay_victoria(tab, ficha):
    #FILAS Y COLUMNAS
    for i in range(3):
        if np.all(tab[i]==ficha): #tab[i], indexacion numpy y sirve para seleccionar filas
            return True
        if np.all(tab[:, i]==ficha): #tab[:, i] = : significa todas las filas + bulce para todas las columnas i (de nuevo indexacion numpy)
            return True
    #diagonal principal con numpy
    if np.all(np.diag(tab)==ficha):
        return True
    #diagonal secundaria con numpy
    if np.all(np.diag(np.fliplr(tab))==ficha): #fliplr permite buscar la diagonal contraria a la principal
        return True
    return False
#HAY EMPATE
def tablero_lleno(tab):
    return 0 not in tab

#CAMBIAR TURNO
def turno_jugador(tab):
    print("ES EL TURNO DEL JUGADOR")
    valido=False
    while not valido:
        fila_elegida=input("ELIGE FILA (0-2): ")
        col_elegida=input("ELIGE COLUMNA (0-2): ")
        #BUCLE FILTRO: SON NUMEROS Y NO OTRA COSA
        if fila_elegida and col_elegida:
            fila=int(fila_elegida)
            col=int(col_elegida)
            #BUCLE FILTRO: COMPROBAR QUE ESTA EN RANGO
            if 0 <= fila <= 2 and 0 <= col <= 2:
                #BUCLE FILTRO: COMPROBAR SI HAY CASILLA LIBRE
                if tab[fila][col]==0:
                    tab[fila][col]=1
                    valido=True
                else:
                    print("CASILLA OCUPADA.")
            else:
                print("NUMEWRO NO VÁLIDO.")
        else:
            print("ESCRIBRE NUMEROS DEL 0 AL 2.")
#TRUNO CPU CON RANDOM RANDIT
def turno_cpu(tab):
    valido=False
    while not valido:
        #RANDOM RANDIT PARA POSICION ALEATORIA
        fila=random.randint(0, 2)
        col=random.randint(0, 2)
        #BUCLE FILTRO: COMPROBAR SI HAY CASILLA LIBRE
        if tab[fila][col]==0:
            tab[fila][col]=2
            valido=True
        print("LA CPU HA MARCADO LA POSICIÓN: ", fila, col)

#MODOS DE JUEGO
def vs_cpu():
    tab=crear_tablero()
    fin=False
    while not fin:
        #LLAMAR A FUNCIONES
        pintar_tablero(tab)
        turno_jugador(tab)
        if hay_victoria(tab, 1):
            pintar_tablero(tab)
            print(" VICTORIA")
            fin=True
        if not fin and tablero_lleno(tab):
            pintar_tablero(tab)
            print("EMPATE")
            fin=True
        #SALTAR AL TURNO CPU
        if not fin:
            turno_cpu(tab)
            if hay_victoria(tab, 2):
                pintar_tablero(tab)
                print("GANA LA CPU")
                fin=True
            if not fin and tablero_lleno(tab):
                pintar_tablero(tab)
                print("EMPATE")
                fin=True
def vs_jugador():
    tab=crear_tablero()
    fin=False
    jugador=1   #EMPIEZA SIEMPRE EL 1
    while not fin:
        pintar_tablero(tab)
        turno_jugador(tab, jugador)
        if hay_victoria(tab, jugador):
            pintar_tablero(tab)
            print(f"GANA EL JUGADOR {jugador}")
            fin=True
        elif tablero_lleno(tab):
            pintar_tablero(tab)
            print("EMPATE")
            fin=True
        else:
            #CAMBIO TURNO ENTRE PLAYERS
            if jugador==1:
                jugador=2
            else:
                jugador=1