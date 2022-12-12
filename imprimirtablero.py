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

def imprimir_tablero(tablero):
    i=0
    cabecera= ['A','B','C','D','E','F','G','H']
    print('Este es el tablero inicial:')
    print(' ',cabecera)
    for k in tablero:
        i+=1
        print(i,end=' ')
        print(k)

imprimir_tablero()