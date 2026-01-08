##ARTIUCLOS ---------------------------------------------------------------------------------

#MENU ARTICULOS
def menu_articulos(articulos):
    opcion = 0

    while opcion != 7:  #Bucle principal del menú
        print("-----MENÚ ARTÍCULOS-----")
        print("1. Crear artículo")
        print("2. Lista artículos")
        print("3. Buscar artículo por ID")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Alternar artículo: activo/inactivo")
        print("7. Salir")
        print("-----------------------------------")

        opcion = leer_int("Selecciona una opción: ", 1)  #Se valida que sea un entero válido

        if opcion == 1:
            crear_articulo(articulos)  #Llama a la función que agrega un nuevo artículo
        elif opcion == 2:
            print("1. Todos")
            print("2. Sólo activos")
            print("3. Sólo inactivos")

            respuesta = leer_int("Elige una opción: ", 1)
            if respuesta == 1:
                lista_articulos(articulos)  #Lista todos los artículos
            elif respuesta == 2:
                lista_articulos(articulos, solo_activos=True)  #Lista solo los activos
            elif respuesta == 3:
                lista_articulos(articulos, solo_activos=False)  #Lista solo los inactivos
            else:
                print("Opción no válida.")
        elif opcion == 3:
            id_busqueda = leer_int("Ingrese el ID: ", 1)
            art = buscar_articulo_por_id(articulos, id_busqueda)  #Busca un artículo específico
            if art:
                estado = "Activo" if art["activo"] else "Inactivo"
                print(f"ID: {art['id']} | Nombre: {art['nombre']} | Precio: {art['precio']} | Stock: {art['stock']} | Estado: {estado}")
            else:
                print("Artículo no encontrado.")
        elif opcion == 4:
            actualizar_articulo(articulos)  #Permite editar nombre, precio o stock
        elif opcion == 5:
            eliminar_articulo(articulos)  #Elimina un artículo por ID
        elif opcion == 6:
            alternar_articulo(articulos)  #Cambia el estado activo/inactivo
        elif opcion == 7:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")

#GENERAR ID
def generar_id(lista):
    #Genera un ID único autoincremental según el último artículo registrado
    if len(lista) == 0:
        return 1
    else:
        return max(a["id"] for a in lista) + 1

#CREAR ARTÍCULO
def crear_articulo(articulos):
    print("Crear un nuevo artículo:")
    nombre = input("Nombre del artículo: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Intente de nuevo: ").strip()

    #Validaciones de entrada con funciones reutilizables
    precio = leer_float("Precio (>0): ", 0.01)
    stock = leer_int("Stock (>=0): ", 0)

    #Estructura de datos principal: diccionario
    nuevo = {
        "id": generar_id(articulos),  # ID único
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True  #Todos los artículos nuevos empiezan activos
    }
    articulos.append(nuevo)  #Se agrega el nuevo artículo a la lista
    print("Artículo creado correctamente.")

#LISTAR ARTÍCULOS
def lista_articulos(articulos, solo_activos=None):
    print("---Listado de artículos---")
    if not articulos:
        print("No hay artículos registrados.")
        return
    for art in articulos:
        #Filtra según el parámetro 'solo_activos' (True/False o None)
        if solo_activos is None or art["activo"] == solo_activos:
            estado = "Activo" if art["activo"] else "Inactivo"
            print(f"ID: {art['id']} | Nombre: {art['nombre']} | Precio: {art['precio']} | Stock: {art['stock']} | Estado: {estado}")

#BUSCAR ARTÍCULO POR ID
def buscar_articulo_por_id(articulos, id_busqueda):
    #Recorre la lista buscando coincidencia exacta de ID
    for art in articulos:
        if art["id"] == id_busqueda:
            return art
    return None  #Si no encuentra, devuelve None

#LECTORES DE DATOS
def leer_int(mensaje, minimo=None):
    #Lee y valida números enteros; se repite hasta que el usuario ingrese un valor válido
    while True:
        valor = input(mensaje)
        try:
            numero = int(valor)
            if minimo is not None and numero < minimo:
                print(f"El número debe ser mayor o igual a {minimo}.")
            else:
                return numero
        except ValueError:
            print("Debes ingresar un número entero válido.")

def leer_float(mensaje, minimo=None):
    #Lee y valida números decimales; similar a leer_int
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            if minimo is not None and numero < minimo:
                print(f"El número debe ser mayor o igual a {minimo}.")
            else:
                return numero
        except ValueError:
            print("Debes ingresar un número decimal válido.")

#ACTUALIZAR ARTÍCULO
def actualizar_articulo(articulos):
    print("---Actualizar artículo---")
    id_busqueda = leer_int("Ingrese el ID del artículo: ", 1)
    art = buscar_articulo_por_id(articulos, id_busqueda)

    if art is None:
        print("Artículo no encontrado.")
        return

    #Se muestra el artículo actual antes de modificar
    print(f"Editando '{art['nombre']}' (ID {art['id']})")

    #Si el usuario deja vacío el campo, el valor se mantiene igual
    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{art['nombre']}'): ").strip()
    if nuevo_nombre:
        art["nombre"] = nuevo_nombre

    valor = input(f"Nuevo precio (Enter para mantener {art['precio']}): ").strip()
    if valor:
        try:
            nuevo_precio = float(valor)
            if nuevo_precio > 0:
                art["precio"] = nuevo_precio
            else:
                print("El precio debe ser mayor que 0.")
        except ValueError:
            print("Valor no válido. Se mantiene el anterior.")

    valor = input(f"Nuevo stock (Enter para mantener {art['stock']}): ").strip()
    if valor:
        try:
            nuevo_stock = int(valor)
            if nuevo_stock >= 0:
                art["stock"] = nuevo_stock
            else:
                print("El stock no puede ser negativo.")
        except ValueError:
            print("Valor no válido. Se mantiene el anterior.")

    print("Artículo actualizado correctamente.")

#ELIMINAR ARTÍCULO
def eliminar_articulo(articulos):
    print("---Eliminar artículo---")
    id_busqueda = leer_int("Ingrese el ID del artículo: ", 1)
    art = buscar_articulo_por_id(articulos, id_busqueda)

    if art is None:
        print("Artículo no encontrado.")
        return

    articulos.remove(art)  #Se elimina el artículo de la lista principal
    print("Artículo eliminado del inventario.")

#ALTERNAR ESTADO DE UN ARTÍCULO
def alternar_articulo(articulos):
    print("---Alternar estado activo/inactivo---")
    id_busqueda = leer_int("Ingrese el ID del artículo: ", 1)
    art = buscar_articulo_por_id(articulos, id_busqueda)

    if art is None:
        print("Artículo no encontrado.")
        return

    #Cambia el valor booleano de 'activo' por el contrario
    art["activo"] = not art["activo"]
    estado = "activo" if art["activo"] else "inactivo"
    print(f"Estado del producto cambiado a {estado}.")