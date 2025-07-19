def generate_fibonacci_up_to(max_value):
    """Genera todos los números de Fibonacci menores o iguales a max_value."""
    fibs = [1, 2]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > max_value:
            break
        fibs.append(next_fib)
    return fibs

def expected_attempts(fib_list, F):
    """Calcula el número promedio de intentos para adivinar un número en el rango 1 .. F usando números de Fibonacci."""
    # Crear una lista para almacenar el número esperado de intentos
    dp = [float('inf')] * (F + 1)
    
    # Inicializar para rango de tamaño 1 (solo 1 intento necesario)
    for i in range(1, F + 1):
        dp[i] = 1
    
    # Recorrer todos los tamaños posibles
    for size in range(2, F + 1):
        for fib in fib_list:
            if fib >= size:
                break
            # Evaluar la división del rango en dos partes usando fib
            left_part = fib - 1
            right_part = size - fib
            dp[size] = min(dp[size], 1 + (dp[left_part] if left_part > 0 else 0) + (dp[right_part] if right_part > 0 else 0))
    
    return dp[F]

def main(input_data):
    """Procesa los datos de entrada y devuelve los resultados esperados."""
    lines = input_data.strip().split('\n')
    N = int(lines[0])
    ranges = [int(lines[i]) for i in range(1, N + 1)]
    
    # Encontrar el máximo número en las consultas
    max_value = max(ranges)
    
    # Generar números de Fibonacci hasta el máximo número de la lista
    fibs = generate_fibonacci_up_to(max_value)
    
    # Obtener resultados para cada consulta
    results = [expected_attempts(fibs, F) for F in ranges]
    
    # Formatear resultados con 2 decimales
    formatted_results = ' '.join(f"{result:.2f}" for result in results)
    return formatted_results

# Datos de entrada
input_data = """
4
21
377
2584
75025
"""

# Ejecución
print(main(input_data))