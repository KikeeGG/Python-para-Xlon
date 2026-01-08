#JUGADORES
from tabulate import tabulate

#FUNCIONES
#MENÚ MODULO JUGADORES
def menu_jugadores(jugadores, equipos):
    opcion = 0
    while opcion != 6:
        print("\n--- MENÚ DE JUGADORES ---")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador por ID")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6. Volver al menú principal")

        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            opcion = 0

        if opcion == 1:
            jugadores = crear_jugador(jugadores, equipos)
        elif opcion == 2:
            listar_jugadores(jugadores, equipos)
        elif opcion == 3:
            buscar_jugador(jugadores, equipos)
        elif opcion == 4:
            jugadores = actualizar_jugador(jugadores)
        elif opcion == 5:
            jugadores = eliminar_jugador(jugadores)
        elif opcion == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")
    return jugadores

#CREAR JUGADOR
def crear_jugador(jugadores, equipos):
    print("\n--- Crear jugador nuevo ---")
    nombre=input("Nombre del jugador: ").strip()
    edad=input("Edad del jugador: ").strip()

    if nombre =="" or edad =="":
        print("El nombre y la edad no pueden estar vacíos.")
        return jugadores

    #SELECCIONAR EQUIPO EXISTENTE
    print("\nEquipos disponibles:")
    activos = []
    for e in equipos:
        if e["activo"]:
            activos.append([e["id"], e["nombre"]])
    if len(activos) == 0:
        print("No hay equipos activos, no se puede crear jugador, CREA UN EQUIPO PRIMERO.")
        return jugadores
    else:
        print(tabulate(activos, headers=["ID", "Nombre"], tablefmt="grid"))

    try:
        id_equipo = int(input("Introduce el ID del equipo al que pertenece: "))
    except:
        print("ID de equipo no válido.")
        return jugadores

    #VERIFICAR QUE EQUIPO EXISTE Y ESTA ACTIVO
    existe=False
    for e in equipos:
        if e["id"] ==id_equipo and e["activo"]:
            existe=True
    if not existe:
        print("Equipo no encontrado o inactivo.")
        return jugadores

    #GENERAR ID JUGADOR
    nuevo_id=1
    for j in jugadores:
        if j["id"] >=nuevo_id:
            nuevo_id=j["id"] + 1
    jugador= {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "equipo_id": id_equipo,
        "activo": True
    }
    
    jugadores.append(jugador)
    print("¡Jugador creado correctamente!\n")
    return jugadores

#LISTAR JUGADORES ACTIVOS
def listar_jugadores(jugadores, equipos):
    print("\n--- Lista de jugadores activos ---")
    activos=[]
    for j in jugadores:
        if j["activo"]:
            nombre_equipo=""
            for e in equipos:
                if e["id"]==j["equipo_id"]:
                    nombre_equipo=e["nombre"]
            activos.append([j["id"], j["nombre"], j["edad"], nombre_equipo])
    if len(activos)==0:
        print("No hay jugadores activos todavía.")
    else:
        print(tabulate(activos, headers=["ID", "Nombre", "Edad", "Equipo"], tablefmt="grid"))

#BUSCAR JUGADOR POR ID
def buscar_jugador(jugadores, equipos):
    print("\n--- Buscar jugador por ID ---")
    try:
        id_buscar=int(input("Introduce el ID del jugador: "))
    except:
        print("ID inválido.")
        return
    encontrado=None
    for j in jugadores:
        if j["id"]== id_buscar:
            encontrado= j

    if encontrado==None:
        print("Jugador no encontrado.")
    else:
        equipo_nombre =""
        for e in equipos:
            if e["id"]==encontrado["equipo_id"]:
                equipo_nombre=e["nombre"]

        datos=[[encontrado["id"], encontrado["nombre"], encontrado["edad"], equipo_nombre, encontrado["activo"]]]
        print(tabulate(datos, headers=["ID", "Nombre", "Edad", "Equipo", "Activo"], tablefmt="grid"))

#ACTUALIZAR DATOS JUGADOR
def actualizar_jugador(jugadores):
    print("\n--- Actualizar datos del jugador ---")
    try:
        id_actualizar=int(input("Introduce el ID del jugador a modificar: "))
    except:
        print("ID inválido.")
        return jugadores

    jugador=None
    for j in jugadores:
        if j["id"] ==id_actualizar:
            jugador =j
    if jugador ==None:
        print("Jugador no encontrado.")
        return jugadores

    print("Nota: si dejas un campo vacío, no se cambiará.")
    nuevo_nombre = input("Nuevo nombre: ").strip()
    nueva_edad = input("Nueva edad: ").strip()
    if nuevo_nombre != "":
        jugador["nombre"] =nuevo_nombre
    if nueva_edad != "":
        jugador["edad"] =nueva_edad

    print("Jugador actualizado correctamente.\n")
    return jugadores

#ELIMINAR JUGADOR
def eliminar_jugador(jugadores):
    print("\n--- Eliminar jugador ---")
    try:
        id_eliminar=int(input("Introduce el ID del jugador a eliminar: "))
    except:
        print("ID no válido.")
        return jugadores

    encontrado=None
    for j in jugadores:
        if j["id"] ==id_eliminar:
            encontrado =j

    if encontrado ==None:
        print("Jugador no encontrado.")
    else:
        encontrado["activo"] = False
        print("El jugador ha sido eliminado correctamente.\n")
    return jugadores