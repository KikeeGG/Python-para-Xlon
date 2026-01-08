import pickle
from rich import print
#DICCIONARIO DENTRO DE OTRO DICCIONARIO, CLAVE DNI VALOR OTRO DICCIONARIO CON MAS DATOS
clientes={}

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
    if dni in clientes:
        print("Este DNI ya existe, no se puede añadir.")
        return #SI EXISTE EL DNI, MANDAMOS UN RETURN, SI NO, CONTINUAMOS CON EL RESTO DE DATOS
    nombre = input("Escribe el nombre del cliente: ")
    apellido = input("Escribe ahora su apellido: ")
    telefono = int(input("Escribe ahora el teléfono: "))
    #DICCIONARIO, LA CLAVE SERÁ "DNI"
    clientes[dni]={
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }
    print(f"La ficha de {nombre} se ha creado correctamente.")

def eliminar_cliente(): #ELIMINAR CLIENTE
    dni=input("Introduce el DNI del cliente a borrar: ")
    if dni in clientes:
        del clientes[dni] #DEL ELIMINA LA ENTRADA DEL DICCIONARIO CON LA CLAVE DNI QUE HEMOS MANDADO
        print("Cliente eliminado correctamente.")
    else:
        print("No existe un cliente con ese DNI.")

def buscar_cliente(): #BUSCAR CLIENTE POR CLAVE DNI
    dni = input("Introduce el DNI a consultar: ")
    if dni in clientes: #BUCLE QUE COMPRUEBA Y ENSEÑA LOS DATOS DEL DICCIONARIO
        print(f"DNI: {dni}")
        print(f"Nombre: {clientes[dni]['nombre']}")
        print(f"Apellido: {clientes[dni]['apellido']}")
        print(f"Teléfono: {clientes[dni]['telefono']}")
    else:
        print("El cliente no existe.")

def modificar_cliente(): #MODIFICAR DATOS DE CLIENTE SEGUN DNI
    dni = input("Introduce el DNI del cliente a modificar: ")
    if dni not in clientes: #BUCLE QUE DEVUELVE SI DNI NO EXISTE
        print("Ese cliente no existe.")
        return
    print("Deja vacío un campo si no quieres cambiarlo.") #AÑADE CALIDAD DE VIDA AL PROGRAMA
    nombre=input("Nuevo nombre: ")
    apellido=input("Nuevo apellido: ")
    telefono=input("Nuevo teléfono: ")
    #BUCLES QUE PERMITEN NO CAMBIAR o NO LOS DATOS, LOS ESPACIOS VACIOS SE REPRESENTAN CON ""
    if nombre != "":
        clientes[dni]["nombre"]=nombre
    if apellido != "":
        clientes[dni]["apellido"]=apellido
    if telefono != "":
        clientes[dni]["telefono"]=int(telefono)
    print(f"Datos modificados de {nombre}.")

def listar_clientes(): #ENSEÑAR LISTA DE CLIENTES
    if not clientes: #BUCLE QUE COMPRUEBA SI HAY O NO DATOS EN DICCIONARIO
        print("No hay registros. ")
        return
    for dni, datos in clientes.items(): #BUCLE QUE ENSEÑA LOS DATOS DE LOS DICCIONARIOS
        print(f"{dni} -- {datos['nombre']} {datos['apellido']} {datos['telefono']}")
    print()

#TRATA DE DATOS CON PICKLE
def guardar_clientes(): #GUARDAR
    with open("clientes.pkl", "wb") as fichero:
        pickle.dump(clientes, fichero)
    print("Datos de clientes guardados correctamente.")

def cargar_clientes(): #CARGAR
    global clientes #LINEA DE CODIGO NECESARIA, SI NO SE PONE, PICKLE INTERPRETA EL DICCIONARIO CLIENTES COMO NUEVA VARIABLE Y LA CREA DESDE 0
    with open("clientes.pkl", "rb") as fichero:
        clientes = pickle.load(fichero)
    print("Datos de clientes cargados correctamente.")