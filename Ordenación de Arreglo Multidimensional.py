# Ordenación de arreglos multidimensionales
matriz = [
    [1, 22, 3],
    [42, 5, 68],
    [79, 8, 19]
]

# Función para ordenar una fila en orden ascendente (método de burbuja)
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambia los elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Imprimir matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz
for fila in matriz:
    bubble_sort_fila(fila)

# Imprimir la matriz ordenada por filas
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)
