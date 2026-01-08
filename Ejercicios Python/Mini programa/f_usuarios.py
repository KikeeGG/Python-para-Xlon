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