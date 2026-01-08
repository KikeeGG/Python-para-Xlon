#EQUIPOS
from tabulate import tabulate

#DEFINIR VARIABLES
equipos = []
ultimo_id = 0

#FUNCIONES
#MENU DEL MODULO EQUIPOS
def menu_equipos(equipos):
    opcion = 0
    while opcion != 6:
        print("--- MENÚ DE EQUIPOS ---")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo por ID")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo (dar de baja)")
        print("6. Volver al menú principal")

        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            opcion = 0

        if opcion == 1:
            equipos = crear_equipo(equipos)
        elif opcion == 2:
            listar_equipos(equipos)
        elif opcion == 3:
            buscar_equipo(equipos)
        elif opcion == 4:
            equipos = actualizar_equipo(equipos)
        elif opcion == 5:
            equipos = eliminar_equipo(equipos)
        elif opcion == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")
    return equipos


#CREAR EQUIPO
def crear_equipo(equipos):
    print("--- Crear equipo nuevo ---")
    nombre = input("Nombre del equipo: ").strip()
    ciudad = input("Ciudad del equipo: ").strip()

    if nombre == "" or ciudad == "":
        print("El nombre y ciudad no pueden estar vacíos!")
        return equipos

    # GENERAR ID ÚNICO (selecciona el mayor y le suma 1)
    nuevo_id = 1
    for e in equipos:
        if e["id"] >= nuevo_id:
            nuevo_id = e["id"] + 1

    # DICCIONARIO
    equipo = {
        "id": nuevo_id,
        "nombre": nombre,
        "ciudad": ciudad,
        "activo": True
    }

    equipos.append(equipo)
    print("El equipo ha sido creado.\n")
    return equipos


#LISTAR EQUIPOS ACTIVOS
def listar_equipos(equipos):
    print("--- Lista de equipos activos ---")
    activos = []
    for e in equipos:
        if e["activo"]:
            activos.append([e["id"], e["nombre"], e["ciudad"]])
    if len(activos) == 0:
        print("No hay equipos activos todavía.")
    else:
        print(tabulate(activos, headers=["ID", "Nombre", "Ciudad"], tablefmt="grid"))


#BUSCAR EQUIPOS POR ID
def buscar_equipo(equipos):
    print("--- Buscar equipos por su ID ---")
    try:
        id_buscar = int(input("Introduce el ID del equipo a buscar: "))
    except:
        print("ID inválido.")
        return

    encontrado = None
    for e in equipos:
        if e["id"] == id_buscar:
            encontrado = e

    if encontrado == None:
        print("Equipo no encontrado.")
    else:
        datos = [[encontrado["id"], encontrado["nombre"], encontrado["ciudad"], encontrado["activo"]]]
        print(tabulate(datos, headers=["ID", "Nombre", "Ciudad", "Activo"], tablefmt="grid"))


#ACTUALIZAR DATOS
def actualizar_equipo(equipos):
    print("--- Actualizar datos equipo ---")
    try:
        id_actualizar = int(input("Introduce el ID del equipo a modificar: "))
    except:
        print("ID de equipo no válido")
        return equipos

    equipo = None
    for e in equipos:
        if e["id"] == id_actualizar:
            equipo = e

    if equipo == None:
        print("Equipo no encontrado.")
        return equipos

    print("Nota: Si dejas la casilla en blanco, no se cambiará.")
    nuevo_nombre = input("Nuevo nombre para el equipo: ").strip()
    nueva_ciudad = input("Nueva ciudad para el equipo: ").strip()

    if nuevo_nombre != "":
        equipo["nombre"] = nuevo_nombre
    if nueva_ciudad != "":
        equipo["ciudad"] = nueva_ciudad

    print("El equipo ha sido actualizado!\n")
    return equipos


#ELIMINACIÓN DE EQUIPOS
def eliminar_equipo(equipos):
    print("--- Eliminar equipo ---")
    try:
        id_eliminar = int(input("Introduce el ID del equipo a eliminar: "))
    except:
        print("ID inválido.")
        return equipos

    encontrado = None
    for e in equipos:
        if e["id"] == id_eliminar:
            encontrado = e

    if encontrado == None:
        print("Equipo no encontrado.")
    else:
        encontrado["activo"] = False
        print("El equipo ha sido eliminado correctamente.\n")

    return equipos