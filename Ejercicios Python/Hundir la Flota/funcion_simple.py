import random
import numpy as np

MAXIMOTABLERO = 19

def colocarBarco(barco, posiciones):
    
    #posiciones es una lista que contiene tuplas de tuplas
    #ejemplo:
    #posiciones[0] = ((0,1),(1,0))
    
    colocado = False
    while not colocado:
    
        fila_correcta = False
        
        while not fila_correcta:
            #fila de inicio y de fin del barco, el fin será siempre la fila de inicio más el tamaño del barco menos 1 porque inicial está incluida
            fila_inicio = random.randint(0, MAXIMOTABLERO)
            fila_fin = fila_inicio + barco - 1
            
            if fila_fin <= MAXIMOTABLERO:
                fila_correcta = True
        
        
        columna_inicio = random.randint(0, MAXIMOTABLERO)
        columna_fin = columna_inicio   #como todos los barcos van en vertical, la columna inicial y la final son iguales.
        
        inicio = (fila_inicio, columna_inicio)
        fin = (fila_fin, columna_fin)
        
        posicion_barco = (inicio, fin)
        
        hay_colision = False
        
        for (inicio_existente, fin_existente) in posiciones:
            
            fila_inicio_existente, columna_inicio_existente = inicio_existente
            fila_fin_existente, columna_fin_existente = fin_existente
                    
            if columna_inicio_existente == columna_inicio:
                #recorremos las filas de nuestro nuevo barco
                for fila_nueva in range(fila_inicio, fila_fin):
                    #recorremos las filas que ocupa el barco de la lista posiciones
                    for fila_existente in range(fila_inicio_existente, fila_fin_existente):
                        if fila_nueva == fila_existente:
                            hay_colision = True
                        
        if not hay_colision:
            posiciones.append(posicion_barco)
            colocado = True     
            
    return posiciones   