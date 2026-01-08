import numpy as np
from funciones import *
from rich import print
import os

#CARGAR PARTIDA
print("[yellow]CARGANDO PARTIDA GUARDADA...[/yellow]")
intentos, barcos_restantes, tablero, hundidos, visible = cargar_partida()

if intentos == 0:  #SI NO SE CARGA CORRECTAMENTE, CREAMOS PARTIDA NUEVA
    #CREAR TABLERO(OCULTO POR DEFECTO PERO YO HE AÑADIDO LA VERSION TRAMPA)
    tablero = np.zeros([20, 20])
    barcos = [2, 3, 4]
    for i, barco in enumerate(barcos):
        colocar_barco(tablero, barco, i + 1)

    visible = np.zeros([20, 20])
    intentos = 0
    barcos_restantes = len(barcos)
    hundidos = []
print("-------¡ES HORA DE JUGAR A [green]HUNDIR LA FLOTA[/green]!---------")
print("----------------------------------------------------")
print("~:Agua -- O:Disparo fallido -- X:Tocado -- #:Hundido -- B:Barco (guia)")
mostrar_tablero_guia(visible, tablero, mostrar_barcos=True)

while barcos_restantes > 0:
    fila_input = input("Numero FILA a disparar (0-19): ")
    #ACCEDER AL MENU DE GUARDAR CUANDO EL JUGADOR PONE 111 EN LA FILA
    if fila_input == "111": #TANTO POR FILA
        menu_opciones(intentos, barcos_restantes, tablero, visible, hundidos)
        entrada_valida = False
    else:
        col_input = input("Numero COLUMNA a disparar (0-19): ")
        if col_input == "111": #TANTO POR COLUMNA
            menu_opciones(intentos, barcos_restantes, tablero, visible, hundidos)
            entrada_valida = False
        else:
            entrada_valida = True
    if entrada_valida: #BUCLE: NUMEROS HAN DE SER VALIDOS
        if not fila_input.isdigit() or not col_input.isdigit():
            print("Esos numeros no son validos.")
            entrada_valida = False
        else:
            fila = int(fila_input)
            col = int(col_input)
            if not (0 <= fila < 20 and 0 <= col < 20): #BUCLE: PARA NO SALIRSE DEL TABLERO
                print("¡COORDENADAS fuera de nuestro ALCANCE!, Capitán.")
                entrada_valida = False
    #BUCLE: DISPARAR
    if entrada_valida:
        intentos += 1
        if tablero[fila, col] > 0:
            id_barco = tablero[fila, col]
            print("[yellow]¡TOCADO![/yellow]")
            visible[fila, col] = 2
            if np.all((visible[tablero == id_barco] == 2) |
                      (visible[tablero == id_barco] == 4)):
                if id_barco not in hundidos:
                    hundidos.append(id_barco)
                    barcos_restantes -= 1
                    print("[red]¡HUNDIDO![/red]")
                    visible[tablero == id_barco] = 4
        elif tablero[fila, col] == 0:
            print("[blue]AGUA...[/blue].")
            tablero[fila, col] = 3
            visible[fila, col] = 3
        else:
            print("YA hemos disparado AHÍ, Capitán.")
        mostrar_tablero_guia(visible, tablero)
print(f"¡HAS GANADO EN {intentos} INTENTOS!")