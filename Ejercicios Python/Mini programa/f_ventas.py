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