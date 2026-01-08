from funciones_arrays import *
from rich import print

#NO CAMBIA NADA DEL EJERCICIO CON DICCIONARIOS
opcion="" #VALOR INICIAL VACÍO
while opcion != "8":
    mostrar_menu()
    opcion = input("Qué quieres hacer: ")
    if opcion == "1":
        alta_cliente()
    elif opcion == "2":
        listar_clientes()
    elif opcion == "3":
        buscar_cliente()
    elif opcion == "4":
        modificar_cliente()
    elif opcion == "5":
        eliminar_cliente()
    elif opcion == "6":
        guardar_clientes()
    elif opcion == "7":
        cargar_clientes()
    elif opcion == "8":
        print("Hasta luego!")
    else:
        print("Opción no válida.")