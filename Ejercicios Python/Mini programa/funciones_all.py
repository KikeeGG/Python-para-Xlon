
#FUNCIONES:
#MENU PRINCIPAL (DA PASO A LOS 3 SUBMENUS)
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

##USUARIOS---------------------------------------------------------------

#MENU USUARIOS
def menu_usuarios(usuarios):
    opcion = 0

    while opcion != 7:
        print("-----MENÚ USUARIOS-----")
        print("1. Crear usuario")
        print("2. Lista usuarios")
        print("3. Buscar usuario por ID")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Alternar activo/inactivo")
        print("7. Volver")
        print("-----------------------------------")

        opcion = leer_int("Selecciona una opción: ", 1)

        if opcion == 1:
            crear_usuario(usuarios)
        elif opcion == 2:
            print("1. Todos")
            print("2. Sólo activos")
            print("3. Sólo inactivos")
            respuesta = leer_int("Elige una opción: ", 1)
            if respuesta == 1:
                listar_usuarios(usuarios)
            elif respuesta == 2:
                listar_usuarios(usuarios, solo_activos=True)
            elif respuesta == 3:
                listar_usuarios(usuarios, solo_activos=False)
            else:
                print("Opción no válida.")
        elif opcion == 3:
            id_busqueda = leer_int("Ingrese el ID: ", 1)
            usr = buscar_usuario_por_id(usuarios, id_busqueda)
            if usr:
                estado = "Activo" if usr["activo"] else "Inactivo"
                print(f"ID: {usr['id']} | Nombre: {usr['nombre']} | Email: {usr['email']} | Estado: {estado}")
            else:
                print("Usuario no encontrado.")
        elif opcion == 4:
            actualizar_usuario(usuarios)
        elif opcion == 5:
            eliminar_usuario(usuarios)
        elif opcion == 6:
            alternar_usuario(usuarios)
        elif opcion == 7:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")

#CREACION USUARIO NUEVO
def crear_usuario(usuarios):
    print("Crear un nuevo usuario:")
    nombre = input("Nombre del usuario: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Intente de nuevo: ").strip()

    #Validación básica de formato de email
    email = input("Correo electrónico: ").strip()
    while "@" not in email or "." not in email:
        email = input("Email inválido. Ingrese un correo válido: ").strip()

    nuevo = {
        "id": generar_id(usuarios),  #Reutiliza la misma función de generación de ID
        "nombre": nombre,
        "email": email,
        "activo": True
    }
    usuarios.append(nuevo)
    print("Usuario creado correctamente.")

#ENSEÑAR LISTA USUARIOS, COMO LA DE PRODUCTOS
def listar_usuarios(usuarios, solo_activos=None):
    print("---Listado de usuarios---")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usr in usuarios:
        if solo_activos is None or usr["activo"] == solo_activos:
            estado = "Activo" if usr["activo"] else "Inactivo"
            print(f"ID: {usr['id']} | Nombre: {usr['nombre']} | Email: {usr['email']} | Estado: {estado}")

#BUSCAR USUARIO
def buscar_usuario_por_id(usuarios, id_busqueda):
    for usr in usuarios:
        if usr["id"] == id_busqueda:
            return usr
    return None

#ACTUALIZAR USUARIO, DATOS
def actualizar_usuario(usuarios):
    print("---Actualizar usuario---")
    id_busqueda = leer_int("Ingrese el ID del usuario: ", 1)
    usr = buscar_usuario_por_id(usuarios, id_busqueda)

    if usr is None:
        print("Usuario no encontrado.")
        return

    print(f"Editando '{usr['nombre']}' (ID {usr['id']})")

    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{usr['nombre']}'): ").strip()
    if nuevo_nombre:
        usr["nombre"] = nuevo_nombre

    nuevo_email = input(f"Nuevo email (Enter para mantener {usr['email']}): ").strip()
    if nuevo_email:
        if "@" in nuevo_email and "." in nuevo_email:
            usr["email"] = nuevo_email
        else:
            print("Email no válido. Se mantiene el anterior.")

    print("Usuario actualizado correctamente.")

#ELIMINAR USUARIO
def eliminar_usuario(usuarios):
    print("---Eliminar usuario---")
    id_busqueda = leer_int("Ingrese el ID del usuario: ", 1)
    usr = buscar_usuario_por_id(usuarios, id_busqueda)

    if usr is None:
        print("Usuario no encontrado.")
        return

    usuarios.remove(usr)
    print("Usuario eliminado correctamente.")

#ALTERNAR USUARIO, ACTIVO-INACTIVO
def alternar_usuario(usuarios):
    print("---Alternar estado activo/inactivo---")
    id_busqueda = leer_int("Ingrese el ID del usuario: ", 1)
    usr = buscar_usuario_por_id(usuarios, id_busqueda)

    if usr is None:
        print("Usuario no encontrado.")
        return

    usr["activo"] = not usr["activo"]
    estado = "activo" if usr["activo"] else "inactivo"
    print(f"Estado del usuario cambiado a {estado}.")

##VENTAS---------------------------------------------------------

#MENU VENTAS
def menu_ventas(usuarios, articulos, ventas, carrito_actual, usuario_activo):
    opcion = 0
    while opcion != 8:
        print("----- MENÚ VENTAS / CARRITO -----")
        print("1. Seleccionar usuario activo")
        print("2. Añadir artículo al carrito")
        print("3. Quitar artículo del carrito")
        print("4. Ver carrito")
        print("5. Confirmar compra")
        print("6. Historial de ventas por usuario")
        print("7. Vaciar carrito")
        print("8. Volver")
        print("-----------------------------------")

        opcion = leer_int("Selecciona una opción: ", 1)

        if opcion == 1:
            usuario_activo = seleccionar_usuario_activo(usuarios)
        elif opcion == 2:
            if usuario_activo is None:
                print("Debe seleccionar un usuario activo antes de añadir artículos.")
            else:
                anadir_al_carrito(carrito_actual, articulos)
        elif opcion == 3:
            quitar_del_carrito(carrito_actual)
        elif opcion == 4:
            ver_carrito(carrito_actual, articulos)
        elif opcion == 5:
            confirmar_compra(carrito_actual, articulos, usuario_activo, ventas, usuarios)
        elif opcion == 6:
            if usuario_activo:
                historial_ventas_por_usuario(ventas, usuario_activo)
            else:
                print("Debes seleccionar un usuario activo primero.")
        elif opcion == 7:
            carrito_actual.clear()
            print("Carrito VACIADO.")
        elif opcion == 8:
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida.")
    return usuario_activo

#SELECCIONAR USUARIO (HA DE EXISTIR, SI NO, CREAR UNO)
def seleccionar_usuario_activo(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
        return None
    listar_usuarios(usuarios)
    user_id = leer_int("Ingrese el ID del usuario que comprará: ", 1)
    usr = buscar_usuario_por_id(usuarios, user_id)
    if usr and usr["activo"]:
        print(f"Usuario {usr['nombre']} seleccionado.")
        return usr["id"]
    else:
        print("Usuario no válido o inactivo.")
        return None

#AÑADIR ARTICULO AL CARRITO
def anadir_al_carrito(carrito, articulos):
    art_id = leer_int("Ingrese ID del artículo: ", 1)
    art = buscar_articulo_por_id(articulos, art_id)
    if not art or not art["activo"]:
        print("Artículo no válido o inactivo.")
        return
    cantidad = leer_int("Cantidad: ", 1)
    if cantidad > art["stock"]:
        print("No hay suficiente stock.")
        return
    for i, (idc, cant) in enumerate(carrito):
        if idc == art_id:
            if cant + cantidad > art["stock"]:
                print("No hay suficiente stock disponible para añadir esa cantidad.")
                return
            carrito[i] = (idc, cant + cantidad)
            print("Cantidad actualizada en carrito.")
            return
    carrito.append((art_id, cantidad))
    print("Artículo añadido al carrito.")

#ELIMINAR ARTICULO DEL CARRITO
def quitar_del_carrito(carrito):
    if not carrito:
        print("Carrito vacío.")
        return
    art_id = leer_int("Ingrese ID del artículo a quitar: ", 1)
    for i, (idc, cant) in enumerate(carrito):
        if idc == art_id:
            carrito.pop(i)
            print("Artículo quitado del carrito.")
            return
    print("Ese artículo no estaba en el carrito.")

#VER EL CARRITO Y TOTAL
def ver_carrito(carrito, articulos):
    if not carrito:
        print("Carrito vacío.")
        return
    total = 0
    for art_id, cant in carrito:
        art = buscar_articulo_por_id(articulos, art_id)
        if art:
            subtotal = art["precio"] * cant
            total += subtotal
            print(f"{art['nombre']} x {cant} = {subtotal:.2f}")
    print(f"TOTAL: {total:.2f}")

#CONFIRMAR LA COMPRA
def confirmar_compra(carrito, articulos, usuario_activo, ventas, usuarios):
    if not carrito:
        print("Carrito vacío.")
        return
    if usuario_activo is None:
        print("Debe seleccionar usuario.")
        return
    usr = buscar_usuario_por_id(usuarios, usuario_activo)
    if not usr or not usr["activo"]:
        print("El usuario no es válido o está inactivo.")
        return
    total = 0
    items = []
    for art_id, cant in carrito:
        art = buscar_articulo_por_id(articulos, art_id)
        if not art or cant > art["stock"]:
            print("Stock insuficiente o artículo inválido.")
            return
    for art_id, cant in carrito:
        art = buscar_articulo_por_id(articulos, art_id)
        art["stock"] -= cant
        subtotal = art["precio"] * cant
        total += subtotal
        items.append((art_id, cant, art["precio"]))
    nueva_venta = {
        "id_venta": len(ventas) + 1,
        "usuario_id": usuario_activo,
        "items": items,
        "total": total
    }
    ventas.append(nueva_venta)
    carrito.clear()
    print(f"Compra confirmada. Total = {total:.2f}")

#HISTORIAL DE VENTAS X USUARIO
def historial_ventas_por_usuario(ventas, usuario_id):
    historial = [v for v in ventas if v["usuario_id"] == usuario_id]
    if not historial:
        print("El usuario no tiene ventas registradas.")
        return
    for v in historial:
        print(f"Venta {v['id_venta']} | Total: {v['total']:.2f}")
        for art_id, cant, precio in v["items"]:
            print(f"   Artículo {art_id} x{cant} (pu: {precio})")