import numpy as np

#CREAR TABLERO
def crear_tablero():
    return np.zeros((6,7), dtype=int) #COMO EN EL 3 EN RAYA, DTYPE=INT NOS AYUDA A ELEGIR LA CASILLA SIN DAR ERROR
#PINTAR EL TABLERO (sacado de ia para que no de dolor de cabeza ejecutar el programa)
def pintar_tablero(tablero):
    fichas = {0:" ", 1:"X", 2:"O"}  #Jugador 1=X, Jugador 2=O
    print("   " + "   ".join(str(i) for i in range(tablero.shape[1])))
    print("  +" + "---+"*tablero.shape[1])
    for fila_index, fila in enumerate(tablero):
        print(f"{fila_index} | " + " | ".join(fichas[x] for x in fila) + " |")
        print("  +" + "---+"*tablero.shape[1])
    print()

#COLOCAR LA FICHA, MOVIMIENTO DE JUGADOR
def colocar_jugador(posiciones, tablero, jugador):
    colocado=False
    while not colocado:
        # CORRECCIÓN: input con un solo string usando f-string
        col = int(input(f"JUGADOR {jugador} ELIGE COLUMNA PARA TU FICHA (0-6): "))
        if 0 <= col <= 6:
            fila = 5  #SE EMPIEZA DESDE LA FILA DE ABAJO EN EL CONECTA 4
            #WHILE QUE SUBE HASTA ENCONTRAR FILA LIBRE
            while (fila, col, 1) in posiciones or (fila, col, 2) in posiciones:
                fila -= 1
            if fila >= 0:
                tablero[fila, col]=jugador
                posiciones.append((fila, col, jugador))
                print("FICHA COLOCADA EN FILA", fila, "COLUMNA", col)
                colocado= True
            else:
                print("COLUMNA LLENA, ELIGE OTRA")
        else:
            print("TE SALES DEL TABLERO")

#COMPROBAR VICTORIA/4 EN RAYA
def hay_cuatro_en_raya(tablero, jugador):
    #VICTORIA HORIZONTAL
    for fila in range(6): #BUCLE RECORRE TODAS LAS FILAS
        for col in range(4): #SOLO HASTA LA COLUMNA 3 PARA QUE QUEPAN 4
            if all(tablero[fila, col+i]==jugador for i in range(4)): #BUCLE QUE REVISA SI LAS FICHAS SON DEL MISMO JUGADOR
                return True
    #VICTORIA VERTICAL
    for col in range(7):
        for fila in range(3): #SOLO HASTA LA FILA 2 PARA QUE QUEPAN 4
            if all(tablero[fila+i, col]==jugador for i in range(4)):
                return True
    #DIAGONAL DESCENDENTE CON NUMPY
    for offset in range(-2, 4):  #OFFSET=0 EQUIVALE A LA DIAGONAL K, LA PRINCIPAL, SE CREA UN RANGO PARA COMPARAR DIAGONALES POR ENCIMA Y DEBAJO DE K
        diag=np.diag(tablero, k=offset) #ENTENDEMOS K COMO LA DIAGONAL PRINCIPAL DEL TABLERO
        for i in range(len(diag) - 3):
            if all(diag[i+j]==jugador for j in range(4)):
                return True
    #DIAGONAL ASCENDENTE O MATRIZ VOLTEADA CON NUMPY
    tablero_volteado=np.fliplr(tablero) # np.fliplr VOLTEA EL TABLERO HORIZONTALMENTE
    for offset in range(-2, 4):
        diag=np.diag(tablero_volteado, k=offset)
        for i in range(len(diag) - 3):
            if all(diag[i+j]==jugador for j in range(4)):
                return True
    return False
#HAY EMPATE
def tablero_lleno(tab):
    return 0 not in tab