##FUNCIONES PARA EJERCICIO CAPTURAR MONSTRUOS
import random
from rich import print
#ELEGIR MONSTRUO ALEATORIO
def elegir_monstruo(monstruos):
    monstruo=random.choice(monstruos)
    print(f"Te has encontrado con un [green]{monstruo['nombre']}[/green] (Ratio captura: [yellow]{monstruo['ratio']}[/yellow])")
    return monstruo
#LISTAR OBJETOS DISPONIBLES
def mostrar_objetos(objetos):
    print("Objetos de captura disponibles:")
    for i, obj in enumerate(objetos):
        print(f"{i+1}. [magenta]{obj['nombre']}[/magenta] [yellow](x{obj['multiplicador']}[/yellow] de captura)")