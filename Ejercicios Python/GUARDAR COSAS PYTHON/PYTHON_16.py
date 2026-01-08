#EJERCICIO 1
# # nombres=[]
# #METER NOMBRES EN LISTAS
# nombre=str(input("Escribe un nombre de persona o 'fin' para acabar: "))
# while nombre != "fin":
#     nombres.append(nombre)
#     nombre=str(input("Escribe otro nombre de persona o 'fin' para acabar: "))

# #CREAR Y ESCRIBRI ARCHIVO
# with open("nombres.txt", "w") as archivo:
#     for nombre in nombres:
#         archivo.write(nombre + "\n") #Mostrar de uno en uno
# print("Archivo 'nombres.txt' creado.")

# #MOSTRAR ARCHIVO CREADO(DA ERROR SI NO SE HA HECHO EL PASO ANTERIOR)
# with open("nombres.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())

#EJERCICIO 2
# dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# temperaturas={}
# #BUCLE TEMPERATURAS
# for dia in dias:
#     temperatura=float(input(f"Introduce la temperatura media del {dia}: "))
#     temperaturas[dia]=temperatura

# #GUARDAR
# with open("temperaturas.txt", "w") as archivo:
#     for dia in dias:
#         archivo.write(f"{dia}: {temperaturas[dia]}\n")
# print("Archivo 'temperaturas.txt' creado.")
# #ENSEÑAR
# with open("temperaturas.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())

# #EJERCICIO 3
# import pickle

# alumnos={}
# nombre=""
# #BUCLE NOMBRES/NOTA
# print("Escribe alumnos y sus notas o 'fin' para salir.")
# while nombre != "fin":
#     nombre=input("Nombre del alumno: ")
#     if nombre != "fin":
#         nota=float(input("Nota del alumno: "))
#         alumnos[nombre]=nota
# #GUARDAR
# with open("alumnos.pkl", "wb") as archivo:
#     pickle.dump(alumnos, archivo)
# print("Diccionario guardado en 'alumnos.pkl'.")

# #MOVIDAS CON PICKLE
# #CARGAR DICCIONARIO
# with open("alumnos.pkl", "rb") as archivo:
#     alumnos=pickle.load(archivo)
# #SHOW LISTA ALUMOS
# print("Lista de alumnos y sus notas:")
# for nombre, nota in alumnos.items():
#     print(f"{nombre} tiene: {nota}")
# #NOTA MEDIA
# media=sum(alumnos.values())/len(alumnos)
# print(f"Nota media:{media:.2f}")

# # EJERCICIO 4
# # Importar pickle y os
# import pickle
# import os
# # Clase Producto
# class Producto:
#     def __init__(self, nombre, precio, cantidad):
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad
#     def __str__(self):
#         return f"{self.nombre} - Precio: {self.precio}€ - Cantidad: {self.cantidad}"

# # Función para cargar el archivo si existe
# def cargar_inventario():
#     if os.path.exists("inventario.pkl"):
#         archivo = open("inventario.pkl", "rb")
#         inventario = pickle.load(archivo)
#         archivo.close()
#         # Mostrar los productos que hay guardados
#         for producto in inventario:
#             print(f"Producto: {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
#         return inventario
#     else:
#         return []

# # Función para crear producto y añadirlo a la lista
# def crear_producto(inventario):
#     # Preguntar nombre, precio y cantidad
#     nombre = input("Nombre: ")
#     precio = float(input("Precio: "))
#     while precio < 0:
#         print("Precio no válido, prueba otra vez")
#         precio = float(input("Precio: "))
#     cantidad = int(input("Cantidad: "))
#     while cantidad < 0:
#         print("Cantidad no válida, prueba otra vez")
#         cantidad = int(input("Cantidad: "))
#     # Añadir el producto a la lista
#     p = Producto(nombre, precio, cantidad)
#     inventario.append(p)
#     print("Producto añadido")

# # Función para guardar el inventario
# def guardar_inventario(inventario):
#     with open("inventario.pkl", "wb") as archivo:
#         pickle.dump(inventario, archivo)

# # Función para mostrar el menú
# def mostrar_menu():
#     print("--- MENÚ ---")
#     print("1. Crear producto y añadirlo a la lista")
#     print("2. Guardar el inventario")
#     print("3. Salir")

# #Función para el menú
# def menu():
#     #Cargar la lista del inventario o dejarla vacía
#     inventario = cargar_inventario()
#     mostrar_menu()
#     opcion = int(input("Opción: "))
#     while opcion != 3:
#         match opcion:
#             case 1:
#                 crear_producto(inventario)
#             case 2:
#                 guardar_inventario(inventario)
#             case 3:
#                 print("Saliendo...")
#             case _:
#                 print("Opción no válida")
#         # Mostrar menú nuevamente
#         mostrar_menu()
#         opcion = int(input("Opción: "))
# #ARRANQUE
# menu()