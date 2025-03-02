# Fundamentos

# crear una matriz 3x3
matriz = [
    [2, 4, 6],
    [8, 1, 7],
    [5, 9, 3]
]
# definimos el valor que buscamos
valor_buscado = 1
# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1
 #Recorrer la matriz para encontrar el valor
for fila in range(len(matriz)):
     for columna in range (len(matriz[fila])):
        if matriz [fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
        if fila_encontrada != -1:  # Si se encontró, salir del bucle externo
            break
#si se encuentra el valor
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
