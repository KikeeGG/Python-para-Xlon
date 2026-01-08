import numpy as np

#CONSTANTE PARA LIMITAR MOVIMIENTOS DENTRO DEL TABLERO
MAXTABLERO = 7
#FUNCION QUE REVISA SI UNA POSICION ESTA DENTRO DEL TABLERO
def dentro(f, c):
    return f >= 0 and f <= MAXTABLERO and c >= 0 and c <= MAXTABLERO
#FUNCION PARA REALIZAR MOVIMIENTO Y COMIDAS ENCENDIDAS
def mover_y_comer(tablero, fila, columna, df, dc, enemigos, nuevo_valor):
    #CALCULA LA PRIMERA CASILLA A LA QUE SE QUIERE MOVER
    fila_nueva = fila + df
    columna_nueva = columna + dc
    #SI ESTA FUERA DEL TABLERO NO SE MUEVE
    if not dentro(fila_nueva, columna_nueva):
        print("ESTA FICHA NO SE PUEDE MOVER HACIA ESA DIRECCION")
        return
    #ELIMINA LA FICHA ORIGINAL
    tablero[fila, columna] = 0
    #MIENTRAS ENCUENTRE ENEMIGOS SIGUE AVANZANDO
    seguir = True
    while seguir:
        if dentro(fila_nueva, columna_nueva):
            if tablero[fila_nueva, columna_nueva] in enemigos:
                print("HAS COMIDO UNA FICHA DEL OPONENTE")
                tablero[fila_nueva, columna_nueva] = 0
                fila_nueva = fila_nueva + df
                columna_nueva = columna_nueva + dc
            else:
                seguir = False
        else:
            seguir = False
    #AL FINAL COLOCA LA FICHA SOLO SI LA CASILLA ES VALIDA
    if dentro(fila_nueva, columna_nueva):
        tablero[fila_nueva, columna_nueva] = nuevo_valor
    else:
        print("EL MOVIMIENTO TERMINO FUERA DEL TABLERO")
#FUNCION PARA VER SI UNA FICHA DEBE CORONARSE
def coronar(jugador, fila):
    if jugador == 1 and fila == 0:
        return 2
    if jugador == 2 and fila == 7:
        return 4
    return None
#FUNCION QUE COLOCA LAS FICHAS EN EL TABLERO CON UN PATRON INICIAL
def colocar_fichas(tablero):
    fila1 = 0
    fila2 = 1
    fila3 = 2
    fila4 = 5
    fila5 = 6
    fila6 = 7
    patron = np.tile([3, 0], 4) #PATRON PARA PEONES DEL JUGADOR 2
    tablero[fila2] = patron

    patron = np.tile([1, 0], 4) #PATRON PARA PEONES DEL JUGADOR 1
    tablero[fila4] = patron
    tablero[fila6] = patron

    patron2 = np.tile([0, 1], 4) #PATRON PARA EL JUGADOR 1
    tablero[fila5] = patron2

    patron2 = np.tile([0, 3], 4) #PATRON PARA EL JUGADOR 2
    tablero[fila1] = patron2
    tablero[fila3] = patron2

    print(tablero)
#FUNCION DEL JUGADOR 1: MANEJA PEONES, REYES, MOVIMIENTOS Y CORONACION
def jugador1(tablero):
    encontrado = False
    while not encontrado:
        fila = int(input("Fila: (de 0 a 7) "))
        while fila < 0 or fila > 7:
            print("ESTA FILA NO ES VALIDA")
            fila = int(input("Fila: (de 0 a 7) "))
        columna = int(input("Columna: (de 0 a 7) "))
        while columna < 0 or columna > 7:
            print("COLUMNA NO VALIDA")
            columna = int(input("Columna: (de 0 a 7) "))
        pieza = tablero[fila, columna]
        #PEON SIMPLE DEL JUGADOR 1
        if pieza == 1:
            encontrado = True
            lado = input("HAY UN PEON, A QUE LADO QUIERES MOVER? ('i'=izquierda 'd'=derecha) ")
            enemigos = [3, 4]
            df = -1
            if lado == "i":
                dc = -1
            elif lado == "d":
                dc = 1
            else:
                print("DIRECCION NO VALIDA")
                return
            nuevo_valor = 1
            mover_y_comer(tablero, fila, columna, df, dc, enemigos, nuevo_valor)
            #REVISA CORONACION
            for i in range(8):
                for j in range(8):
                    if tablero[i, j] == 1:
                        corona = coronar(1, i)
                        if corona is not None:
                            tablero[i, j] = corona
        #REY DEL JUGADOR 1
        elif pieza == 2:
            encontrado = True
            lado = input("HAY UN REY, A QUE LADO QUIERES MOVER? ('ai','ad','li','ld') ")
            enemigos = [3, 4]
            df = 0
            dc = 0
            if lado == "ai":
                df = -1; dc = -1
            elif lado == "ad":
                df = -1; dc = 1
            elif lado == "li":
                df = 1; dc = -1
            elif lado == "ld":
                df = 1; dc = 1
            else:
                print("DIRECCION NO VALIDA")
                return
            mover_y_comer(tablero, fila, columna, df, dc, enemigos, 2)
        else:
            print("NO HAY PEON NI REY EN ESA POSICION")
#FUNCION DEL JUGADOR 2: MANEJA PEONES, REYES, MOVIMIENTOS Y CORONACION
def jugador2(tablero):
    encontrado = False
    while not encontrado:
        fila = int(input("Fila: (de 0 a 7) "))
        while fila < 0 or fila > 7:
            print("ESTA FILA NO ES VALIDA")
            fila = int(input("Fila: (de 0 a 7) "))

        columna = int(input("Columna: (de 0 a 7) "))
        while columna < 0 or columna > 7:
            print("COLUMNA NO VALIDA")
            columna = int(input("Columna: (de 0 a 7) "))
        pieza = tablero[fila, columna]
        #PEON DEL JUGADOR 2
        if pieza == 3:
            encontrado = True
            lado = input("HAY UN PEON, A QUE LADO QUIERES MOVER? ('i'=izquierda 'd'=derecha) ")
            enemigos = [1, 2]
            df = 1
            if lado == "i":
                dc = -1
            elif lado == "d":
                dc = 1
            else:
                print("DIRECCION NO VALIDA")
                return
            nuevo_valor = 3
            mover_y_comer(tablero, fila, columna, df, dc, enemigos, nuevo_valor)
            #CORONACION
            for i in range(8):
                for j in range(8):
                    if tablero[i, j] == 3:
                        corona = coronar(2, i)
                        if corona is not None:
                            tablero[i, j] = corona
        #REY DEL JUGADOR 2
        elif pieza == 4:
            encontrado = True
            lado = input("HAY UN REY, A QUE LADO QUIERES MOVER? ('ai','ad','li','ld') ")
            enemigos = [1, 2]
            df = 0; dc = 0
            if lado == "ai":
                df = -1; dc = -1
            elif lado == "ad":
                df = -1; dc = 1
            elif lado == "li":
                df = 1; dc = -1
            elif lado == "ld":
                df = 1; dc = 1
            else:
                print("DIRECCION NO VALIDA")
                return
            mover_y_comer(tablero, fila, columna, df, dc, enemigos, 4)
        else:
            print("NO HAY PEON NI REY EN ESA POSICION")
#FUNCION QUE MIRA SI YA NO QUEDAN PIEZAS DE ALGUN JUGADOR
def verSiHaTerminado(tablero):
    if not np.any((tablero == 1) | (tablero == 2)):
        print("GANADOR: JUGADOR 2")
        return True
    if not np.any((tablero == 3) | (tablero == 4)):
        print("GANADOR: JUGADOR 1")
        return True
    return False