#IMPORTAR FUNCIONES
from f_menu_principal import menu_principal
from f_articulos import (
    generar_id,
    crear_articulo,
    lista_articulos,
    buscar_articulo_por_id,
    leer_int,
    leer_float,
    actualizar_articulo,
    eliminar_articulo,
    alternar_articulo
)
from f_usuarios import (
    menu_usuarios,
    crear_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    actualizar_usuario,
    eliminar_usuario,
    alternar_usuario
)
from f_ventas import (
    menu_ventas,
    seleccionar_usuario_activo,
    anadir_al_carrito,
    quitar_del_carrito,
    ver_carrito,
    confirmar_compra,
    historial_ventas_por_usuario
)

#PROGRAMA PRINCIPAL
articulos = []
usuarios = []
ventas = []
carrito_actual = []
usuario_activo = None

menu_principal(articulos, usuarios, ventas, carrito_actual, usuario_activo)

