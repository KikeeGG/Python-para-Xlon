from c4_core import *

#MAIN O JUEGO PRINCIPAL
def jugar_conecta4():
    tab=crear_tablero() 
    posiciones=[] #LISTA PARA POSICIONES Y COMPROBAR LUEGO SI EL JUGADRO PUEDE GANAR
    jugador=1 #EMPIEZA SIEMPRE EL PLAYER 1
    fin=False
    while not fin:
        #LLAMAMOS A LAS FUNCIONES
        pintar_tablero(tab)
        colocar_jugador(posiciones, tab, jugador)
        #CORRECCIÓN: pasamos tab, no posiciones
        if hay_cuatro_en_raya(tab, jugador):
            pintar_tablero(tab)
            print("¡HA GANADO EL JUGADOR", jugador, "!")
            fin=True
        elif tablero_lleno(tab):
            pintar_tablero(tab)
            print("¡HA HABIDO UN EMPATE!")
            fin=True
        else:
            #CAMBIO TURNO ENTRE PLAYERS
            if jugador==1:
                jugador=2
            else:
                jugador=1
                
#ARRANQUE                
jugar_conecta4()