
#este será el tablero inicial
tablero = [
    ['♜',	'♞',	'♝',	'♛',	'♚',	'♝',	'♞',	'♜'],
    ['♟',	'♟',	'♟',	'♟',	'♟',	'♟',	'♟',	'♟'],
    [' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
    [' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
    [' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
    [' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
    ['♙',	'♙',	'♙',	'♙',	'♙',	'♙',	'♙',	'♙'],
    ['♖',	'♘',	'♗',	'♕',	'♔',	'♗',	'♘',	'♖'],
]

#definimos una seie de variables
columnas={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
movimientos=0
i=0



#definimos una funcion para imprimir el tablero
def imprimir_tablero(tablero):
    i=0
    cabecera= ['A','B','C','D','E','F','G','H']
    print('Este es el tablero inicial:')
    print(' ',cabecera)
    for k in tablero:
        i+=1
        print(i,end=' ')
        print(k)

imprimir_tablero(tablero)




#pedir el nombre del archivo donde se guardara el tablero
nombre_archivo=input('Ingrese el nombre del archivo donde desea guardar el tablero, recuerde debe estar seguido de txt: ')
file=open(nombre_archivo,'w')

for i in range(8):
    for j in range(8):
        file.write(tablero[i][j]+'\t')
        if j==7:
            file.write('\n')
file.close()

#BLOQUE PRINCIPAL

respuesta='S'
while respuesta!='N':
    print('Desea hacer algun movimiento?')
    respuesta=input('S/N: ')

    #Preguntar si desea hacer algun movimiento
    if respuesta == 'N':
        print('De acuerdo, su tablero se quedara asi:')
        for k in tablero:
            print(k)
    #si desea hacer algun movimiento, explicar como hacerlo
    elif respuesta == 'S':
        movimientos+=1
        print('INSTRUCCIONES PARA MOVER LAS PIEZAS:')
        print('--> Para mover una pieza, primero debe indicar la fila y columna donde se encuentra la pieza que desea mover')
        print('--> Para indicar la fila, debe escribir un numero del 1 al 8, donde la fila uno son las piezas negrasy la fila 8 son las piezas blancas')
        print('-->Para indicar la columna debe guiarse por las letras que esta en la parte superior del tablero')
        print('')
        print('Ingrese la fila y columna donde se encuentra la pieza que desea mover')
    #Pedir fila y columna donde se encuentra la pieza que desea mover
    fila_pieza_a_mover=int(input('Fila: '))
    fila_pieza_a_mover=fila_pieza_a_mover-1
    columna_pieza_a_mover=input('Columna:')
    columna_pieza_a_mover=columnas[columna_pieza_a_mover]
    print('Usted ha seleccionado la pieza:')
    print(tablero[fila_pieza_a_mover][columna_pieza_a_mover])



    #pedir fila y columna donde desea mover la pieza
    print('Ingrese la fila y columna donde desea mover la pieza')
    fila_nueva_posicion_pieza=int(input('Fila: '))
    fila_nueva_posicion_pieza=fila_nueva_posicion_pieza-1
    columna_nueva_posicion_pieza=input('Columna:')
    columna_nueva_posicion_pieza=columnas[columna_nueva_posicion_pieza]


    #aqui se mueve la pieza
    tablero[fila_nueva_posicion_pieza][columna_nueva_posicion_pieza]=tablero[fila_pieza_a_mover][columna_pieza_a_mover]
    #se deja vacio el lugar donde estaba la pieza
    tablero[fila_pieza_a_mover][columna_pieza_a_mover]=' '

    #imprimir tablero
    print('Su tablero es el siguiente:')
    for k in tablero:
        print(k)

    #se actualiza el archivo
    file=open(nombre_archivo,'w')

    for i in range(8):
        for j in range(8):
            file.write(tablero[i][j]+'\t')
            if j==7:
                file.write('\n')
    file.close()

