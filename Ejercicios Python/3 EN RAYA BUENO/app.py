from ttt_core import *

#MENU SELECCION JUEGO
def menu():
    salir=False
    while not salir:
        print("---- MENÚ PRINCIPAL ----")
        print("1. VS CPU")
        print("2. JUGADOR VS JUGADOR")
        print("3. SALIR")
        print("------------------------")
        opcion = int(input("ELIGE MODO DE JUEGO: "))
        if opcion == 1:
                vs_cpu()
        elif opcion == 2:
                vs_jugador()
        elif opcion == 3:
                print("¡CHAO!")
                salir=True
        else:
            print("OPCION NO VALIDA. ELIGE 0, 1 o 2.")
    else:
        print("ESCRIBE UN NUMERO, POR FAVOR.")

#JUGAR
menu()