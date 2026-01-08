import numpy as np
import os

#PINTAR TABLERO
def mostrar_tablero(visible, tablero):
    print("   " + " ".join([f"{i:2}" for i in range(20)]))
    for i in range(20):
        fila_simbolos = []
        for j in range(20):
            if visible[i, j] == 0:
                fila_simbolos.append("~  ")
            elif visible[i, j] == 3:
                fila_simbolos.append("O  ")
            elif visible[i, j] == 2:
                fila_simbolos.append("X  ")
            elif visible[i, j] == 4:
                fila_simbolos.append("#  ")
        print(f"{i:2}  " + "".join(fila_simbolos))

#COLOCAR BARCO
def colocar_barco(tablero, longitud, id_barco):
    colocado = False
    while not colocado:
        orientacion = np.random.choice([0, 1])
        if orientacion == 0:
            fila = np.random.randint(0, 20)
            columna = np.random.randint(0, 20 - longitud + 1)
            if np.all(tablero[fila, columna:columna + longitud] == 0):
                tablero[fila, columna:columna + longitud] = id_barco
                colocado = True
        else:
            fila = np.random.randint(0, 20 - longitud + 1)
            col = np.random.randint(0, 20)
            if np.all(tablero[fila:fila + longitud, col] == 0):
                tablero[fila:fila + longitud, col] = id_barco
                colocado = True

#MODO TRAMPA, MOSTRAR TABLERO CON BARCOS VISIBLES
def mostrar_tablero_guia(visible, tablero, mostrar_barcos=False):
    print("   " + " ".join([f"{i:2}" for i in range(20)]))
    for i in range(20):
        fila_simbolos = []
        for j in range(20):
            if visible[i, j] == 0:
                if mostrar_barcos and tablero[i, j] > 0:
                    fila_simbolos.append("B  ")
                else:
                    fila_simbolos.append("~  ")
            elif visible[i, j] == 3:
                fila_simbolos.append("O  ")
            elif visible[i, j] == 2:
                fila_simbolos.append("X  ")
            elif visible[i, j] == 4:
                fila_simbolos.append("#  ")
        print(f"{i:2}  " + "".join(fila_simbolos))

#MENÚ OPCIONES, PULSAR 111
def menu_opciones(intentos, barcos_restantes, tablero, visible, hundidos):
    print("1. GUARDAR PARTIDA")
    print("2. SALIR")
    opcion = input("ELIGE una OPCIÓN: ")
    if opcion == "1":
        guardar_partida(intentos, barcos_restantes, tablero, hundidos, visible)
        print("PARTIDA GUARDADA.")
    elif opcion == "2":
        print("SALIENDO...")
        exit()
    else:
        print("OPCION NO VALIDA.")

#GUARDAR PARTIDA CON "w"
def guardar_partida(intentos, barcos_restantes, tablero, hundidos, visible):
    with open("partida_comenzada.txt", "w") as f:
        # Guardamos los datos principales
        f.write(f"{intentos}\n")
        f.write(f"{barcos_restantes}\n")
        
        # Guardamos el tablero
        for fila in tablero:
            texto = " ".join([str(int(n)) for n in fila])
            f.write(texto + "\n")
        
        # Guardamos los barcos hundidos
        texto = " ".join([str(h) for h in hundidos])
        f.write(texto + "\n")
        
        # Guardamos el tablero visible
        for fila in visible:
            texto = " ".join([str(int(n)) for n in fila])
            f.write(texto + "\n")

#CARGAR PARTIDA CON "r"
def cargar_partida():
    if not os.path.exists("partida_comenzada.txt") or os.path.getsize("partida_comenzada.txt") == 0:
        print("[red]No se encontró partida guardada, creando una nueva.[/red]")
        return 0, 3, np.zeros([20, 20]), [], np.zeros([20, 20])

    with open("partida_comenzada.txt", "r") as comenzar:
        lineas = comenzar.read().splitlines()

    #VERIFICAR ARCHIVO, SI NO, ARRANCA PARTIDA NUEVA
    if len(lineas) < 23:
        print("Archivo de partida corrupto — Creando partida nueva")
        return 0, 3, np.zeros([20, 20]), [], np.zeros([20, 20])
    intentos = int(lineas[0])
    barcos_restantes = int(lineas[1])
    #BUCLE: LEER TABLERO
    tablero = []
    for i in range(2, 22):
        partes = lineas[i].split()
        fila = [int(p) for p in partes]
        tablero.append(fila)
    tablero = np.array(tablero)
    #BUCLE: BARCOS HUNDIDOS
    hundidos = []
    if len(lineas) > 22:
        partes = lineas[22].split()
        hundidos = [int(p) for p in partes]
    #LEER TABLERO TRAMPA
    visible = np.zeros([20, 20])
    if len(lineas) > 23:
        for i in range(24, len(lineas)):
            fila_visible = list(map(int, lineas[i].split()))
            visible[i - 24] = fila_visible
    return intentos, barcos_restantes, tablero, hundidos, visible