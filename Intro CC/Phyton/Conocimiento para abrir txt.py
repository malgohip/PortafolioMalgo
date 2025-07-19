# Abre el archivo 'Datos.txt' en modo de lectura usando un bloque with
with open('Talleres pre-parcial\Taller_2\TXTs\Datos.txt', 'r') as f:
    # Lee todas las líneas del archivo y las almacena en la lista L
    L = f.readlines()

# Imprime la lista de líneas
print(L)