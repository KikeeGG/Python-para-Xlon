#RANKING
from tabulate import tabulate

#FUNCIONES
#MENU PRINCIPAL RANKING
def menu_resultados(partidos, equipos):
    opcion = 0
    while opcion != 4:
        print("\n--- MENÚ DE RESULTADOS Y CLASIFICACIÓN ---")
        print("1. Registrar resultado")
        print("2. Mostrar clasificación general")
        print("3. Ver estadísticas por equipo")
        print("4. Volver al menú principal")
        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            opcion=0
        if opcion == 1:
            partidos = registrar_resultado(partidos, equipos)
        elif opcion == 2:
            calcular_clasificacion(partidos, equipos)
        elif opcion == 3:
            estadisticas_equipo(partidos, equipos)
        elif opcion == 4:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")
    return partidos

#REGISTRAR RESULTADO
def registrar_resultado(partidos, equipos):
    print("\n--- Registrar resultado de un partido ---")
    #MOSTRAR !!SOLO!! PARTIDOS PENDIENTES
    pendientes = [p for p in partidos if not p["jugado"]]
    if len(pendientes) == 0:
        print("No hay partidos pendientes de resultado.")
        return partidos

    filas = []
    for p in pendientes:
        local=visitante= ""
        for e in equipos:
            if e["id"] == p["local_id"]:
                local=e["nombre"]
            if e["id"] == p["visitante_id"]:
                visitante=e["nombre"]
        filas.append([p["id"], p["jornada"], local, visitante, p["fecha"], p["hora"]])
    print(tabulate(filas, headers=["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora"], tablefmt="grid"))

    try:
        id_partido=int(input("Introduce el ID del partido para registrar resultado: "))
    except:
        print("ID inválido.")
        return partidos

    partido=None
    for p in partidos:
        if p["id"] == id_partido:
            partido=p

    if partido is None:
        print("Partido no encontrado.")
        return partidos

    if partido["jugado"]:
        print("Este partido ya tiene resultado registrado.")
        return partidos
    #GANA LOCAL O VISITANTE
    try:
        gL = int(input("Goles equipo local: "))
        gV = int(input("Goles equipo visitante: "))
    except:
        print("Entrada inválida. Usa números enteros pringao.")
        return partidos

    if gL < 0 or gV < 0:
        print("Los goles deben ser numeros enteros o cero.")
        return partidos

    partido["resultado"]= (gL, gV)
    partido["jugado"]=True
    print("El resultado ha sido registrado correctamente.\n")
    return partidos

#CLASIFICACIÓN GENERAL
def calcular_clasificacion(partidos, equipos):
    print("\n--- Clasificación general ---")
    #DICCIONARIO CON STATS
    tabla={}
    for e in equipos:
        if e["activo"]:
            tabla[e["id"]] = {
                "equipo": e["nombre"],
                "PJ": 0, "G": 0, "E": 0, "P": 0,
                "GF": 0, "GC": 0, "DG": 0, "PTS": 0
            }
    #BUCLE RECORRE LOS PARTIDOS JUGADOS
    for p in partidos:
        if p["jugado"] and p["resultado"] is not None:
            gL, gV = p["resultado"]
            local = p["local_id"]
            visitante = p["visitante_id"]

            if local in tabla and visitante in tabla:
                #PARTIDOS JUGADOS
                tabla[local]["PJ"] += 1
                tabla[visitante]["PJ"] += 1
                #GOLES
                tabla[local]["GF"] += gL
                tabla[local]["GC"] += gV
                tabla[visitante]["GF"] += gV
                tabla[visitante]["GC"] += gL
                #DIFERENCIA DE GOLES
                tabla[local]["DG"] = tabla[local]["GF"] - tabla[local]["GC"]
                tabla[visitante]["DG"] = tabla[visitante]["GF"] - tabla[visitante]["GC"]
                #RESULTADO
                if gL > gV:
                    tabla[local]["G"] += 1
                    tabla[visitante]["P"] += 1
                    tabla[local]["PTS"] += 3
                elif gV > gL:
                    tabla[visitante]["G"] += 1
                    tabla[local]["P"] += 1
                    tabla[visitante]["PTS"] += 3
                else:
                    tabla[local]["E"] += 1
                    tabla[visitante]["E"] += 1
                    tabla[local]["PTS"] += 1
                    tabla[visitante]["PTS"] += 1
    #LISTA POR PUNTUAJE
    lista_ordenada=sorted(tabla.values(), key=lambda x: x["PTS"], reverse=True)
    filas=[]
    for t in lista_ordenada:
        filas.append([
            t["equipo"], t["PJ"], t["G"], t["E"], t["P"],
            t["GF"], t["GC"], t["DG"], t["PTS"]
        ])
    print(tabulate(
        filas,
        headers=["Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS"],
        tablefmt="grid"
    ))

#ESTADÍSTICAS DE EQUIPO
def estadisticas_equipo(partidos, equipos):
    print("\n--- Estadísticas por equipo ---")
    try:
        id_equipo = int(input("Introduce el ID del equipo: "))
    except:
        print("Entrada inválida.")
        return
    equipo=None
    for e in equipos:
        if e["id"] == id_equipo:
            equipo=e
    if equipo is None:
        print("Equipo no encontrado.")
        return

    PJ = G = E = P = GF = GC = PTS = 0 #SUGERIDO POR COPILOT
    for p in partidos:
        if p["jugado"] and p["resultado"] is not None:
            gL, gV=p["resultado"]
            if p["local_id"] == id_equipo:
                PJ += 1
                GF += gL
                GC += gV
                if gL > gV:
                    G += 1
                    PTS += 3
                elif gV > gL:
                    P += 1
                else:
                    E += 1
                    PTS += 1
            elif p["visitante_id"] == id_equipo:
                PJ += 1
                GF += gV
                GC += gL
                if gV > gL:
                    G += 1
                    PTS += 3
                elif gL > gV:
                    P += 1
                else:
                    E += 1
                    PTS += 1
    DG = GF - GC
    filas = [[equipo["nombre"], PJ, G, E, P, GF, GC, DG, PTS]]
    print(tabulate(
        filas,
        headers=["Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS"],
        tablefmt="grid"
    ))