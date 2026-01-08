#UTILES
#Función que muestra el menú, solicita opcion y la devuelve
def menu(opcionesMenu):
    for i in opcionesMenu:
        print(i)
    opcion = int(input("Elige la opción: "))
    return opcion