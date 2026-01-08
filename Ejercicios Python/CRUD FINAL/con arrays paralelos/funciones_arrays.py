import pickle
from rich import print
#AHORA USO ARRAYS PARALELOS EN VEZ DE DICCIONARIO DENTRO DE DICCIONARIO
#CADA POSICIÓN REPRESENTA A UN CLIENTE: MISMO ÍNDICE EN TODOS LOS ARRAYS
#SE RECICLAN MUCHAS FUNCIONES, SE AÑADE UN BUCLE PARA BUSCAR INDICE 
#(Haría una función auxiliar pero me huelo que puedes mandar optimizar funciones o algo similar)
dnis=[]
nombres=[]
apellidos=[]
telefonos=[]

def mostrar_menu(): #PINTAR MENU
    print("[blue]--- Menú principal ---[/blue]")
    print("1. Alta de ciente")
    print("2. Listar todos los clientes")
    print("3. Buscar cliente por DNI")
    print("4. Modificar teléfono de un cliente")
    print("5. Eliminar cliente")
    print("6. Guardar clientes en fichero")
    print("7. Cargar clientes desde fichero")
    print("8. Salir")
    print("----------------------")

def alta_cliente(): #CREAR CLIENTE
    dni=input("Escribe el DNI del cliente: ")
    #BUSCAR ÍNDICE
    indice=None
    posicion=0
    for d in dnis: #BUCLE QUE RECORRE LOS DNI
        if d == dni:
            indice=posicion
        posicion=posicion+1
    if indice != None: #SI EXISTE EL DNI, NO SE PUEDE AÑADIR
        print("Este DNI ya existe, no se puede añadir.")
        return
    nombre=input("Escribe el nombre del cliente: ")
    apellido=input("Escribe ahora su apellido: ")
    telefono=int(input("Escribe ahora el teléfono: "))
    #AÑADIMOS EL CLIENTE EN ARRAYS PARALELOS
    dnis.append(dni)
    nombres.append(nombre)
    apellidos.append(apellido)
    telefonos.append(telefono)
    print(f"La ficha de {nombre} se ha creado correctamente.")

def eliminar_cliente(): #ELIMINAR CLIENTE
    dni=input("Introduce el DNI del cliente a borrar: ")
    #BUSCAR ÍNDICE DEL CLIENTE
    indice=None
    posicion=0
    for d in dnis:
        if d == dni:
            indice=posicion
        posicion=posicion+1
    if indice != None: #SI EL DNI EXISTE, ELIMINAMOS EN TODOS LOS ARRAYS
        dnis.pop(indice)
        nombres.pop(indice)
        apellidos.pop(indice)
        telefonos.pop(indice)
        print("Cliente eliminado correctamente.")
    else:
        print("No existe un cliente con ese DNI.")

def buscar_cliente(): #BUSCAR CLIENTE POR CLAVE DNI
    dni=input("Introduce el DNI a consultar: ")
    #BUSCAR ÍNDICE
    indice=None
    posicion=0
    for d in dnis: #BUCLE QUE BUSCA EL DNI
        if d == dni:
            indice=posicion
        posicion=posicion+1
    if indice != None: #SI SE HA ENCONTRADO, ENSEÑAMOS LOS DATOS
        print(f"DNI: {dnis[indice]}")
        print(f"Nombre: {nombres[indice]}")
        print(f"Apellido: {apellidos[indice]}")
        print(f"Teléfono: {telefonos[indice]}")
    else:
        print("El cliente no existe.")

def modificar_cliente(): #MODIFICAR DATOS DE CLIENTE SEGUN DNI
    dni=input("Introduce el DNI del cliente a modificar: ")
    #BUSCAR ÍNDICE
    indice=None
    posicion=0
    for d in dnis:
        if d == dni:
            indice=posicion
        posicion=posicion+1
    if indice == None: #SI NO EXISTE, LO DECIMOS Y SALIMOS
        print("Ese cliente no existe.")
        return
    print("Deja vacío un campo si no quieres cambiarlo.") #AÑADE CALIDAD DE VIDA
    nombre=input("Nuevo nombre: ")
    apellido=input("Nuevo apellido: ")
    telefono=input("Nuevo teléfono: ")
    #BUCLES QUE PERMITEN NO CAMBIAR O SÍ LOS DATOS (VACÍO = NO CAMBIAR)
    if nombre != "":
        nombres[indice]=nombre
    if apellido != "":
        apellidos[indice]=apellido
    if telefono != "":
        telefonos[indice]=int(telefono)
    print("Datos modificados correctamente.")

def listar_clientes(): #ENSEÑAR LISTA DE CLIENTES
    if len(dnis) == 0: #BUCLE QUE COMPRUEBA SI HAY O NO DATOS
        print("No hay registros. ")
        return
    #BUCLE QUE ENSEÑA LOS DATOS DE CADA CLIENTE SEGÚN ÍNDICE
    posicion=0
    while posicion < len(dnis):
        print(f"{dnis[posicion]} -- {nombres[posicion]} {apellidos[posicion]} {telefonos[posicion]}")
        posicion=posicion+1
    print()

#TRATA DE DATOS CON PICKLE
def guardar_clientes(): #GUARDAR
    with open("clientes.pkl","wb") as fichero:
        pickle.dump([dnis, nombres, apellidos, telefonos], fichero)
    print("Datos de clientes guardados correctamente.")

def cargar_clientes(): #CARGAR
    global dnis, nombres, apellidos, telefonos #LINEA NECESARIA PARA QUE NO SEAN NUEVAS VARIABLES
    with open("clientes.pkl","rb") as fichero:
        dnis, nombres, apellidos, telefonos = pickle.load(fichero)
    print("Datos de clientes cargados correctamente.")