#FUNCION PARA IMPRIMIR TABLERO EN DONDE EL PARAMETRO SERA EL TABLERO ANTERIOR
def mostrarTablero(tablero):
    print(tablero[1] + '|' + tablero[2] + '|' + tablero[3]) #SE IMPRIME EL DICCIONARIO CON IDENTIFICADOR UNO Y SE AGREGA '|' 
    print('-+-+-')                                          #Y ENSEGUIDA SE HACE LOS MISMO CON LOS DEMAS ELEMENTOS DEL DICCIONARIO
    print(tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    print('-+-+-')
    print(tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    print(" ")

def evaluarPosicionElemento(pos): #ESTA FUNCION AYUDA A NO PONER UN ELEMENTO EN UNA POSICION OCUPADA DEL TABLERO
    if(tablero[pos]== ' '): #SI POS ACTUAL ES IGUAL A VACIO ENTONCES
        return True         #RETORNA UN VERDADERO
    else:                   #SI NO ESTA VACION ENTONCES...
        return False        #RETORNA FALSO

def agregarElemento(elemento, pos): #FUNCION PARA AGREGAR ELEMENTOS, PARAMETRO DEL ELEMENTO Y LA POSICION 
    if evaluarPosicionElemento(pos): #SI LA POSICION ACTUAL NO ESTA OCUPADA ENTONCES:
        tablero[pos]= elemento      #LA POSCION ACTUAL SERA IGUAL AL ELEMTO ES DECIR QUE SE AGREGA A ESA POSICION
        mostrarTablero(tablero)     #SE MUESTRA LA POSICION
        if elementoAgregado():      #SI ELEMENTO ES AGREGADO COREECTAMENTE MOSTRARA UN MENSAJE 
            print("EMPATE ")
            exit()                  #SE DETIENE 
        if ganador():               #SI HAY UNA COMBINACION GANADORA ENTONCES...
            if elemento == 'X':      #SI ESA COMBINACION ESTA CONFORMADO POR X ENTONCES MUESTRA MENSAJE 
                print("EL BOT HA GANADO c:")
                exit()              #SE DETIENE 
            else:
                print("HAS GANADO :D") #SI ESA COMBINACION ESTA CONFORMADO POR O ENTONCES MUESTRA MENSAJE 
                exit()              #SE DETIENE 
        return
    
    else:   #SI LA FUNCION ESTA OCUAPADO ENTONCES...
        print("POSICION OCUPADA, INTENTE AGREGAR SU ELEMENTO EN OTRA POSICION :( ") #MUESTRA MENSAJE QUE LA POSICION ESTA OCUAPADO
        pos = int(input("ELIGE NUEVA POSICION: "))  #TE LPIDE NUEVAMENTE QUE INGRESE UNA NUEVA POSICION 
        agregarElemento(elemento,pos)           #SE LLAMA LA FUNCION AGREGAR ELEMENTO PARA QUE PUEDA AGREGAR L APOSICION
        return
    
def ganador(): #COMBINACIONES DE LINEAS DE GANE 
    if (tablero[1] == tablero[2] and tablero [1] == tablero[3] and tablero[1] != ' '):
        return True
    elif (tablero[4] == tablero[5] and tablero [4] == tablero[6] and tablero[4] != ' '):
        return True
    elif (tablero[7] == tablero[8] and tablero [7] == tablero[9] and tablero[7] != ' '):
        return True
    elif (tablero[1] == tablero[4] and tablero [1] == tablero[7] and tablero[1] != ' '):
        return True
    elif (tablero[2] == tablero[5] and tablero [2] == tablero[8] and tablero[2] != ' '):
        return True
    elif (tablero[3] == tablero[6] and tablero [3] == tablero[9] and tablero[3] != ' '):
        return True
    elif (tablero[1] == tablero[5] and tablero [1] == tablero[9] and tablero[1] != ' '):
        return True
    elif (tablero[7] == tablero[5] and tablero [7] == tablero[3] and tablero[7] != ' '):
        return True
    else:
        return False
    
def ganadorr(hacer):
    if tablero[1] == tablero[2] and tablero [1] == tablero[3] and tablero[1] == hacer:
        return True
    elif (tablero[4] == tablero[5] and tablero [4] == tablero[6] and tablero[4] == hacer):
        return True
    elif (tablero[7] == tablero[8] and tablero [7] == tablero[9] and tablero[7] == hacer):
        return True
    elif (tablero[1] == tablero[4] and tablero [1] == tablero[7] and tablero[1] == hacer):
        return True
    elif (tablero[2] == tablero[5] and tablero [2] == tablero[8] and tablero[2] == hacer):
        return True
    elif (tablero[3] == tablero[6] and tablero [3] == tablero[9] and tablero[3] == hacer):
        return True
    elif (tablero[1] == tablero[5] and tablero [1] == tablero[9] and tablero[1] == hacer):
        return True
    elif (tablero[7] == tablero[5] and tablero [7] == tablero[3] and tablero[7] == hacer):
        return True
    else:
        return False
    
def elementoAgregado():
    for key in tablero.keys(): #EL FOR RECORRE TODAS LAS CLAVES DEL DICCIONARIO DE TABLA
        if (tablero[key]==' '): #SI LA CLAVE ACTUAL ES IGUAL A VACION ENTONCES...
            return False       #RETORNA FALSO
    return True

def jugador1(): #FUNCION QUE PERMITE JUGAR AL JUGADOR1
    pos=int(input("INGRESA LA POSICION DE O:")) #PIDE LA POSICION 
    agregarElemento(jugador, pos) #SE LLAMA LA FUNCION AGREGRA ELEMENTO Y EN ELEMENTO VA EL JUGADOR O
    return #SE RETORNA DE NUEVO LA FUNCION 

def juegoBot():
    mejorPuntaje = -800
    mejorMovimiento = 0
    for key in tablero.keys():
        if (tablero[key] == ' '):
            tablero[key] = bot
            puntaje = minMax(tablero, 0, False)
            tablero[key] = ' '
            if (puntaje > mejorPuntaje):
                mejorPuntaje = puntaje
                mejorMovimiento = key

    agregarElemento(bot, mejorMovimiento)
    return

def minMax(tablero, profundidad, maximo):
    if (ganadorr(bot)):
        return 1 
    elif (ganadorr(jugador)):
        return -1
    elif (elementoAgregado()): 
        return 0
    
    if (maximo):
        mejorPuntaje = -800
        for key in tablero.keys():
            if(tablero[key] == ' '):
                tablero[key] = bot
                puntaje = minMax(tablero, profundidad + 1 , False)
                tablero[key] = ' '
                if(puntaje > mejorPuntaje):
                    mejorPuntaje = puntaje
        return mejorPuntaje

    else:
        mejorPuntaje = 800

        for key in tablero.keys():
            if(tablero[key] == ' '):
                tablero[key] = jugador
                puntaje = minMax(tablero, profundidad + 1, True)
                tablero[key] = ' '
                if(puntaje < mejorPuntaje):
                    mejorPuntaje = puntaje
        return mejorPuntaje
                    
def elegirInicio():
    while True:
        eleccion = input("¿DESEA INICIAR? SI/NO: ").strip().lower()
        if eleccion == "si":
            return "jugador"
        elif eleccion == "no":
            return "bot"
        else:
            print("INGRESE SI/NO")

inicio = elegirInicio()

#SE CREA UN DICCIONARIO PARA EL TABLERO EN DONDE SE UTILIZA COMO IDENTIFICADOR NUMEROS (POS) 
#Y EL ELEMNTO SERÁ EL ESPACIO VACIO EN DONDE SE ASIGANRA EL ELEMENTO
tablero = {1:' ', 2:' ', 3:' ',
           4:' ', 5:' ', 6:' ',
           7:' ', 8:' ', 9:' ' }

jugador = 'O' 
bot = 'X'

if inicio == "jugador":
    while not ganador(): 
        jugador1()
        if not ganador():
            juegoBot()
else:
    while not ganador(): 
        juegoBot()
        if not ganador():
            jugador1()
#while not ganador(): #MIENTRAS NO HAYA GANADOR SEGUIRA EL JUEGO 
    #juegoBot()
    #jugador1()

   
    


