#f_menu_principal.py
from f_articulos import leer_int, menu_articulos
from f_usuarios import menu_usuarios
from f_ventas import menu_ventas

def menu_principal(articulos, usuarios, ventas, carrito_actual, usuario_activo):
    opcion = 0
    while opcion != 4:
        print("-----MENÚ PRINCIPAL-----")
        print("1. Gestión de artículos")
        print("2. Gestión de usuarios")
        print("3. Ventas / Carrito")
        print("4. Salir")
        print("-----------------------------------")
        opcion = leer_int("Selecciona una opción: ", 1)
        if opcion == 1:
            menu_articulos(articulos)
        elif opcion == 2:
            menu_usuarios(usuarios)
        elif opcion == 3:
            usuario_activo = menu_ventas(usuarios, articulos, ventas, carrito_actual, usuario_activo)
        elif opcion == 4:
            print("Programa finalizado.")
        else:
            print("Opción no válida.")
