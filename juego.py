#1# --------------------IMPORTACIONES------------------------------------

from mod_funciones.booleano import (
    pedir_entrada_si_o_no
)

from mod_funciones.puntuacion import (
    puntuacion_cartas,
    comprobar_ganador
)

from mod_funciones.repartir_cartas import (
    repartir_dos_cartas_al_jugador,
    repartir_dos_cartas_al_croupier,
    repartir_una_carta_mas
)

#2# --------------------DECLARACION VARIABLES-------------------------------------------------
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

lista_cartas = list(cartas.keys()) #para poder escoger una carta, hacemos una lista de las claves del dict

J = [] #lista vacía con las cartas del jugador
C = [] #lista vacía con las cartas del croupier
#3# --------------------FUNCIONES-------------------------------------------------

def mostrar_cartas(lista):
    '''
    Esta funcion muestra las cartas (gráficas), dado una lista de indices de cartas
    -INPUT -------------
    lista : list
        lista de indices de cartas
    -OUTPUT ------------
    lista de cartas (gráficas)
    '''
    return [lista_cartas[c] for c in lista]



def accion_croupier(J, C):
    '''
    Esta funcion modeliza las acciones del croupier según las reglas del juego
    -INPUT -------------
    J : list
        lista de cartas del jugador
    C : list
        lista de cartas del croupier
    -OUTPUT ------------
    cartas del croupier actualizadas
    '''
    #si el croupier tiene 16 o menos, se le reparte una carta
    if puntuacion_cartas(C) >= 17:
        print('El croupier se planta.')
    else:
        C.append( repartir_una_carta_mas(J,C) )
        print('El croupier saca otra carta. Las cartas del croupier ahora son:', mostrar_cartas(C), '. Su puntuación es:', puntuacion_cartas(C))



def jugar():
    #se reparten dos cartas visibles al jugador
    global J
    J.extend( repartir_dos_cartas_al_jugador() ) #añadimos las dos cartas repartidas al azar a la lista de cartas del jugador
    print('Tus cartas son: ', mostrar_cartas(J), '. Tu puntuación es: ', puntuacion_cartas(J))
    
    #se reparten dos cartas al croupier
    global C
    C.extend( repartir_dos_cartas_al_croupier(J) ) #añadimos las dos cartas repartidas al azar a la lista de cartas del croupier
    print('Las cartas del croupier son: ', mostrar_cartas(C), '. Su puntuación es: ', puntuacion_cartas(C))

    #TURNO JUGADOR -----------------------------------------------------------------------------------
    #se pregunta al jugador si quiere otra carta, siempre que su puntuacion no pase de 21
    
    while pedir_entrada_si_o_no('¿Quieres otra carta? (s/n): ') == True: #mientras el jugador quiera otra carta
        J.append( repartir_una_carta_mas(J,C) ) #se le reparte una carta al azar
        print('Tus cartas ahora son: ', mostrar_cartas(J), '. Tu puntuación es: ', puntuacion_cartas(J))
        
        if puntuacion_cartas(J)<=21: #si su puntuacion no pasa de 21
            continue #volvemos a preguntar al jugador

        else: #si pt >21
            print('Te has pasado de 21. HAS PERDIDO')
            return #se sale de la función jugar()
            
    #cuando no quiera otra carta, y su puntuacion sea <=21, continuamos
    print('Te plantas con', puntuacion_cartas(J), 'puntos.')
    
    #TURNO CROUPIER -----------------------------------------------------------------------------------
    #el croupier debe sacar cartas siempre que su puntuacion sea <=16
    while puntuacion_cartas(C) < 17:
        accion_croupier(J, C)

    #COMPROBAR GANADOR
    comprobar_ganador(J, C)


def jugar_blackjack():
    global J
    global C
    print('Bienvenido al juego del Blackjack, el objetivo es conseguir una puntuación de 21 o lo más cercana posible.')
    jugar()
    while pedir_entrada_si_o_no('¿Quieres jugar otra partida? (s/n): ') == True:
        J=[]
        C=[]
        jugar()
    #si no quiere jugar otra partida, se sale del programa
    print('¡Hasta la próxima!')






