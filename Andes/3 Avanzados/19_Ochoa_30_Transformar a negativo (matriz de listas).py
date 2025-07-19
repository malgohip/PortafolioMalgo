"""
Descripción del problema
En este ejercicio se debe transformar la imagen a su negativo. A cada posición de la matriz que representa la imagen se asigna una lista de 3 flotantes entre 0 y 1 que indican los valores R, G y B del píxel correspondiente. Para obtener el negativo de una imagen se debe calcular el color negativo de cada píxel. Para ello, se debe restar 1 a cada componente (es decir, el máximo valor que podría adquirir) y tomar el valor de absoluto del resultado. Con los nuevos valores de los componentes se forma cada nuevo color. Recuerde que cuenta con la función abs( ) de Python.
"""
def convertir_negativo(imagen: list)->list:
    """ convertir_negativo
    Transforma a negativo los valroes de una imagen
    Parámetros:
      imagen (list): Matriz que representa la imagen
    Retorno:
      list: Matriz que representa la imagen convertida a negativo
    """
    filas = len(imagen)
    columnas = len(imagen[0])
    negativo = [[None] * columnas for a in range(filas)]
    for x in range(filas):
        for y in range(columnas):
            r, g, b = imagen[x][y]
            r_neg = abs(1 - r)
            g_neg = abs(1 - g)
            b_neg = abs(1 - b)
            negativo[x][y] = [r_neg, g_neg, b_neg]
    return negativo