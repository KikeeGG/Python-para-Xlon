#CALENDARIO
from tabulate import tabulate
from datetime import datetime
from rich.console import Console
console = Console()

#FUNCIONES
#MENU DEL CALENDARIO
def menu_calendario(partidos, equipos):
    opcion = 0
    while opcion != 5:
        print("\n--- MENÚ DE CALENDARIO ---")
        print("1. Crear partido")
        print("2. Listar partidos")
        print("3. Reprogramar partido")
        print("4. Eliminar partido")
        print("5. Volver al menú principal")

        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            opcion = 0

        if opcion == 1:
            partidos = crear_partido(partidos, equipos)
        elif opcion == 2:
            listar_partidos(partidos, equipos)
        elif opcion == 3:
            partidos = reprogramar_partido(partidos)
        elif opcion == 4:
            partidos = eliminar_partido(partidos)
        elif opcion == 5:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")
    return partidos

#CREAR PARTIDO
def crear_partido(partidos, equipos):
    print("\n--- Crear partido ---")

    #MOSTRAR EQUIPOS ACTIVOS
    activos = []
    for e in equipos:
        if e["activo"]:
            activos.append([e["id"], e["nombre"]])
    if len(activos) < 2:
        print("No hay suficientes equipos ACTIVOS para crear un partido.")
        return partidos
    print(tabulate(activos, headers=["ID", "Equipo"], tablefmt="grid"))

    try:
        jornada = int(input("Jornada: "))
        if jornada < 1:
            print("La jornada debe ser al menos 1.")
            return partidos
        local_id=int(input("ID del equipo local: "))
        visitante_id=int(input("ID del equipo visitante: "))
    except:
        print("Entrada inválida.")
        return partidos

    if local_id ==visitante_id:
        print("¡Un equipo no puede enfrentarse a sí mismo!")
        return partidos

    #VERIFICAR QUE AMBOS EQUIPOS ESTEN ACTIVOS
    ids_activos = [e["id"] for e in equipos if e["activo"]]
    if local_id not in ids_activos or visitante_id not in ids_activos:
        print("Uno o los dos equipos no existen o están inactivos.")
        return partidos

    #PARA NO DUPLICADOS(SACADO DE UN CHICO DE REDDIT)
    for p in partidos:
        if p["jornada"] == jornada and (
            (p["local_id"] == local_id and p["visitante_id"] == visitante_id) or
            (p["local_id"] == visitante_id and p["visitante_id"] == local_id)
        ):
            print("Ya existe un partido entre estos equipos en esta jornada.")
            return partidos
    #USO DE DATETIME
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    hora = input("Hora (HH:MM): ").strip()

    #GENERAR ID ÚNICO PARA EL ENCUENTRO
    nuevo_id = 1
    for p in partidos:
        if p["id"] >= nuevo_id:
            nuevo_id = p["id"] + 1

    partido = {
        "id": nuevo_id,
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None  #(golesLocal, golesVisitante)
    }
    partidos.append(partido)
    print("Partido creado correctamente.\n")
    return partidos

#LISTAR PARTIDOS
def listar_partidos(partidos, equipos):
    print("\n--- Calendario de partidos ---")
    if len(partidos) ==0:
        print("No hay partidos programados.")
        return
    try:
        filtro=input("¿Deseas filtrar por jornada? (S/N): ").strip().upper()
    except:
        filtro="N"

    if filtro=="S":
        try:
            jornada = int(input("Introduce el número de jornada: "))
        except:
            print("Entrada inválida.")
            return
        seleccionados = []
        for p in partidos:
            if p["jornada"]==jornada:
                seleccionados.append(p)
        if len(seleccionados)==0:
            print("No hay partidos en esa jornada.")
            return
        mostrar_tabla(seleccionados, equipos)
    else:
        mostrar_tabla(partidos, equipos)

#REPROGRAMAR O EDITAR PARTIDO
def reprogramar_partido(partidos):
    print("\n--- Reprogramar partido ---")
    try:
        id_partido=int(input("Introduce el ID del partido: "))
    except:
        print("ID inválido.")
        return partidos

    partido=None
    for p in partidos:
        if p["id"]==id_partido:
            partido=p
    if partido ==None:
        print("Partido no encontrado.")
        return partidos
    #FILTRO PARA PARTIDOS QUE YA HAN SIDO JUGADOS(SON NO EDITABLES)
    if partido["jugado"]:
        print("No se puede reprogramar un partido ya jugado.")
        return partidos
    #USO DATETIME
    nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ").strip()
    nueva_hora = input("Nueva hora (HH:MM): ").strip()
    try:
        datetime.strptime(nueva_fecha, "%Y-%m-%d")
        datetime.strptime(nueva_hora, "%H:%M")
    except:
        print("Formato de fecha/hora no válido.")
        return partidos

    partido["fecha"] = nueva_fecha
    partido["hora"] = nueva_hora
    print("Partido reprogramado correctamente.\n")
    return partidos

#ELIMINAR PARTIDO
def eliminar_partido(partidos):
    print("\n--- Eliminar partido ---")
    try:
        id_eliminar=int(input("Introduce el ID del partido a eliminar: "))
    except:
        print("ID inválido.")
        return partidos

    partido=None
    for p in partidos:
        if p["id"]==id_eliminar:
            partido=p
    if partido==None:
        print("Partido no encontrado.")
        return partidos
    #FILTRO PARA NO ELIMINAR UN PARTIDO YA JUGADO
    if partido["jugado"]:
        print("No se puede eliminar un partido que ya se ha jugado.")
        return partidos

    partidos.remove(partido)
    print("Partido eliminado correctamente.\n")
    return partidos

#FUNCION DE UTILIDAD: MOSTRAR LA TABLA
def mostrar_tabla(lista, equipos):
    filas=[]
    for p in lista:
        local=visitante=""
        for e in equipos:
            if e["id"] == p["local_id"]:
                local=e["nombre"]
            if e["id"] == p["visitante_id"]:
                visitante=e["nombre"]
        resultado="-"
        #USO DE LIBRERIA RICH(COLORES EN RESULTADOS)
        if p["resultado"] is not None:
            goles_local, goles_visitante = p["resultado"]
            if goles_local > goles_visitante:
                local = f"[green]{local}[/green]"
                visitante = f"[red]{visitante}[/red]"
            elif goles_visitante > goles_local:
                local = f"[red]{local}[/red]"
                visitante = f"[green]{visitante}[/green]"
            resultado = f"{goles_local} - {goles_visitante}"
        filas.append([
            p["id"], p["jornada"], local, visitante, p["fecha"], p["hora"], 
            "Sí" if p["jugado"] else "No", resultado
        ])
    #CONSOLE.PRINT PARA MOSTRAR RESULTADO CON RICH
    console.print(tabulate(filas, headers=["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora", "Jugado", "Resultado"], tablefmt="grid"))